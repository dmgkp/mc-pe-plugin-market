# PureEntitiesX(更新)

## 功能简介

**更新(PureEntitiesX)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `0.2.2_dev`,作者 unknown。
主要功能方向:世界/传送。
原插件说明:Implement all MCPE entities into your worlds
本插件共提供 **2** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/pesummon` | Summons a creature | `/pesummon <mob-name> [playername] [isBaby(true|false)]` | pureentities.command.pesummon | - |
| `/peremove` | Removes all entities from the current level | `/peremove` | pureentities.command.peremove | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `pureentities` | Allows remove of all entities in current level | op |

## 如何使用

1. 下载下方插件文件 `PureEntitiesX-0.2.2_dev.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `pureentitiesx`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.12.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0, 1.12.0
- **plugin_version**: `0.2.2_dev`
- **author**: unknown
- **main**: `revivalpmmp\pureentities\PureEntities`
- **license**: NOASSERTION (unknown)
- **tags**: world

## 下载

- `PureEntitiesX-0.2.2_dev.phar`(**184629** 字节,sha256 `6f4f2d1867b8a5cd3c8a081c99019d5895e003aaa5a0d141270712b1c2b10a6e`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.12.0/pureentitiesx/PureEntitiesX-0.2.2_dev.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
