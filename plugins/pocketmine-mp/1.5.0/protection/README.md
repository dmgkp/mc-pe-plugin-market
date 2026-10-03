# Protection(有)

## 功能简介

**有(Protection)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.8.6`,作者 zzx。
主要功能方向:保护/防作弊。
原插件说明:服务器登入插件
本插件共提供 **3** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/keys` | keys 开/关/生成 | `/keys (on/off/null)` | Protection.command.op | - |
| `/unregister` | 玩家密码修改 | `/unreturn [旧密码] [新密码]` | - | - |
| `/sban` | 超级BAN | `/sban (add/remove/list) [id]` | Protection.command.op | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `Protection` | Allows access to the Protection command. | op |

## 如何使用

1. 下载下方插件文件 `Protection-1.8.6.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `protection`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `1.5.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.0, 1.5.0
- **plugin_version**: `1.8.6`
- **author**: zzx
- **main**: `Protection\Protection`
- **license**: NOASSERTION (unknown)
- **tags**: protection

## 下载

- `Protection-1.8.6.phar`(**8363** 字节,sha256 `4f1b06d1f9b29275a59a5f4c8b527384fe1321cd9b67aeb80b5123b6445891a6`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/1.5.0/protection/Protection-1.8.6.phar`

## 历史版本

- 破解版身份证登录插件: Protection-file.phar
- 1.8.0: Protection-1.8.0.phar
- 1.8.3: Protection-1.8.3.phar
- 1.8.5: Protection-1.8.5.phar

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
