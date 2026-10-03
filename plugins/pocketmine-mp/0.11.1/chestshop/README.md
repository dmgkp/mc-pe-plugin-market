# ChestShop(箱子商店)

## 功能简介

**箱子商店(ChestShop)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `2.0.1 luo123优化`,作者 MinecrafterJPN（原作者）。
主要功能方向:经济/商店、管理/权限、保护/防作弊。
原插件说明:Open your ChestShop
本插件共提供 **2** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/id` | 查看物品ID | `Usage: /id <物品名字>` | chestshop.command.id | - |
| `/remove` | 移除一个玩家的所有玩家商店 | `Usage: /remove <玩家名字>` | chestshop.command.remove | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `chestshop` | Allows removing player's ChestShop | op |

## 如何使用

1. 下载下方插件文件 `ChestShop-2.0.1_luo123.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `chestshop`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.11.1` (推断来源: path)
- **minecraft_versions**: 0.11.1, 1.6.0
- **plugin_version**: `2.0.1 luo123优化`
- **author**: MinecrafterJPN（原作者）
- **dependencies**: EconomyAPI
- **main**: `ChestShop\ChestShop`
- **license**: NOASSERTION (unknown)
- **tags**: economy, admin, protection

## 下载

- `ChestShop-2.0.1_luo123.phar`(**4212** 字节,sha256 `64adfe07e2cc6dcf0aec207acbaf491565c9aadcf8d67f9f90685509854bf567`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.11.1/chestshop/ChestShop-2.0.1_luo123.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
