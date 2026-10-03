# bolirongqi(物品展示窗汉化)

## 功能简介

**物品展示窗汉化(bolirongqi)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `DeBe.ch 汉化cre`,作者 DeBe。
主要功能方向:玩法。
原插件说明:玻璃容器命令 用法:/容器 添加 <物品代码> (数目1-3) ;移除某容器内物品/容器 移除 然后触摸容器 ;移除所有容器内物品/容器 重置 ;
本插件共提供 **2** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/容器` | 玻璃容器命令 用法:/容器 添加 <物品代码> (数目1-3) ;移除某容器内物品/容器 移除 然后触摸容器 ;移除所有容器内物品/容器 重置 ; | `/容器 <添加|移除|重置|再生|玻璃>` | debe.itemcase.cmd | - |
| `/rq` | 玻璃容器命令 用法:/容器 添加 <物品代码> (数目1-3) ;/容器 <移除|重置|再生|玻璃> | `/容器 <添加|移除|重置|再生|玻璃>` | debe.itemcase.cmd | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `debe` | ItemCase - Spawn itemcase | op |

## 如何使用

1. 下载下方插件文件 `bolirongqi-DeBe.ch_cre.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `bolirongqi`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.11.1` (推断来源: path)
- **minecraft_versions**: 0.11.1, 1.2.0
- **plugin_version**: `DeBe.ch 汉化cre`
- **author**: DeBe
- **main**: `DeBePlugins\ItemCase\ItemCase`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `bolirongqi-DeBe.ch_cre.phar`(**10950** 字节,sha256 `7f07a331212c54892e7618a553965b61707798421c02a6db042039473b3ba9e5`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.11.1/bolirongqi/bolirongqi-DeBe.ch_cre.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
