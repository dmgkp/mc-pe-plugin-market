# essentialsTP(传送插件)

## 功能简介

**传送插件(essentialsTP)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.9`,作者 unknown。
主要功能方向:世界/传送。
原插件说明:传送到你的家\n 使用/home 展示家的列表\n 使用/home < 家的名字 > 传送到那里.
本插件共提供 **16** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/home` | 传送到你的家\n 使用/home 展示家的列表\n 使用/home < 家的名字 > 传送到那里. | `/home 或 /home < 家的名字 >` | essentialstp.command.home | - |
| `/sethome` | 设置家. | `/sethome < 家的名字 >` | essentialstp.command.sethome | - |
| `/delhome` | 删除家. | `/delhome < 家的名字 >` | essentialstp.command.delhome | - |
| `/back` | 传送到你上次死亡的地点. | `/back` | essentialstp.command.back | - |
| `/wild` | 随机传送. | `/wild` | essentialstp.command.wild | - |
| `/setspawn` | 设置世界出生点. | `/setspawn` | essentialstp.command.setspawn | - |
| `/spawn` | 传送到世界出生点. | `/spawn` | essentialstp.command.spawn | - |
| `/warp` | 使用 /warp 展示传送点列表\n 使用/warp < 传送点名字 > 传送到传送点. | `/warp 或 /warp < 传送点名字 >` | essentialstp.command.tpahere | - |
| `/setwarp` | 设置传送点. | `/setwarp < 传送点名字 >` | essentialstp.command.setwarp | - |
| `/delwarp` | 删除传送点. | `/delwarp < 传送点名字 >` | essentialstp.command.delwarp | - |
| `/addswd` | 添加无法set home之类的 | `addswd [世界名字]` | essentialstp.command.setwarp | - |
| `/delswd` | 取消set home之类的 | `delswd [世界名字]` | essentialstp.command.setwarp | - |
| `/tpa` | 向玩家发送传送到AT的位置的请求. | `/tpa < 玩家名 > ` | essentialstp.command.tpa | - |
| `/tpahere` | 向玩家发送传送到你的位置的请求. | `/tpahere < 玩家名 >` | essentialstp.command.tpahere | - |
| `/tpaccept` | 接收请求. | `/tpaccept` | essentialstp.command.tpaccept | - |
| `/tpdeny` | 拒绝请求. | `/tpdeny` | essentialstp.command.tpdeny | - |

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

- **id**: `essentialstp`
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

- `essentialsTP-1.0.9.phar`(**83263** 字节,sha256 `7c359a300c1e2e004f99ae81b357ca5f06d15b7529de605c0df060ed5a23dd0e`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/essentialstp/essentialsTP-1.0.9.phar`

## 历史版本

- 1.0.0_乌兰托娅万岁: EssentialsTP-1.0.0.phar
- 1.0.4.ch 汉化cre: essentialsTP-1.0.4.ch_cre.phar
- 1.0.9_风鸟优化: EssentialsTP-1.0.9.phar

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
