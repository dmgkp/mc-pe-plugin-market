# LockPlayer(设备锁定)

## 功能简介

**设备锁定(LockPlayer)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.0`,作者 Draemon。
主要功能方向:管理/权限、保护/防作弊。
原插件说明:The main command
本插件共提供 **1** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/lock` | The main command | `/lock` | lock.command | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `lock.command` | cid permissions and set cid | true |

## 如何使用

1. 下载下方插件文件 `LockPlayer-1.0.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `lockplayer`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0
- **plugin_version**: `1.0.0`
- **author**: Draemon
- **main**: `LockPlayer\Main`
- **license**: NOASSERTION (unknown)
- **tags**: admin, protection

## 下载

- `LockPlayer-1.0.0.phar`(**2083** 字节,sha256 `7f03806cf100a8c51491692c02616b1def15e9bb171458a9e606644cea11c724`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/lockplayer/LockPlayer-1.0.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
