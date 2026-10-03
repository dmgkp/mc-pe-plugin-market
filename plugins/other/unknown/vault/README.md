# Vault(基础插件)

## 功能简介

**基础插件(Vault)** 是一款运行于 **其它服务端** 的 Minecraft 基岩版插件,插件版本 `1.4.1-b436`,作者 unknown。
主要功能方向:经济/商店、管理/权限、前置/API 库。
原插件说明:Vault is a Permissions & Economy API to allow plugins to more easily hook into these systems without needing to hook each individual system themselves.
本插件共提供 **2** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/vault-info` | Displays information about Vault | `|` | - | - |
| `/vault-convert` | Converts all data in economy1 and dumps it into economy2 | `|` | - | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `vault.admin` | Notifies the player when vault is in need of an update. | op |

## 如何使用

1. 下载下方插件文件 `Vault-1.4.1-b436.jar`。
2. 放入服务器 `plugins/` 目录(其它服务端)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `vault`
- **edition**: bedrock
- **server_type**: `other`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: unknown
- **plugin_version**: `1.4.1-b436`
- **author**: unknown
- **main**: `net.milkbowl.vault.Vault`
- **website**: http://dev.bukkit.org/server-mods/vault/
- **license**: NOASSERTION (unknown)
- **tags**: economy, admin, library

## 下载

- `Vault-1.4.1-b436.jar`(**337004** 字节,sha256 `21ed1c2cd4a5b531b73056fb5c8a445e17486bc7c7649eb58e4417c7cc1fc01a`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/other/unknown/vault/Vault-1.4.1-b436.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
