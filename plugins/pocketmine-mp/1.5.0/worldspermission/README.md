# WorldsPermission(世界白名单)

## 功能简介

**世界白名单(WorldsPermission)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.4.0.0_JCB`,作者 zzx。
主要功能方向:世界/传送、管理/权限。
原插件说明:服务器地图权限插件
本插件共提供 **11** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/p` | 给予玩家地图权限 | `/p [id] [world]` | WorldsPermission.command.op | - |
| `/dp` | 移除玩家地图权限 | `/dp [id] [world]` | WorldsPermission.command.op | - |
| `/wp` | 给予玩家(你)所在地图权限 | `/wp [id]` | WorldsPermission.command.op | - |
| `/mywp` | 查看自己拥有权限的地图 | `/mywp 查看自己拥有权限的地图` | - | - |
| `/seewp` | 查看某玩家拥有权限的地图 | `/seewp [id]` | WorldsPermission.command.op | - |
| `/ww` | 设置白名单地图 | `/ww [world]` | WorldsPermission.command.op | - |
| `/bw` | 设置禁止地图名单 | `/bw [world]` | WorldsPermission.command.op | - |
| `/wadmin` | 地图权限管理员 | `/wadmin [id]` | WorldsPermission.command.op | - |
| `/setwcs` | 设置地图游戏模式 | `/setwcs [world] (0/1/off)` | WorldsPermission.command.op | - |
| `/wperlist` | 查看设置列表 | `/wperlist` | WorldsPermission.command.op | - |
| `/onwlist` | 在线玩家地图信任状态 | `/onwlist` | WorldsPermission.command.op | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `WorldsPermission` | Allows access to the WorldsPermission command. | op |

## 如何使用

1. 下载下方插件文件 `WorldsPermission-1.4.0.0_JCB.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `worldspermission`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.5.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.0, 0.11.1, 1.5.0
- **plugin_version**: `1.4.0.0_JCB`
- **author**: zzx
- **main**: `WorldsPermission\WorldsPermission`
- **license**: NOASSERTION (unknown)
- **tags**: world, admin

## 下载

- `WorldsPermission-1.4.0.0_JCB.phar`(**7264** 字节,sha256 `7b1480133a58200cb254a25f0fcd4e08769667b06d69d22191c7f65319e4503d`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.5.0/worldspermission/WorldsPermission-1.4.0.0_JCB.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
