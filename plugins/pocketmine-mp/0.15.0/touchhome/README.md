# TouchHome(回家)

## 功能简介

**回家(TouchHome)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `2.0`,作者 LDX。
主要功能方向:世界/传送。
原插件说明:Teleports you to your home.
本插件共提供 **3** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/home` | Teleports you to your home. | `/home` | touchhome.command.home | - |
| `/sethome` | Sets your home. | `/sethome` | touchhome.command.sethome | - |
| `/delhome` | Deletes your home. | `/delhome` | touchhome.command.delhome | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `touchhome` | Allows access to delete other's homes. | op |

## 如何使用

1. 下载下方插件文件 `TouchHome-2.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `touchhome`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.15.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.15.0
- **plugin_version**: `2.0`
- **author**: LDX
- **main**: `LDX\TouchHome\Main`
- **license**: NOASSERTION (unknown)
- **tags**: world

## 下载

- `TouchHome-2.0.phar`(**2818** 字节,sha256 `6e6d31cf39d55331ef8d2fb40e1d50b09ca734744c2c89c9b614ab57cba7c478`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.15.0/touchhome/TouchHome-2.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
