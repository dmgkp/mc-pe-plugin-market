# ServerLoveMCPE(恋爱插件汉化)

## 功能简介

**恋爱插件汉化(ServerLoveMCPE)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.1`,作者 TheDeibo, ratchetgame98, YYT汉化。
主要功能方向:玩法。
原插件说明:给你的服务器添加一点浪漫!
本插件共提供 **4** 条命令(见下表)。
共定义 **4** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/serverlove` | §5ServerLove插件信息 | `§5/serverlove.` | serverlovemcpe.serverlove | - |
| `/love` | §5 爱一个玩家 | `/爱 <playerName>` | serverlovemcpe.love | 爱 |
| `/breakup` | §5 和一个玩家分手 | `§5/分手 <playerName>` | serverlovemcpe.breakup | 分手 |
| `/nolove` | §5设置你是否可以被爱 | `§5/状态 <nolove | love>` | serverlovemcpe.nolove | 状态 |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `serverlovemcpe.serverlove` | §5显示插件信息 | true |
| `serverlovemcpe.love` | §5允许用户爱上另一个玩家 | true |
| `serverlovemcpe.breakup` | §5允许用户与另一个玩家分手 | true |
| `serverlovemcpe.nolove` | §5允许用户被/不被爱 | true |

## 如何使用

1. 下载下方插件文件 `ServerLoveMCPE-1.0.1.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `serverlovemcpe`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.12.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.12.0
- **plugin_version**: `1.0.1`
- **author**: TheDeibo, ratchetgame98, YYT汉化
- **main**: `ServerLoveMCPE\Main`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `ServerLoveMCPE-1.0.1.phar`(**11567** 字节,sha256 `208af845d8d2e21e63863fc77c2aeba4b84253e847d717ac82afef11ffaf3689`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.12.0/serverlovemcpe/ServerLoveMCPE-1.0.1.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
