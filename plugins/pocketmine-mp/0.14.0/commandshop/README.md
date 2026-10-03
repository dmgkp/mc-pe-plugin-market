# CommandShop(智慧点商店)

## 功能简介

**智慧点商店(CommandShop)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.1`,作者 Fanghao。
主要功能方向:经济/商店、管理/权限。
原插件说明:查看自己智慧点
本插件共提供 **4** 条命令(见下表)。
共定义 **2** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/智慧点` | 查看自己智慧点 | `/智慧点` | CommandShop.command.yoo | - |
| `/兑换vip` | 兑换vip指令 | `/兑换vip` | CommandShop.command.yoo | - |
| `/兑换op` | 兑换永久op | `/兑换op` | CommandShop.command.yoo | - |
| `/zj` | - | `/zj` | CommandShop.command.vip | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `CommandShop.command.yoo` | 这代表普通玩家也能使用这个指令 | true |
| `CommandShop.command.vip` | 这代表op使用这个指令 | op |

## 如何使用

1. 下载下方插件文件 `CommandShop-1.0.1.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `commandshop`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0, 1.12.0
- **plugin_version**: `1.0.1`
- **author**: Fanghao
- **main**: `C\Sh\Main`
- **license**: NOASSERTION (unknown)
- **tags**: economy, admin

## 下载

- `CommandShop-1.0.1.phar`(**8566** 字节,sha256 `b3ca34e2c43114f55e1db7c2c14a509f4fddd005013d1413eca2e0940580b1e8`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/commandshop/CommandShop-1.0.1.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
