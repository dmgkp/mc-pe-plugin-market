# Status(信息查看)

## 功能简介

**信息查看(Status)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.4.0`,作者 plus。
主要功能方向:玩法。
原插件说明:Status, 发布论坛: mcpe.tw
本插件共提供 **5** 条命令(见下表)。
共定义 **4** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/status` | Status, 发布论坛: mcpe.tw | `/status <-你的状态. /status [玩家名] <-玩家的状态` | - | - |
| `/displayname` | displayname,发布论坛: mcpe.tw | `/displayname [玩家名] [要修改的名字]` | - | - |
| `/announcement` | announcement, 发布论坛: mcpe.tw | `1. /announcement no@p [消息]  2. /announcement @p [消息] 3. /announcement [消息1] @p [消息2]` | - | - |
| `/nametag` | nametag, 发布论坛: mcpe.tw | `/nametag [玩家名] [要修改的名字]` | - | - |
| `/onlineplayers` | onlineplayers, 发布论坛: mcpe.tw | `/onlineplayers` | - | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `status` | - | op |
| `displayname` | - | op |
| `announcement` | - | op |
| `nametag` | - | op |

## 如何使用

1. 下载下方插件文件 `Status-1.4.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `status`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.6.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.1, 1.6.0
- **plugin_version**: `1.4.0`
- **author**: plus
- **main**: `Status\Status`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `Status-1.4.0.phar`(**15105** 字节,sha256 `2578b7a3ab5c42005d59411a00bbd0b38551a998ee3f6ef3323b267e5ea2fa8d`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.6.0/status/Status-1.4.0.phar`

## 历史版本

- 1.1.2: Status-1.1.2.phar

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
