# MyPlot(基地地皮)

## 功能简介

**基地地皮(MyPlot)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0`,作者 Wies and Exxarion。
主要功能方向:世界/传送、保护/防作弊。
原插件说明:Plot and protection plugin
本插件未在 plugin.yml 中声明命令,可能通过 GUI / 物品 / 事件触发。
共定义 **3** 个权限点位(见下表,可用于判断插件能力)。

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `myplot.command` | Gives the warp command | true |
| `myplot.admin` | Allow player to use the biome command on all plots | op |
| `myplot.claimplots` | Allow player to claim unlimited plots | op |

## 如何使用

1. 下载下方插件文件 `MyPlot-1.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。

## 元数据

- **id**: `myplot`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.16.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0, 0.16.0, 1.12.0
- **plugin_version**: `1.0`
- **author**: Wies and Exxarion
- **softdependencies**: [EconomyAPI, PocketMoney]
- **main**: `MyPlot\MyPlot`
- **license**: NOASSERTION (unknown)
- **tags**: world, protection

## 下载

- `MyPlot-1.0.phar`(**120785** 字节,sha256 `a1f45d7dccec9bb7a15cfca86bbcfaa24c0eb978e59c48b924f6c35fe824ac9e`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.16.0/myplot/MyPlot-1.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
