# RandomSpawn(随机出生点插件)

## 功能简介

**随机出生点插件(RandomSpawn)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.0`,作者 Angus。
主要功能方向:世界/传送。
原插件说明:spawn Random
本插件共提供 **4** 条命令(见下表)。
共定义 **3** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/setspawn1` | set spawn 1 | `/setspawn1` | randomspawn.command.setspawn1 | - |
| `/setspawn2` | set spawn 2 | `/setspawn2` | randomspawn.command.setspawn2 | - |
| `/setspawn3` | set spawn 3 | `/setspawn3` | randomspawn.command.setspawn3 | - |
| `/setspawn4` | set spawn 4 | `/setspawn4` | randomspawn.command.setspawn4 | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `randomspawn.command.setspawn1` | set spawn 2 | op |
| `randomspawn.command.setspawn3` | set spawn 3 | op |
| `randomspawn.command.setspawn4` | set spawn 4 | op |

## 如何使用

1. 下载下方插件文件 `RandomSpawn-1.0.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `randomspawn`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.1, 0.14.0, 1.6.0
- **plugin_version**: `1.0.0`
- **author**: Angus
- **main**: `RandomSpawn\RandomSpawn`
- **license**: NOASSERTION (unknown)
- **tags**: world

## 下载

- `RandomSpawn-1.0.0.phar`(**5594** 字节,sha256 `59bb32ca3693c3c1ac5782712d66ae3613d05cddf01ef8181cb6297a66021bbb`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/randomspawn/RandomSpawn-1.0.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
