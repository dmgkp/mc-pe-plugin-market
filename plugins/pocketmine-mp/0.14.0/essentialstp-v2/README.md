# essentialsTP(插件预装)

## 功能简介

**插件预装(essentialsTP)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.9`,作者 unknown。
主要功能方向:世界/传送。
原插件说明:传送到你的家, 使用/回家 展示家的列表, 使用/回家 < 家的名字 > 传送到那里.
本插件共提供 **14** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/回家` | 传送到你的家, 使用/回家 展示家的列表, 使用/回家 < 家的名字 > 传送到那里. | `/回家 或 /回家 < 家的名字 >` | essentialstp.command.home | - |
| `/安家` | 设置家 . | `/安家 < 家的名字 >` | essentialstp.command.sethome | - |
| `/搬家` | 删除家 . | `/搬家 < 家的名字 >` | essentialstp.command.delhome | - |
| `/返回` | 传送到你上次死亡的地点 . | `/返回` | essentialstp.command.back | - |
| `/瞬移` | 随机传送 . | `/瞬移` | essentialstp.command.wild | - |
| `/出生点` | 设置世界出生点 . | `/出生点` | essentialstp.command.setspawn | - |
| `/出生` | 传送到世界出生点 . | `/出生` | essentialstp.command.spawn | - |
| `/传送` | 使用 /传送 展示传送点列表, 使用/传送 < 传送点名字 > 传送到传送点 . | `/传送 或 /传送 < 传送点名字 >` | essentialstp.command.tpahere | - |
| `/传送点` | 设置传送点 . | `/传送点 < 传送点名字 >` | essentialstp.command.setwarp | - |
| `/删传送点` | 删除传送点 . | `/删传送点 < 传送点名字 >` | essentialstp.command.delwarp | - |
| `/找人` | 向玩家发送传送到AT的位置的请求 . | `/找人 < 玩家名 >` | essentialstp.command.tpa | - |
| `/邀请` | 向玩家发送传送到你的位置的请求 . | `/邀请 < 玩家名 >` | essentialstp.command.tpahere | - |
| `/接受` | 接受请求. | `/接受` | essentialstp.command.tpaccept | - |
| `/拒绝` | 拒绝请求. | `/拒绝` | essentialstp.command.tpdeny | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `essentialstp` | Allows player to break spawn signs | op |

## 如何使用

1. 下载下方插件文件 `essentialsTP-1.0.9.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `essentialstp-v2`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.0, 0.11.1, 0.14.0
- **plugin_version**: `1.0.9`
- **author**: unknown
- **main**: `essentialsTP\essentialsTP`
- **license**: NOASSERTION (unknown)
- **tags**: world

## 下载

- `essentialsTP-1.0.9.phar`(**91322** 字节,sha256 `552a9cc206210322f6bb94e91f68dc6a0c58ea63512d8ec6848c66fc8603d4af`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/essentialstp-v2/essentialsTP-1.0.9.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
