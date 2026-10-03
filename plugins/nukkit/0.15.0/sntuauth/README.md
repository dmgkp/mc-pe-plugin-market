# SntuAuth(SntuAuth)

## 功能简介

**SntuAuth(SntuAuth)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `1.2`,作者 Huiyuzhe。
主要功能方向:玩家/登录。
原插件说明:SNTU登录指令
本插件共提供 **4** 条命令(见下表)。
共定义 **2** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/log` | SNTU登录指令 | `使用 / log [密码]` | SntuAuth.command.log | - |
| `/reg` | SNTU注册指令 | `使用 / reg [密码] [确认密码]` | SntuAuth.command.reg | - |
| `/login` | SNTU登录指令 | `可直接替换为 / log [密码]` | SntuAuth.command.log | - |
| `/register` | SNTU注册指令 | `可直接替换为/reg [密码] [确认密码]` | SntuAuth.command.reg | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `SntuAuth.command.log` | SNTU登录指令 | true |
| `SntuAuth.command.reg` | SNTU注册指令 | true |

## 如何使用

1. 下载下方插件文件 `SntuAuth-1.2.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `sntuauth`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `0.15.0` (推断来源: path)
- **minecraft_versions**: 0.15.0, 1.1.0
- **plugin_version**: `1.2`
- **author**: Huiyuzhe
- **main**: `cn.sntumc.nukkit.sntuauth.Main`
- **license**: NOASSERTION (unknown)
- **tags**: player

## 下载

- `SntuAuth-1.2.jar`(**15525** 字节,sha256 `8785e21c64469629faa9b0b0f412304482291e99bce1401e1d51809867d7e7e4`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/0.15.0/sntuauth/SntuAuth-1.2.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
