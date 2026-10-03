# Slapper(插件)

## 功能简介

**插件(Slapper)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.1`,作者 jojoe77777。
主要功能方向:世界/传送、管理/权限、特效/粒子。
原插件说明:Adds player NPCs into your world that you can slap to run commands!
本插件共提供 **1** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/slapper` | Create a slappable player! | `/slapper <name>` | slapper.create | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `slapper.create` | allow using command /slapper | op |

## 如何使用

1. 下载下方插件文件 `Slapper-1.0.1.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `slapper`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.11.1` (推断来源: path)
- **minecraft_versions**: 0.11.0, 0.11.1, 1.6.0, 1.8.0
- **plugin_version**: `1.0.1`
- **author**: jojoe77777
- **main**: `slapper\main`
- **license**: NOASSERTION (unknown)
- **tags**: world, admin, cosmetic

## 下载

- `Slapper-1.0.1.phar`(**8688** 字节,sha256 `013fb69650518dcb34a34aedb2b8447a93b310db3b58c6db4b3db8038c1f7411`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.11.1/slapper/Slapper-1.0.1.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
