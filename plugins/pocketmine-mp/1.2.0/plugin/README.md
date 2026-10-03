# 史蒂夫大战僵尸(史蒂夫大战僵尸)

## 功能简介

**史蒂夫大战僵尸(史蒂夫大战僵尸)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `2.1.0`,作者 boybook。
主要功能方向:玩法。
原插件说明:ZombieVsSteve Game in PE!
本插件共提供 **6** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/zvsstart` | start a game in a room | `/zvsstart <room>` | ZombieVsSteve.command.zvsstart | - |
| `/zvsstop` | stop a game in a room | `/zvsstop <room>` | ZombieVsSteve.command.zvsstop | - |
| `/zvsgo` | Maternal zombie | `/zvsgo <room>` | ZombieVsSteve.command.zvsgo | - |
| `/zvstest` | see the array of gamers | `/zvstest` | ZombieVsSteve.command.zvstest | - |
| `/join` | join room | `/join <room number>` | ZombieVsSteve.command.join | - |
| `/zvsrb` | rollback the maps | `/rb <room number>` | ZombieVsSteve.command.rb | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `ZombieVsSteve` | rollback | op |

## 如何使用

1. 下载下方插件文件 `file-2.1.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `plugin`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.2.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.0, 0.11.1, 0.14.0, 0.16.0, 1.2.0, 1.6.0, 1.8.0, 1.9.0, 1.12.0
- **plugin_version**: `2.1.0`
- **author**: boybook
- **main**: `ZombieVsSteve\ZombieVsSteve`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `file-2.1.0.phar`(**126692** 字节,sha256 `f4d44626435053ffb1b74e05a6f0065a39466805f15247576596d7779ee86291`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.2.0/plugin/file-2.1.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
