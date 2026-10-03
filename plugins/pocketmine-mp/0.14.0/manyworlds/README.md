# ManyWorlds(世界管理插件)

## 功能简介

**世界管理插件(ManyWorlds)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `2.0.0`,作者 aliuly。
主要功能方向:世界/传送。
原插件说明:Manage Multiple Worlds
本插件共提供 **1** 条命令(见下表)。
共定义 **8** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/mw` | Manage worlds | `/mw <help|sub-cmd> [options]` | mw.cmds | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `mw.cmds` | Allow all the ManyWorlds functionality | true |
| `mw.cmd.tp` | Allows users to travel to other worlds | op |
| `mw.cmd.tp.others` | Allows users to make others travel to other worlds | op |
| `mw.cmd.ls` | Allows users to list worlds | op |
| `mw.cmd.world.create` | Allows users to create worlds | op |
| `mw.cmd.world.load` | Allows users to load worlds | op |
| `mw.cmd.lvdat` | Manipulate level.dat | op |
| `mw.cmd.default` | Changes default world | op |

## 如何使用

1. 下载下方插件文件 `ManyWorlds-2.0.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `manyworlds`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.1, 0.14.0, 1.6.0
- **plugin_version**: `2.0.0`
- **author**: aliuly
- **main**: `aliuly\manyworlds\Main`
- **license**: NOASSERTION (unknown)
- **tags**: world

## 下载

- `ManyWorlds-2.0.0.phar`(**60905** 字节,sha256 `c3c1e6816c056553d0d8bd87d7569f6df1425429163a3f39c6adf915aff9bc81`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/manyworlds/ManyWorlds-2.0.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
