# ZombieGame(生化游戏)

## 功能简介

**生化游戏(ZombieGame)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `0.0.3 alpha`,作者 Khinenw。
主要功能方向:玩法。
原插件说明:The Genius S1E4 Main Match into PocketMine-MP!
本插件共提供 **3** 条命令(见下表)。
共定义 **4** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/setspawnpos` | Set spawnposition for ZombieGame | `/setspawnpos` | zombiegame.spawnpos | - |
| `/setresetpos` | Set resetposition for ZombieGame | `/setresetpos` | zombiegame.resetpos | - |
| `/explanation` | Explain Zombie Game | `/explanation [page number]` | zombiegame.explanation | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `zombiegame.*` | The permission for using zombie game commands | true |
| `zombiegame.spawnpos` | The permission for setting spawn position | op |
| `zombiegame.resetpos` | The permission for setting reset position | op |
| `zombiegame.explanation` | The permission for explain zombie game | true |

## 如何使用

1. 下载下方插件文件 `ZombieGame-0.0.3_alpha.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `zombiegame`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.8.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.8.0
- **plugin_version**: `0.0.3 alpha`
- **author**: Khinenw
- **main**: `Khinenw\ZombieGame\GameGenius`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `ZombieGame-0.0.3_alpha.phar`(**99560** 字节,sha256 `80ae86abebbea7556444e1ceb0b2dd928f53b57f524d14da50db04300489ead8`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.8.0/zombiegame/ZombieGame-0.0.3_alpha.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
