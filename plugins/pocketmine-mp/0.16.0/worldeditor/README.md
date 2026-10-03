# WorldEditor(翻新)

## 功能简介

**翻新(WorldEditor)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `1.0.3`,作者 Kagehis4。
主要功能方向:世界/传送。
原插件说明:切换魔杖的功能,使之生效(变成创世魔杖)或失效(变成普通破铁锄).
本插件共提供 **14** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/魔法` | 切换魔杖的功能,使之生效(变成创世魔杖)或失效(变成普通破铁锄). | `/魔法` | worldeditor | - |
| `/剪切` | 剪切当前选中的方块编辑区域. | `/剪切` | worldeditor.command | - |
| `/复制` | 复制当前选中的方块编辑区域. | `/复制` | worldeditor.command | - |
| `/粘贴` | 把剪切或复制的方块编辑区域粘贴到当前位置. | `/粘贴` | worldeditor.command | - |
| `/实心` | 自动生成半径为r的实心球形方块区域. | `/实心 <方块ID> <实心球形方块区域的半径r>` | worldeditor.command | - |
| `/空心` | 自动生成半径为r的空心球形方块区域. | `/空心 <方块ID> <空心球形方块区域的半径r>` | worldeditor.command | - |
| `/清除` | 清除当前选择的方块编辑区域起点坐标和终点坐标. | `/清除` | worldeditor.command | - |
| `/限制` | 设置可编辑的方块数目上限. | `/限制 <可编辑的方块数目上限>` | worldeditor.command | - |
| `/坐标1` | 把你当前所站的位置设为方块编辑区域的起点坐标. | `/坐标1` | worldeditor.command | - |
| `/坐标2` | 把你当前所站的位置设为方块编辑区域的终点坐标. | `/坐标2` | worldeditor.command | - |
| `/置换` | 把选中的方块编辑区域内所有方块替换为给定ID的方块(点石成金) | `/置换 <方块ID>` | worldeditor.command | - |
| `/替换` | 把选中的方块编辑区域内的某种方块ID替换为特定的方块ID(局部替换). | `/替换 <需要被替换的某种方块ID> <替换为特定的方块ID>` | worldeditor.command | - |
| `/创世神` | 列出创世神插件相关的常用命令 | `/创世神` | worldeditor.command | - |
| `/魔杖` | 上帝赋予建筑师们的神之手:创世魔杖. | `/魔杖` | worldeditor.command | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `worldeditor` | Allow the usage of the WorldEditor command | op |

## 如何使用

1. 下载下方插件文件 `WorldEditor-1.0.3.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `worldeditor`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.16.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.11.0, 0.11.1, 0.16.0
- **plugin_version**: `1.0.3`
- **author**: Kagehis4
- **main**: `WorldEditor\WorldEditor`
- **license**: NOASSERTION (unknown)
- **tags**: world

## 下载

- `WorldEditor-1.0.3.phar`(**43835** 字节,sha256 `66524ada330aa02e91321dd0db324c34c24010a13569a56406381d0b1912ae24`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.16.0/worldeditor/WorldEditor-1.0.3.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
