# TempBanUI(玩家封禁)

## 功能简介

**玩家封禁(TempBanUI)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.1`,作者 SonsaYT。
主要功能方向:管理/权限。
原插件说明:开启玩家封禁表单
本插件共提供 **2** 条命令(见下表)。
共定义 **2** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/tban` | 开启玩家封禁表单 | `/tban` | use.tban | - |
| `/tcheck` | 检查封禁玩家列表 | `/tcheck` | use.tcheck | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `use.tban` | Use /tban command | op |
| `use.tcheck` | Use /tcheck command | op |

## 如何使用

1. 下载下方插件文件 `TempBanUI-1.1.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `tempbanui`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.12.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.12.0
- **plugin_version**: `1.1`
- **author**: SonsaYT
- **main**: `TempBanUI\Main`
- **license**: NOASSERTION (unknown)
- **tags**: admin

## 下载

- `TempBanUI-1.1.phar`(**32093** 字节,sha256 `f185e9df98783fbb29f92328ac1390a90a102e686598ad72e67fc04d6a5402ff`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.12.0/tempbanui/TempBanUI-1.1.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
