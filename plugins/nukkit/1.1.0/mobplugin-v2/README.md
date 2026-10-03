# MobPlugin(生物)

## 功能简介

**生物(MobPlugin)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `1.0`,作者 kniffo80,PikyCZ,CreeperFace,NycuRO。
主要功能方向:世界/传送、管理/权限、玩法、特效/粒子。
原插件说明:Spawn a simple mob to the player, that is using this command
本插件共提供 **2** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/mob` | Spawn a simple mob to the player, that is using this command | `/mob spawn <mob_name>` | mob-plugin.command | mob |
| `/removemobs` | Remove all living mobs | `/mob removeall` | mob-plugin.command | removeall |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `mob-plugin.command` | - | op |

## 如何使用

1. 下载下方插件文件 `MobPlugin-1.0.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `mobplugin-v2`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `1.1.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.1.0
- **plugin_version**: `1.0`
- **author**: kniffo80,PikyCZ,CreeperFace,NycuRO
- **main**: `com.pikycz.mobplugin.MobPlugin`
- **license**: NOASSERTION (unknown)
- **tags**: world, admin, gameplay, cosmetic

## 下载

- `MobPlugin-1.0.jar`(**2408960** 字节,sha256 `3800debc84ef4018a57bc4d7510f705b5c0c7ac4704be35ca18228f378f0c261`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/1.1.0/mobplugin-v2/MobPlugin-1.0.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
