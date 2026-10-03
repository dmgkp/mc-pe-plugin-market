# EconomyLand(经济)

## 功能简介

**经济(EconomyLand)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `2.0.7`,作者 onebone。
主要功能方向:经济/商店、世界/传送、前置/API 库。
原插件说明:Allows player to use all functions in EconomyLand
本插件共提供 **4** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/startp` | Sets start position | `/startp` | economyland.command.startp | - |
| `/endp` | Sets second position | `/endp` | economyland.command.endp | - |
| `/land` | Manage land | `/land <buy|move|list|whose|give|here>` | economyland.command.land;economyland.command.land.list;economyland.command.land.buy;economyland.command.land.whose;economyland.command.land.move;economyland.land.give;economyland.command.land.whose;economyland.command.land.here | - |
| `/landsell` | Sell land | `/landsell <here|land num>` | economyland.command.landsell;economyland.command.landsell.here;economyland.command.landsell.number | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `economyland.*` | Allows player to sell land with numbers | true |

## 如何使用

1. 下载下方插件文件 `EconomyLand-2.0.7.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `economyland`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.11.1` (推断来源: path)
- **minecraft_versions**: 0.11.0, 0.11.1, 0.14.0, 1.8.0, 1.12.0
- **plugin_version**: `2.0.7`
- **author**: onebone
- **dependencies**: [EconomyAPI]
- **main**: `onebone\economyland\EconomyLand`
- **license**: NOASSERTION (unknown)
- **tags**: economy, world, library

## 下载

- `EconomyLand-2.0.7.phar`(**51199** 字节,sha256 `03b4b8947c47236887bada709c7a85a65e4a1fd6d4e3ee5c229c6c6a3154187b`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.11.1/economyland/EconomyLand-2.0.7.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
