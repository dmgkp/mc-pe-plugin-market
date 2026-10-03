# SimplePrison(监狱插件)

## 功能简介

**监狱插件(SimplePrison)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.1.1`,作者 BOX。
主要功能方向:玩法。
原插件说明:SimplePrison
本插件共提供 **6** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/spsp1` | 监狱地点一 | `Usage: /spsp1` | SimplePrison.makepos | - |
| `/spsp2` | 监狱地点二 | `Usage: /spsp2` | SimplePrison.makepos | - |
| `/spsp` | 监狱地点中心 | `Usage: /spsp2` | SimplePrison.makepos | - |
| `/spout` | 释放犯人 | `Usage: /spput [playername]` | SimplePrison.out | - |
| `/spin` | 添加犯人 | `Usage: /spin [playername]` | SimplePrison.out | - |
| `/spupdate` | 更新插件 | `Usage: /spupdate` | - | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `SimplePrison.makepos` | Allows the user set SimplePrison's position | op |

## 如何使用

1. 下载下方插件文件 `SimplePrison-1.1.1.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `simpleprison`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.6.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.0, 0.11.1, 1.6.0
- **plugin_version**: `1.1.1`
- **author**: BOX
- **main**: `SimplePrison\main`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `SimplePrison-1.1.1.phar`(**18697** 字节,sha256 `be46482e7c66b7ccef52e054fcce0b9211f53727c5ad911dfcc23e6a1b9c319b`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.6.0/simpleprison/SimplePrison-1.1.1.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
