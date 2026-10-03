# CClearChat(基础插件)

## 功能简介

**基础插件(CClearChat)** 是一款运行于 **其它服务端** 的 Minecraft 基岩版插件,插件版本 `1.7`,作者 unknown。
主要功能方向:聊天/公告、特效/粒子。
原插件说明:Lets you clear chat whenever you want!
本插件共提供 **1** 条命令(见下表)。
共定义 **8** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/cc` | Main command for cc | `/cc [command]` | cc.use | cclearchat, clearchat |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `cc.*` | Access of using cc! | op |
| `cc.use` | Allows you to use /cc | op |
| `cc.me` | Lets you clear your own chat | op |
| `cc.other` | Lets you another player's chat | op |
| `cc.all` | Lets you clean everyone's chat | op |
| `cc.lock` | Lets you lock the chat | op |
| `cc.lock.bypass` | Lets you chat if chat is locked | op |
| `cc.prefix` | - | op |

## 如何使用

1. 下载下方插件文件 `CClearChat-1.7.jar`。
2. 放入服务器 `plugins/` 目录(其它服务端)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `cclearchat`
- **edition**: bedrock
- **server_type**: `other`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: unknown
- **plugin_version**: `1.7`
- **author**: unknown
- **main**: `me.r0m3x.cclearchat.CC`
- **license**: NOASSERTION (unknown)
- **tags**: chat, cosmetic

## 下载

- `CClearChat-1.7.jar`(**7438** 字节,sha256 `0e422f55da78c5186c41bb115e0f46dd6f4a6851ee6682b9af9f9b9309975f86`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/other/unknown/cclearchat/CClearChat-1.7.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
