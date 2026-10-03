# ProtocolLib(基础插件)

## 功能简介

**基础插件(ProtocolLib)** 是一款运行于 **其它服务端** 的 Minecraft 基岩版插件,插件版本 `3.6.4`,作者 unknown。
主要功能方向:玩法。
原插件说明:Provides read/write access to the Minecraft protocol.
本插件共提供 **3** 条命令(见下表)。
共定义 **3** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/protocol` | Performs administrative tasks regarding ProtocolLib. | `/<command> config|timings|listeners|version` | protocol.admin | - |
| `/packet` | Add or remove a simple packet listener. | `/<command> add|remove|names client|server [ID start]-[ID stop] [detailed]` | protocol.admin | - |
| `/filter` | Add or remove programmable filters to the packet listeners. | `/<command> add|remove name [ID start]-[ID stop]` | protocol.admin | packet_filter |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `protocol.*` | Gives access to everything. | - |
| `protocol.admin` | Able to initiate the update process, and can configure debug mode. | op |
| `protocol.info` | Can read update notifications and error reports. | op |

## 如何使用

1. 下载下方插件文件 `ProtocolLib-3.6.4.jar`。
2. 放入服务器 `plugins/` 目录(其它服务端)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `protocollib`
- **edition**: bedrock
- **server_type**: `other`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: unknown
- **plugin_version**: `3.6.4`
- **author**: unknown
- **main**: `com.comphenix.protocol.ProtocolLibrary`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `ProtocolLib-3.6.4.jar`(**1448394** 字节,sha256 `cb7aff23ea7206e4e5df7646a68181e1a82f4d11257bb158989ed4c69805a204`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/other/unknown/protocollib/ProtocolLib-3.6.4.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
