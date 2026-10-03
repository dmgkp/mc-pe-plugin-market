# HeadHunting(追杀神器)

## 功能简介

**追杀神器(HeadHunting)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.5`,作者 dzj。
主要功能方向:玩法。
原插件说明:悬赏一个人
本插件共提供 **5** 条命令(见下表)。
共定义 **5** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/hunt` | 悬赏一个人 | `/hunt <名字> <赏金>` | HeadHunting.Command.hunt | - |
| `/rm` | 取消悬赏一个人 | `/removehunt <名字>` | HeadHunting.Command.rm | - |
| `/gethunt` | 杀手获取一个任务 | `/gethunt <任务名字>` | HeadHunting.Command.gethunt | - |
| `/joinhunter` | 注册为杀手 | `/joinhunters` | HeadHunting.Command.joinhunter | - |
| `/check` | 查看一个玩家是否被追杀 | `/check <玩家名字>` | HeadHunting.Command.check | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `HeadHunting.Command.hunt` | - | true |
| `HeadHunting.Command.rm` | - | true |
| `HeadHunting.Command.gethunt` | - | true |
| `HeadHunting.Command.joinhunter` | - | true |
| `HeadHunting.Command.check` | - | true |

## 如何使用

1. 下载下方插件文件 `HeadHunting-1.0.5.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `headhunting`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.6.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0, 1.6.0
- **plugin_version**: `1.0.5`
- **author**: dzj
- **main**: `HeadHunting\HeadHunting`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `HeadHunting-1.0.5.phar`(**14250** 字节,sha256 `902ddfdb2d3117ef7be1c8708c693863d2ffb9fae482c2d77bbbe73c7426961d`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.6.0/headhunting/HeadHunting-1.0.5.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
