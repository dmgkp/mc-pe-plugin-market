# BetterGen(高逼格地图生成器)

## 功能简介

**高逼格地图生成器(BetterGen)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.1`,作者 Ad5001。
主要功能方向:世界/传送。
原插件说明:Generates a new world.
本插件共提供 **3** 条命令(见下表)。
共定义 **3** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/createworld` | Generates a new world. | `/createworld <name> [generator = betternormal] [seed = rand()] [options (json)]` | bettergen.cmd.createworld | - |
| `/worldtp` | Teleports you to an another world | `/worldtp <world name>` | bettergen.cmd.worldtp | - |
| `/temple` | Spawns a temple for debugging | `/temple` | bettergen.cmd.debug | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `bettergen.cmd.createworld` | - | op |
| `bettergen.cmd.worldtp` | - | op |
| `bettergen.cmd.debug` | - | op |

## 如何使用

1. 下载下方插件文件 `BetterGen-1.1.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `bettergen`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.12.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.12.0
- **plugin_version**: `1.1`
- **author**: Ad5001
- **main**: `Ad5001\BetterGen\Main`
- **license**: NOASSERTION (unknown)
- **tags**: world

## 下载

- `BetterGen-1.1.phar`(**19997501** 字节,sha256 `44763be902b00ea224c2efe58f0d6831e1d53a5261b929e7bc8f8b2228a32d2a`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.12.0/bettergen/BetterGen-1.1.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
