# DisableFlow(禁止流动)

## 功能简介

**禁止流动(DisableFlow)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `1.2.0`,作者 uuuuone。
主要功能方向:玩法。
原插件说明:禁止液体流动
本插件共提供 **2** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/flow` | flow命令集 | `/flow [on/off]` | DisableFlow.command.flow | - |
| `/cflow` | cflow命令集 | `/cflow [add/del/list] [world]` | DisableFlow.command.flow | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `DisableFlow.command.flow` | 允许OP运行/flow 命令 | op |

## 如何使用

1. 下载下方插件文件 `DisableFlow-1.2.0.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `disableflow`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `1.1.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.0, 0.11.1, 1.1.0, 1.4.0
- **plugin_version**: `1.2.0`
- **author**: uuuuone
- **main**: `DisableFlow.DisableFlow`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `DisableFlow-1.2.0.jar`(**4143** 字节,sha256 `26c373ae978c7dba5023713bfefb55c742b60d412f17628863423d5bb690422d`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/1.1.0/disableflow/DisableFlow-1.2.0.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
