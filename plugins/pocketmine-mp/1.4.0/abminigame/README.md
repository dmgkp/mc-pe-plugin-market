# ABMiniGame(猜数字)

## 功能简介

**猜数字(ABMiniGame)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.0`,作者 Mico。
主要功能方向:玩法。
原插件说明:1A2B Mini Game
本插件共提供 **2** 条命令(见下表)。
共定义 **2** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/AOB` | ABMiniGame OP Command | `/AOB <create/remove> 設定或刪除遊戲` | AB.command.op | - |
| `/1A2B` | ABMiniGame Command | `/1A2B 查詢1A2B遊玩方式` | AB.command.player | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `AB.command.op` | Only OP can use this CMD | op |
| `AB.command.player` | Any Player can use this CMD | true |

## 如何使用

1. 下载下方插件文件 `ABMiniGame-1.0.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `abminigame`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.4.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.4.0
- **plugin_version**: `1.0.0`
- **author**: Mico
- **main**: `Mico\ABMiniGame`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `ABMiniGame-1.0.0.phar`(**161225** 字节,sha256 `fc4a163e761f8e70d943be6767a45cbf7d54ff51f94e2ff3dffad6e48f5335a9`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.4.0/abminigame/ABMiniGame-1.0.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
