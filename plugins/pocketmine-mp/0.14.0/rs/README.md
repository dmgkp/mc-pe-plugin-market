# RS(特色生存系统)

## 功能简介

**特色生存系统(RS)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `0.0.7`,作者 kinglegend。
主要功能方向:玩法。
原插件说明:demo
本插件共提供 **2** 条命令(见下表)。
共定义 **2** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/rsworld` | rs_command | `/rsworld add [worldname]or /rsworld del [worldname]` | - | - |
| `/rssend` | rs_command | `/rssend [type]->type:tip1/tip2/pup1/pup2` | - | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `f.command` | Allow use of all faction commands | true |
| `c.command` | Allows use of all faction commands | op |

## 如何使用

1. 下载下方插件文件 `RS-0.0.7.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `rs`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0
- **plugin_version**: `0.0.7`
- **author**: kinglegend
- **main**: `RS\Main`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `RS-0.0.7.phar`(**7381** 字节,sha256 `4d05f99425934ae72dc4338d1c0e99710d45eee3ee6e2600c898d288a0ac4a85`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/rs/RS-0.0.7.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
