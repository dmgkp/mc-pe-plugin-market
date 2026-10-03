# MoneyLand(经济领地)

## 功能简介

**经济领地(MoneyLand)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `1.3.1`,作者 Him188。
主要功能方向:经济/商店、世界/传送。
原插件说明:A nice land plugin for Nukkit
本插件共提供 **4** 条命令(见下表)。
共定义 **4** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/startp` | Save land start position | 保存领地起始点 | `/startp` | Money.MoneyLand.command.startp | 起始点 |
| `/endp` | Save land end position | 保存领地结束点 | `/endp` | Money.MoneyLand.command.endp | 结束点 |
| `/land` | Land Command | 领地命令 | `/land <buy|whose|sell|goto|list|name>   /领地 <购买|主人|回收|前往|列表|改名>` | Money.MoneyLand.command.land | 领地 |
| `/landop` | Land OP Command | 领地OP命令 | `/landop <remove | see | list>   /领地 <删除 | 查看 | 列表>` | Money.MoneyLand.command.landop | 领地op |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `Money.MoneyLand.command.startp` | Save land start position | 保存领地起始点 | true |
| `Money.MoneyLand.command.endp` | Save land end position | 保存领地结束点 | true |
| `Money.MoneyLand.command.land` | Land Command | 领地命令 | true |
| `Money.MoneyLand.command.landop` | Land OP Command | 领地OP命令 | op |

## 如何使用

1. 下载下方插件文件 `MoneyLand-1.3.1.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `moneyland`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `1.1.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.15.0, 1.1.0
- **plugin_version**: `1.3.1`
- **author**: Him188
- **dependencies**: Money
- **main**: `money.MoneyLand`
- **license**: NOASSERTION (unknown)
- **tags**: economy, world

## 下载

- `MoneyLand-1.3.1.jar`(**19373** 字节,sha256 `690bedf843b2064f1589e6d3d8538ce8d0f5ca2bc197af2c70c18cd3257815f1`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/1.1.0/moneyland/MoneyLand-1.3.1.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
