# 待补译字符串

- 源码可翻译字符串（去重）：2196
- `zh_CN.ts` 消息总数：1941
- 源码中未被 TS 覆盖：**481**

> 本表由 `tools/sync_strings.py` 静态扫描生成，可能包含 Qt lupdate 不会提取的字符串。
> 请以 `lupdate` 的实际输出为准。

| Context | Source | 出现文件 |
| --- | --- | --- |
| `AboutDialog` | <html><body><p><a href="https://github.com/zortos293/Eglantine">Source Code</a> \| <a href="https://github.com/zortos293/Eglantine/issues">Report an Issue</a> \| <a href="https://github.com/zortos293/Eglantine#credits-and-license">Credits a | `src/yuzu/aboutdialog.ui` |
| `AboutDialog` | <html><head/><body><p><span style=" font-size:28pt;">Lichii</span></p></body></html> | `src/yuzu/aboutdialog.ui` |
| `AboutDialog` | <html><head/><body><p><span style=" font-size:7pt;">&quot;Nintendo Switch&quot; is a trademark of Nintendo. Lichii is not affiliated with Nintendo in any way.</span></p></body></html> | `src/yuzu/aboutdialog.ui` |
| `AboutDialog` | About Lichii | `src/yuzu/aboutdialog.ui` |
| `ConfigureCpuDebug` | <div style="white-space: nowrap">This optimization speeds up exclusive memory accesses by the guest program.</div>             <div style="white-space: nowrap">Enabling it reduces the overhead of fastmem failure of exclusive memory accesses | `src/yuzu/configuration/configure_cpu_debug.ui` |
| `ConfigureCpuDebug` | <div style="white-space: nowrap">This optimization speeds up memory accesses by allowing invalid memory accesses to succeed.</div>             <div style="white-space: nowrap">Enabling it reduces the overhead of all memory accesses and has  | `src/yuzu/configuration/configure_cpu_debug.ui` |
| `ConfigureCpuDebug` | <div style="white-space: nowrap">This optimization speeds up memory accesses by the guest program.</div>             <div style="white-space: nowrap">Enabling it causes guest memory reads/writes to be done directly into memory and make use  | `src/yuzu/configuration/configure_cpu_debug.ui` |
| `ConfigureCpuDebug` | <div style="white-space: nowrap">This optimization speeds up memory accesses by the guest program.</div>             <div style="white-space: nowrap">Enabling it inlines accesses to PageTable::pointers into emitted code.</div>             < | `src/yuzu/configuration/configure_cpu_debug.ui` |
| `ConfigureCpuDebug` | <div style="white-space: nowrap">When enabled, a misalignment is only triggered when an access crosses a page boundary.</div>             <div style="white-space: nowrap">When disabled, a misalignment is triggered on all misaligned accesses | `src/yuzu/configuration/configure_cpu_debug.ui` |
| `ConfigureCpuDebug` | <div>Enable a two-tiered dispatch system. A faster dispatcher written in assembly has a small MRU cache of jump destinations is used first. If that fails, dispatch falls back to the slower C++ dispatcher.</div> | `src/yuzu/configuration/configure_cpu_debug.ui` |
| `ConfigureCpuDebug` | <div>Enables an IR optimization that reduces unnecessary accesses to the CPU context structure.</div> | `src/yuzu/configuration/configure_cpu_debug.ui` |
| `ConfigureCpuDebug` | <div>Enables IR optimizations that involve constant propagation.</div> | `src/yuzu/configuration/configure_cpu_debug.ui` |
| `ConfigureCpuDebug` | <div>Enables miscellaneous IR optimizations.</div> | `src/yuzu/configuration/configure_cpu_debug.ui` |
| `ConfigureCpuDebug` | <div>This optimization avoids dispatcher lookups by allowing emitted basic blocks to jump directly to other basic blocks if the destination PC is static.</div> | `src/yuzu/configuration/configure_cpu_debug.ui` |
| `ConfigureCpuDebug` | <div>This optimization avoids dispatcher lookups by keeping track potential return addresses of BL instructions. This approximates what happens with a return stack buffer on a real CPU.</div> | `src/yuzu/configuration/configure_cpu_debug.ui` |
| `ConfigureDebug` | (bitmask) | `src/yuzu/configuration/configure_debug.ui` |
| `ConfigureDebug` | **This will be reset automatically when Lichii closes. | `src/yuzu/configuration/configure_debug.ui` |
| `ConfigureDialog` | Lichii Configuration | `src/yuzu/configuration/configure.ui` |
| `ConfigureInputAdvanced` | Requires restarting Lichii | `src/yuzu/configuration/configure_input_advanced.ui` |
| `ConfigurePerGame` | Allow online lookup | `src/yuzu/configuration/configure_per_game.ui` |
| `ConfigurePerGame` | Detect Icon | `src/yuzu/configuration/configure_per_game.ui` |
| `ConfigurePerGame` | If no local icon is found, send the game name to GitHub, Wikipedia and Bing to look for an icon. Disabled by default. | `src/yuzu/configuration/configure_per_game.ui` |
| `ConfigurePerGame` | Preview a local icon next to the archive. Online lookup is optional. Apply or OK saves changes. | `src/yuzu/configuration/configure_per_game.ui` |
| `ConfigurePerGame` | Preview a local image as the game icon. Apply or OK saves changes. | `src/yuzu/configuration/configure_per_game.ui` |
| `ConfigurePerGame` | Upload Icon... | `src/yuzu/configuration/configure_per_game.ui` |
| `ConfigureTouchscreenAdvanced` | Warning: The settings in this page affect the inner workings of Lichii's emulated touchscreen. Changing them may result in undesirable behavior, such as the touchscreen partially or not working. You should only use this page if you know wha | `src/yuzu/configuration/configure_touchscreen_advanced.ui` |
| `ConfigureUi` | Screenshots Path: | `src/yuzu/configuration/configure_ui.ui` |
| `ConfigureWeb` | Lichii Web Service | `src/yuzu/configuration/configure_web.ui` |
| `ConfigureWeb` | Token: | `src/yuzu/configuration/configure_web.ui` |
| `ConfigureWeb` | Username: | `src/yuzu/configuration/configure_web.ui` |
| `DepsDialog` | <html><head/><body><p><span style=" font-size:28pt;">Lichii Dependencies</span></p></body></html> | `src/yuzu/deps_dialog.ui` |
| `DepsDialog` | <html><head/><body><p>The projects that make Lichii possible</p></body></html> | `src/yuzu/deps_dialog.ui` |
| `DepsDialog` | Lichii Dependencies | `src/yuzu/deps_dialog.ui` |
| `Hotkeys` | Exit Eglantine | `src/qt_common/config/uisettings.cpp` |
| `Hotkeys` | Exit Lichii | `src/yuzu/configuration/configure_hotkeys.cpp` |
| `MainWindow` | &About Lichii | `src/yuzu/main.ui` |
| `MainWindow` | &Lichii Dependencies | `src/yuzu/main.ui` |
| `MainWindow` | FSR 1 | `src/qt_common/config/shared_translation.h` |
| `MainWindow` | FSR 1 Soft | `src/qt_common/config/shared_translation.h` |
| `MainWindow` | Lichii | `src/yuzu/main.ui` |
| `MainWindow` | LSFG | `src/qt_common/config/shared_translation.h` |
| `MainWindow` | Open &Lichii Folders | `src/yuzu/main.ui` |
| `MainWindow` | Optical Flow | `src/qt_common/config/shared_translation.h` |
| `NewUserDialog` | Lichii | `src/yuzu/configuration/system/new_user_dialog.ui` |
| `NupEditDialog` | Chinese (Simplified) | `src/yuzu/nup_dialogs.cpp` |
| `NupEditDialog` | Chinese (Traditional) | `src/yuzu/nup_dialogs.cpp` |
| `NupEditDialog` | Dutch | `src/yuzu/nup_dialogs.cpp` |
| `NupEditDialog` | English (UK) | `src/yuzu/nup_dialogs.cpp` |
| `NupEditDialog` | French | `src/yuzu/nup_dialogs.cpp` |
| `NupEditDialog` | French (Canada) | `src/yuzu/nup_dialogs.cpp` |
| `NupEditDialog` | German | `src/yuzu/nup_dialogs.cpp` |
| `NupEditDialog` | Italian | `src/yuzu/nup_dialogs.cpp` |
| `NupEditDialog` | Japanese | `src/yuzu/nup_dialogs.cpp` |
| `NupEditDialog` | Korean | `src/yuzu/nup_dialogs.cpp` |
| `NupEditDialog` | Portuguese | `src/yuzu/nup_dialogs.cpp` |
| `NupEditDialog` | Portuguese (Brazil) | `src/yuzu/nup_dialogs.cpp` |
| `NupEditDialog` | Russian | `src/yuzu/nup_dialogs.cpp` |
| `NupEditDialog` | Spanish | `src/yuzu/nup_dialogs.cpp` |
| `NupEditDialog` | Spanish (Latin America) | `src/yuzu/nup_dialogs.cpp` |
| `RyujinxDialog` | From Lichii | `src/yuzu/ryujinx_dialog.ui` |
| `RyujinxDialog` | Linking save data to Ryujinx lets both Ryujinx and Lichii reference the same save files for your games.  By selecting "From Lichii", previous save data stored in Ryujinx will be deleted, and vice versa for "From Ryujinx". | `src/yuzu/ryujinx_dialog.ui` |
| `UpdateDialog` | Would you like to download this update? | `src/yuzu/updater/update_dialog.ui` |
| `bootmanager` | Lichii has not been compiled with OpenGL support. | `src/yuzu/bootmanager.cpp` |
| `bootmanager` | Your GPU may not support one or more required OpenGL extensions. Please ensure you | `src/yuzu/bootmanager.cpp` |
| `bootmanager` | Your GPU may not support OpenGL 4.6, or you do not have the | `src/yuzu/bootmanager.cpp` |
| `chat_room` | Are you sure you would like to <b>kick and ban</b> %1?  This would | `src/yuzu/multiplayer/chat_room.cpp` |
| `chat_room` | When you block a player, you will no longer receive chat messages from | `src/yuzu/multiplayer/chat_room.cpp` |
| `compatibility_report` | All report fields in the preview will be public. Logs, files, | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | An X handle must contain 1–15 letters, digits or underscores, with an optional @. | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Catalog search failed. Check your connection and retry explicitly. | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Check %1: required fields must be filled, within their length limit, | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Check the search text. | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Choose your assessment | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Choose your own compatibility assessment. | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Clear draft | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Compatibility | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Confirm game | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Confirmed: %1 (catalog ID %2) | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Draft cleared. Nothing was sent by clearing it. | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Experience | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Game title to search | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Game version | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | GPU driver / OpenGL version | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Graphics API | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | How far did you play? | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | I understand my name, optional X handle, report text, | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Launch settings | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Lichii build | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Mods (optional) | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | My report contains no game files, keys, firmware, | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Next | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | No catalog game confirmed. | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | No valid receipt was received. Delivery may have succeeded. | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Open public report | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Operating system | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Page %1 of %2. Select the exact game and press Confirm game. | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Prefilled values describe launch settings, not measured | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Previous | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Public nickname | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Public preview | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | RAM (optional) | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Rate limit reached. Wait %1 seconds, then retry explicitly. | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Report submitted. It is public. Thank you. | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Search catalog | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Search for and confirm the catalog game first. | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Search sends only the text above to lichii.zortos.me. | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Searching catalog… Cancel closes the dialog and stops this request. | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Share your experience with the latest completed session. Nothing is sent until you | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Steps to reproduce (optional) | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Submit compatibility report | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Submit report | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Submitting… Closing stops waiting, but cannot retract a report the | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Summary | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | System and settings | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | The catalog returned an invalid response. No game was confirmed. | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | The report is too large. | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | The server rejected the report. Review the fields and length | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | The server rejected the request (HTTP %1). No automatic retry was made. | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | The server rejected these fields: %1. Review them before | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | The server rejected this submission identity. Edit the draft to start | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | The server returned an invalid receipt. The report may have | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | Updates (optional) | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | What worked or failed? | `src/yuzu/compatibility_report.cpp` |
| `compatibility_report` | X handle (optional) | `src/yuzu/compatibility_report.cpp` |
| `configure_filesystem` | Save data exists in both the old and new locations. | `src/yuzu/configuration/configure_filesystem.cpp` |
| `configure_filesystem` | Save data has been migrated successfully. | `src/yuzu/configuration/configure_filesystem.cpp` |
| `configure_filesystem` | Would you like to migrate your save data to the new location? | `src/yuzu/configuration/configure_filesystem.cpp` |
| `configure_general` | Lichii | `src/yuzu/configuration/configure_general.cpp` |
| `configure_general` | This reset all settings and remove all per-game configurations. This will not delete | `src/yuzu/configuration/configure_general.cpp` |
| `configure_graphics` | Hz | `src/yuzu/configuration/configure_graphics.cpp` |
| `configure_graphics_extensions` | Extended Dynamic State is disabled on macOS due to MoltenVK | `src/yuzu/configuration/configure_graphics_extensions.cpp` |
| `configure_input` | Microphone | `src/yuzu/configuration/configure_input.cpp` |
| `configure_input_player` | After pressing OK, first move your joystick horizontally, and then | `src/yuzu/configuration/configure_input_player.cpp` |
| `configure_microphone` | %1 (unavailable) | `src/yuzu/configuration/configure_microphone.cpp` |
| `configure_microphone` | %1% | `src/yuzu/configuration/configure_microphone.cpp` |
| `configure_microphone` | Choose the microphone used by games. Start a test and speak | `src/yuzu/configuration/configure_microphone.cpp` |
| `configure_microphone` | Input level: | `src/yuzu/configuration/configure_microphone.cpp` |
| `configure_microphone` | Listening. Speak into your microphone. | `src/yuzu/configuration/configure_microphone.cpp` |
| `configure_microphone` | Microphone | `src/yuzu/configuration/configure_microphone.cpp` |
| `configure_microphone` | Microphone disconnected or capture failed. | `src/yuzu/configuration/configure_microphone.cpp` |
| `configure_microphone` | Microphone input is unavailable. Choose an available input device. | `src/yuzu/configuration/configure_microphone.cpp` |
| `configure_microphone` | Microphone volume: | `src/yuzu/configuration/configure_microphone.cpp` |
| `configure_microphone` | Refresh devices | `src/yuzu/configuration/configure_microphone.cpp` |
| `configure_microphone` | Start microphone test | `src/yuzu/configuration/configure_microphone.cpp` |
| `configure_microphone` | Stop emulation to change the microphone input device or volume. | `src/yuzu/configuration/configure_microphone.cpp` |
| `configure_microphone` | Stop microphone test | `src/yuzu/configuration/configure_microphone.cpp` |
| `configure_microphone` | System default | `src/yuzu/configuration/configure_microphone.cpp` |
| `configure_microphone` | Unable to open the microphone. Check the device and microphone | `src/yuzu/configuration/configure_microphone.cpp` |
| `configure_motion_touch` | Could not receive valid data from the server.<br>Please verify | `src/yuzu/configuration/configure_motion_touch.cpp` |
| `configure_motion_touch` | Lichii | `src/yuzu/configuration/configure_motion_touch.cpp` |
| `configure_motion_touch` | UDP Test or calibration configuration is in progress.<br>Please | `src/yuzu/configuration/configure_motion_touch.cpp` |
| `configure_mouse_panning` | Mouse panning works better with a deadzone of 0% and a range of 100%. Current | `src/yuzu/configuration/configure_mouse_panning.cpp` |
| `configure_mouse_panning` | Real mouse input and mouse panning are incompatible. Please disable the | `src/yuzu/configuration/configure_mouse_panning.cpp` |
| `configure_per_game` | Detect Icon | `src/yuzu/configuration/configure_per_game.cpp` |
| `configure_per_game` | Detecting... | `src/yuzu/configuration/configure_per_game.cpp` |
| `configure_per_game` | Edit the game name stored in the NUP metadata | `src/yuzu/configuration/configure_per_game.cpp` |
| `configure_per_game` | Enter game name... | `src/yuzu/configuration/configure_per_game.cpp` |
| `configure_per_game` | Failed to update NUP metadata: %1 | `src/yuzu/configuration/configure_per_game.cpp` |
| `configure_per_game` | Images (*.png *.jpg *.jpeg *.bmp *.webp);;All Files (*) | `src/yuzu/configuration/configure_per_game.cpp` |
| `configure_per_game` | Invalid Image | `src/yuzu/configuration/configure_per_game.cpp` |
| `configure_per_game` | Please enter a game name first so the icon can be detected. | `src/yuzu/configuration/configure_per_game.cpp` |
| `configure_per_game` | Select a PNG, JPEG, BMP or WebP image up to 8 MiB, | `src/yuzu/configuration/configure_per_game.cpp` |
| `configure_per_game` | Select Game Icon | `src/yuzu/configuration/configure_per_game.cpp` |
| `configure_per_game` | Stop emulation before changing NUP metadata. | `src/yuzu/configuration/configure_per_game.cpp` |
| `configure_per_game` | The game name is too long to search. | `src/yuzu/configuration/configure_per_game.cpp` |
| `configure_per_game` | Update NUP Metadata | `src/yuzu/configuration/configure_per_game.cpp` |
| `configure_per_game_addons` | Once deleted, these can NOT be recovered. Are you 100% sure | `src/yuzu/configuration/configure_per_game_addons.cpp` |
| `configure_per_game_addons` | Only mods, cheats, and patches can be deleted. To delete | `src/yuzu/configuration/configure_per_game_addons.cpp` |
| `configure_per_game_addons` | You are about to delete the following installed mods: | `src/yuzu/configuration/configure_per_game_addons.cpp` |
| `configure_post_processing` | No effects in use. Pick a preset and press Apply, or add effects one | `src/yuzu/configuration/configure_post_processing.cpp` |
| `configure_post_processing` | No usable ReShade FX effects were found. Place .fx files in the post_shaders | `src/yuzu/configuration/configure_post_processing.cpp` |
| `content` | All previous data in this directory will be deleted. Are you sure you wish to | `src/qt_common/util/content.cpp` |
| `content` | Ensure you have read permissions on the targeted directory and try | `src/qt_common/util/content.cpp` |
| `content` | Failed to clean up extracted firmware cache. | `src/qt_common/util/content.cpp` |
| `content` | Firmware installation cancelled, firmware may be in a bad state or corrupted. | `src/qt_common/util/content.cpp` |
| `content` | Once deleted, your data will NOT come back! | `src/qt_common/util/content.cpp` |
| `content` | This game may require firmware to function properly, and you don't have any installed. | `src/qt_common/util/content.cpp` |
| `content` | UNEXPECTED BAD THINGS MAY HAPPEN IF YOU DON'T READ THIS!<br> | `src/qt_common/util/content.cpp` |
| `fs` | Could not find a valid Ryujinx installation. This may typically occur if you are | `src/qt_common/util/fs.cpp` |
| `game` | This will create a shortcut to the current AppImage. This may | `src/qt_common/util/game.cpp` |
| `game_list` | Build Shader Precache | `src/yuzu/game/game_list.cpp` |
| `game_list` | Convert to NUP... | `src/yuzu/game/game_list.cpp` |
| `game_list` | Delete Shader Precache | `src/yuzu/game/game_list.cpp` |
| `game_list` | Dump NUP... | `src/yuzu/game/game_list.cpp` |
| `game_list` | Edit NUP Metadata... | `src/yuzu/game/game_list.cpp` |
| `game_list` | Rebuild Shader Precache | `src/yuzu/game/game_list.cpp` |
| `game_list` | Submit compatibility report… | `src/yuzu/game/game_list.cpp` |
| `game_list` | u25B2 Move Up | `src/yuzu/game/game_list.cpp` |
| `game_list` | u25bc Move Down | `src/yuzu/game/game_list.cpp` |
| `host_room` | Failed to announce the room to the public lobby. In order to host a | `src/yuzu/multiplayer/host_room.cpp` |
| `icon_search` | API key | `src/yuzu/util/icon_search.cpp` |
| `icon_search` | Choose an Icon | `src/yuzu/util/icon_search.cpp` |
| `icon_search` | Could not reach the icon sources (%1). Check your connection and try again. | `src/yuzu/util/icon_search.cpp` |
| `icon_search` | Create a free key on the <a href="%1">SteamGridDB API preferences</a> page. | `src/yuzu/util/icon_search.cpp` |
| `icon_search` | Find Icon | `src/yuzu/util/icon_search.cpp` |
| `icon_search` | No matching icon was found on switchiconshowdown.com or SteamGridDB. Try a | `src/yuzu/util/icon_search.cpp` |
| `icon_search` | No matching icon was found on switchiconshowdown.com. A | `src/yuzu/util/icon_search.cpp` |
| `icon_search` | Please enter a game name first so the icon can be found. | `src/yuzu/util/icon_search.cpp` |
| `icon_search` | Searching for an icon failed unexpectedly: %1 | `src/yuzu/util/icon_search.cpp` |
| `icon_search` | Searching for an icon took longer than %1 seconds and was stopped. Check | `src/yuzu/util/icon_search.cpp` |
| `icon_search` | SteamGridDB API Key | `src/yuzu/util/icon_search.cpp` |
| `icon_search` | SteamGridDB has several icons for this game. Pick one: | `src/yuzu/util/icon_search.cpp` |
| `icon_search` | SteamGridDB rejected the saved API key. | `src/yuzu/util/icon_search.cpp` |
| `loading_screen` | Precaching shaders %1 / %2 | `src/yuzu/loading_screen.cpp` |
| `loading_screen` | Skip | `src/yuzu/loading_screen.cpp` |
| `loading_screen` | Start the game now. The shaders not precached yet are precached | `src/yuzu/loading_screen.cpp` |
| `main_window` | %1 (IDLE) | `src/yuzu/main_window.cpp` |
| `main_window` | %n file(s) failed to install | `src/yuzu/main_window.cpp` |
| `main_window` | %n file(s) were newly installed | `src/yuzu/main_window.cpp` |
| `main_window` | %n file(s) were overwritten | `src/yuzu/main_window.cpp` |
| `main_window` | Are you sure you want to close Lichii? | `src/yuzu/main_window.cpp` |
| `main_window` | Close the running game first. | `src/yuzu/main_window.cpp` |
| `main_window` | Conversion Cancelled | `src/yuzu/main_window.cpp` |
| `main_window` | Conversion Complete | `src/yuzu/main_window.cpp` |
| `main_window` | Conversion Failed | `src/yuzu/main_window.cpp` |
| `main_window` | Conversion in Progress | `src/yuzu/main_window.cpp` |
| `main_window` | Convert to NUP | `src/yuzu/main_window.cpp` |
| `main_window` | Converting to NUP | `src/yuzu/main_window.cpp` |
| `main_window` | Could not check for updates: GitHub answered with HTTP %1. | `src/yuzu/main_window.cpp` |
| `main_window` | Could not check for updates: GitHub rate limit reached. Lichii will try again at | `src/yuzu/main_window.cpp` |
| `main_window` | Could not restore the previous version: %1 | `src/yuzu/main_window.cpp` |
| `main_window` | Current emulation speed. Values higher or lower than 100% | `src/yuzu/main_window.cpp` |
| `main_window` | Delete Shader Precache | `src/yuzu/main_window.cpp` |
| `main_window` | Delete the shader precache files of this game? They are built | `src/yuzu/main_window.cpp` |
| `main_window` | Disabling the web applet can lead to undefined behavior and should only be used | `src/yuzu/main_window.cpp` |
| `main_window` | Edit Complete | `src/yuzu/main_window.cpp` |
| `main_window` | Edit Failed | `src/yuzu/main_window.cpp` |
| `main_window` | Editing NUP Metadata | `src/yuzu/main_window.cpp` |
| `main_window` | Extract NUP | `src/yuzu/main_window.cpp` |
| `main_window` | Extracting NUP | `src/yuzu/main_window.cpp` |
| `main_window` | Extraction Complete | `src/yuzu/main_window.cpp` |
| `main_window` | Extraction Failed | `src/yuzu/main_window.cpp` |
| `main_window` | Failed to restore | `src/yuzu/main_window.cpp` |
| `main_window` | FG %1 %2X | `src/yuzu/main_window.cpp` |
| `main_window` | FG %1 AUTO | `src/yuzu/main_window.cpp` |
| `main_window` | FG UNAVAILABLE | `src/yuzu/main_window.cpp` |
| `main_window` | Frame generation is off. | `src/yuzu/main_window.cpp` |
| `main_window` | Frame generation is on but generated no frames in the last half second. It pauses | `src/yuzu/main_window.cpp` |
| `main_window` | Frame generation is on but not running. %1 | `src/yuzu/main_window.cpp` |
| `main_window` | Frame generation is on.%1 Whether it runs shows here once a game starts. | `src/yuzu/main_window.cpp` |
| `main_window` | Frame generation is running.%1 | `src/yuzu/main_window.cpp` |
| `main_window` | Frame generation needs the Vulkan renderer. | `src/yuzu/main_window.cpp` |
| `main_window` | Game preparation failed. See the log for details. | `src/yuzu/main_window.cpp` |
| `main_window` | Games cannot be started while the shader precache is being | `src/yuzu/main_window.cpp` |
| `main_window` | Go back to the version this one replaced? Your settings and data are not | `src/yuzu/main_window.cpp` |
| `main_window` | Handheld controller can't be used on docked mode. Pro | `src/yuzu/main_window.cpp` |
| `main_window` | Hardware requirements not met | `src/yuzu/main_window.cpp` |
| `main_window` | How many frames per second the game is currently displaying. | `src/yuzu/main_window.cpp` |
| `main_window` | In order to submit a game compatibility test case, you must set up your web     //             token | `src/yuzu/main_window.cpp` |
| `main_window` | Installable Switch File (*.nca *.nsp *.nsz *.xci *.xcz);;Nintendo Content Archive | `src/yuzu/main_window.cpp` |
| `main_window` | It adds up to %1 frames per game frame to reach %2 FPS. | `src/yuzu/main_window.cpp` |
| `main_window` | It also pauses while the game already reaches %1 FPS. | `src/yuzu/main_window.cpp` |
| `main_window` | Lichii | `src/yuzu/main_window.cpp` |
| `main_window` | Lichii could not allocate the game's memory. Close other applications and | `src/yuzu/main_window.cpp` |
| `main_window` | LSFG needs Lossless.dll from Lossless Scaling in the "lossless" folder | `src/yuzu/main_window.cpp` |
| `main_window` | Missing yuzu Account | `src/yuzu/main_window.cpp` |
| `main_window` | NO FG | `src/yuzu/main_window.cpp` |
| `main_window` | Not enough memory to start the game | `src/yuzu/main_window.cpp` |
| `main_window` | Please select the how you would like the RomFS dumped.<br>Full will copy all of the | `src/yuzu/main_window.cpp` |
| `main_window` | Please select the type of title you would like to install this NCA as: (In | `src/yuzu/main_window.cpp` |
| `main_window` | Precache now | `src/yuzu/main_window.cpp` |
| `main_window` | Precache Shaders | `src/yuzu/main_window.cpp` |
| `main_window` | Preparing game files... | `src/yuzu/main_window.cpp` |
| `main_window` | Recommended Mario Kart World settings | `src/yuzu/main_window.cpp` |
| `main_window` | Restart Lichii to apply the X11 backend. | `src/yuzu/main_window.cpp` |
| `main_window` | Restore Previous Version | `src/yuzu/main_window.cpp` |
| `main_window` | Restore Previous Version... | `src/yuzu/main_window.cpp` |
| `main_window` | Resume Conversion | `src/yuzu/main_window.cpp` |
| `main_window` | Resume the interrupted conversion? | `src/yuzu/main_window.cpp` |
| `main_window` | Shader Precache in Progress | `src/yuzu/main_window.cpp` |
| `main_window` | Shaders are being precached. Try again when it is done. | `src/yuzu/main_window.cpp` |
| `main_window` | Start without | `src/yuzu/main_window.cpp` |
| `main_window` | The conversion can be resumed by choosing | `src/yuzu/main_window.cpp` |
| `main_window` | The currently running application has requested Lichii to not exit. | `src/yuzu/main_window.cpp` |
| `main_window` | The files could not be deleted: %1 | `src/yuzu/main_window.cpp` |
| `main_window` | The NUP metadata was updated. | `src/yuzu/main_window.cpp` |
| `main_window` | The NUP was created and the loose folder was | `src/yuzu/main_window.cpp` |
| `main_window` | The NUP was created. You can delete the loose | `src/yuzu/main_window.cpp` |
| `main_window` | The NUP was extracted. You can delete the NUP file if you no longer | `src/yuzu/main_window.cpp` |
| `main_window` | The shaders of this game are not precached yet. Precache them now? | `src/yuzu/main_window.cpp` |
| `main_window` | The target archive already exists: %1 | `src/yuzu/main_window.cpp` |
| `main_window` | The target directory already exists: %1 | `src/yuzu/main_window.cpp` |
| `main_window` | There is not enough free space at %1 to extract the RomFS. Please | `src/yuzu/main_window.cpp` |
| `main_window` | There was an error copying the RomFS files or the user | `src/yuzu/main_window.cpp` |
| `main_window` | This build was compiled without frame generation. | `src/yuzu/main_window.cpp` |
| `main_window` | This game cannot be started while its dump is being | `src/yuzu/main_window.cpp` |
| `main_window` | This game is being converted. Try again when it is done. | `src/yuzu/main_window.cpp` |
| `main_window` | This GPU can't write to the window's swapchain format from a shader, so | `src/yuzu/main_window.cpp` |
| `main_window` | This GPU lacks Vulkan features LSFG needs (Vulkan memory model, null | `src/yuzu/main_window.cpp` |
| `main_window` | This is usually caused by outdated GPU drivers. | `src/yuzu/main_window.cpp` |
| `main_window` | Time taken to emulate a Switch frame, not counting framelimiting or v-sync. For | `src/yuzu/main_window.cpp` |
| `main_window` | To avoid possible conflicts, we discourage users from installing base games to the | `src/yuzu/main_window.cpp` |
| `main_window` | Unable to prepare game files | `src/yuzu/main_window.cpp` |
| `main_window` | Use the recommended settings for Mario Kart World? | `src/yuzu/main_window.cpp` |
| `main_window` | Wayland is known to have significant performance issues and mysterious bugs. | `src/yuzu/main_window.cpp` |
| `main_window` | Your system does not meet the recommended hardware     //                               requirements. | `src/yuzu/main_window.cpp` |
| `main_window` | Your system does not meet the recommended hardware     //                           requirements. | `src/yuzu/main_window.cpp` |
| `migration_worker` | Citron | `src/yuzu/migration_worker.h` |
| `migration_worker` | If you wish to clean up the files which were left in the old | `src/yuzu/migration_worker.cpp` |
| `migration_worker` | Linking the old directory failed. You may need to re-run with | `src/yuzu/migration_worker.cpp` |
| `migration_worker` | Note that your configuration and data will be shared with %1. | `src/yuzu/migration_worker.cpp` |
| `migration_worker` | Sudachi | `src/yuzu/migration_worker.h` |
| `migration_worker` | Suyu | `src/yuzu/migration_worker.h` |
| `migration_worker` | Yuzu | `src/yuzu/migration_worker.h` |
| `mod` | Could not detect mod type automatically. Please manually | `src/qt_common/util/mod.cpp` |
| `nup_dialogs` | %1 / %2 MB  -  %3 / %4 files | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | %1 MB/s  -  about %2:%3 left | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | %1% | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | <b>File</b><br>%1 | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | <b>Source</b><br>%1<br><b>Target</b><br>%2 | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Approximate space needed: %1 MB. Free on the target volume: | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Auto-detect (nothing found in the dump) | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Auto-detect: %1 (from %2) | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Cancelling... | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Choose Icon | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Choose Icon... | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Convert | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Convert to NUP | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Current icon in the NUP. | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Custom icon, stored as %1x%1 JPEG. | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Drop an icon here or click to browse | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Drop an image here or click to browse | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Drop to replace | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | e.g. 1.2.0 | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Edit NUP Metadata | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Empty fields remove that metadata. The change is written in place; | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Find Icon Online... | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Free space is less than the estimate. | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Icon | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Icon found in the dump. | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Icon will be removed. | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Images (*.png *.jpg *.jpeg *.bmp *.webp);;All Files (*) | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Localized names | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Localized names (%1 set) | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Low storage: delete the original files as they are packed | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Name shown in the game list | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | No icon found in the dump. Add one, or the NUP will have none. | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | No icon in the NUP. Add one, or it will have none. | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Preparing... | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Publisher | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Publisher shown in the game list | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Release to use this image | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Remove Icon | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Same as Name | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Searching... | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Set manually: | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | That file could not be read as an image. | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | The icon that was found could not be read. | `src/yuzu/nup_dialogs.cpp` |
| `nup_dialogs` | Use Detected | `src/yuzu/nup_dialogs.cpp` |
| `path` | Failed to create or open shader cache for this title, | `src/qt_common/util/path.cpp` |
| `qt_error` | An error occurred on %1 at %2. Please try again or contact the developer of the | `src/yuzu/applets/qt_error.cpp` |
| `shader_warm_dialog` | %1: %L2 | `src/yuzu/shader_warm_dialog.cpp` |
| `shader_warm_dialog` | %1: %L2 / %L3 | `src/yuzu/shader_warm_dialog.cpp` |
| `shader_warm_dialog` | Close | `src/yuzu/shader_warm_dialog.cpp` |
| `shader_warm_dialog` | Compute programs: %L1 | `src/yuzu/shader_warm_dialog.cpp` |
| `shader_warm_dialog` | It is built on the loading screen when Precache shaders before game start is | `src/yuzu/shader_warm_dialog.cpp` |
| `shader_warm_dialog` | No details were given. | `src/yuzu/shader_warm_dialog.cpp` |
| `shader_warm_dialog` | Precache shaders: %1 | `src/yuzu/shader_warm_dialog.cpp` |
| `shader_warm_dialog` | Shader precache could not be built. | `src/yuzu/shader_warm_dialog.cpp` |
| `shader_warm_dialog` | Shader precache is ready. | `src/yuzu/shader_warm_dialog.cpp` |
| `shader_warm_dialog` | Shader precache stopped. | `src/yuzu/shader_warm_dialog.cpp` |
| `shader_warm_dialog` | Skipped (could not be read or converted): %L1 | `src/yuzu/shader_warm_dialog.cpp` |
| `shader_warm_dialog` | Starting | `src/yuzu/shader_warm_dialog.cpp` |
| `shader_warm_dialog` | Stopping | `src/yuzu/shader_warm_dialog.cpp` |
| `shader_warm_dialog` | The game files have no compute shaders to prepare. | `src/yuzu/shader_warm_dialog.cpp` |
| `shader_warm_dialog` | The shaders your earlier play sessions saved are still precached. | `src/yuzu/shader_warm_dialog.cpp` |
| `shader_warm_dialog` | This game keeps its shaders in a format Lichii can't read, so none | `src/yuzu/shader_warm_dialog.cpp` |
| `shared_translation` | Accelerates BCn 3D texture decoding using GPU compute. | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Allows saving shaders to storage for faster loading on following game | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Allows the fragment shader to execute per sample in a multi-sampled fragment | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | AMD FidelityFX Super Resolution 1 (FSR 1) | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | AMD FidelityFX Super Resolution 1, softer sharpening | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Ask | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Auto (shader extent) | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Auto Flow Scale | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Bounded wait | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Builds shaders on the loading screen, on every CPU thread, so they don't stutter | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Caps how often the game presents, so the game itself runs at this rate. 0 leaves | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Controls how the emulator manages frame pacing to reduce stuttering and make the | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Controls the game's maximum rendering speed, but it's up to each game if it runs | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Controls the GPU emulation mode. Most games render fine with Fast, but Accurate is still | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Controls the number of features that can be used in Extended Dynamic State. | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Controls the quality of texture rendering at oblique angles. Safe to set at 16x on | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Determines the number of depth slices processed in a single dispatch. | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Dump Optical Flow | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Enable Frame Generation | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Enables access to previous buffer states. This option may improve rendering | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Enables GPU vendor-specific pipeline cache. This option can improve shader loading | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Enables Horizon's built-in overlay applet. Press and hold the home button for 1 | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Ensures data consistency between compute and memory operations. This option fixes | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | FIFO (VSync) does not drop frames or exhibit tearing but is limited by the screen | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Flow Scale | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Forces the game to use its native 30 FPS mode at normal game speed. | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Forces to render at a different resolution. | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | FPS Limit | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Frame Generation Multiplier | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Frame Generation Type | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Frame rate limit (Switch 2): | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Full binding | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | How much of a Switch 2 compute shader's storage buffer is treated as written by | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Increases the amount of emulated RAM. Doesn't affect performance/stability but may | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Lets the game adjust between 30 and 60 FPS using whole-frame timing to maintain | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Lossless Scaling (LSFG) | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Makes the game believe GPU work finishes faster than it does, so it stops lowering | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Mario Kart World: 30 FPS mode | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Mario Kart World: dynamic FPS (experimental) | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Most GPUs lack support for ASTC textures and must decompress to an | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Native compute write mark: | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | No sharpening | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Ocarina of Time anti-aliasing: | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Only applies when asynchronous shader building is on. Decides what a Switch 2 draw | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Optical Flow Interpolation (built-in) | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Overrides prompts asking to confirm stopping the emulation. Enabling | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Pin GPU threads to their own cores | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Pins the emulator's GPU threads to dedicated physical CPU cores and keeps the | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Pipeline wait per frame (ms): | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Precache shaders before game start: | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Queue Target | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Raises the clock the emulated CPU reports, which removes some FPS limiters. | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Rate of the Switch 2 VSync event that games start their frames on (default 60 Hz). | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | RCAS Sharpness: | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Required by some games. This setting only exists for Intel | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Run the game at normal speed during video playback, even when the framerate is | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Runs a Switch 2 game's own DLSS (its upscaling network, translated for this GPU) | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Runs work in the background while waiting for graphics commands to keep the GPU from | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Selects if the console is in Docked or Handheld mode. Games will change | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Selects whether the emulator should prefer to conserve memory or make maximum usage | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Set a custom value of CPU ticks. Higher values can increase performance, but may | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Sets the maximum amount of texture data (in MiB) processed per frame. | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Sets the maximum size (MiB) for GPU-based texture unswizzling. | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Skip | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Skips certain cache invalidations during memory updates, reducing CPU usage and | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Specifies how videos should be decoded. It can either use the CPU or the GPU for | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Strength of RCAS (AMD's contrast-adaptive sharpening) on the upscaler used in place | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Stretches the renderer to fit the specified aspect ratio. Most games only support | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Switch 2 draws with unbuilt pipelines: | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Synchronizes CPU core speed with the game's maximum rendering speed to boost FPS | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Target Frame Rate | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | The anti-aliasing method to use. SMAA offers the best quality. FXAA | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | The Legend of Zelda: Ocarina of Time only. Game: the game's own anti-aliasing | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | The method used to render the window in fullscreen. Borderless offers the best | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | This optimization speeds up memory accesses by the guest program. Enabling it causes | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | This option allows to change the clock of the console. | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | This option controls how ASTC textures should be decoded. | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | This option improves speed by eliminating a safety check before every memory | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | This option improves speed by reducing accuracy of fused-multiply-add instructions on | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | This option improves speed by relying only on the semantics of cmpxchg to ensure | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | This option improves speed by removing NaN checking. Please note this also reduces | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | This option improves the speed of 32 bits ASIMD floating-point functions by running | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | This option improves the speed of some approximate floating-point functions by using | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | This option increases CPU emulation thread use from 1 to the maximum of 4. | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Use NVIDIA DLSS in place of a game's DLSS (experimental) | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Use the game's own DLSS | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Used by the Bounded mode: the most time per frame that Switch 2 draws may wait in | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Uses NVIDIA DLSS on GeForce RTX cards in place of a Switch 2 game's own DLSS, | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Uses reactive flushing instead of predictive flushing, allowing more accurate memory | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | Wait | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | When the Slow Speed hotkey is pressed, the speed will be limited to this | `src/qt_common/config/shared_translation.cpp` |
| `shared_translation` | When the Turbo Speed hotkey is pressed, the speed will be limited to this | `src/qt_common/config/shared_translation.cpp` |
| `state` | Failed to update the room information. Please check your Internet | `src/yuzu/multiplayer/state.cpp` |
| `update_dialog` | <a href="%1">View on GitHub</a> | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | Another Lichii window is already updating this | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | Could not create a folder for the update. | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | Could not replace %1. Your installation was not changed. | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | Could not start the update installer. | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | Download failed verification | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | Failed to install the update | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | Failed to restart | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | Lichii will close, install the update and start again. The previous version is | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | Please start %1 again yourself. | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | Remind Me Later | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | Skip This Version | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | The downloaded file does not match the checksum GitHub published for it, so it | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | The downloaded update could not be unpacked. | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | The new version is installed. The previous version is kept as %1.  Restart now? | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | This release has no PGO build, so the standard build will be downloaded. | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | Unpacking... | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | Update Installed | `src/yuzu/updater/update_dialog.cpp` |
| `update_dialog` | Update Ready | `src/yuzu/updater/update_dialog.cpp` |
| `worker` | Folder size is not calculated during game discovery. | `src/qt_common/game_list/worker.cpp` |
| `worker` | Not scanned | `src/qt_common/game_list/worker.cpp` |
