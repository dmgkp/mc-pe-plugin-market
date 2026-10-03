# PocketDockConsole(网页控制)

## 功能简介

**网页控制(PocketDockConsole)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `0.0.14`,作者 humerusj。
主要功能方向:特效/粒子。
原插件说明:A web console that uses WebSockets
本插件共提供 **2** 条命令(见下表)。
共定义 **2** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/consoleclients` | List the connected PocketDockConsole clients | `Usage: /consoleclients` | pocketdockconsole.command.consoleclients | cc, conclients, showclients |
| `/killclient` | Kill a certain client from connection | `Usage: /killclient <ip:port>` | pocketdockconsole.command.killclient | kc, killc |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `pocketdockconsole.command.consoleclients` | Allows a player to show the connected console clients | op |
| `pocketdockconsole.command.killclient` | Allows a player to kill a connected console client | op |

## 如何使用

1. 下载下方插件文件 `PocketDockConsole-0.0.14.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `pocketdockconsole`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.1, 0.14.0
- **plugin_version**: `0.0.14`
- **author**: humerusj
- **main**: `PocketDockConsole\Main`
- **license**: NOASSERTION (unknown)
- **tags**: cosmetic

## 下载

- `PocketDockConsole-0.0.14.phar`(**268074** 字节,sha256 `c14f16d27de8919fe5abc8291a51470deae1740a34ba87a2533c8b05db0b58a2`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/pocketdockconsole/PocketDockConsole-0.0.14.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
