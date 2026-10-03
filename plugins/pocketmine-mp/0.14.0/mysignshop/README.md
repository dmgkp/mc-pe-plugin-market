# MySignShop(京东个人商店)

## 功能简介

**京东个人商店(MySignShop)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.7`,作者 Him188。
主要功能方向:经济/商店、世界/传送、管理/权限、前置/API 库。
原插件说明:让玩家创建自己的商店 使用EconomyAPI 并检测EconomyLand.
本插件共提供 **2** 条命令(见下表)。
共定义 **2** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/mss` | 个人商店管理命令 | `/mss <删除全部 | delall>` | MySignShop.command.mss | - |
| `/itemid` | 获取手中物品名称和ID | `/itemid` | MySignShop.command.itemid | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `MySignShop.command.mss` | 仅OP使用 | op |
| `MySignShop.command.itemid` | 允许所有人 | true |

## 如何使用

1. 下载下方插件文件 `MySignShop-1.0.7.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `mysignshop`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.0, 0.11.1, 0.14.0
- **plugin_version**: `1.0.7`
- **author**: Him188
- **main**: `MySignShop\MySignShop`
- **license**: NOASSERTION (unknown)
- **tags**: economy, world, admin, library

## 下载

- `MySignShop-1.0.7.phar`(**22982** 字节,sha256 `b8298b243f2e0fb53f32837f2010ce392e12bc368ba27522c2a9fe0ea57d2598`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/mysignshop/MySignShop-1.0.7.phar`

## 历史版本

- 1.0.0: MySignShop-1.0.0.phar
- 1.0.2: MySignShop-1.0.2.phar
- 1.0.5: MySignShop-1.0.5.phar
- 1.0.6: MySignShop-1.0.6.phar

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
