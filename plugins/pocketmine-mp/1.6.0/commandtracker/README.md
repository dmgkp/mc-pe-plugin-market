# CommandTracker(禁止乱发言)

## 功能简介

**禁止乱发言(CommandTracker)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.1`,作者 Scott Handley。
主要功能方向:管理/权限。
原插件说明:Logs commands issued by players and console operators. Censors commands for inappropriate language.
本插件共提供 **1** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/track` | Administer command auditing and censorship | `/track ?|subcmd [options]` | - | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `commandtracker.commands.track` | Grants administrators to manage command tracking behavior | false |

## 如何使用

1. 下载下方插件文件 `CommandTracker-1.1.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `commandtracker`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.6.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.6.0
- **plugin_version**: `1.1`
- **author**: Scott Handley
- **main**: `CommandTracker\CommandTracker`
- **license**: NOASSERTION (unknown)
- **tags**: admin

## 下载

- `CommandTracker-1.1.phar`(**22450** 字节,sha256 `dc8bb4f6835205bcf24dfab58627e0de0052ab81cd7bd6444ecfc279b3573410`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.6.0/commandtracker/CommandTracker-1.1.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
