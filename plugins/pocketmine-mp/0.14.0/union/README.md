# Union(研究用)

## 功能简介

**研究用(Union)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `3.4.0`,作者 Him188。
主要功能方向:玩法。
原插件说明:Union!
本插件共提供 **44** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/uja` | [公会][OP] 添加一个职务 | `/uja` | Union.command | - |
| `/ujr` | [公会][OP] 删除一个职务 | `/ujr` | Union.command | - |
| `/ucshop` | [公会] 贡献度商店 | `/ucshop` | Union.command | - |
| `/upshop` | [公会] 药水商店 | `/upshop` | Union.command | - |
| `/uj` | [公会] 加入一个公会 | `/uj` | Union.command | - |
| `/pla` | [公会] 开启一个世界的我PVP功能 | `/pl+` | Union.command | - |
| `/plr` | [公会] 关闭一个世界的我PVP功能 | `/pl-` | Union.command | - |
| `/pl` | [公会] 设置世界PVP功能 | `/pl` | Union.command | - |
| `/pwa` | [公会] 添加进入一个世界将会获得的物品 | `/pwa` | Union.command | - |
| `/pwl` | [公会] 查看进入一个世界将会获得的物品列表 | `/pwl` | Union.command | - |
| `/pwr` | [公会] 删除进入一个世界将会获得的物品 | `/pwr` | Union.command | - |
| `/ub` | [公会] 查询所在公会金库余额 | `/ub` | Union.command | - |
| `/ui` | [公会] 查看自己公会信息 | `/ui` | Union.command | - |
| `/ubd` | [公会] 向自己公会贡献. 公会会获得不定经验值 | `/ubd` | Union.command | - |
| `/ubt` | [公会][会长] 从公会金库取钱 | `/ubt` | Union.command | - |
| `/ubc` | [公会][会长] 将公会金库的余额转换为公会经验值 | `/ubc` | Union.command | - |
| `/uc` | [公会] 创建公会 | `/uc` | Union.command | - |
| `/uk` | [公会] 踢出成员 | `/uk` | Union.command | - |
| `/ucs` | [公会][OP] 设置创建公会所需的金钱 | `/ucs` | Union.command | - |
| `/ul` | [公会][OP] 设置一个公会的等级 | `/ul` | Union.command | - |
| `/uls` | [公会] 查看公会列表 | `/uls` | Union.command | - |
| `/um` | [公会] 管理功能 | `/um` | Union.command | - |
| `/umc` | [公会] 管理功能: 加入请求 | `/umc+` | Union.command | - |
| `/umva` | [公会] 管理功能: 提升某人权限度 | `/umv+` | Union.command | - |
| `/umvr` | [公会] 管理功能: 降低某人权限度 | `/umv-` | Union.command | - |
| `/upk` | [公会] 1V1 PK | `/upk` | Union.command | - |
| `/uq` | [公会] 退出公会 | `/uq` | Union.command | - |
| `/ur` | [公会] 解散公会 | `/ur` | Union.command | - |
| `/uin` | [公会] 邀请某玩家加入公会 | `/uin` | Union.command | - |
| `/uina` | [公会] 接受邀请 | `/uina` | Union.command | - |
| `/uinr` | [公会] 拒绝邀请 | `/uinr` | Union.command | - |
| `/uw` | [公会] 公会战 | `/uw` | Union.command | - |
| `/uwi` | [公会] 公会战: 设置特定物品 | `/uwi` | Union.command | - |
| `/uwe` | [公会][OP] 公会战: 强制结束 | `/uwe` | Union.command | - |
| `/uwo` | [公会][OP] 公会战: 强制开始(公会战空闲时) | `/uwo` | Union.command | - |
| `/uwj` | [公会] 公会战: 加入 | `/uwj` | Union.command | - |
| `/uwq` | [公会] 公会战: 退出 | `/uwq` | Union.command | - |
| `/uwno` | [公会] 公会战: 拒绝挑战 | `/uwno` | Union.command | - |
| `/uwyes` | [公会] 公会战: 接受挑战 | `/uwyes` | Union.command | - |
| `/uws` | [公会][OP] 公会战: 强制开始(等待时) | `/uws` | Union.command | - |
| `/uwpr` | [公会][OP] 公会战: 删除一个传送地点 | `/uwpr` | Union.command | - |
| `/uwpa` | [公会][OP] 公会战: 添加一个传送地点 | `/uwpa` | Union.command | - |
| `/uwpk` | [公会][会长] 公会战: 挑战某个公会 | `/uwpk` | Union.command | - |
| `/uh` | [公会]  | `/uh [帮助索引]` | Union.command | uhelp, unionhelp, 公会帮助, 工会帮助 |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `Union.command` | Allows the user to run this command | true |

## 如何使用

1. 下载下方插件文件 `Union-3.4.0.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `union`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0
- **plugin_version**: `3.4.0`
- **author**: Him188
- **main**: `Union\Main`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `Union-3.4.0.phar`(**221042** 字节,sha256 `a317ddbe69decd0faa98532d892b5ad1eed99f63f686460711130d894e369104`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/union/Union-3.4.0.phar`

## 历史版本

- 1.0.0: Union-1.0.0.phar
- 1.1.0: Union-1.1.0.phar
- 1.2.0: Union-1.2.0.phar
- 1.3.0: Union-1.3.0.phar
- 1.4.0: Union-1.4.0.phar
- 2.0.0: Union-2.0.0.phar
- 3.0.0: Union-3.0.0.phar
- 3.1.0: Union-3.1.0.phar
- 3.2.0: Union-3.2.0.phar

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
