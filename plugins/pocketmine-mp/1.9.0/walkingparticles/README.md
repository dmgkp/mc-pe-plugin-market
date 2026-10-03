# WalkingParticles(粒子)

## 功能简介

**粒子(WalkingParticles)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `2.0.0 beta`,作者 CyberCube-HK Team & hoyinm14mc。
主要功能方向:管理/权限、特效/粒子。
原插件说明:Admin command of WalkingParticles
本插件共提供 **7** 条命令(见下表)。
共定义 **6** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/walkp` | Admin command of WalkingParticles | `/walkp help` | walkingparticles.command.admin | walkingparticles, walkp |
| `/wplist` | WalkingParticles > Show a list of available particles | `/wplist` | walkingparticles.command.wplist | - |
| `/wpget` | WalkingParticles > Show a list of your using particles | `/wpget` | walkingparticles.command.wpget | - |
| `/wppack` | Let players to apply/get/list packs using money | `/wppack <apply|get|list> <args..>` | walkingparticles.command.wppack | - |
| `/wptry` | Let players to try out a player's particle pack | `/wptry <player>` | walkingparticles.command.wptry | - |
| `/wprand` | Toggles your random mode on/off | `/wprand` | walkingparticles.command.wprand | wprandom, wprandommode, wprandomshow |
| `/wpitem` | Toggles your item mode on/off | `/wpitem` | walkingparticles.command.wpitem | wpitemmode, wpitemshow |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `walkingparticles` | - | true |
| `walkingparticles.try.pay.bypass` | - | op |
| `walkingparticles.command` | - | true |
| `walkingparticles.sign.toggle` | - | true |
| `walkingparticles.sign.create` | - | op |
| `walkingparticles.sign.destroy` | - | op |

## 如何使用

1. 下载下方插件文件 `WalkingParticles-2.0.0_beta.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `walkingparticles`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.9.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.1, 0.14.0, 1.8.0, 1.9.0
- **plugin_version**: `2.0.0 beta`
- **author**: CyberCube-HK Team & hoyinm14mc
- **main**: `WalkingParticles\WalkingParticles`
- **license**: NOASSERTION (unknown)
- **tags**: admin, cosmetic

## 下载

- `WalkingParticles-2.0.0_beta.phar`(**175660** 字节,sha256 `c805e549d790d46fdcb40a3b13d913d9592969b0945709d8a67226eddbb79721`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.9.0/walkingparticles/WalkingParticles-2.0.0_beta.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
