# ServerRestarter(基础插件)

## 功能简介

**基础插件(ServerRestarter)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `0.48`,作者 DarkStorm_。
主要功能方向:玩法。
原插件说明:Simple configurable server restarting plugin
本插件共提供 **1** 条命令(见下表)。
共定义 **2** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/restart` | ServerRestarter command. | `/<command> [restart | [[time] [message]]]` | - | sr |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `sr.*` | ServerRestarter permission nodes. | op |
| `sr.restart` | Permission to use the /restart command. | op |

## 如何使用

1. 下载下方插件文件 `ServerRestarter-0.48.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `serverrestarter`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: unknown
- **plugin_version**: `0.48`
- **author**: DarkStorm_
- **main**: `org.darkstorm.minecraft.bukkit.serverrestarter.ServerRestarter`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `ServerRestarter-0.48.jar`(**33740** 字节,sha256 `e85a6b5bb082055fb617cac6d952bd5f3a10724bb2318e55847aedd1fc89f473`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/unknown/serverrestarter/ServerRestarter-0.48.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
