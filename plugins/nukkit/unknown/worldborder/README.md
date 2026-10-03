# WorldBorder(基础插件)

## 功能简介

**基础插件(WorldBorder)** 是一款运行于 **Nukkit** 的 Minecraft 基岩版插件,插件版本 `1.8.1`,作者 Brettflan。
主要功能方向:世界/传送。
原插件说明:Efficient, feature-rich plugin for limiting the size of your worlds.
本插件共提供 **1** 条命令(见下表)。
共定义 **26** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/wborder` | Primary command for WorldBorder. | `|` | - | worldborder, wb |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `worldborder.*` | Grants all WorldBorder permissions | - |
| `worldborder.bypass` | Can enable bypass mode to go beyond the border | op |
| `worldborder.bypasslist` | Can get list of players with border bypass enabled | op |
| `worldborder.clear` | Can remove any border | op |
| `worldborder.debug` | Can enable/disable debug output to console | op |
| `worldborder.delay` | Can set the frequency at which the plugin checks for border crossings | op |
| `worldborder.denypearl` | Can enable/disable direct cancellation of ender pearls thrown past border | op |
| `worldborder.dynmap` | Can enable/disable DynMap border display integration | op |
| `worldborder.dynmapmsg` | Can set the label text for borders shown in DynMap | op |
| `worldborder.fill` | Can fill in (generate) any missing map chunks out to the border | op |
| `worldborder.fillautosave` | Can set the world save interval for the Fill process | op |
| `worldborder.getmsg` | Can view the border crossing message | op |
| `worldborder.help` | Can view the command reference help pages | op |
| `worldborder.knockback` | Can set the knockback distance for border crossings | op |
| `worldborder.list` | Can view a list of all borders | op |
| `worldborder.portal` | Can enable/disable portal redirection to be inside border | op |
| `worldborder.radius` | Can set the radius of an existing border | op |
| `worldborder.reload` | Can force the plugin to reload from the config file | op |
| `worldborder.remount` | Can set the delay before remounting a player to their vehicle after knockback | op |
| `worldborder.set` | Can set borders for any world | op |
| `worldborder.setmsg` | Can set the border crossing message | op |
| `worldborder.shape` | Can set the default shape (round or square) for all borders | op |
| `worldborder.trim` | Can trim (remove) any excess map chunks outside of the border | op |
| `worldborder.whoosh` | Can enable/disable "whoosh" knockback effect | op |
| `worldborder.wrap` | Can set border crossings to wrap around to the other side of the world | op |
| `worldborder.wshape` | Can set an overriding border shape for a single world | op |

## 如何使用

1. 下载下方插件文件 `WorldBorder-1.8.1.jar`。
2. 放入服务器 `plugins/` 目录(Nukkit)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `worldborder`
- **edition**: bedrock
- **server_type**: `nukkit`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: 0.14.0
- **plugin_version**: `1.8.1`
- **author**: Brettflan
- **softdependencies**: dynmap
- **main**: `com.wimbli.WorldBorder.WorldBorder`
- **license**: NOASSERTION (unknown)
- **tags**: world

## 下载

- `WorldBorder-1.8.1.jar`(**110088** 字节,sha256 `427c4eea85a3efd91a7015b0ed7daeda80e1f57a0b97722eb4e91b33e5f23cb5`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/unknown/worldborder/WorldBorder-1.8.1.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
