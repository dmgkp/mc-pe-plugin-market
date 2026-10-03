# MySignShop(MySignShop)

## 功能简介

**MySignShop(MySignShop)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.1`,作者 Him188。
主要功能方向:经济/商店、管理/权限、前置/API 库。
原插件说明:让玩家创建自己的商店 使用EconomyAPI.
本插件共提供 **2** 条命令(见下表)。
共定义 **2** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/mss` | 个人商店管理命令 | `/mss <删除全部 | delall>` | MySignShop.command.mss | - |
| `/id` | 获取手中物品名称和ID | `/id` | MySignShop.command.id | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `MySignShop.command.mss` | 仅OP使用 | op |
| `MySignShop.command.id` | 允许所有人 | true |

## 如何使用

1. 下载下方插件文件 `MySignShop-1.0.1.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `mysignshop`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.11.0` (推断来源: path)
- **minecraft_versions**: 0.11.0, 0.11.1, 0.14.0
- **plugin_version**: `1.0.1`
- **author**: Him188
- **main**: `MySignShop\MySignShop`
- **license**: NOASSERTION (unknown)
- **tags**: economy, admin, library

## 下载

- `MySignShop-1.0.1.phar`(**21690** 字节,sha256 `51b1948d759e9c26a52f4a09221d83d88d44a1f12026187351ee0c991ba3ec2d`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.11.0/mysignshop/MySignShop-1.0.1.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
