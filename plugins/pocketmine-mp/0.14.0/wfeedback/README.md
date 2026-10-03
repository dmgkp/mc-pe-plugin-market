# WFeedback(反馈插件)

## 功能简介

**反馈插件(WFeedback)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `3.0.5`,作者 unknown。
主要功能方向:玩法。
原插件说明:§6[WFeedback]正式版总指令
本插件共提供 **4** 条命令(见下表)。
共定义 **4** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/fe` | §6[WFeedback]正式版总指令 | `/fe` | wfeedback.fe | - |
| `/fadmin` | §6[WFeedback]一个小彩蛋 | `/fadmin` | - | - |
| `/par` | §6[WFeedback]FloatingText | `/par` | wfeedback.broad | - |
| `/setchat` | 222 | `/setchat` | wfeedback.re | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `wfeedback.re` | 222 | true |
| `wfeedback.fe` | §6[WFeedback]正式版总指令 | true |
| `wfeedback.fadmin` | §6[WFeedback]正式版管理员指令 | true |
| `wfeedback.broad` | §6[WFeedback]正式版公告指令 | true |

## 如何使用

1. 下载下方插件文件 `WFeedback-3.0.5.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `wfeedback`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0
- **plugin_version**: `3.0.5`
- **author**: unknown
- **main**: `feedback\Main`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `WFeedback-3.0.5.phar`(**10282** 字节,sha256 `a93b0fe24c83dd2d8ff1cda97b9a6e134bd4014dcd2213be5b00c19dae59073d`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/wfeedback/WFeedback-3.0.5.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
