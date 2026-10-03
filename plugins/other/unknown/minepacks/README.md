# MinePacks(基础插件)

## 功能简介

**基础插件(MinePacks)** 是一款运行于 **其它服务端** 的 Minecraft 基岩版插件,插件版本 `1.13`,作者 GeorgH93。
主要功能方向:前置/API 库。
原插件说明:Minepacks is a backpack plugin with different backpack sizes, multilanguage and MySQL storage support. It is a simple plugin, but still has a lot of functions.
本插件共提供 **1** 条命令(见下表)。
共定义 **19** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/backpack` | Main command | `/backpack` | - | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `backpack.*` | Gives access to the full MinePacks functionality. | - |
| `backpack.use` | Allows a player to open the backpack. | - |
| `backpack` | Allows a player to open the backpack. | false |
| `backpack.size.1` | Mini size for a backpack, if the player has backpack permission he will also have at least a backpack with the size 1. | false |
| `backpack.size.2` | 2*9 backpack | false |
| `backpack.size.3` | 3*9 backpack | false |
| `backpack.size.4` | 4*9 backpack | false |
| `backpack.size.5` | 5*9 backpack | false |
| `backpack.size.6` | 6*9 backpack | false |
| `backpack.size.7` | 7*9 backpack (broken gui) | false |
| `backpack.size.8` | 8*9 backpack (broken gui) | false |
| `backpack.size.9` | 9*9 backpack (broken gui) | false |
| `backpack.clean` | Allows the player to clean their own backpack. | false |
| `backpack.fullpickup` | - | - |
| `backpack.clean.other` | Allows the player to clean other players backpacks. | op |
| `backpack.others` | Allows the player open backpacks of other players. | op |
| `backpack.others.edit` | Allows the player to edit backpacks of other players. | op |
| `backpack.KeepOnDeath` | Allows the player to keep their items in their backpack on death. | op |
| `backpack.noCooldown` | Allows to bypass the cooldown to open the backpack. | op |

## 如何使用

1. 下载下方插件文件 `MinePacks-1.13.jar`。
2. 放入服务器 `plugins/` 目录(其它服务端)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `minepacks`
- **edition**: bedrock
- **server_type**: `other`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: unknown
- **plugin_version**: `1.13`
- **author**: GeorgH93
- **main**: `at.pcgamingfreaks.georgh.MinePacks.MinePacks`
- **website**: http://dev.bukkit.org/bukkit-plugins/minepacks/
- **license**: NOASSERTION (unknown)
- **tags**: library

## 下载

- `MinePacks-1.13.jar`(**64226** 字节,sha256 `9fbb360b303beb7cc5364b1a8662b4a5da90320f013354395db193002dff80ed`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/other/unknown/minepacks/MinePacks-1.13.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
