# Welcome(欢迎登录插件)

## 功能简介

**欢迎登录插件(Welcome)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `0.0.6`,作者 fromgate, nukkit.ru。
主要功能方向:玩家/登录。
原插件说明:User authentication plugin
本插件未在 plugin.yml 中声明命令,可能通过 GUI / 物品 / 事件触发。
共定义 **6** 个权限点位(见下表,可用于判断插件能力)。

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `welcome.login` | - | true |
| `welcome.register` | Allows to use command /register | true |
| `welcome.changepassword` | Allows to use command /changepassword | true |
| `welcome.help` | Allows to use command /welcome help | op |
| `welcome.remove` | Allows to use command /welcome remove | op |
| `welcome.unregister` | Allows to use command /unregister | op |

## 如何使用

1. 下载下方插件文件 `Welcome-0.0.6.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。

## 元数据

- **id**: `welcome`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `1.1.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.1.0
- **plugin_version**: `0.0.6`
- **author**: fromgate, nukkit.ru
- **softdependencies**: [DbLib]
- **main**: `ru.nukkit.welcome.Welcome`
- **license**: NOASSERTION (unknown)
- **tags**: player

## 下载

- `Welcome-0.0.6.jar`(**52214** 字节,sha256 `83d378de8ca0b5092ce36e42eae4721e3672cac028d0b12ab50b3aac4125a3d7`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/1.1.0/welcome/Welcome-0.0.6.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
