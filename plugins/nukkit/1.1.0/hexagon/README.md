# Hexagon(多功能)

## 功能简介

**多功能(Hexagon)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `1.0.0`,作者 SoleMemory。
主要功能方向:管理/权限。
原插件说明:Hexagon 管理主命令
本插件共提供 **5** 条命令(见下表)。
共定义 **5** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/admin` | Hexagon 管理主命令 | `/admin` | sole.memory.admincommand | - |
| `/v` | Uninvited VIP主命令 | `/v` | sole.memory.vipcommand | - |
| `/公会` | Hexagon 公会主命令 | `/公会` | sole.memory.factioncommand | - |
| `/结婚` | Hexagon 结婚主命令 | `/结婚` | sole.memory.marrycommand | - |
| `/称号` | Hexagon 称号主命令 | `/称号` | sole.memory.prefixcommand | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `sole.memory.admincommand` | - | op |
| `sole.memory.vipcommand` | - | true |
| `sole.memory.factioncommand` | - | true |
| `sole.memory.marrycommand` | - | true |
| `sole.memory.prefixcommand` | - | true |

## 如何使用

1. 下载下方插件文件 `Hexagon-1.0.0.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `hexagon`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `1.1.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.1.0
- **plugin_version**: `1.0.0`
- **author**: SoleMemory
- **dependencies**: ["Money"]
- **main**: `sole.memory.Communication`
- **license**: NOASSERTION (unknown)
- **tags**: admin

## 下载

- `Hexagon-1.0.0.jar`(**18028** 字节,sha256 `b28b40e3398c628802c2fd469e8bb457c1d94e2608dc0e2daf34ca2e2f3efcc8`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/1.1.0/hexagon/Hexagon-1.0.0.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
