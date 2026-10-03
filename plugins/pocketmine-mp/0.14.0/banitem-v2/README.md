# BanItem(极致整合)

## 功能简介

**极致整合(BanItem)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `2.2`,作者 LDX。
主要功能方向:管理/权限。
原插件说明:BanItem main command.
本插件共提供 **1** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/banitem` | BanItem main command. | `/banitem <ban/unban/list> [ID[:Damage]]` | banitem.command.banitem | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `banitem` | Allows access to the item command. | op |

## 如何使用

1. 下载下方插件文件 `BanItem-2.2.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `banitem-v2`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0, 1.1.0
- **plugin_version**: `2.2`
- **author**: LDX
- **main**: `LDX\BanItem\Main`
- **license**: NOASSERTION (unknown)
- **tags**: admin

## 下载

- `BanItem-2.2.phar`(**5962** 字节,sha256 `407b9b9b2530d9a531771dfae28724aa773588bdbdfe201083140872f07bf7c3`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/banitem-v2/BanItem-2.2.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
