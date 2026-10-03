# EconomyShop(掉落物商店)

## 功能简介

**掉落物商店(EconomyShop)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `2.0.7`,作者 onebone。
主要功能方向:经济/商店、管理/权限。
原插件说明:Management command for creating/removing shop
本插件共提供 **1** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/shop` | Management command for creating/removing shop | `/shop <create|remove|list> [物品[:后缀]] [数量] [价格] [side]` | economyshop.command.shop;economyshop.command.shop.create;economyshop.command.shop.remove;economyshop.command.shop.list; | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `economyshop.*` | Allows player to buy from shop | true |

## 如何使用

1. 下载下方插件文件 `EconomyShop-2.0.7.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `economyshop`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: 0.11.0, 0.11.1, 0.14.0, 1.0.0, 1.8.0, 1.12.0
- **plugin_version**: `2.0.7`
- **author**: onebone
- **dependencies**: [EconomyAPI]
- **main**: `onebone\economyshop\EconomyShop`
- **license**: NOASSERTION (unknown)
- **tags**: economy, admin

## 下载

- `EconomyShop-2.0.7.phar`(**32801** 字节,sha256 `dd3beb2c41f9198ea5369254dfabb5982753633c8c05da74caf926327c2a0ea5`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/unknown/economyshop/EconomyShop-2.0.7.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
