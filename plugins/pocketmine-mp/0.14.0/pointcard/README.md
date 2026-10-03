# PointCard(点卡)

## 功能简介

**点卡(PointCard)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `2.0.4`,作者 CKylinMC。
主要功能方向:玩法。
原插件说明:PointCard兑换
本插件共提供 **8** 条命令(见下表)。
共定义 **8** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/pc` | PointCard兑换 | `/pc <cdk>` | pc.cmd.pc | - |
| `/pcmgr` | PointCard管理 | `/pcmgr <options>` | pc.cmd.pcmgr | - |
| `/pcgen` | PointCard生成 | `/pcgen <options>` | pc.cmd.pcgen | - |
| `/pcget` | PointCard获取 | `/pcget <cdk>` | pc.cmd.pcget | - |
| `/pclog` | PointCard查询 | `/pclog <cdk>` | pc.cmd.pclog | - |
| `/pcreset` | PointCard重置 | `/pcreset <cdk>` | pc.cmd.pcreset | - |
| `/pcclose` | PointCard关闭 | `/pcclose <cdk>` | pc.cmd.pcclose | - |
| `/vipinfo` | VIP信息打印 | `/vipinfo <player>` | pc.cmd.vipinfo | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `pc.cmd.pc` | 玩家兑换权限 | true |
| `pc.cmd.vipinfo` | 玩家VIP查询权限 | true |
| `pc.cmd.pcmgr` | 管理员管理权 | op |
| `pc.cmd.pclog` | 卡密日志查询 | op |
| `pc.cmd.pcgen` | 卡密生成权限 | op |
| `pc.cmd.pcget` | 卡密查看权限 | op |
| `pc.cmd.pcreset` | 卡密重置权限 | op |
| `pc.cmd.pcclose` | 卡密关停权限 | op |

## 如何使用

1. 下载下方插件文件 `PointCard-2.0.4.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `pointcard`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0
- **plugin_version**: `2.0.4`
- **author**: CKylinMC
- **main**: `CsNle\PointCard\Main`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `PointCard-2.0.4.phar`(**39762** 字节,sha256 `83bcc54bcfa490f86e7e7ba799fb29107c4de30a4a524e90678fd6ee67733390`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/pointcard/PointCard-2.0.4.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
