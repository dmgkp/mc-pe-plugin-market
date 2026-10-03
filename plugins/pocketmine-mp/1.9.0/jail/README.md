# Jail(监狱)

## 功能简介

**监狱(Jail)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `2.0.3`,作者 hoyinm14mc。
主要功能方向:管理/权限。
原插件说明:Command to jail a player (/jail <player> ..) OR Help page of the plugin (/jail help)
本插件共提供 **15** 条命令(见下表)。
共定义 **4** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/jail` | Command to jail a player (/jail <player> ..) OR Help page of the plugin (/jail help) | `/jail <player> <jail> <time(minutes)> <reason..>` | jail.command.jail | - |
| `/unjail` | Command to unjail(release) a player | `/unjail <player>` | jail.command.unjail | - |
| `/setjail` | Sets a jail at sender's location | `/setjail <jail>` | jail.command.setjail | createjail |
| `/deljail` | Deletes a jail | `/deljail <jail>` | jail.command.deljail | rmjail, remjail |
| `/jailed` | Get a list of jailed players | `/jailed` | jail.command.jailed | - |
| `/jails` | Get a list of jails | `/jails` | jail.command.jails | jaillist |
| `/jailtp` | Teleport to a jail | `/jailtp <jail>` | jail.command.jailtp | tpjail |
| `/jailmute` | Mute/Unmute players in the jail | `/jailmute <jail>` | jail.command.jailmute | mutejail |
| `/jailswitch` | Switch a player from original jail to another | `/jailswitch <player> <jail>` | jail.command.jailswitch | switchjail |
| `/jailclear` | To unjail all prisoners in the jail | `/jailclear <jail>` | jail.command.jailclear | clearjail |
| `/jailversion` | To check the version and info of the Jail plugin using | `/jailversion` | jail.command.jailversion | - |
| `/jailconfig` | To set the properties of a jail | `/jailconfig help` | jail.command.jailconfig | jailcfg |
| `/prisonerconfig` | To set the properties of a prisoner | `/prisonerconfig help` | jail.command.prisonerconfig | prisonercfg |
| `/bail` | Bail to release from jail! | `/bail` | jail.command.bail | jailbail, jailpay |
| `/votejail` | Vote a player to be jailed | `/votejail <player>` | jail.command.votejail | jailvote |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `jail.command` | - | true |
| `jail.sign` | - | op |
| `jail.protect.override` | - | op |
| `votejail.override` | - | op |

## 如何使用

1. 下载下方插件文件 `Jail-2.0.3.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `jail`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.9.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.9.0
- **plugin_version**: `2.0.3`
- **author**: hoyinm14mc
- **softdependencies**: SimpleAuth, EconomyAPI, MassiveEconomy, PocketMoney
- **main**: `hoyinm14mc\jail\Jail`
- **license**: NOASSERTION (unknown)
- **tags**: admin

## 下载

- `Jail-2.0.3.phar`(**160357** 字节,sha256 `82b30ab273c91b9ef7fc5a479f3d2006f5b9a923808df10b61c12bb154f8a239`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.9.0/jail/Jail-2.0.3.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
