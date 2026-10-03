# WorldProtect(极致整合)

## 功能简介

**极致整合(WorldProtect)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.5`,作者 happylife。
主要功能方向:世界/传送、管理/权限、保护/防作弊。
原插件说明:禁用物品插件(可设置管理员)
本插件共提供 **1** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/wp` | wp (world/admin/list) <世界名称/管理员名称> 添加世界/管理员/世界和管理员列表 | `/wp (world/admin/list) <世界名称/管理员名称> 添加世界/管理员/世界和管理员列表` | wp.command.wp | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `worldprotect` | Allows access to the wp command. | op |

## 如何使用

1. 下载下方插件文件 `WorldProtect-1.5.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `worldprotect-v2`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.1, 0.14.0, 1.1.0, 1.5.0, 1.6.0
- **plugin_version**: `1.5`
- **author**: happylife
- **main**: `WorldProtect\WorldProtect`
- **license**: NOASSERTION (unknown)
- **tags**: world, admin, protection

## 下载

- `WorldProtect-1.5.phar`(**2527** 字节,sha256 `662d39a4795d2950159c4d625fbf27f25d7364ad6629c297c29aeaddcfa6c3db`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/worldprotect-v2/WorldProtect-1.5.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
