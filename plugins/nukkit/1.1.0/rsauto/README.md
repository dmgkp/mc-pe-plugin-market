# RsAuto(多语言登录插件)

## 功能简介

**多语言登录插件(RsAuto)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `1.3.8`,作者 zmdd。
主要功能方向:玩法。
原插件说明:Auto of Rs
本插件共提供 **1** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/unregister` | 注销某个玩家账号账号，消除密码 | `/unregister [账号] #如果你是普通玩家，你就只能输入你自己的账号` | Rs.Command.Auto.unregister | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `Rs.Command.Auto.unregister` | 注销某个玩家账号账号，消除密码 | true |

## 如何使用

1. 下载下方插件文件 `RsAuto-1.3.8.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `rsauto`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `1.1.0` (推断来源: api-inferred)
- **minecraft_versions**: 1.1.0
- **plugin_version**: `1.3.8`
- **author**: zmdd
- **dependencies**: RsFunction
- **main**: `Rs.Plugin.Auto.RsAutoMainClass`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `RsAuto-1.3.8.jar`(**15450** 字节,sha256 `df75c11ac9955083751f8c18d3d1b58fbc097a13265a33b0d24f6d886cde9feb`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/1.1.0/rsauto/RsAuto-1.3.8.jar`

## 历史版本

- 1.2.0: RsAuto-1.2.0.jar

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
