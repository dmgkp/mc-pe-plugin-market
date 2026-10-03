# PvPToggle(基础插件)

## 功能简介

**基础插件(PvPToggle)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `3.0.0`,作者 Sleelin。
主要功能方向:玩法。
原插件说明:Allows players to decide whether or not they want PvP enabled
本插件共提供 **3** 条命令(见下表)。
共定义 **28** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/pvp` | main command used by the plugin | `/pvp` | - | - |
| `/pvpt` | alternate command used by the plugin | `/pvpt` | - | - |
| `/tpvp` | alternate command used by the plugin | `/tpvp` | - | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `pvptoggle` | Gives someone full use of the PvPToggle plugin | false |
| `pvptoggle.use` | Allows players to be affected by PvPToggle | false |
| `pvptoggle.self` | Allows players to use /pvp command on themselves | false |
| `pvptoggle.self.toggle` | Whether or not a player is allowed to toggle their own PvP | false |
| `pvptoggle.self.status` | Whether a player can check their own PvP status in a world | false |
| `pvptoggle.other` | Allows players to use /pvp command on others | false |
| `pvptoggle.other.toggle` | Whether or not a player is allowed to toggle someone else's PvP | false |
| `pvptoggle.other.status` | Whether a player can check someone else's PvP status | false |
| `pvptoggle.other.reset` | Whether a player can reset someone else's PvP status to default | false |
| `pvptoggle.world` | Allows players to modify world-specific PvP | false |
| `pvptoggle.world.toggle` | Whether or not a player is allowed to toggle world-wide PvP | false |
| `pvptoggle.world.status` | Whether a player can check a world's PvP status | false |
| `pvptoggle.world.reset` | Whether a player can reset PvP for all players in a world | false |
| `pvptoggle.global` | Allows players to modify server-wide global PvP | false |
| `pvptoggle.global.toggle` | Whether or not a player is allowed to toggle server-wide PvP | false |
| `pvptoggle.global.status` | Whether a player can check server-wide PvP status | false |
| `pvptoggle.global.reset` | Whether a player can reset server-wide PvP status to default in all worlds | false |
| `pvptoggle.pvp` | SuperPerms is fucking retarded | true |
| `pvptoggle.pvp.force` | Force player PvP enabled | false |
| `pvptoggle.pvp.deny` | Force player PvP disabled | false |
| `pvptoggle.pvp.autoenable` | Automatically enable PvP on combat | false |
| `pvptoggle.pvp.bypass` | Bypass the cooldown period of player PvPing | false |
| `pvptoggle.pvp.bypass.warmup` | Bypass the warmup period of player PvPing | false |
| `pvptoggle.pvp.bypass.cooldown` | Bypass the cooldown period of player PvPing | false |
| `pvptoggle.admin` | Allows a player to toggle the PvP status of any other player or world | false |
| `pvptoggle.regions` | Whether or not a player is allowed to add or remove regions | false |
| `pvptoggle.regions.add` | Whether or not a player is allowed to add a region | false |
| `pvptoggle.regions.remove` | Whether or not a player is allowed to remove a region | false |

## 如何使用

1. 下载下方插件文件 `PvPToggle-3.0.0.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `pvptoggle`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: unknown
- **plugin_version**: `3.0.0`
- **author**: Sleelin
- **main**: `com.sleelin.pvptoggle.PvPToggle`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `PvPToggle-3.0.0.jar`(**47227** 字节,sha256 `11e10d44ceb84ad3c72ea4576c2c434292ac80853b8441e529b8ec25d8e6c676`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/unknown/pvptoggle/PvPToggle-3.0.0.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
