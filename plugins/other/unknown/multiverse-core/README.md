# Multiverse-Core(基础插件)

## 功能简介

**基础插件(Multiverse-Core)** 是一款运行于 **其它服务端** 的 Minecraft 基岩版插件,插件版本 `2.5-b678`,作者 unknown。
主要功能方向:管理/权限、前置/API 库。
原插件说明:Generic Multiverse Command
本插件共提供 **51** 条命令(见下表)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/mv` | Generic Multiverse Command | `/<command>` | - | - |
| `/mvcreate` | World create command | `|` | - | - |
| `/mvc` | World create command | `|` | - | - |
| `/mvimport` | World import command | `|` | - | - |
| `/mvim` | World import command | `|` | - | - |
| `/mvremove` | World remove command | `|` | - | - |
| `/mvdelete` | World delete command | `|` | - | - |
| `/mvunload` | World unload command | `|` | - | - |
| `/mvmodify` | Modify the settings of an existing world | `|` | - | - |
| `/mvmset` | Modify the settings of an existing world | `|` | - | - |
| `/mvmadd` | Modify the settings of an existing world | `|` | - | - |
| `/mvmremove` | Modify the settings of an existing world | `|` | - | - |
| `/mvmclear` | Modify the settings of an existing world | `|` | - | - |
| `/mvm` | Modify the settings of an existing world | `|` | - | - |
| `/mvtp` | Command to teleport between Worlds | `|` | - | - |
| `/mvlist` | Print list of loaded Worlds | `|` | - | - |
| `/mvl` | Print list of loaded Worlds | `|` | - | - |
| `/mvsetspawn` | Set the spawn area for a particular world | `/<command> -- Sets the spawn area of the current world to your location.` | - | - |
| `/mvset` | Set the spawn area for a particular world | `/<command> -- Sets the spawn area of the current world to your location.` | - | - |
| `/mvss` | Set the spawn area for a particular world | `/<command> -- Sets the spawn area of the current world to your location.` | - | - |
| `/mvspawn` | Teleport to the spawn area | `/<command> -- Teleports you to the spawn area of your current world.` | - | - |
| `/mvs` | Teleport to the spawn area | `/<command> -- Teleports you to the spawn area of your current world.` | - | - |
| `/mvcoord` | Display World, Coordinates, Direction & Compression for a world. | `|` | - | - |
| `/mvc` | Display World, Coordinates, Direction & Compression for a world. | `|` | - | - |
| `/mvwho` | Display online users per world. | `|` | - | - |
| `/mvw` | Display online users per world. | `|` | - | - |
| `/mvreload` | Reload Configuration files. | `/<command>` | - | - |
| `/mvr` | Reload Configuration files. | `/<command>` | - | - |
| `/mvpurge` | Purge the targetted world of creatures. | `|` | - | - |
| `/mvconfirm` | Confirms sensitive decisions like deleting a world. | `|` | - | - |
| `/mvinfo` | Gets world info. | `|` | - | - |
| `/mvi` | Gets world info. | `|` | - | - |
| `/mvenv` | Tells the user all possible environment types. | `|` | - | - |
| `/mvv` | Prints out version info. | `|` | - | - |
| `/mvversion` | Prints out version info. | `|` | - | - |
| `/mvco` | Displays the player's coordinates. | `|` | - | - |
| `/mvh` | Displays the Multiverse Help. | `|` | - | - |
| `/mvsearch` | Displays the Multiverse Help. | `|` | - | - |
| `/mvhelp` | Displays the Multiverse Help. | `|` | - | - |
| `/mvdebug` | Turns on debugging. | `|` | - | - |
| `/mvgenerators` | Displays all found world generators. | `|` | - | - |
| `/mvgens` | Displays all found world generators. | `|` | - | - |
| `/mvload` | Loads a world into Multiverse. | `|` | - | - |
| `/mvregen` | Regenerates a world Multiverse already knows about. | `|` | - | - |
| `/mvscript` | Runs a script from the Multiverse scripts directory. | `|` | - | - |
| `/mvclone` | World clone command | `|` | - | - |
| `/mvsilent` | Reduces startup messages | `|` | - | - |
| `/mvgamerule` | Sets a gamerule. | `|` | - | - |
| `/mvrule` | Sets a gamerule. | `|` | - | - |
| `/mvgamerules` | Lists the gamerules. | `|` | - | - |
| `/mvrules` | Lists the gamerules. | `|` | - | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|

## 如何使用

1. 下载下方插件文件 `Multiverse-Core-2.5-b678.jar`。
2. 放入服务器 `plugins/` 目录(其它服务端)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `multiverse-core`
- **edition**: bedrock
- **server_type**: `other`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: unknown
- **plugin_version**: `2.5-b678`
- **author**: unknown
- **main**: `com.onarandombox.MultiverseCore.MultiverseCore`
- **license**: NOASSERTION (unknown)
- **tags**: admin, library

## 下载

- `Multiverse-Core-2.5-b678.jar`(**1643924** 字节,sha256 `7e9e33bad4cc53715e234ac24e2c1c5ead0506009346b3193e7c2df8b273e5c4`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/other/unknown/multiverse-core/Multiverse-Core-2.5-b678.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
