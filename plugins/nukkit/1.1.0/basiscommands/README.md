# BasisCommands(传送插件)

## 功能简介

**传送插件(BasisCommands)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `0.0.4.33`,作者 to2mbn。
主要功能方向:管理/权限、玩法。
原插件说明:A Nukkit plugin which adds some useful commands in game like '/sethome
本插件共提供 **19** 条命令(见下表)。
共定义 **6** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/sethome` | Set your home position | `/sethome <home name>` | - | - |
| `/home` | Teleport to your home or list all your homes | `/home [home name]` | - | - |
| `/delhome` | Delete your home | `/delhome <home name>` | - | - |
| `/tpa` | Ask a player to accept you to teleport to him | `/tpa <player name>` | - | - |
| `/tpahere` | Ask a player to teleport to you | `/tpahere <player name>` | - | - |
| `/tpaccept` | Accept a teleporting request | `/tpaccept` | - | - |
| `/tp` | Teleport to a player | `/tp <player name>` | basiscommands.tp | - |
| `/tpall` | Teleport all the players to you | `/tpall` | basiscommands.tp | - |
| `/addnotice` | Add a notice to show | `/addnotice <notice>` | basiscommands.notice | - |
| `/delnotice` | Delete a notice | `/delnotice <notice id>` | basiscommands.notice | - |
| `/noticelist` | List all the notices with ids | `/noticelist` | basiscommands.notice | - |
| `/setwarp` | Set a global warp point | `/setwarp <name>` | basiscommands.warp | - |
| `/warp` | Teleport to a global warp point | `/warp <name>` | - | - |
| `/delwarp` | Delete a global warp point | `/delwarp <name>` | basiscommands.warp | - |
| `/warplist` | List all the available global warp points | `/warplist` | - | - |
| `/back` | Teleport back to the last teleport point (including death position) | `/back` | - | - |
| `/suicide` | Kill your self | `/suicide` | - | - |
| `/spawn` | Teleport to the global spawn point | `/spawn` | - | - |
| `/setspawn` | - | `/setspawn` | basiscommands.setspawn | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `basiscommands.tpa` | Allows players to use tpa commands | true |
| `basiscommands.home` | Allows players to use home commands | true |
| `basiscommands.tp` | Allows players to use teleport commands | op |
| `basiscommands.notice` | - | op |
| `basiscommands.warp` | Allows players to set and remove the global warp points | op |
| `basiscommands.setspawn` | Allows players to set the global spawn point | op |

## 如何使用

1. 下载下方插件文件 `BasisCommands-0.0.4.33.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `basiscommands`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `1.1.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.1.0
- **plugin_version**: `0.0.4.33`
- **author**: to2mbn
- **main**: `org.to2mbn.basiscommands.BasisCommands`
- **license**: NOASSERTION (unknown)
- **tags**: admin, gameplay

## 下载

- `BasisCommands-0.0.4.33.jar`(**60955** 字节,sha256 `f501d74a19f963c9f6bf9dcc2860485c02446e7960c7dc571237ab5b3e889e26`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/1.1.0/basiscommands/BasisCommands-0.0.4.33.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
