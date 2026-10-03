# Residence(基础插件)

## 功能简介

**基础插件(Residence)** 是一款运行于 **其它服务端** 的 Minecraft 基岩版插件,插件版本 `2.6.6.6`,作者 unknown。
主要功能方向:玩法。
原插件说明:Cuboid Residence Plugin
本插件共提供 **7** 条命令(见下表)。
共定义 **5** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/res` | Manage Residences | `§c/res ? for more info` | - | - |
| `/residence` | Manage Residences | `§c/residence ? for more info` | - | - |
| `/resadmin` | Residence admin functions. | `§c/res ? or /resadmin ? for more info` | - | - |
| `/resreload` | Reload the entire residence plugin. | `§c/resreload` | - | - |
| `/resload` | Load the save file again after you have made modifications. | `§c/resload` | - | - |
| `/rc` | §cChat in current residence channel. | `§c/rc to toggle, or /rc <message>` | - | - |
| `/resworld` | §cRemoves every residence in a world. | `§c/resworld remove [world]` | - | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `residence.admin` | Gives you access to /resadmin | op |
| `residence.admin.tp` | Allows to override tp flag | op |
| `residence.admin.move` | Allows to override move flag | op |
| `residence.create` | Allows you to create residences | op |
| `residence.select` | Allows you to select an area to make residences | op |

## 如何使用

1. 下载下方插件文件 `Residence-2.6.6.6.jar`。
2. 放入服务器 `plugins/` 目录(其它服务端)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `residence`
- **edition**: bedrock
- **server_type**: `other`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: unknown
- **plugin_version**: `2.6.6.6`
- **author**: unknown
- **softdependencies**: [Vault,Essentials,RealPlugin,BOSEconomy,iConomy,bPermissions,PermissionsBukkit,Permissions,WorldEdit,My Worlds]
- **main**: `com.bekvon.bukkit.residence.ResidenceCommandListener`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `Residence-2.6.6.6.jar`(**400157** 字节,sha256 `4c59502c798ffc3d61d8f07d5b45bc262eccde01215fd517cfcb5d056d6f7fad`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/other/unknown/residence/Residence-2.6.6.6.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
