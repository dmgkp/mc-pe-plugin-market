# MoreTeam(团队插件)

## 功能简介

**团队插件(MoreTeam)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.1.9`,作者 guestc。
主要功能方向:玩法。
原插件说明:[MoreTeam] 选择队伍
本插件共提供 **4** 条命令(见下表)。
共定义 **4** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/team` | [MoreTeam] 选择队伍 | `/team TeamName` | MoreTeam.command.team | - |
| `/teamadd` | [MoreTeam] 添加队伍 | `/teamadd TeamName TeamTag` | MoreTeam.command.teamadd | - |
| `/teamremove` | [MoreTeam] 移除队伍 | `/teamremove TeamName` | MoreTeam.command.teamremove | - |
| `/teamlist` | [MoreTeam] 队伍列表 | `/teamlist` | MoreTeam.command.teamlist | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `MoreTeam.command.team` | [MoreTeam] 选择队伍 | true |
| `MoreTeam.command.teamlist` | [MoreTeam] 队伍列表 | true |
| `MoreTeam.command.teamadd` | [MoreTeam] 添加队伍 | true |
| `MoreTeam.command.teamremove` | [MoreTeam] 移除队伍 | true |

## 如何使用

1. 下载下方插件文件 `MoreTeam-1.1.9.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `moreteam`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.8.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.8.0
- **plugin_version**: `1.1.9`
- **author**: guestc
- **main**: `MoreTeam\MoreTeam`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `MoreTeam-1.1.9.phar`(**9390** 字节,sha256 `3e8f685ad95bff2121e4e344e50b1f62690d9c639857c6436e6b3e4aaf78d4ba`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.8.0/moreteam/MoreTeam-1.1.9.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
