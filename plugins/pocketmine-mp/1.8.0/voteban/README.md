# VoteBan(人)

## 功能简介

**人(VoteBan)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.2`,作者 GmWM。
主要功能方向:管理/权限。
原插件说明:Vote for a player to be banned or kicked from the server.
本插件共提供 **1** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/v` | Vote for a player to be banned or kicked from the server. | `/v` | voteban.command | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `voteban.command` | Permission for /vote kick command. | true |

## 如何使用

1. 下载下方插件文件 `VoteBan-1.0.2.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `voteban`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.8.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.8.0, 1.12.0
- **plugin_version**: `1.0.2`
- **author**: GmWM
- **main**: `GmWM\VoteBan\VoteBan`
- **license**: NOASSERTION (unknown)
- **tags**: admin

## 下载

- `VoteBan-1.0.2.phar`(**9773** 字节,sha256 `bc9ae3fcf9f3427878b23cfdf779c4aecb03d382d28a59889bedcb38b3b734fb`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.8.0/voteban/VoteBan-1.0.2.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
