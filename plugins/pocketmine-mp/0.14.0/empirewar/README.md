# EmpireWar(帝国之战)

## 功能简介

**帝国之战(EmpireWar)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.0`,作者 zmdd&xmt。
主要功能方向:玩法。
原插件说明:[帝国之战]设置积分
本插件共提供 **9** 条命令(见下表)。
共定义 **9** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/sp` | [帝国之战]设置积分 | `/sp 玩家 积分` | war.command.sp | - |
| `/sh` | [帝国之战]设置生命 | `/sp 玩家 生命` | war.command.sh | - |
| `/sd` | [帝国之战]设置伤害 | `/sp 玩家 伤害` | war.command.sd | - |
| `/se` | [帝国之战]设置等级 | `/sp 玩家 等级` | war.command.se | - |
| `/xp` | [帝国之战]查询积分 | `/xp` | war.command.xp | - |
| `/up` | [帝国之战]晋级指令 | `/up` | war.command.up | - |
| `/jdq` | [帝国之战]兑换积分指令 | `/jdq 想兑换的积分` | war.command.jdq | - |
| `/vipup` | [帝国之战]会员晋级指令 | `/vipup` | war.command.vipup | - |
| `/nation` | [帝国之战]加入国家 | `/nation 1/2/3` | war.command.nation | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `war.command.sh` | - | op |
| `war.command.sd` | - | op |
| `war.command.se` | - | op |
| `war.command.sp` | - | op |
| `war.command.xp` | - | true |
| `war.command.nation` | - | true |
| `war.command.up` | - | true |
| `war.command.vipup` | - | true |
| `war.command.jdq` | - | true |

## 如何使用

1. 下载下方插件文件 `EmpireWar-1.0.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `empirewar`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0
- **plugin_version**: `1.0.0`
- **author**: zmdd&xmt
- **main**: `EmpireWar\EmpireWar`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `EmpireWar-1.0.0.phar`(**6641** 字节,sha256 `188ce3cab2350af4aef28bbedd884c6ce0d3e2c788ad665f4ce6831948e6f729`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/empirewar/EmpireWar-1.0.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
