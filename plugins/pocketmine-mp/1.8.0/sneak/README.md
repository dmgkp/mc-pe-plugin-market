# Sneak(潜行插件)

## 功能简介

**潜行插件(Sneak)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.1`,作者 CrazedMiner。
主要功能方向:管理/权限。
原插件说明:Players can Sneak by simply using a Command!
本插件共提供 **1** 条命令(见下表)。
共定义 **2** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/sneak` | Toggles Sneaking for you or the specified Player | `/sneak` | - | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `sneak.command.other` | Players with this permission are able to toggle sneaking for other Players | op |
| `sneak.command.self` | Players with this permission are able to toggle Sneaking for themselves | true |

## 如何使用

1. 下载下方插件文件 `Sneak-1.1.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `sneak`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.8.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.1, 0.14.0, 1.8.0
- **plugin_version**: `1.1`
- **author**: CrazedMiner
- **main**: `Sneak\Main`
- **license**: NOASSERTION (unknown)
- **tags**: admin

## 下载

- `Sneak-1.1.phar`(**6522** 字节,sha256 `b19a6fd63f578fd8af2db2c96f0bbfd08d8997aa8b54137683e1fa6deaaf65fa`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.8.0/sneak/Sneak-1.1.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
