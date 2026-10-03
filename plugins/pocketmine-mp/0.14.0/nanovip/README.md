# NanoVip(配套插件)

## 功能简介

**配套插件(NanoVip)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.0`,作者 FENGberd&Anapopo。
主要功能方向:玩法。
原插件说明:VIP系统主命令
本插件共提供 **5** 条命令(见下表)。
共定义 **3** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/vip` | VIP系统主命令 | `/vip [add <玩家> <天数>|remove <玩家>]` | NanoVip.command | - |
| `/svip` | VIP系统主命令 (SVIP) | `/svip [add <玩家> <天数>|remove <玩家>]` | NanoVip.command | - |
| `/vtp` | VIP强制传送命令 | `/vtp <玩家>` | NanoVip.command.player | - |
| `/vgm` | SVIP切换游戏模式命令 | `/vgm <1/0>` | NanoVip.command.player | - |
| `/vfly` | VIP切换飞行模式命令 | `/vfly` | NanoVip.command.player | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `NanoVip.*` | 根权限 | op |
| `NanoVip.command` | OP指令使用权限 | op |
| `NanoVip.command.player` | VIP指令使用权限 | true |

## 如何使用

1. 下载下方插件文件 `NanoVip-1.0.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `nanovip`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0
- **plugin_version**: `1.0.0`
- **author**: FENGberd&Anapopo
- **main**: `NanoVip\NanoVip`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `NanoVip-1.0.0.phar`(**9053** 字节,sha256 `b613e266c30ab82f90dea648206df655c078ed83e11ebb5d58998cd53548c7b3`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/nanovip/NanoVip-1.0.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
