# CJChat(超级称号)

## 功能简介

**超级称号(CJChat)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0`,作者 Qing。
主要功能方向:聊天/公告、特效/粒子。
原插件说明:聊天插件
本插件共提供 **2** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/setch` | shezhi | `/setch [id] [称号]` | ChatPro.command.op | - |
| `/mute` | 禁言/解禁 玩家 | `mute [id]` | ChatPro.command.op | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `ChatPro.command.op` | 只有OP可以使用 | op |

## 如何使用

1. 下载下方插件文件 `CJChat-1.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `cjchat`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.5.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.5.0
- **plugin_version**: `1.0`
- **author**: Qing
- **main**: `ChatPro\ChatPro`
- **license**: NOASSERTION (unknown)
- **tags**: chat, cosmetic

## 下载

- `CJChat-1.0.phar`(**2576** 字节,sha256 `48bf651b9621ea07e804a2fb3a6b03a91681b505a7482e8d0c62611b693da6e9`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.5.0/cjchat/CJChat-1.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
