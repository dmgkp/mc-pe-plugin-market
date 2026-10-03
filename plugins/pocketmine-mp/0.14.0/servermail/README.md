# ServerMail(邮件插件)

## 功能简介

**邮件插件(ServerMail)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `0.0.1`,作者 tschrock (tschrock123@gmail.com)。
主要功能方向:玩法。
原插件说明:Mail for your server! :D
本插件共提供 **1** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/mail` | Main command. | `Usage: /mail <read|view|clear> or /mail send <player> <message>` | tschrock.servermail.command.mail | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `tschrock.servermail.command.mail` | Allows the user to run the mail command | true |

## 如何使用

1. 下载下方插件文件 `ServerMail-0.0.1.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `servermail`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.1, 0.14.0
- **plugin_version**: `0.0.1`
- **author**: tschrock (tschrock123@gmail.com)
- **main**: `tschrock\ServerMail\ServerMail`
- **website**: http://www.tschrock.net
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `ServerMail-0.0.1.phar`(**4430** 字节,sha256 `382146d2cddc7550ab7a92c22fd9828499f3cd917a6c625b0cb0cd84c41b3e3d`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/servermail/ServerMail-0.0.1.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
