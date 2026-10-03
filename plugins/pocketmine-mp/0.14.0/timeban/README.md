# TimeBan(自定义禁言时间插件)

## 功能简介

**自定义禁言时间插件(TimeBan)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `2.0.0`,作者 linger。
主要功能方向:管理/权限。
原插件说明:时间ban系命令包
本插件共提供 **2** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/timeban` | 时间ban系命令包 | `/timeban [set (玩家 日期20160101)/removeall(移除所有)/remove(移除玩家)]` | TimeBan. | - |
| `/chatban` | Chatban系命令包 | `/chatban [set (玩家 分钟数)/removeall(移除所有)/remove(移除玩家)]` | TimeBan. | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `TimeBan.` | OP允许! | op |

## 如何使用

1. 下载下方插件文件 `TimeBan-2.0.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `timeban`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0
- **plugin_version**: `2.0.0`
- **author**: linger
- **main**: `TimeBan\Main`
- **license**: NOASSERTION (unknown)
- **tags**: admin

## 下载

- `TimeBan-2.0.0.phar`(**9415** 字节,sha256 `abde4f1e7e9102f4ac1794819f42694456794e126c2b13d8558e40a7a6a8b7d6`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/timeban/TimeBan-2.0.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
