# PlayerSendCommand(强制玩家执行命令插件)

## 功能简介

**强制玩家执行命令插件(PlayerSendCommand)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.0`,作者 linger。
主要功能方向:管理/权限。
原插件说明:/cplayer [名字] [指令(不加/)]
本插件共提供 **1** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/cplayer` | /cplayer [名字] [指令(不加/)] | `/cplayer [名字] [指令(不加/)]` | PlayerSendCommand. | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `PlayerSendCommand.` | OP允许! | op |

## 如何使用

1. 下载下方插件文件 `PlayerSendCommand-1.0.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `playersendcommand`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0
- **plugin_version**: `1.0.0`
- **author**: linger
- **main**: `PlayerSendCommand\PlayerSendCommand`
- **license**: NOASSERTION (unknown)
- **tags**: admin

## 下载

- `PlayerSendCommand-1.0.0.phar`(**8446** 字节,sha256 `814d67204b9104cabd50c74de7071741938c91fb8a98fb64e75589484467305c`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/playersendcommand/PlayerSendCommand-1.0.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
