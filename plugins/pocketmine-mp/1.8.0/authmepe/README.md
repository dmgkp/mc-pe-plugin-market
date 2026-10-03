# AuthMePE(登录系统插件)

## 功能简介

**登录系统插件(AuthMePE)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `0.1.4`,作者 hoyinm & CyberCube-HK™。
主要功能方向:玩家/登录。
原插件说明:Port of most features of Bukkit's AuthMe_Reloaded
本插件共提供 **5** 条命令(见下表)。
共定义 **6** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/unregister` | 移除自己的密码.包括ip .简化命令:/ur | `/unregister` | authmepe.command.unregister | ur |
| `/changepass` | 改变你的密码.简化命令:/mima | `/changepass <old> <new> <new>` | authmepe.command.changepass | mima, changepw |
| `/chgemail` | 设置你的邮箱.简化命令:/email | `/chgemail <email>` | authmepe.command.chgemail | email |
| `/logout` | 退出登录状态 | `/logout` | authmepe.command.logout | - |
| `/authme` | SAuth管理员命令 | `/authme help` | authmepe.command.authme | ah |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `authmepe.command.unregister` | - | true |
| `authmepe.command.changepass` | - | true |
| `authmepe.command.chgemail` | - | true |
| `authmepe.command.logout` | - | true |
| `authmepe.command.authme` | - | op |
| `authmepe.login.bypass` | - | false |

## 如何使用

1. 下载下方插件文件 `AuthMePE-0.1.4.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `authmepe`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.8.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0, 1.8.0
- **plugin_version**: `0.1.4`
- **author**: hoyinm & CyberCube-HK™
- **main**: `AuthMePE\AuthMePE`
- **license**: NOASSERTION (unknown)
- **tags**: player

## 下载

- `AuthMePE-0.1.4.phar`(**45942** 字节,sha256 `4d5f4c4fb1fadeb75ef66a45d54c4c085a3da802ceeac566f2eee456c8d37f3f`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.8.0/authmepe/AuthMePE-0.1.4.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
