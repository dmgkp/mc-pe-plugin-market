# EconomyAuction(EconomyAuction)

## 功能简介

**EconomyAuction(EconomyAuction)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `2.0.2-3`,作者 onebone。
主要功能方向:经济/商店。
原插件说明:Manages all auctions
本插件共提供 **1** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/auction` | Manages all auctions | `/auction <start|stop|time|bid>` | economyauction.command.auction | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `economyauction.*` | Allows player to stop others' auctions | op |

## 如何使用

1. 下载下方插件文件 `EconomyAuction-2.0.2-3.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `economyauction`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.12.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.0, 0.11.1, 0.14.0, 1.12.0
- **plugin_version**: `2.0.2-3`
- **author**: onebone
- **dependencies**: [EconomyAPI]
- **main**: `onebone\economyauction\EconomyAuction`
- **license**: NOASSERTION (unknown)
- **tags**: economy

## 下载

- `EconomyAuction-2.0.2-3.phar`(**4200** 字节,sha256 `8b175322969559d0297a9c41c0d93357a63b4edcf4dfb833b9b56a48804750bb`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.12.0/economyauction/EconomyAuction-2.0.2-3.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
