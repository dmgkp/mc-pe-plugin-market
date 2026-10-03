# Grade(等级)

## 功能简介

**等级(Grade)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.6`,作者 Him188。
主要功能方向:玩法。
原插件说明:A EXP Plugin
本插件共提供 **3** 条命令(见下表)。
共定义 **3** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/exp` | 等级插件命令 | `/exp` | Grade.command.exp | grade |
| `/convert` | 用节操兑换物品 | `/convert <编号> [数量]` | Grade.command.convert | 兑换 |
| `/setfix` | 设置昵称 | `/setfix <目标玩家> [昵称]` | Grade.command.setfix | 设置昵称 |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `Grade.command.exp` | 等级插件命令 | true |
| `Grade.command.convert` | 兑换物品 | true |
| `Grade.command.setfix` | 设置昵称 | op |

## 如何使用

1. 下载下方插件文件 `Grade-1.0.6.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `grade`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.1, 0.14.0
- **plugin_version**: `1.0.6`
- **author**: Him188
- **main**: `Grade\Grade`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `Grade-1.0.6.phar`(**9176** 字节,sha256 `12b87ae3f121d1b48ae50684a284d6483f1ed6dff08adbc909bdffadb0890cbd`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/grade/Grade-1.0.6.phar`

## 历史版本

- 1.0.0: Grade-1.0.0.phar
- 1.0.1: Grade-1.0.1.phar
- 1.0.2: Grade-1.0.2.phar
- 1.0.3: Grade-1.0.3.phar
- 1.0.4: Grade-1.0.4.phar, Grade-1.0.4.phar, Grade-1.0.4.phar

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
