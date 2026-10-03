# WMultiWorld(多功能世界)

## 功能简介

**多功能世界(WMultiWorld)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.1.0`,作者 Whale。
主要功能方向:世界/传送。
原插件说明:§6多世界传送指令
本插件共提供 **4** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/w` | §6多世界传送指令 | `/w` | - | - |
| `/lw` | §6查看世界列表 | `/lw` | - | - |
| `/makemap` | §6新地图生成器 | `/makemap` | wmw.command.op | - |
| `/setworld` | §6多世界其他功能 | `/setworld` | wmw.command.op | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `wmw.command.op` | - | op |

## 如何使用

1. 下载下方插件文件 `WMultiWorld-1.1.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `wmultiworld`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0
- **plugin_version**: `1.1.0`
- **author**: Whale
- **main**: `WMultiWorld\WMultiWorld`
- **license**: NOASSERTION (unknown)
- **tags**: world

## 下载

- `WMultiWorld-1.1.0.phar`(**12761** 字节,sha256 `44bce645c18797814ccbba9e0070c1999b57ccc7e2316fcc6573b1a64d714e8d`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/wmultiworld/WMultiWorld-1.1.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
