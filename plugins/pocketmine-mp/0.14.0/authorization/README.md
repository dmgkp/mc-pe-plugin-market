# Authorization(授权插件)

## 功能简介

**授权插件(Authorization)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.5`,作者 MUedsa。
主要功能方向:玩家/登录。
原插件说明:授权登录
本插件共提供 **1** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/autho` | 授权登录 | `Usage: /autho` | authorization.command.autho | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `authorization.command.autho` | 使用登录命令 | op |

## 如何使用

1. 下载下方插件文件 `Authorization-1.0.5.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `authorization`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0
- **plugin_version**: `1.0.5`
- **author**: MUedsa
- **main**: `Authorization\Authorization`
- **license**: NOASSERTION (unknown)
- **tags**: player

## 下载

- `Authorization-1.0.5.phar`(**39134** 字节,sha256 `73f1e4e4fdfd1645aef2a1e862991d9061c3f4ce5acce2c3935ff0c9d330ee9b`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/authorization/Authorization-1.0.5.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
