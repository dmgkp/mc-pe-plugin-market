# ChestLocker(锁插件指令全汉化)

## 功能简介

**锁插件指令全汉化(ChestLocker)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.2`,作者 EvolSoft。
主要功能方向:保护/防作弊。
原插件说明:Lock/Unlock Chests.
本插件共提供 **3** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/锁箱子` | 锁箱子命令. | `/锁箱子` | - | chlock, chl, chestlock, cl |
| `/锁` | 锁箱子. | `/锁` | - | - |
| `/开` | 开箱子. | `/开` | - | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `chestlocker` | ChestLocker command UnlockChest permission. | true |

## 如何使用

1. 下载下方插件文件 `ChestLocker-1.2.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `chestlocker`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.4.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.0, 0.11.1, 1.4.0
- **plugin_version**: `1.2`
- **author**: EvolSoft
- **main**: `ChestLocker\Main`
- **website**: https://www.evolsoft.tk
- **license**: NOASSERTION (unknown)
- **tags**: protection

## 下载

- `ChestLocker-1.2.phar`(**6922** 字节,sha256 `67f918f545d7f4764df51a13e47a5110948aaf668f4984233db4b1b9134b59e5`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.4.0/chestlocker/ChestLocker-1.2.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
