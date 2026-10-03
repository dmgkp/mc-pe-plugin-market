# [底部]Ssend(版)

## 功能简介

**版([底部]Ssend)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.0`,作者 app。
主要功能方向:玩家/登录。
原插件说明:结婚 主命令
本插件共提供 **3** 条命令(见下表)。
共定义 **2** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/结婚` | 结婚 主命令 | `/结婚` | jh.marry | - |
| `/称号` | 设置称号 | `/称号 [id] [称号]` | db.command.op | - |
| `/禁言` | 禁言/解禁 玩家 | `/禁言 [id]` | db.command.op | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `jh.marry` | 结婚 主命令 | true |
| `db.command.op` | 只有OP可以使用 | op |

## 如何使用

1. 下载下方插件文件 `Ssend-1.0.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `ssend`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0
- **plugin_version**: `1.0.0`
- **author**: app
- **main**: `db\Main`
- **license**: NOASSERTION (unknown)
- **tags**: player

## 下载

- `Ssend-1.0.0.phar`(**30434** 字节,sha256 `b4c7985c1f1b077618452cc5e6d3b57b17918224605805327e398c2793c83706`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/ssend/Ssend-1.0.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
