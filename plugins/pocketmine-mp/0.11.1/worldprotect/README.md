# WorldProtect(世界保护新版)

## 功能简介

**世界保护新版(WorldProtect)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `2.0.2`,作者 aliuly。
主要功能方向:世界/传送、玩法、保护/防作弊。
原插件说明:protect worlds from griefers, pvp, limits and borders
本插件共提供 **1** 条命令(见下表)。
共定义 **15** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/worldprotect` | Manage worlds | `/wp <help|sub-cmd> [options]` | wp.cmd.all | wp |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `wp.motd` | Display MOTD | true |
| `wp.cmd.all` | Allow access to protect command | op |
| `wp.cmd.protect` | Change protect mode | op |
| `wp.cmd.protect.auth` | Permit place/destroy in protected worlds | op |
| `wp.cmd.border` | Allow contfol of border functionality | op |
| `wp.cmd.pvp` | Allow PvP controls | op |
| `wp.cmd.noexplode` | Allow NoExplode controls | op |
| `wp.cmd.limit` | Allow control to limit functionality | op |
| `wp.cmd.wpmotd` | Allow editing the motd | op |
| `wp.cmd.addrm` | Allow modifying the auth list | op |
| `wp.cmd.unbreakable` | Modify unbreakable block list | op |
| `wp.cmd.banitem` | Ban/unban items | op |
| `wp.cmd.info` | Show WP config info | true |
| `wp.cmd.gm` | Allow setting a per-world gamemode | op |
| `wp.cmd.gm.exempt` | Users with this permissions will ignore per world gm | false |

## 如何使用

1. 下载下方插件文件 `WorldProtect-2.0.2.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `worldprotect`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.11.1` (推断来源: path)
- **minecraft_versions**: 0.11.1, 0.14.0, 1.1.0, 1.5.0, 1.6.0
- **plugin_version**: `2.0.2`
- **author**: aliuly
- **main**: `aliuly\worldprotect\Main`
- **license**: NOASSERTION (unknown)
- **tags**: world, gameplay, protection

## 下载

- `WorldProtect-2.0.2.phar`(**32090** 字节,sha256 `fb8827f6858964cfeb4887c9617bc65f3998a23ed71081785d82884d3f7bcf0b`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.11.1/worldprotect/WorldProtect-2.0.2.phar`

## 历史版本

- 1.5: WorldProtect-1.5.phar

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
