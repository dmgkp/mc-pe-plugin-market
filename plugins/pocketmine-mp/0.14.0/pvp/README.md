# PVP(开关)

## 功能简介

**开关(PVP)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.3`,作者 Fanghao。
主要功能方向:玩法。
原插件说明:开启PVP指令
本插件共提供 **4** 条命令(见下表)。
共定义 **2** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/pvp1` | 开启PVP指令 | `/pvp1` | MyFirstPlugin.command.pvp | - |
| `/pvp2` | 关闭PVP指令 | `/pvp2` | MyFirstPlugin.command.pvp | - |
| `/pvps` | 设置浮空字命令 | `/pvps` | MyFirstPlugin.command.pvpb | - |
| `/pvpd` | 删除空字命令 | `/pvpd` | MyFirstPlugin.command.pvpb | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `MyFirstPlugin.command.pvp` | - | true |
| `MyFirstPlugin.command.pvpb` | - | op |

## 如何使用

1. 下载下方插件文件 `PVP-1.0.3.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `pvp`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0
- **plugin_version**: `1.0.3`
- **author**: Fanghao
- **main**: `pvp\PVP\Main`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `PVP-1.0.3.phar`(**9179** 字节,sha256 `dfb54374a87e10ffd11a33bc23981ab2d4217fa791d8109de7d420a59d681639`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/pvp/PVP-1.0.3.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
