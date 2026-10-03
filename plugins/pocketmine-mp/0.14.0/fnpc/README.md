# FNPC(多功能)

## 功能简介

**多功能(FNPC)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.1.8`,作者 FENGberd && anseEND。
主要功能方向:玩法。
原插件说明:NPC系统指令
本插件共提供 **1** 条命令(见下表)。
共定义 **3** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/fnpc` | NPC系统指令 | `使用 /fnpc help 查看帮助` | FNPC.command.fnpc | npc |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `FNPC.*` | 根权限 | op |
| `FNPC.command.*` | 使用命令权限 | op |
| `FNPC.command.fnpc` | NPC命令使用权限 | op |

## 如何使用

1. 下载下方插件文件 `FNPC-1.1.8.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `fnpc`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0, 1.1.0
- **plugin_version**: `1.1.8`
- **author**: FENGberd && anseEND
- **main**: `FNPC\Main`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `FNPC-1.1.8.phar`(**15459** 字节,sha256 `37104974be8957eea9739d295975728a66e1068aec23784c71a8a5d1f0323491`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/fnpc/FNPC-1.1.8.phar`

## 历史版本

- 1.1.4: FNPC-1.1.4.phar
- 1.1.7: FNPC-1.1.7.phar

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
