# Yop(更新)

## 功能简介

**更新(Yop)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.1.6`,作者 xMing。
主要功能方向:管理/权限。
原插件说明:提示指令
本插件共提供 **8** 条命令(见下表)。
共定义 **8** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/yop` | 提示指令 | `/yop` | yop.command | - |
| `/yaddop` | 添加op | `/yaddop` | yaddop.command | - |
| `/ydelop` | 删除op | `/ydelop` | ydelop.command | - |
| `/ylistop` | op列表 | `/ylistop` | ylistop.command | - |
| `/yaddma` | 添加Yop管理员 | `/yaddma` | yaddma.command | - |
| `/ydelma` | 删除Yop管理员 | `/ydelma` | ydelma.command | - |
| `/ylistma` | Yop管理员列表 | `/ylistma` | ylistma.command | - |
| `/yopbc` | 添加/删除op禁用指令 | `/yopbc` | yopbc.command | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `yop.command` | - | op |
| `yaddop.command` | - | op |
| `ydelop.command` | - | op |
| `yaddma.command` | - | op |
| `ydelma.command` | - | op |
| `yopbc.command` | - | op |
| `ylistop.command` | - | op |
| `ylistma.command` | - | op |

## 如何使用

1. 下载下方插件文件 `Yop-1.1.6.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `yop`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0
- **plugin_version**: `1.1.6`
- **author**: xMing
- **main**: `Yop\Yop`
- **license**: NOASSERTION (unknown)
- **tags**: admin

## 下载

- `Yop-1.1.6.phar`(**4610** 字节,sha256 `c8f82f9c57eec61f70fb3dd81a2ebb2025c6bb8aaba9769e5ee93e707007e358`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/yop/Yop-1.1.6.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
