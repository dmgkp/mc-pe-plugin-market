# WEconomyAPI(全新的经济)

## 功能简介

**全新的经济(WEconomyAPI)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.0`,作者 Himpq。
主要功能方向:经济/商店、管理/权限、前置/API 库。
原插件说明:Admin or Player Use commands.
本插件共提供 **7** 条命令(见下表)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/we` | Admin or Player Use commands. | `/we` | economy.help | - |
| `/paymoney` | Pay Money | `/paymoney <玩家> <金钱>` | economy.pay | - |
| `/setmoney` | Set Money | `/setmoney <玩家> <金钱>` | economy.set | - |
| `/delmoney` | Del Money | `/delmoney <玩家> <金钱>` | economy.del | - |
| `/addmoney` | Add Money | `/addmoney <玩家> <金钱>` | economy.add | - |
| `/resetmoney` | Remove Set Money | `/resetmoney <玩家>` | economy.reset | - |
| `/lookmoney` | Look Money | `/lookmoney <玩家>` | economy.look | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|

## 如何使用

1. 下载下方插件文件 `WEconomyAPI-1.0.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `weconomyapi`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0
- **plugin_version**: `1.0.0`
- **author**: Himpq
- **main**: `himpq\economyapi\main`
- **license**: NOASSERTION (unknown)
- **tags**: economy, admin, library

## 下载

- `WEconomyAPI-1.0.0.phar`(**8583** 字节,sha256 `d84b315db95be8a6031e06f648c0201128eaf9aae796db61db24922ac5b7f405`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/weconomyapi/WEconomyAPI-1.0.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
