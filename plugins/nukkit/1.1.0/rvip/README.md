# RVIP(插件)

## 功能简介

**插件(RVIP)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `1.0.0`,作者 zmdd。
主要功能方向:玩法。
原插件说明:RVIP of Rs
本插件共提供 **2** 条命令(见下表)。
共定义 **2** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/vip` | RVIP command | `/vip help` | Rs.vip.command.vip | - |
| `/point` | RVIP command | `/point help` | Rs.vip.command.help | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `Rs.vip.command.vip` | Can use it to add/remove/... vip | true |
| `Rs.vip.command.point` | Can use it to add/remove/... point | true |

## 如何使用

1. 下载下方插件文件 `RVIP-1.0.0.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `rvip`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `1.1.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.1, 0.14.0, 1.1.0
- **plugin_version**: `1.0.0`
- **author**: zmdd
- **main**: `RVIP.MainClass`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `RVIP-1.0.0.jar`(**3083248** 字节,sha256 `29fe19d73ee2da902e232c0063c26946395e7e957310a693e2cc88ceebe5d6b8`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/1.1.0/rvip/RVIP-1.0.0.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
