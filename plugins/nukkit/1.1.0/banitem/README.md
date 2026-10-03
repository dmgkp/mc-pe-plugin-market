# Banitem(禁止物品)

## 功能简介

**禁止物品(Banitem)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `1.2.1`,作者 uuuuone。
主要功能方向:管理/权限。
原插件说明:禁止物品
本插件共提供 **1** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/banitem` | banitem命令集 | `/banitem [item/admin/list] [add/del] [ID] [meta]` | Banitem.command.banitem | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `Banitem.command.banitem` | 允许OP运行/banitem 命令 | op |

## 如何使用

1. 下载下方插件文件 `Banitem-1.2.1.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `banitem`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `1.1.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0, 1.1.0
- **plugin_version**: `1.2.1`
- **author**: uuuuone
- **main**: `Banitem.Banitem`
- **license**: NOASSERTION (unknown)
- **tags**: admin

## 下载

- `Banitem-1.2.1.jar`(**4965** 字节,sha256 `e2a05c8d9678f5ff34163d14815b9c85992698623c17043e52ac776a0e57e6e2`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/1.1.0/banitem/Banitem-1.2.1.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
