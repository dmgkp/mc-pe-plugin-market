# Killheart(杀死玩家获得生命插件)

## 功能简介

**杀死玩家获得生命插件(Killheart)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.0`,作者 BukkitPlaysMC。
主要功能方向:玩法。
原插件说明:Change the Amount of given Hearts at a kill
本插件共提供 **1** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/changehearts` | Change the Amount of given Hearts at a kill | `/changeahearts <Amount>` | KillHeart.changehearts | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `KillHeart.changehearts` | Permission for /changehearts | op |

## 如何使用

1. 下载下方插件文件 `Killheart-1.0.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `killheart`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.11.0` (推断来源: path)
- **minecraft_versions**: 0.11.0, 0.11.1, 0.14.0
- **plugin_version**: `1.0.0`
- **author**: BukkitPlaysMC
- **main**: `BukkitPlaysMC\Killheart\Main`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `Killheart-1.0.0.phar`(**4293** 字节,sha256 `17ca0ba494c0b7ea50b2ac27344c0639371a3d1e48cd701f48f5ee3499e40065`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.11.0/killheart/Killheart-1.0.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
