# WorldGM(多世界模式)

## 功能简介

**多世界模式(WorldGM)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `7.0`,作者 Exxarion。
主要功能方向:世界/传送、玩法。
原插件说明:Set different gamemodes for certain worlds
本插件共提供 **1** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/wgm` | 为不同的世界设置不同的游戏模式。 | `/wgm set <游戏模式> (世界)\n/wgm <include/exclude> <游戏模式>\n/wgm version\n/wgm check\n/wgm gm\n/wgm update` | worldgm.use | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `worldgm.use` | 允许用户使用该插件的功能 | op |

## 如何使用

1. 下载下方插件文件 `WorldGM-7.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `worldgm`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.7.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.1, 1.7.0
- **plugin_version**: `7.0`
- **author**: Exxarion
- **main**: `WorldGM\WorldGM`
- **website**: http://aplus-craft.tk
- **license**: NOASSERTION (unknown)
- **tags**: world, gameplay

## 下载

- `WorldGM-7.0.phar`(**17153** 字节,sha256 `c519d501ee27014e1acb0027ec6eb04feb2c2f749b1103c4dee1d02996896618`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.7.0/worldgm/WorldGM-7.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
