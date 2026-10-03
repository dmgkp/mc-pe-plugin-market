# Broadcaster(公告插件)

## 功能简介

**公告插件(Broadcaster)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.13`,作者 EvolSoft。
主要功能方向:聊天/公告。
原插件说明:Broadcast Plugin
本插件共提供 **2** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/broadcaster` | Broadcaster Commands. | `/broadcaster` | broadcaster | bc, broadcast |
| `/sendmessage` | Send message to specified player (* for all players) | `/sendmessage` | broadcaster.sendmessage | sm, smsg |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `broadcaster` | Allows sending messages to players with /sendmessage command. | op |

## 如何使用

1. 下载下方插件文件 `Broadcaster-1.13.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `broadcaster`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.11.1` (推断来源: path)
- **minecraft_versions**: 0.11.1, 0.14.0, 1.4.0, 1.12.0
- **plugin_version**: `1.13`
- **author**: EvolSoft
- **main**: `Broadcaster\Main`
- **website**: https://www.evolsoft.tk
- **license**: NOASSERTION (unknown)
- **tags**: chat

## 下载

- `Broadcaster-1.13.phar`(**5046** 字节,sha256 `e043ab5937f0690ce9677c4a24c56d5ad7f6bb43e7519b87dc94ee3798bde9f5`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.11.1/broadcaster/Broadcaster-1.13.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
