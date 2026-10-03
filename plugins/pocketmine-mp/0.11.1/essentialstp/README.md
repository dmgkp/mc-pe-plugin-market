# EssentialsTP(传送插件)

## 功能简介

**传送插件(EssentialsTP)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.9_风鸟优化`,作者 unknown。
主要功能方向:世界/传送。
原插件说明:传送到家
本插件共提供 **15** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/home` | 传送到家 | `/home [名称]` | essentialstp.command.home | - |
| `/sethome` | 设置你的家 | `/sethome <名称>` | essentialstp.command.sethome | - |
| `/delhome` | 删除你的家 | `/delhome <名称>` | essentialstp.command.delhome | - |
| `/back` | 传送到上次死亡地点 | `/back` | essentialstp.command.back | - |
| `/wild` | 进行随机传送 | `/wild` | essentialstp.command.wild | - |
| `/setspawn` | 设置世界出生地 | `/setspawn` | essentialstp.command.setspawn | - |
| `/spawn` | 传送到出生地 | `/spawn` | essentialstp.command.spawn | - |
| `/warp` | 传送到地标 | `/warp [名称]` | essentialstp.command.setwarp | - |
| `/setwarp` | 设置传送地标 | `/setwarp <名称>` | essentialstp.command.setwarp | - |
| `/delwarp` | 删除传送地标 | `/delwarp <名称>` | essentialstp.command.delwarp | - |
| `/tpa` | 向别人发送一个传送请求原谅 | `/tpa <玩家>` | essentialstp.command.tpa | - |
| `/tpahere` | 请求别人传送到你这里 | `/tpahere <玩家>` | essentialstp.command.tpahere | - |
| `/tpaccept` | 接受传送请求 | `/tpaccept` | essentialstp.command.tpaccept | - |
| `/tpdeny` | 拒绝所有传送请求 | `/tpdeny` | essentialstp.command.tpdeny | - |
| `/notp` | 设置传送系统禁止传送世界 | `/notp [<add|remove> <世界>|list]` | essentialstp.command.tpahere | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `essentialstp` | Allows player to break spawn signs | op |

## 如何使用

1. 下载下方插件文件 `EssentialsTP-1.0.9.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `essentialstp`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.11.1` (推断来源: path)
- **minecraft_versions**: 0.11.0, 0.11.1, 0.14.0
- **plugin_version**: `1.0.9_风鸟优化`
- **author**: unknown
- **main**: `EssentialsTP\essentialsTP`
- **license**: NOASSERTION (unknown)
- **tags**: world

## 下载

- `EssentialsTP-1.0.9.phar`(**11442** 字节,sha256 `d245ae4afb530184f5798f6d482520ec242c623669d904ab7f588d659bec9665`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.11.1/essentialstp/EssentialsTP-1.0.9.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
