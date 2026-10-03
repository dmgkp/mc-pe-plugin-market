# EconomyLand(EconomyLand)

## 功能简介

**EconomyLand(EconomyLand)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `2.1.1-3`,作者 onebone。
主要功能方向:经济/商店、世界/传送、前置/API 库。
原插件说明:Allows player to use all functions in EconomyLand
本插件共提供 **4** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/startp` | Sets start position | `/startp` | economyland.command.startp | - |
| `/endp` | Sets second position | `/endp` | economyland.command.endp | - |
| `/land` | Manage land | `/land <buy|move|list|whose|give|here|[r:]invite|kick|invitee>` | economyland.command.land;economyland.command.land.buy;economyland.command.land.move;economyland.command.land.list;economyland.command.land.whose;economyland.command.land.give;economyland.command.land.here;economyland.command.land.invite;economyland.command.land.invite.remove;economyland.command.land.invitee | - |
| `/landsell` | Sell land | `/landsell <here|land num>` | economyland.command.landsell;economyland.command.landsell.here;economyland.command.landsell.number | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `economyland.*` | Allows player to sell land with numbers | true |

## 如何使用

1. 下载下方插件文件 `EconomyLand-2.1.1-3.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `economyland`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.12.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.0, 0.11.1, 0.14.0, 1.8.0, 1.12.0
- **plugin_version**: `2.1.1-3`
- **author**: onebone
- **dependencies**: EconomyAPI
- **main**: `onebone\economyland\EconomyLand`
- **license**: NOASSERTION (unknown)
- **tags**: economy, world, library

## 下载

- `EconomyLand-2.1.1-3.phar`(**20370** 字节,sha256 `30bfa4cfa229b713840610db4bf4ece6240d52a02ea3bcf71ea082a6d42cc9a6`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.12.0/economyland/EconomyLand-2.1.1-3.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
