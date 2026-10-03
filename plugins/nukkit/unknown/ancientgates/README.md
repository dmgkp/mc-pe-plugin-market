# AncientGates(基础插件)

## 功能简介

**基础插件(AncientGates)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `1.8.0`,作者 peewi96。
主要功能方向:世界/传送。
原插件说明:Easily create portals with any custom design.
本插件共提供 **1** 条命令(见下表)。
共定义 **41** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/gate` | All of the Ancient Gates commands. | `See documentation.` | - | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `ancientgates.*` | Gives access to all Ancient Gates and commands. | - |
| `ancientgates.close` | Allows the use of Ancient Gates close command. | op |
| `ancientgates.closeall` | Allows the use of Ancient Gates closeall command. | op |
| `ancientgates.create` | Allows the use of Ancient Gates create command. | op |
| `ancientgates.delete` | Allows the use of Ancient Gates delete command. | op |
| `ancientgates.help` | Allows the use of Ancient Gates help command. | op |
| `ancientgates.info` | Allows the use of Ancient Gates info command. | op |
| `ancientgates.info.exec` | Allows access to exec info in info command. | op |
| `ancientgates.list` | Allows the use of Ancient Gates list command. | op |
| `ancientgates.open` | Allows the use of Ancient Gates open command. | op |
| `ancientgates.openall` | Allows the use of Ancient Gates openall command. | op |
| `ancientgates.remexec` | Allows the use of Ancient Gates remexec command. | op |
| `ancientgates.rename` | Allows the use of Ancient Gates rename command. | op |
| `ancientgates.setbungeetype` | Allows the use of Ancient Gates setbungeetype command. | op |
| `ancientgates.setconf` | Allows the use of Ancient Gates setconf command. | op |
| `ancientgates.setcost` | Allows the use of Ancient Gates setcost command. | op |
| `ancientgates.setentities` | Allows the use of Ancient Gates setentities command. | op |
| `ancientgates.setexec` | Allows the use of Ancient Gates setexec command. | op |
| `ancientgates.setfrom` | Allows the use of Ancient Gates setfrom command. | op |
| `ancientgates.setinv` | Allows the use of Ancient Gates setinventory command. | op |
| `ancientgates.setmaterial` | Allows the use of Ancient Gates setmaterial command. | op |
| `ancientgates.setmessage` | Allows the use of Ancient Gates setmessage command. | op |
| `ancientgates.setvehicles` | Allows the use of Ancient Gates setvehicles command. | op |
| `ancientgates.tpfrom` | Allows the use of Ancient Gates tpfrom command. | op |
| `ancientgates.tpto` | Allows the use of Ancient Gates tpto command. | op |
| `ancientgates.addfrom` | Allows the use of Ancient Gates addfrom command. | op |
| `ancientgates.remfrom` | Allows the use of Ancient Gates remfrom command. | op |
| `ancientgates.addto.*` | Allows the use of Ancient Gates addto command globally. | - |
| `ancientgates.addto.local` | Allows the use of Ancient Gates addto command locally. | op |
| `ancientgates.addto.bungee` | Allows the use of Ancient Gates addto command externally. | op |
| `ancientgates.remto.*` | Allows the use of Ancient Gates remto command globally. | - |
| `ancientgates.remto.local` | Allows the use of Ancient Gates remto command locally. | op |
| `ancientgates.remto.bungee` | Allows the use of Ancient Gates remto command externally. | op |
| `ancientgates.setto.*` | Allows the use of Ancient Gates setto command globally. | - |
| `ancientgates.setto.local` | Allows the use of Ancient Gates setto command locally. | op |
| `ancientgates.setto.bungee` | Allows the use of Ancient Gates setto command externally. | op |
| `ancientgates.use.*` | Gives access to all Ancient Gates. | op |
| `ancientgates.econbypass` | Bypasses gate costs on all Ancient Gates. | op |
| `ancientgates.addserver` | Allows the use of Ancient Gates addserver command. | op |
| `ancientgates.remserver` | Allows the use of Ancient Gates remserver command. | op |
| `ancientgates.serverlist` | Allows the use of Ancient Gates serverlist command. | op |

## 如何使用

1. 下载下方插件文件 `AncientGates-1.8.0.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `ancientgates`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: unknown
- **plugin_version**: `1.8.0`
- **author**: peewi96
- **softdependencies**: [Vault, Multiverse-Core, MultiWorld]
- **main**: `org.mcteam.ancientgates.Plugin`
- **license**: NOASSERTION (unknown)
- **tags**: world

## 下载

- `AncientGates-1.8.0.jar`(**231529** 字节,sha256 `41721f1f080d18e3663178ff6d516fd400f56c0e5da1353e8febace5bb51560e`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/unknown/ancientgates/AncientGates-1.8.0.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
