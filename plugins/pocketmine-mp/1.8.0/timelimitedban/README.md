# TimeLimitedBan(定时)

## 功能简介

**定时(TimeLimitedBan)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.0`,作者 beito。
主要功能方向:管理/权限。
原插件说明:時間制限を付けてBanできます
本插件共提供 **2** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/tban` | 時間制限を付けてBanします | `/tban <プレーヤー名> <時間(分)> [理由]` | tban.command.tban | - |
| `/tban-ip` | 時間制限を付けてIPBanします | `/tban-ip <プレーヤー名|IPアドレス> <時間(分)> [理由]` | tban.command.tbanip | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `tban` | /tban-ipを使用できるようになります | op |

## 如何使用

1. 下载下方插件文件 `TimeLimitedBan-1.0.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `timelimitedban`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.8.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.8.0
- **plugin_version**: `1.0.0`
- **author**: beito
- **main**: `beito\TimeLimitedBan\MainClass`
- **license**: NOASSERTION (unknown)
- **tags**: admin

## 下载

- `TimeLimitedBan-1.0.0.phar`(**13226** 字节,sha256 `9003de8b9c37bd65695895be788ed268d87df3d99ad22e801f76f4648e06919a`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.8.0/timelimitedban/TimeLimitedBan-1.0.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
