# MagicTelePortal(MagicTelePortal)

## 功能简介

**MagicTelePortal(MagicTelePortal)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.3.2`,作者 aliuly。
主要功能方向:世界/传送。
原插件说明:A simple portal plugin
本插件共提供 **1** 条命令(见下表)。
共定义 **2** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/mtp` | Create a portal | `/mtp [world|addr:port] [x y z]` | mtp.cmd.mtp | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `mtp.cmd.mtp` | Allow to create portal | op |
| `mtp.destroy` | Allow destruction of portals | op |

## 如何使用

1. 下载下方插件文件 `MagicTelePortal-1.3.2.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `magicteleportal`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.11.0` (推断来源: path)
- **minecraft_versions**: 0.11.0, 0.11.1, 1.6.0
- **plugin_version**: `1.3.2`
- **author**: aliuly
- **main**: `aliuly\mtp\Main`
- **license**: NOASSERTION (unknown)
- **tags**: world

## 下载

- `MagicTelePortal-1.3.2.phar`(**8612** 字节,sha256 `ca320ff4387e2223a012c2290cd86a386d2d56256a5ad9c3ac7c4e69c443972e`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.11.0/magicteleportal/MagicTelePortal-1.3.2.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
