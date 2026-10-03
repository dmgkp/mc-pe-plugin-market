# SuperBlock(方块效果)

## 功能简介

**方块效果(SuperBlock)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.03`,作者 Kirt and Tasada。
主要功能方向:保护/防作弊。
原插件说明:SuperBlock总命令 DA★ZE~
本插件共提供 **3** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/sb` | SuperBlock总命令 DA★ZE~ | `/sb set/mypos/gopos` | superblock.command.op | - |
| `/myspawn` | 回到出生点 ~Kira | `/sb set/mypos/gopos` | superblock.command | - |
| `/setmyspawn` | 设置自己的出生点 ~Kira | `/sb set/mypos/gopos` | superblock.command | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `superblock.*` | SuperBlock permissions | op |

## 如何使用

1. 下载下方插件文件 `SuperBlock-1.03.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `superblock`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.8.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.8.0
- **plugin_version**: `1.03`
- **author**: Kirt and Tasada
- **main**: `Kirt\SuperBlock\SuperBlock`
- **license**: NOASSERTION (unknown)
- **tags**: protection

## 下载

- `SuperBlock-1.03.phar`(**36181** 字节,sha256 `568423953358b8da7a4d3c6def15739934d5c3fb55ae4f3ca9133e2afb74fddc`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.8.0/superblock/SuperBlock-1.03.phar`

## 历史版本

- 0.2.1 Beta: SuperBlock-0.2.1_Beta.phar
- 0.3.1 Beta: SuperBlock-0.3.1_Beta.phar
- 1.0.0 Finally: SuperBlock-1.0.0_Finally.phar
- 1.0.1: SuperBlock-1.0.1.phar

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
