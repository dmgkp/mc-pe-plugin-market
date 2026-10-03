# MyRegion(保护服务器主城或者玩家自己的重要建筑)

## 功能简介

**保护服务器主城或者玩家自己的重要建筑(MyRegion)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `1.0`,作者 Doomhawk。
主要功能方向:世界/传送。
原插件说明:Команды MyRegion
本插件共提供 **1** 条命令(见下表)。
共定义 **7** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/rg` | Команды MyRegion | `/rg` | myregion.select | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `myregion.select` | Allow to select positions | true |
| `myregion.expand` | Allow to use /rg expand | true |
| `myregion.wand` | Allow to use /rg wand | true |
| `myregion.claim` | Allow to claim region | true |
| `myregion.info` | Allow to use /rg info | true |
| `myregion.remove` | Allow to use /rg remove | true |
| `myregion.admin` | Allow to manipulate with other regions | op |

## 如何使用

1. 下载下方插件文件 `MyRegion-1.0.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `myregion`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `1.1.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.1.0
- **plugin_version**: `1.0`
- **author**: Doomhawk
- **main**: `MyRegion.MainClass`
- **license**: NOASSERTION (unknown)
- **tags**: world

## 下载

- `MyRegion-1.0.jar`(**15178** 字节,sha256 `cf06e7d99cb245580a29ef49611ba5093703f7e1d80a69dc9a59a61c83ff22e2`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/1.1.0/myregion/MyRegion-1.0.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
