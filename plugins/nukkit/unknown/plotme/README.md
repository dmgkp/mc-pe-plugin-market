# [地皮]PlotMe(基础插件)

## 功能简介

**基础插件([地皮]PlotMe)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `0.13e`,作者 ZachBora。
主要功能方向:世界/传送。
原插件说明:>
本插件共提供 **1** 条命令(见下表)。
共定义 **54** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/plotme` | 列出PlotMe的所有命令 | `/plotme` | - | p, plot |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `plotme.use` | Gives default user commands | - |
| `plotme.admin` | Gives default administrator commands | - |
| `plotme.use.buy` | Gives the buy command | - |
| `plotme.use.sell` | Gives the sell command | - |
| `plotme.use.auction` | Gives the auction command | - |
| `plotme.use.bid` | Gives the bid command | - |
| `plotme.use.dispose` | Gives the dispose command | - |
| `plotme.use.done` | Gives the done command | - |
| `plotme.use.claim` | Gives the claim command | - |
| `plotme.use.auto` | Gives the auto claim command | - |
| `plotme.use.home` | Gives the home command | - |
| `plotme.use.info` | Gives the info command | - |
| `plotme.use.comment` | Gives the comment command | - |
| `plotme.use.comments` | Gives the comments command | - |
| `plotme.use.biome` | Gives the biome and biomelist command | - |
| `plotme.use.clear` | Gives the clear command for plots owned | - |
| `plotme.use.list` | Gives the list command | - |
| `plotme.use.add` | Gives the add command for plots owned | - |
| `plotme.use.deny` | Gives the deny command for plots owned | - |
| `plotme.use.remove` | Gives the remove command for plots owned | - |
| `plotme.use.undeny` | Gives the undeny command for plots owned | - |
| `plotme.use.protect` | Gives the protect command | - |
| `plotme.limit.*` | Gives unlimited plots | - |
| `plotme.limit.1` | Gives 1 plot | - |
| `plotme.limit.2` | Gives 2 plots | - |
| `plotme.limit.3` | Gives 3 plots | - |
| `plotme.limit.4` | Gives 4 plots | - |
| `plotme.limit.5` | Gives 5 plots | - |
| `plotme.limit.10` | Gives 10 plots | - |
| `plotme.admin.claim.other` | Gives the claim command for any player | - |
| `plotme.admin.home.other` | Gives the home command for any players | - |
| `plotme.admin.tp` | Gives the tp command | - |
| `plotme.admin.id` | Gives the id command | - |
| `plotme.admin.clear` | Gives the clear command for any plots | - |
| `plotme.admin.reset` | Gives the reset command | - |
| `plotme.admin.add` | Gives the add command for any plots | - |
| `plotme.admin.deny` | Gives the deny command for any plots | - |
| `plotme.admin.remove` | Gives the remove command for any plots | - |
| `plotme.admin.undeny` | Gives the undeny command for any plots | - |
| `plotme.admin.bypassdeny` | Allows to enter denied plots | - |
| `plotme.admin.setowner` | Gives the setowner command | - |
| `plotme.admin.move` | Gives the move command | - |
| `plotme.admin.weanywhere` | Gives the weanywhere command | - |
| `plotme.admin.list` | Gives the list command for any players | - |
| `plotme.admin.reload` | Gives the reload command | - |
| `plotme.admin.buy` | Gives the buy command | - |
| `plotme.admin.sell` | Gives the sell command for any plots | - |
| `plotme.admin.auction` | Gives the auction command for any plots | - |
| `plotme.admin.dispose` | Gives the dispose command for any plots | - |
| `plotme.admin.done` | Gives the done command for any plots and the donelist command | - |
| `plotme.admin.addtime` | Gives the addtime command for any plots | - |
| `plotme.admin.expired` | Gives the expired command | - |
| `plotme.admin.resetexpired` | Resets expired plots | - |
| `plotme.admin.buildanywhere` | Allows to build anywhere in the plot world | - |

## 如何使用

1. 下载下方插件文件 `PlotMe-0.13e.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `plotme`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: unknown
- **plugin_version**: `0.13e`
- **author**: ZachBora
- **softdependencies**: [WorldEdit, Vault, LWC]
- **main**: `com.worldcretornica.plotme.PlotMe`
- **website**: http://dev.bukkit.org/server-mods/plotme/
- **license**: NOASSERTION (unknown)
- **tags**: world

## 下载

- `PlotMe-0.13e.jar`(**160870** 字节,sha256 `c99a96256ae3b293113ec148af271ae3ab082f3662981d67c4ffb62203343751`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/unknown/plotme/PlotMe-0.13e.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
