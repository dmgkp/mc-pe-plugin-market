# SiteLand(地皮插件)

## 功能简介

**地皮插件(SiteLand)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.2.9`,作者 MUedsa,Mentha_Haplocalyx。
主要功能方向:世界/传送。
原插件说明:SiteLand
本插件共提供 **8** 条命令(见下表)。
共定义 **2** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/giveland` | check my RPGinfo | `/giveland [ 名字 ]` | uniteland.zzx | - |
| `/guest` | add my guest | `/guest [ 名字 ]` | uniteland.zzx | - |
| `/myguest` | check my guests | `/myguest` | uniteland.zzx | - |
| `/landinfo` | check land info | `/landinfo` | uniteland.zzx | - |
| `/mylands` | check my lands | `/mylands` | uniteland.zzx | - |
| `/seelands` | check other's lands | `/seelands [ 名字 ]` | uniteland.zzx | - |
| `/tpland` | go to other's land | `/tpland [ 地皮编号 ]` | uniteland.zzx | - |
| `/checkhost` | check land's host | `/checkhost [ 地皮编号 ]` | uniteland.zzx | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `uniteland.zzx` | Allows access to all UniteRPG features. | true |
| `uniteland.du` | Allows access to Player UniteRPG features. | op |

## 如何使用

1. 下载下方插件文件 `SiteLand-1.2.9.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `siteland`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.8.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.8.0
- **plugin_version**: `1.2.9`
- **author**: MUedsa,Mentha_Haplocalyx
- **dependencies**: [EconomyAPI]
- **main**: `SiteLand\SiteLand`
- **license**: NOASSERTION (unknown)
- **tags**: world

## 下载

- `SiteLand-1.2.9.phar`(**7290** 字节,sha256 `7300c4d09fbfaf41834367a811efd3916720f4d221859be1e02535e2163896d6`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.8.0/siteland/SiteLand-1.2.9.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
