# QwickTree(基础插件)

## 功能简介

**基础插件(QwickTree)** 是一款运行于 **其它服务端** 的 Minecraft 基岩版插件,插件版本 `2.1.1`,作者 gorbb。
主要功能方向:管理/权限。
原插件说明:Quickly chop down trees with the swing of an axe!
本插件共提供 **1** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/qt` | QwickTree admin/debug command | `Try /<command> for help.` | - | qwicktree |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `qwicktree.*` | Lets the player see and clear the list of players for who the plugin is disabled for. | op |

## 如何使用

1. 下载下方插件文件 `QwickTree-2.1.1.jar`。
2. 放入服务器 `plugins/` 目录(其它服务端)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `qwicktree`
- **edition**: bedrock
- **server_type**: `other`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: unknown
- **plugin_version**: `2.1.1`
- **author**: gorbb
- **softdependencies**: [CoreProtect]
- **main**: `uk.co.gorbb.qwicktree.QwickTree`
- **website**: http://dev.bukkit.org/bukkit-plugins/qwicktree/
- **license**: NOASSERTION (unknown)
- **tags**: admin

## 下载

- `QwickTree-2.1.1.jar`(**59271** 字节,sha256 `1c3086a620cc1507f8c0e65355b9d4ed94a443ac519d07214b3c6a98b020e130`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/other/unknown/qwicktree/QwickTree-2.1.1.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
