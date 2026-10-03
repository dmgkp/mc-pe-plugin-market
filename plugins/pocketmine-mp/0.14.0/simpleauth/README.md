# SimpleAuth(SimpleAuth)

## 功能简介

**SimpleAuth(SimpleAuth)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.2.0`,作者 PocketMine Team。
主要功能方向:玩家/登录。
原插件说明:Prevents people to impersonate an account, requering registration and login when connecting.
本插件共提供 **2** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/login` | Logs into an account | `/login <password>` | simpleauth.command.login | - |
| `/register` | Registers an account | `/register <password>` | simpleauth.command.register | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `simpleauth` | Allows logging into an account | true |

## 如何使用

1. 下载下方插件文件 `SimpleAuth-1.2.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `simpleauth`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.1, 0.14.0, 1.4.0, 1.8.0
- **plugin_version**: `1.2.0`
- **author**: PocketMine Team
- **main**: `SimpleAuth\SimpleAuth`
- **license**: NOASSERTION (unknown)
- **tags**: player

## 下载

- `SimpleAuth-1.2.0.phar`(**19168** 字节,sha256 `8bb1f20ce32dc871e38cbdbdf1fc23ad76a5fae547985dec2168e0afdfb09978`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/simpleauth/SimpleAuth-1.2.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
