# ALLVIP(等级插件)

## 功能简介

**等级插件(ALLVIP)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.0`,作者 happylife。
主要功能方向:玩法。
原插件说明:VIP and SVIP
本插件共提供 **8** 条命令(见下表)。
共定义 **8** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/addvip` | 添加VIP | `Usage: /addvip [游戏名] [时间]` | allvip.command.addvip | - |
| `/delvip` | 删除VIP | `Usage : /delvip [游戏名]` | allvip.command.delvip | - |
| `/rvip` | 减少VIP时间 | `Usage : /rvip [游戏名] [时间]` | allvip.command.rvip | - |
| `/addsvip` | 添加SVIP | `Usage: /addsvip [游戏名] [时间]` | allvip.command.addsvip | - |
| `/delsvip` | 删除SVIP“ | `Usage : /delsvip [游戏名]` | allvip.command.delsvip | - |
| `/rsvip` | 减少SVIP时间 | `Usage : /rsvip [游戏名] [时间]` | allvip.command.rsvip | - |
| `/vip` | VIP命令 | `Usage : /vip sign(签到)/gm(切换模式)` | allvip.command.vip | - |
| `/svip` | SVIP命令 | `Usage : /svip sign(签到)/gm(切换模式)` | allvip.command.svip | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `allvip.command.addvip` | 添加VIP | op |
| `allvip.command.delvip` | - | op |
| `allvip.command.rvip` | - | op |
| `allvip.command.addsvip` | 添加SVIP | op |
| `allvip.command.delsvip` | - | op |
| `allvip.command.rsvip` | - | op |
| `allvip.command.vip` | - | true |
| `allvip.command.svip` | - | true |

## 如何使用

1. 下载下方插件文件 `ALLVIP-1.0.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `allvip`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.11.0` (推断来源: path)
- **minecraft_versions**: 0.11.0, 0.11.1, 1.5.0
- **plugin_version**: `1.0.0`
- **author**: happylife
- **main**: `ALLVIP\main`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `ALLVIP-1.0.0.phar`(**18914** 字节,sha256 `e78cd29628680b5203aab36993bf3ec8affe66bbb77ef80e595e26f156b5bdd4`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.11.0/allvip/ALLVIP-1.0.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
