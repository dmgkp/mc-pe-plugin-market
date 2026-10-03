# ZhyProtect(查熊优化)

## 功能简介

**查熊优化(ZhyProtect)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `2.0`,作者 Zhy,fenhuo。
主要功能方向:管理/权限、保护/防作弊。
原插件说明:The main command of ZhyProtect XD
本插件共提供 **1** 条命令(见下表)。
共定义 **2** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/zp` | The main command of ZhyProtect XD | `/zp <i|n> <xxx>` | ZhyProtect.command.zp | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `ZhyProtect.*` | 这代表只有OP有这个权限 | op |
| `ZhyProtect.command.zp` | 这代表普通玩家也能使用这个指令 | true |

## 如何使用

1. 下载下方插件文件 `ZhyProtect-2.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `zhyprotect`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.11.1` (推断来源: path)
- **minecraft_versions**: 0.11.1, 0.14.0
- **plugin_version**: `2.0`
- **author**: Zhy,fenhuo
- **main**: `ZhyProtect\Main`
- **license**: NOASSERTION (unknown)
- **tags**: admin, protection

## 下载

- `ZhyProtect-2.0.phar`(**19993** 字节,sha256 `7a7a8d6acd7025d63c9f27eb4a73e277db88ce4b7d844fac03a88ac380facee8`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.11.1/zhyprotect/ZhyProtect-2.0.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
