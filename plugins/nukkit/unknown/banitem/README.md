# BanItem(基础插件)

## 功能简介

**基础插件(BanItem)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `2.8`,作者 abcalvin。
主要功能方向:管理/权限。
原插件说明:Version
本插件共提供 **9** 条命令(见下表)。
共定义 **11** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/banitem` | Version | `/banitem` | - | - |
| `/banitem add` | Add ban item to ban item list | `/banitem add` | - | - |
| `/banitem add all` | Add ban item with all the data to ban item list | `/banitem add all` | - | - |
| `/banitem remove` | Remove ban item from ban item list | `/banitem remove` | - | - |
| `/banitem del` | Remove ban item from ban item list | `/banitem del` | - | - |
| `/banitem check` | Check if item is banned | `/banitem check` | - | - |
| `/banitem toggle conf` | toggles confiscation of items | `/banitem toggle conf` | - | - |
| `/banitem reload` | Reload banitem. | `/banitem reload` | - | - |
| `/banitem clear` | check inventory for items that are banned. | `/banitem clear` | - | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `banitem.reload` | Reload banitem. | - |
| `banitem.check` | Check if item is banned | - |
| `banitem.add` | Blacklist an Item | - |
| `banitem.del` | remove an item from blacklist | - |
| `banitem.toggle` | toggle options in config. | - |
| `banitem.bypass.<itemid>` | bypass banned items | - |
| `banitem.int.<itemid>` | bypass interaction of ban item | - |
| `banitem.break.<itemid>` | bypass block break of ban item | - |
| `banitem.place.<itemid>` | bypass block place of ban item | - |
| `banitem.pickup.<itemid>` | bypass pickup of ban item | - |
| `banitem.click.<itemid>` | bypass Click of banned item | - |

## 如何使用

1. 下载下方插件文件 `BanItem-2.8.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `banitem`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: 0.14.0, 1.1.0
- **plugin_version**: `2.8`
- **author**: abcalvin
- **main**: `com.abcalvin.BanItem.main`
- **license**: NOASSERTION (unknown)
- **tags**: admin

## 下载

- `BanItem-2.8.jar`(**31025** 字节,sha256 `1e7490f1efbb14458096b349b0cdb44132ba1798a620b637a9561d612b6534b7`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/unknown/banitem/BanItem-2.8.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
