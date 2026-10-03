# SntuAuth(登录)

## 功能简介

**登录(SntuAuth)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `1.3.2`,作者 Huiyuzhe。
主要功能方向:玩家/登录。
原插件说明:SNTU登录指令
本插件共提供 **7** 条命令(见下表)。
共定义 **5** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/log` | SNTU登录指令 | `使用 / log [密码]` | SntuAuth.command.log | - |
| `/reg` | SNTU注册指令 | `使用 / reg [密码] [确认密码] [邮箱]` | SntuAuth.command.reg | - |
| `/login` | SNTU登录指令 | `可直接替换为 / log [密码]` | SntuAuth.command.log | - |
| `/register` | SNTU注册指令 | `可直接替换为/reg [密码] [确认密码] [邮箱]` | SntuAuth.command.reg | - |
| `/uppassword` | SNTU修改密码指令 | `/uppassword [老密码] [新密码]` | SntuAuth.command.uppassword | - |
| `/forgot` | SNTU找回密码指令 | `/forgot [邮箱]` | SntuAuth.command.forgot | - |
| `/resetpwd` | SNTU找回密码指令 | `/resetpwd [邮箱标识码] [新密码]` | SntuAuth.command.resetpwd | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `SntuAuth.command.log` | SNTU登录指令 | true |
| `SntuAuth.command.reg` | SNTU注册指令 | true |
| `SntuAuth.command.uppassword` | SNTU修改密码指令 | true |
| `SntuAuth.command.forgot` | SNTU获取验证码指令 | true |
| `SntuAuth.command.resetpwd` | SNTU重置密码指令 | true |

## 如何使用

1. 下载下方插件文件 `SntuAuth-1.3.2.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `sntuauth`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `1.1.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.15.0, 1.1.0
- **plugin_version**: `1.3.2`
- **author**: Huiyuzhe
- **main**: `cn.sntumc.nukkit.sntuauth.Main`
- **license**: NOASSERTION (unknown)
- **tags**: player

## 下载

- `SntuAuth-1.3.2.jar`(**51789** 字节,sha256 `ec6eeea51252772064f56edb12f535293df360a09bbe2902b83baed2e499958d`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/1.1.0/sntuauth/SntuAuth-1.3.2.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
