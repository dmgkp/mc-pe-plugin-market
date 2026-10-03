# Question(金钱审问)

## 功能简介

**金钱审问(Question)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.0`,作者 Smile。
主要功能方向:玩法。
原插件说明:一个简单的问答插件
本插件共提供 **1** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/q` | 关于本插件的一切指令 | `<ask[问题][奖金]>||<answer[发出问题的玩家名字][回答]>||<right[答对的玩家名字]>||<cancell>` | Question.command.q | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `Question.command.q` | 是否允许玩家使用本插件的指令 | true |

## 如何使用

1. 下载下方插件文件 `Question-1.0.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `question`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.8.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.8.0
- **plugin_version**: `1.0.0`
- **author**: Smile
- **main**: `Question\Question`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `Question-1.0.0.phar`(**6640** 字节,sha256 `a2455ce77f9be78c729d410e0856af6bb17c032e93ffd1e926ca5d5b8df3c3ac`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.8.0/question/Question-1.0.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
