# GroupManager(基础插件)

## 功能简介

**基础插件(GroupManager)** 是一款运行于 **其它服务端** 的 Minecraft 基岩版插件,插件版本 `2.0 (2.12.1) (Phoenix)`,作者 unknown。
主要功能方向:管理/权限。
原插件说明:Provides on-the-fly system for permissions system created by Nijikokun. 权限加载于内存并定时保存至文件 汉化 尘曲.
本插件共提供 **42** 条命令(见下表)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/manuadd` | 移动玩家到指定组. (如果不存在会添加至文件) | `/<command> <玩家> <组> | [世界]` | - | - |
| `/manudel` | 移除指定玩家的配置文件, 并移动到默认组. | `/<command> <玩家>` | - | - |
| `/manuaddsub` | 移动玩家到子组. | `/<command> <玩家> <组>` | - | - |
| `/manudelsub` | 将玩家从子组中移出. | `/<command> <玩家> <组>` | - | - |
| `/mangadd` | 增加一个权限组. | `/<command> <组>` | - | - |
| `/mangdel` | 移除一个权限组, 玩家会被移动到默认组 | `/<command> <组>` | - | - |
| `/manuaddp` | 为玩家增加权限. | `/<command> <玩家> <权限>` | - | - |
| `/manudelp` | 为玩家移除权限. | `/<command> <玩家> <权限>` | - | - |
| `/manuclearp` | 移除指定玩家所有权限. | `/<command> <玩家>` | - | - |
| `/manulistp` | 列出玩家全部权限. | `/<command> <玩家>` | - | - |
| `/manucheckp` | 检查玩家是否具有权限并查看来源. | `/<command> <玩家> <权限>` | - | - |
| `/mangaddp` | 为组增加权限. | `/<command> <组> <权限>` | - | - |
| `/mangdelp` | 为组移除权限. | `/<command> <组> <权限>` | - | - |
| `/mangclearp` | 移除权限组全部权限. | `/<command> <组> <权限>` | - | - |
| `/manglistp` | 列出权限组全部权限. | `/<command> <组>` | - | - |
| `/mangcheckp` | 检查权限组是否具有权限并查看来源. | `/<command> <组> <权限>` | - | - |
| `/mangaddi` | 添加组1到组2的继承列表. | `/<command> <组1> <组2>` | - | - |
| `/mangdeli` | 将组1从组2的继承列表中移除. | `/<command> <组1> <组2>` | - | - |
| `/manuaddv` | 添加/替换玩家的变量. 目前支持 prefix 和 suffix. | `/<command> <玩家> <变量> <值>` | - | - |
| `/manudelv` | 移除玩家的变量. | `/<command> <玩家> <变量>` | - | - |
| `/manulistv` | 列出玩家的全部变量. | `/<command> <玩家>` | - | - |
| `/manucheckv` | 查询玩家是否具有变量并查看来源. | `/<command> <玩家> <变量>` | - | - |
| `/mangaddv` | 添加/替换组的变量. 目前支持 prefix 和 suffix. | `/<command> <组> <变量> <值>` | - | - |
| `/mangdelv` | 移除组的变量. | `/<command> <组> <变量>` | - | - |
| `/manglistv` | 列出组的全部变量 | `/<command> <组>` | - | - |
| `/mangcheckv` | 查询组是否具有变量并查看来源. | `/<command> <组> <变量>` | - | - |
| `/manwhois` | 查看玩家属于何组 | `/<command> <玩家>` | - | - |
| `/tempadd` | 为玩家创建一个临时权限拷贝. | `/<command> <玩家>` | - | - |
| `/tempdel` | 移除玩家的临时权限拷贝. | `/<command> <玩家>` | - | - |
| `/templist` | 列出使用/tempadd进入超载权限模式下的玩家 . | `/<command>` | - | - |
| `/tempdelall` | 移除所有使用 /tempadd 进入超载模式的玩家. | `/<command>` | - | - |
| `/mansave` | 保存权限至文件. | `/<command>` | - | - |
| `/manload` | 重载当前世界和配置文件. 或重载指定世界. | `/<command> [世界]` | - | - |
| `/listgroups` | 列出可用组. | `/<command>` | - | manlistg |
| `/manpromote` | 提升同一继承组的玩家到更高级别. | `/<command> <玩家> <组>` | - | - |
| `/mandemote` | 降低同一继承组的玩家到更低级别. | `/<command> <玩家> <组>` | - | - |
| `/mantogglevalidate` | 开启/关闭在线验证. | `/<command>` | - | - |
| `/mantogglesave` | 开启/关闭自动保存. | `/<command>` | - | - |
| `/manworld` | 查看已选世界名称 | `/<command>` | - | - |
| `/manselect` | 选择一个世界以进行后续指令. | `/<command> <世界>` | - | - |
| `/manclear` | 清空所选世界, 指令将作用在当前世界. | `/<command>` | - | - |
| `/mancheckw` | 查看权限文件保存路径. | `/<command> <世界>` | - | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|

## 如何使用

1. 下载下方插件文件 `GroupManager-2.0_2.12.1_Phoenix.jar`。
2. 放入服务器 `plugins/` 目录(其它服务端)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `groupmanager`
- **edition**: bedrock
- **server_type**: `other`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: unknown
- **plugin_version**: `2.0 (2.12.1) (Phoenix)`
- **author**: unknown
- **main**: `org.anjocaido.groupmanager.GroupManager`
- **website**: http://ess.khhq.net/wiki/Group_Manager
- **license**: NOASSERTION (unknown)
- **tags**: admin

## 下载

- `GroupManager-2.0_2.12.1_Phoenix.jar`(**121881** 字节,sha256 `fbb6a37c509eae5cdfaace859010dc5c8edfb228fbe26eb4a1d3fc937a1ace1b`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/other/unknown/groupmanager/GroupManager-2.0_2.12.1_Phoenix.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
