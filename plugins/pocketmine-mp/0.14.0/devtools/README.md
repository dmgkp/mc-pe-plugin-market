# DevTools(插件)

## 功能简介

**插件(DevTools)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.11.1`,作者 PocketMine Team。
主要功能方向:管理/权限、前置/API 库。
原插件说明:Helps develop and distribute PocketMine-MP plugins
本插件共提供 **3** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/makeserver` | Creates a PocketMine-MP Phar | `/makeserver` | devtools.command.makeserver | - |
| `/makeplugin` | Creates a Phar plugin from one in source code form | `/makeplugin <pluginName>` | devtools.command.makeplugin | - |
| `/checkperm` | Checks a permission value for the current sender, or a player | `/checkperm <node> [playerName]` | devtools.command.checkperm;devtools.command.checkperm.other | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `devtools` | Allows checking others permission value | op |

## 如何使用

1. 下载下方插件文件 `DevTools-1.11.1.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `devtools`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.1, 0.14.0
- **plugin_version**: `1.11.1`
- **author**: PocketMine Team
- **main**: `DevTools\DevTools`
- **license**: NOASSERTION (unknown)
- **tags**: admin, library

## 下载

- `DevTools-1.11.1.phar`(**34218** 字节,sha256 `a074599dca1f49021a45eeabe9831fea92c2aef11d325b519925b379c1dbb567`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/devtools/DevTools-1.11.1.phar`

## 历史版本

- 1.8.0_乌兰托娅万岁制造: DevTools-1.8.0.phar
- 1.8.0_bingshen优化: DevTools-1.8.0_bingshen.phar
- 1.10.0: DevTools-1.10.0.phar

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
