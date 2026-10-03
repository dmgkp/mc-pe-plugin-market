# SimpleWarp(简单传送)

## 功能简介

**简单传送(SimpleWarp)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0`,作者 Falk。
主要功能方向:世界/传送。
原插件说明:Warp to a location
本插件共提供 **3** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/warp` | Warp to a location | `/warp <NAME>` | - | - |
| `/addwarp` | Add a new warp point | `/addwarp <NAME>` | simplewarp.manage | - |
| `/delwarp` | Delete a warp point | `/delwarp <NAME>` | simplewarp.manage | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `simplewarp` | Allows usage of all warps | op |

## 如何使用

1. 下载下方插件文件 `SimpleWarp-1.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `simplewarp`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0, 0.16.0
- **plugin_version**: `1.0`
- **author**: Falk
- **main**: `SimpleWarp\SimpleWarp`
- **license**: NOASSERTION (unknown)
- **tags**: world

## 下载

- `SimpleWarp-1.0.phar`(**5081** 字节,sha256 `bedb0bd01547f6b52e9ce4aee5c70744a6b5384137f31c7a0193e9457b25bb47`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/simplewarp/SimpleWarp-1.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
