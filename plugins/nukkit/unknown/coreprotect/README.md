# CoreProtect(基础插件)

## 功能简介

**基础插件(CoreProtect)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `2.0.8`,作者 Intelli。
主要功能方向:保护/防作弊、前置/API 库。
原插件说明:>
本插件共提供 **3** 条命令(见下表)。
共定义 **15** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/core` | Utilize the plugin | `|` | - | - |
| `/coreprotect` | Utilize the plugin | `|` | - | - |
| `/co` | Utilize the plugin | `|` | - | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `coreprotect.*` | Gives access to all CoreProtect actions and commands | false |
| `coreprotect.lookup` | Has permission to use the lookup command | false |
| `coreprotect.lookup.chat` | Has permission to lookup chat messages | false |
| `coreprotect.lookup.command` | Has permission to lookup player commands | false |
| `coreprotect.lookup.session` | Has permission to lookup player sessions | false |
| `coreprotect.lookup.block` | Has permission to lookup block data | false |
| `coreprotect.lookup.click` | Has permission to lookup player interactions | false |
| `coreprotect.lookup.container` | Has permission to lookup container transactions | false |
| `coreprotect.lookup.container` | Has permission to lookup entity kills | false |
| `coreprotect.rollback` | Has permission to perform rollbacks | false |
| `coreprotect.restore` | Has permission to perform restores | false |
| `coreprotect.inspect` | Has permission to use the inspector | false |
| `coreprotect.help` | Has permission to use the help command | false |
| `coreprotect.purge` | Has permission to use the purge command | false |
| `coreprotect.reload` | Has permission to use the reload command | false |

## 如何使用

1. 下载下方插件文件 `CoreProtect-2.0.8.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `coreprotect`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: unknown
- **plugin_version**: `2.0.8`
- **author**: Intelli
- **main**: `net.coreprotect.CoreProtect`
- **website**: http://coreprotect.net
- **license**: NOASSERTION (unknown)
- **tags**: protection, library

## 下载

- `CoreProtect-2.0.8.jar`(**246269** 字节,sha256 `aab250a2b540c9d8f10b87f90940db16ab7f46fb772e0f0cd2bbfde7b73fa687`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/unknown/coreprotect/CoreProtect-2.0.8.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
