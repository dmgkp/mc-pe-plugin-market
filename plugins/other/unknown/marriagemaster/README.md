# MarriageMaster(基础插件)

## 功能简介

**基础插件(MarriageMaster)** 是一款运行于 **其它服务端** 的 Minecraft 基岩版插件,插件版本 `1.24`,作者 GeorgH93。
主要功能方向:管理/权限、玩家/登录。
原插件说明:Marry main command
本插件共提供 **1** 条命令(见下表)。
共定义 **29** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/marry` | Marry main command | `/marry` | - | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `marry.*` | Gives access to all MarriageMaster commands | - |
| `marry.admin` | Gives access to all Marriage Admin commands | - |
| `marry.bypass` | Gives all bypassing permissions | - |
| `marry.user` | Gives acces to all user functions | - |
| `marry.chat.*` | Gives acces to all private message formats | - |
| `marry.list` | Allows you to use the List command | true |
| `marry.pvpon` | Allows you to enable pvp with your partner | true |
| `marry.pvpoff` | Allows you to disable pvp with your partner | true |
| `marry.tp` | Allows you to tp to your partner | true |
| `marry.home` | Allows you to tp / set to your home | true |
| `marry.chat` | Allows you to chat with your partner | true |
| `marry.chat.color` | Allows colors in private messages | true |
| `marry.chat.format` | Allows formating private messages (except magic) | true |
| `marry.chat.magic` | Allows magic format in private messages | false |
| `marry.gift` | Allows you to gift items to your partner | true |
| `marry.backpack` | Allows to share the backpacks (requires Minepacks) | true |
| `marry.kiss` | Allows to kiss your partner | true |
| `marry.selfmarry` | Allows to marry an other player without a priest | - |
| `marry.changesurname` | Allows to change the surname when self marry is on. | true |
| `marry.skiptpdelay` | Allows to skip the delay on tps | op |
| `marry.bypassrangelimit` | Allows to bypass the range limits | op |
| `marry.bypassgiftgamemode` | Allows to bypass gamemode check for item gifting | op |
| `marry.offlinedivorce` | Allows a priest to divorce players when only one of them is online. | op |
| `marry.priest` | Allows you to marry two players | op |
| `marry.setpriest` | Allows you to set a priest | op |
| `marry.listenchat` | Allows to see the private chat | op |
| `marry.update` | Allows to update the plugin | op |
| `marry.reload` | Allows you to reload the config | op |
| `marry.home.others` | Allows to teleport to homes of other players | op |

## 如何使用

1. 下载下方插件文件 `MarriageMaster-1.24.jar`。
2. 放入服务器 `plugins/` 目录(其它服务端)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `marriagemaster`
- **edition**: bedrock
- **server_type**: `other`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: unknown
- **plugin_version**: `1.24`
- **author**: GeorgH93
- **softdependencies**: [Vault,MinePacks]
- **main**: `at.pcgamingfreaks.MarriageMaster.Bukkit.MarriageMaster`
- **website**: http://dev.bukkit.org/bukkit-plugins/marriage-master/
- **license**: NOASSERTION (unknown)
- **tags**: admin, player

## 下载

- `MarriageMaster-1.24.jar`(**397293** 字节,sha256 `65d5549fde1fc92429a9e6cc7cf5ac6bd3e9501be3ea0653d6561fea0f2a64e7`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/other/unknown/marriagemaster/MarriageMaster-1.24.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
