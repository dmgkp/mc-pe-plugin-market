# EconomyCasino(EconomyCasino)

## 功能简介

**EconomyCasino(EconomyCasino)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `2.0.2`,作者 onebone。
主要功能方向:经济/商店、管理/权限。
原插件说明:Allows player to use all commands of EconomyCasino
本插件共提供 **2** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/casino` | Casino master command | `/casino <start|stop|join|leave|list|gamble>` | economycasino.command.casino;economycasino.command.casino.start;economycasino.command.casino.stop;economycasino.command.casino.join;economycasino.command.casino.leave;economycasino.command.casino.list;economycasino.command.casino.gamble | - |
| `/jackpot` | Try jackpot | `/jackpot <money>` | economycasino.command.jackpot | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `economycasino.command.*` | Allows player to gamble the money | true |

## 如何使用

1. 下载下方插件文件 `EconomyCasino-2.0.2.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `economycasino`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.0, 0.11.1, 0.14.0, 1.12.0
- **plugin_version**: `2.0.2`
- **author**: onebone
- **dependencies**: [EconomyAPI]
- **main**: `onebone\economycasino\EconomyCasino`
- **license**: NOASSERTION (unknown)
- **tags**: economy, admin

## 下载

- `EconomyCasino-2.0.2.phar`(**13616** 字节,sha256 `e7f1e073875460765710ea3aab9c65f3a901b9bea763971837b8330d7e3801a0`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/economycasino/EconomyCasino-2.0.2.phar`

## 历史版本

- 2.0.1: EconomyCasino-2.0.1.phar, EconomyCasino-2.0.1.phar

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
