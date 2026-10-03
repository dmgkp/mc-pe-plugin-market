# WalkingParticles(走路粒子插件)

## 功能简介

**走路粒子插件(WalkingParticles)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `9.9.9`,作者 CyberCube-HK Team/aojiao修改。
主要功能方向:管理/权限、特效/粒子。
原插件说明:Admin command of WalkingParticles
本插件共提供 **3** 条命令(见下表)。
共定义 **5** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/walkingparticles` | Admin command of WalkingParticles | `/wparticles help` | walkingparticles.command.admin | wparticles, walkp |
| `/wplist` | WalkingParticles > Show a list of available particles | `/wplist` | walkingparticles.command.wplist | - |
| `/wpget` | WalkingParticles > Show a list of your using particles | `/wpget` | walkingparticles.command.wpget | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `walkingparticles` | - | true |
| `walkingparticles.command` | - | true |
| `walkingparticles.sign.toggle` | - | true |
| `walkingparticles.sign.create` | - | op |
| `walkingparticles.sign.destroy` | - | op |

## 如何使用

1. 下载下方插件文件 `WalkingParticles-9.9.9.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `walkingparticles`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.1, 0.14.0, 1.8.0, 1.9.0
- **plugin_version**: `9.9.9`
- **author**: CyberCube-HK Team/aojiao修改
- **main**: `WalkingParticles\WalkingParticles`
- **license**: NOASSERTION (unknown)
- **tags**: admin, cosmetic

## 下载

- `WalkingParticles-9.9.9.phar`(**121934** 字节,sha256 `9c21c024a848fde24f40af906e8d162a4044b620e1d0b808f34c34d676912c6a`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/walkingparticles/WalkingParticles-9.9.9.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
