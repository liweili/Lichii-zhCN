'use strict';
/**
 * Lichii-zhCN GitHub 发布助手。
 *
 * 用法（token 通过环境变量 GH_TOKEN 传入，不写进任何仓库文件）：
 *   GH_TOKEN=<pat> node tools/publish.js create-repo
 *   GH_TOKEN=<pat> node tools/publish.js push
 *   GH_TOKEN=<pat> node tools/publish.js release v0.1.0
 *   GH_TOKEN=<pat> node tools/publish.js assets v0.1.0
 *   GH_TOKEN=<pat> node tools/publish.js all v0.1.0
 *   node tools/publish.js verify                 # 只读，不需要 token
 *
 * token 需具备 repo 权限（classic PAT）。脚本本身不含任何凭据。
 *
 * 网络说明：
 *   本机 Steam++ 在 hosts 里把 api.github.com / uploads.github.com 指向
 *   127.0.0.1，REST API 不通。这里用公共 DNS 直查真实 IP 并在 TLS 层
 *   保留原域名，绕过 hosts 劫持；git push 则临时清掉 ghfast.top 镜像重写。
 */
const https = require('https');
const dns = require('dns');
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const OWNER = 'liweili';
const REPO = 'Lichii-zhCN';
const RELEASE_DIR = path.join(ROOT, 'release');
const DIST_DIR = path.join(ROOT, 'dist');
const UA = 'Lichii-zhCN-publisher';

// ---------------------------------------------------------------- DNS 绕过
const resolver = new dns.Resolver();
resolver.setServers(['8.8.8.8', '1.1.1.1']);
const ipCache = new Map();

function resolveRealIp(hostname) {
  if (ipCache.has(hostname)) return ipCache.get(hostname);
  return new Promise((resolve) => {
    resolver.resolve4(hostname, (err, addresses) => {
      if (err || !addresses || !addresses.length) {
        console.warn(`  ! 无法解析 ${hostname}（${err && err.message || '无结果'}），改用系统 DNS`);
        ipCache.set(hostname, null);
        resolve(null);
        return;
      }
      ipCache.set(hostname, addresses[0]);
      resolve(addresses[0]);
    });
  });
}

async function requestOptions(hostname, extra) {
  const ip = await resolveRealIp(hostname);
  const opts = { hostname, ...extra };
  if (ip) {
    // Node 18+ 传 options.all=true 要求返回地址数组，老版本要求 (err, ip, family)。
    opts.lookup = (host, lookupOpts, cb) => {
      if (lookupOpts && lookupOpts.all) return cb(null, [{ address: ip, family: 4 }]);
      return cb(null, ip, 4);
    };
  }
  return opts;
}

// ---------------------------------------------------------------- API
async function api(token, method, path_, body) {
  const data = body ? JSON.stringify(body) : null;
  const opts = await requestOptions('api.github.com', {
    path: path_,
    method,
    headers: {
      'User-Agent': UA,
      'Accept': 'application/vnd.github+json',
      ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
      'X-GitHub-Api-Version': '2022-11-28',
      ...(data ? { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(data) } : {}),
    },
  });
  return new Promise((resolve, reject) => {
    const req = https.request(opts, (res) => {
      const chunks = [];
      res.on('data', (c) => chunks.push(c));
      res.on('end', () => {
        const text = Buffer.concat(chunks).toString('utf8');
        let json = null;
        try { json = JSON.parse(text); } catch (e) { /* 非 JSON 响应 */ }
        resolve({ status: res.statusCode, json, text });
      });
    });
    req.on('error', reject);
    if (data) req.write(data);
    req.end();
  });
}

// ---------------------------------------------------------------- 建仓库
async function createRepo(token) {
  console.log(`检查仓库 ${OWNER}/${REPO} ...`);
  const chk = await api(token, 'GET', `/repos/${OWNER}/${REPO}`);
  if (chk.status === 200) {
    console.log('  仓库已存在，跳过创建');
    return true;
  }
  if (chk.status !== 404) {
    console.error('  ✗ 查询失败:', chk.status, chk.json && chk.json.message);
    return false;
  }
  console.log('  仓库不存在，正在创建...');
  const res = await api(token, 'POST', '/user/repos', {
    name: REPO,
    description: 'Lichii 简体中文语言包 —— 可插拔 zh_CN.qm + 最小外部加载补丁',
    private: false,
    auto_init: false,
    has_wiki: false,
    has_issues: true,
    has_projects: false,
    has_downloads: true,
    topics: ['lichii', 'yuzu', 'eden', 'switch-emulator', 'chinese', 'zh-cn',
             'localization', 'i18n', 'qt', 'translation'],
  });
  if (res.status === 201) {
    console.log(`  ✓ 创建成功: https://github.com/${OWNER}/${REPO}`);
    return true;
  }
  console.error('  ✗ 创建失败:', res.status, res.json && res.json.message);
  return false;
}

// ---------------------------------------------------------------- 推代码
function pushCode(token) {
  const url = `https://${token}@github.com/${OWNER}/${REPO}.git`;
  console.log('推送 main ...');
  // 全局 insteadOf 会把 github.com 重写到 ghfast.top 镜像；镜像 ref 状态
  // 常不同步，这里用 GIT_CONFIG_* 临时清空该重写，直连真实 GitHub。
  const env = {
    ...process.env,
    GIT_CONFIG_COUNT: '1',
    GIT_CONFIG_KEY_0: 'url.https://ghfast.top/https://github.com/.insteadof',
    GIT_CONFIG_VALUE_0: 'https://github.invalid/',
  };
  try {
    execSync(`git push -u "${url}" main`, { cwd: ROOT, stdio: 'inherit', env });
    console.log('  ✓ 推送完成');
    return true;
  } catch (e) {
    console.error('  ✗ 推送失败:', e.message);
    return false;
  }
}

// ---------------------------------------------------------------- 附件
function collectAssets() {
  const out = [];
  if (fs.existsSync(RELEASE_DIR)) {
    for (const f of fs.readdirSync(RELEASE_DIR)) {
      if (f.endsWith('.zip')) out.push(path.join(RELEASE_DIR, f));
    }
  }
  const qm = path.join(DIST_DIR, 'zh_CN.qm');
  if (fs.existsSync(qm)) out.push(qm);
  return out;
}

function toAsciiAssetName(name) {
  const ext = path.extname(name);
  const base = path.basename(name, ext);
  const ascii = base.replace(/[^\x20-\x7E]+/g, '-')
    .replace(/-{2,}/g, '-').replace(/^-|-$/g, '');
  return (ascii || 'asset') + ext;
}

async function uploadAsset(token, uploadUrl, name, file) {
  const url = new URL(uploadUrl);
  const stat = fs.statSync(file);
  const opts = await requestOptions(url.hostname, {
    path: url.pathname + '?name=' + encodeURIComponent(name),
    method: 'POST',
    headers: {
      'User-Agent': UA,
      'Accept': 'application/vnd.github+json',
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/octet-stream',
      'Content-Length': stat.size,
    },
  });
  return new Promise((resolve) => {
    const req = https.request(opts, (res) => {
      let body = '';
      res.on('data', (c) => { body += c; });
      res.on('end', () => {
        if (res.statusCode === 201) resolve(true);
        else { console.error(`\n    HTTP ${res.statusCode}: ${body.slice(0, 300)}`); resolve(false); }
      });
    });
    req.on('error', (e) => { console.error(`\n    上传失败: ${e.message}`); resolve(false); });
    fs.createReadStream(file).pipe(req);
  });
}

async function uploadAll(token, uploadUrl) {
  const base = uploadUrl.replace(/\{[^}]*\}$/, '');
  const assets = collectAssets();
  if (!assets.length) {
    console.error('  ✗ 没有可上传的附件（请先运行 python tools/make_release.py）');
    return false;
  }
  let ok = true;
  for (const file of assets) {
    const name = toAsciiAssetName(path.basename(file));
    const size = fs.statSync(file).size;
    process.stdout.write(`  上传 ${name} (${(size / 1024).toFixed(1)} KB) ... `);
    const done = await uploadAsset(token, base, name, file);
    console.log(done ? '✓' : '✗');
    if (!done) ok = false;
  }
  return ok;
}

const RELEASE_BODY = [
  '## Lichii-zhCN v0.1.0',
  '',
  '面向 [zortos293/Lichii](https://github.com/zortos293/Lichii)（`nx2` 分支，2026-11-09 快照）的**第三方简体中文界面语言包**。',
  '目标是让「设置 → 界面 → 语言」下拉里能选到中文，并且以后换翻译只需替换一个 `.qm` 文件、重启即可。',
  '',
  '### 为什么需要它',
  '',
  '- 上游 `ENABLE_QT_TRANSLATION` 默认 OFF，官方 Release 也没打开 → 语言下拉只有 `<系统>` 和 `English`；',
  '- `.qm` 被编译进 exe 的 Qt 资源 `:/languages/`，原版程序不会读取程序目录下的文件；',
  '- 上游 `dist/languages/zh_CN.ts` 是 Eden 时代的，Lichii 改名与新增界面导致大量条目失配。',
  '',
  '因此本项目 = **重做的 `zh_CN.qm` + 一段最小外部加载补丁**（2 个函数 + 1 个 include）。',
  '',
  '### 安装',
  '',
  '- **已打补丁的 Lichii**：把 `Lichii-zhCN-v0.1.0.zip` 里的 `languages/` 解压到 `lichii.exe` 同级目录，重启后在「设置 → 界面 → 语言」选 `Chinese (China)`。以后更新只需替换 `zh_CN.qm`。',
  '- **官方原版**：首次必须应用 `patch/external-language-loader.patch` 并自行编译一次 Lichii（参见仓库 `docs/使用说明.md`）。本 Release **不含** Lichii 主程序。',
  '',
  '### 语言包数据',
  '',
  '| 项目 | 数值 |',
  '| --- | --- |',
  '| 源码骨架（Qt 6.8.3 `lupdate`） | 2282 条 / 101 context |',
  '| 继承上游译文（含 Eden → Lichii 品牌修正） | 1933 条 |',
  '| 新译 Lichii 新增界面文案 | 348 条 |',
  '| 已译 / 覆盖率 | 2281 条 / 100%（余 1 条为空白占位串） |',
  '',
  '验证：用 Qt 6.8.3 `QTranslator` 真实加载 QM，10/10 抽检精确命中，0 处占位符错误；重复构建 QM 哈希不变。',
  '',
  '### 合规',
  '',
  '独立第三方语言包，未向上游仓库创建 Issue / 分支 / 提交 / PR；不含游戏 ROM、固件、密钥或任天堂素材。',
  '补丁与工具以 GPL-3.0-or-later 提供，译文数据继承上游许可，详见仓库 `LICENSE.txt` 与 `docs/合规说明.md`。',
].join('\n');

async function createRelease(token, tag) {
  console.log(`创建 Release ${tag} ...`);
  const res = await api(token, 'POST', `/repos/${OWNER}/${REPO}/releases`, {
    tag_name: tag,
    name: `Lichii 简体中文语言包 ${tag}`,
    body: RELEASE_BODY,
    draft: false,
    prerelease: false,
  });
  if (res.status !== 201) {
    console.error('  ✗ 创建失败:', res.status, res.json && res.json.message);
    return false;
  }
  console.log(`  ✓ Release 已创建: ${res.json.html_url}`);
  return uploadAll(token, res.json.upload_url);
}

async function uploadAssetsOnly(token, tag) {
  const rel = await api(token, 'GET', `/repos/${OWNER}/${REPO}/releases/tags/${tag}`);
  if (rel.status !== 200) {
    console.error('  ✗ 找不到 Release:', rel.status, rel.json && rel.json.message);
    return false;
  }
  console.log(`Release ${rel.json.tag_name} (id ${rel.json.id})`);
  for (const a of rel.json.assets || []) {
    const del = await api(token, 'DELETE', `/repos/${OWNER}/${REPO}/releases/assets/${a.id}`);
    console.log(`  删除旧附件 ${a.name} -> ${del.status}`);
  }
  return uploadAll(token, rel.json.upload_url);
}

async function verify() {
  const res = await api(null, 'GET', `/repos/${OWNER}/${REPO}`);
  if (res.status !== 200) {
    console.error('  ✗ 仓库不可访问:', res.status, res.json && res.json.message);
    return false;
  }
  const r = res.json;
  console.log(`  ✓ ${r.full_name} | ${r.visibility} | default=${r.default_branch} | size=${r.size} KB`);
  const rel = await api(null, 'GET', `/repos/${OWNER}/${REPO}/releases/latest`);
  if (rel.status === 200) {
    console.log(`  ✓ 最新 Release: ${rel.json.tag_name} | 附件 ${rel.json.assets.length} 个`);
    for (const a of rel.json.assets) console.log(`     - ${a.name} (${a.size} bytes)`);
  } else {
    console.log('  · 暂无 Release');
  }
  return true;
}

// ---------------------------------------------------------------- 主流程
async function main() {
  const [cmd, arg] = process.argv.slice(2);
  const token = process.env.GH_TOKEN || '';
  if (!cmd) {
    console.log('用法: node tools/publish.js <create-repo|push|release|assets|all|verify> [tag]');
    process.exit(1);
  }
  if (cmd !== 'verify' && !token) {
    console.error('✗ 缺少 GH_TOKEN 环境变量');
    process.exit(1);
  }
  if ((cmd === 'release' || cmd === 'assets' || cmd === 'all') && !arg) {
    console.error('请指定 tag，例如 v0.1.0');
    process.exit(1);
  }
  try {
    if (cmd === 'verify') {
      process.exit(await verify() ? 0 : 1);
    } else if (cmd === 'create-repo') {
      process.exit(await createRepo(token) ? 0 : 1);
    } else if (cmd === 'push') {
      process.exit(pushCode(token) ? 0 : 1);
    } else if (cmd === 'release') {
      process.exit(await createRelease(token, arg) ? 0 : 1);
    } else if (cmd === 'assets') {
      process.exit(await uploadAssetsOnly(token, arg) ? 0 : 1);
    } else if (cmd === 'all') {
      if (!await createRepo(token)) process.exit(1);
      if (!pushCode(token)) process.exit(1);
      process.exit(await createRelease(token, arg) ? 0 : 1);
    } else {
      console.error('未知命令:', cmd);
      process.exit(1);
    }
  } catch (e) {
    console.error('执行失败:', e.message);
    process.exit(1);
  }
}

main();
