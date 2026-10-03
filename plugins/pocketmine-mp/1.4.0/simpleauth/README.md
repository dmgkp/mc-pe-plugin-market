# SimpleAuth(的)

## 功能简介

**的(SimpleAuth)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.6.0`,作者 PocketMine Team。
主要功能方向:保护/防作弊、玩家/登录。
原插件说明:防止别人冒充帐户，在连接时注册或登录。
本插件共提供 **2** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/登入` | 登录到一个帐户 | `/登入 <密码>` | simpleauth.command.login | - |
| `/注册` | 注册一个账户 | `/注册 <password>` | simpleauth.command.register | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `simpleauth` | 允许登录帐号 | true |

## 如何使用

1. 下载下方插件文件 `SimpleAuth-1.6.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `simpleauth`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.4.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.1, 0.14.0, 1.4.0, 1.8.0
- **plugin_version**: `1.6.0`
- **author**: PocketMine Team
- **main**: `SimpleAuth\SimpleAuth`
- **license**: NOASSERTION (unknown)
- **tags**: protection, player

## 下载

- `SimpleAuth-1.6.0.phar`(**55539** 字节,sha256 `5af22db00c29745266520fb2672a823886e3665d590af0e1ed1189033931a066`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.4.0/simpleauth/SimpleAuth-1.6.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
