# ChatMode(聊天管理)

## 功能简介

**聊天管理(ChatMode)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.2`,作者 Smile。
主要功能方向:聊天/公告、管理/权限、特效/粒子。
原插件说明:一个好用聊天管理插件
本插件共提供 **5** 条命令(见下表)。
共定义 **5** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/cm` | 设置自己的聊天模式 | `/cm <0|1|2>` | ChatMode.Command.cm | - |
| `/mute` | 禁言一个玩家 | `/mute <玩家名字> <禁言秒数>` | ChatMode.Command.mute | - |
| `/unmute` | 解除一个玩家的禁言 | `/unmute <玩家名字>` | ChatMode.Command.unmute | - |
| `/l` | 发出一些只有自己世界中的玩家才可收到的信息 | `/l <信息>` | ChatMode.Command.l | - |
| `/sl` | 和一个玩家私聊 | `/sl <私聊目标> <信息>` | ChatMode.Command.sl | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `ChatMode.Command.cm` | 允许玩家设置自己的聊天模式 | true |
| `ChatMode.Command.mute` | 允许禁言玩家 | true |
| `ChatMode.Command.unmute` | 允许解除禁言玩家 | true |
| `ChatMode.Command.l` | 允许玩家发出世界中的信息 | true |
| `ChatMode.Command.sl` | 允许玩家和别人私聊 | true |

## 如何使用

1. 下载下方插件文件 `ChatMode-1.0.2.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `chatmode`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.8.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.8.0
- **plugin_version**: `1.0.2`
- **author**: Smile
- **main**: `ChatMode\ChatMode`
- **license**: NOASSERTION (unknown)
- **tags**: chat, admin, cosmetic

## 下载

- `ChatMode-1.0.2.phar`(**17505** 字节,sha256 `47b0af9a727db7c67ad0af7a66fdc784af0c5e291378eb105908e8e2535cb6fb`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.8.0/chatmode/ChatMode-1.0.2.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
