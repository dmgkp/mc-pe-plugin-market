# Lever(等级)

## 功能简介

**等级(Lever)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.3.0 #Build 5`,作者 Easter。
主要功能方向:玩法。
原插件说明:设置物品增加血量
本插件共提供 **3** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/setIH` | 设置物品增加血量 | `/setIH <id> <health>` | Lever.command.health | - |
| `/setIB` | 设置物品增加buffer | `/setIB <id> <bufferID>` | Lever.command.buffer | - |
| `/兑换` | 兑换经验丹 | `/兑换` | Lever.command.get | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `Lever.*` | 兑换物品指令 | true |

## 如何使用

1. 下载下方插件文件 `Lever-1.3.0_Build_5.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `lever`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.12.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.12.0
- **plugin_version**: `1.3.0 #Build 5`
- **author**: Easter
- **main**: `Lever\Main`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `Lever-1.3.0_Build_5.phar`(**23296** 字节,sha256 `dfc1791b8bb1b602189cfc5a2f10e07297c17283b302b1e928d49b529bb2762c`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.12.0/lever/Lever-1.3.0_Build_5.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
