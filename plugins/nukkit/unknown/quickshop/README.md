# QuickShop(基础插件)

## 功能简介

**基础插件(QuickShop)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `4.5 #Beta`,作者 Netherfoam。
主要功能方向:经济/商店、管理/权限。
原插件说明:Economy Shops plugin
本插件共提供 **1** 条命令(见下表)。
共定义 **15** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/qs` | QuickShop command | `/qs` | - | shop |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `quickshop.create.sell` | Allows a player to sell from a shop | op |
| `quickshop.create.buy` | Allows a player to buy from a shop | op |
| `quickshop.create.double` | Allows a player to create a double shop | op |
| `quickshop.use` | Allows a player to buy/sell using other players shops | true |
| `quickshop.unlimited` | Allows a Staff Member to use /qs unlimited and make a shop infinite | - |
| `quickshop.bypass.<itemID>` | Allows a player to sell <itemID>, even if its blacklisted | - |
| `quickshop.other.destroy` | Allows a Staff Member to destroy other players shops if they are locked in the config | - |
| `quickshop.other.open` | Allows a Staff Member to open someone elses shop if they are locked in the config | - |
| `quickshop.other.price` | Allows a Staff Member to change the price of someone elses shop | - |
| `quickshop.setowner` | Allows a Staff Member to change the owner of any shop | - |
| `quickshop.find` | Allows a player to locate the nearest shop of a specific item type. Works in a 3 chunk radius. | true |
| `quickshop.refill` | Allows a Staff Member to refill the shop theyre looking at with the given number of items. | op |
| `quickshop.empty` | Allows a Staff Member to empty the shop theyre looking at of all items. | op |
| `quickshop.debug` | Enables debug info to console | op |
| `quickshop.export` | Allows exporting database to mysql or sqlite | op |

## 如何使用

1. 下载下方插件文件 `QuickShop-4.5_Beta.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `quickshop`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: unknown
- **plugin_version**: `4.5 #Beta`
- **author**: Netherfoam
- **softdependencies**: [Herochat, Vault, Spout]
- **main**: `org.maxgamer.QuickShop.QuickShop`
- **website**: http://maxgamer.org
- **license**: NOASSERTION (unknown)
- **tags**: economy, admin

## 下载

- `QuickShop-4.5_Beta.jar`(**119051** 字节,sha256 `bf782a278e9fe6592f816ce5688afb61776b688f9286960a6a08e0ffaf85b8ba`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/unknown/quickshop/QuickShop-4.5_Beta.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
