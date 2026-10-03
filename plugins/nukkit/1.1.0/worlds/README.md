# Worlds(多世界)

## 功能简介

**多世界(Worlds)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `1.1.0`,作者 uuuuone。
主要功能方向:世界/传送。
原插件说明:多世界
本插件共提供 **5** 条命令(见下表)。
共定义 **2** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/w` | 传送到某个地图 | `/w [地图名]` | Worlds.command.Worlds | - |
| `/lw` | 列出世界列表 | `/lw` | Worlds.command.Worlds | - |
| `/load` | 加载地图 | `/load [地图名]` | Worlds.command.opWorlds | - |
| `/unload` | 卸载地图 | `/unload [地图名]` | Worlds.command.opWorlds | - |
| `/newworld` | 新建地图 | `/newworld [地图名] [seed]` | Worlds.command.opWorlds | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `Worlds.command.Worlds` | 允许玩家运行/w ,/lw | true |
| `Worlds.command.opWorlds` | 允许 OP 运行/load , /unload | op |

## 如何使用

1. 下载下方插件文件 `Worlds-1.1.0.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `worlds`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `1.1.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.15.0, 1.1.0, 1.12.0
- **plugin_version**: `1.1.0`
- **author**: uuuuone
- **main**: `Worlds.Worlds`
- **license**: NOASSERTION (unknown)
- **tags**: world

## 下载

- `Worlds-1.1.0.jar`(**2906** 字节,sha256 `331c83399aa8d8d4c2c0088f3836efc74dcb2b7790c539fd8949bd2fcc1e8910`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/1.1.0/worlds/Worlds-1.1.0.jar`

## 历史版本

- 1.0.0: Worlds-1.0.0.jar

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
