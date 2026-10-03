# Essentials(基础插件)

## 功能简介

**基础插件(Essentials)** 是一款运行于 **其它服务端** 的 Minecraft 基岩版插件,插件版本 `Pre2.13.1.2`,作者 unknown。
主要功能方向:管理/权限、前置/API 库。
原插件说明:Provides an essential, core set of commands for Bukkit.
本插件共提供 **116** 条命令(见下表)。
共定义 **1** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/afk` | 切换暂离状态. | `/<command> [玩家]` | - | eafk, away, eaway |
| `/antioch` | 在目标位置放置一个点燃的TNT. | `/<command> [文本]` | - | eantioch, grenade, egrenade, tnt, etnt |
| `/back` | 回到你上次传送(tp/spawn/warp)的地方. | `/<command>` | - | eback, return, ereturn |
| `/backup` | 进行备份. | `/<command>` | - | ebackup |
| `/balance` | 查看玩家拥有的现金,不输入默认为自己. | `/<command> [玩家]` | - | bal, ebal, ebalance, money, emoney |
| `/balancetop` | 查看服务器财富榜. | `/<command> <page>` | - | ebalancetop, baltop, ebaltop |
| `/ban` | 封禁一个玩家. | `/<command> <玩家> [理由]` | - | eban |
| `/banip` | 封禁一个玩家的IP地址. | `/<command> <IP地址或玩家名称>` | - | ebanip |
| `/book` | 允许打开并编辑一本书. | `/<command> [标题|作者 [名称]]` | - | ebook |
| `/break` | 破坏掉你面对着的方块. | `/<command>` | - | ebreak |
| `/broadcast` | 发送一个全服广播. | `/<command> <文本>` | - | bc, ebc, bcast, ebcast, ebroadcast, shout, eshout |
| `/bigtree` | 在你的视野内生成一颗大树. | `/<command> <tree|redwood|jungle>` | - | ebigtree, largetree, elargetree |
| `/burn` | 使玩家着火. | `/<command> <玩家> <时间(秒)>` | - | eburn |
| `/clearinventory` | 清空指定玩家背包物品. | `/<command> [玩家|*] [物品[:<数据值>]|*|**]` | - | ci, eci, clean, eclean, clear, eclear, clearinvent, eclearinvent, eclearinventory |
| `/compass` | 显示当前你的面朝方向. | `/<command>` | - | ecompass, direction, edirection |
| `/customtext` | 允许创建自定义信息指令. | `/<alias> - 在bukkit.yml中定义` | - | - |
| `/delhome` | 删除一个家. | `/<command> [玩家:]<名称>` | - | edelhome, remhome, eremhome, rmhome, ermhome |
| `/deljail` | 删除一个监狱. | `/<command> <监狱名称>` | - | edeljail, remjail, eremjail, rmjail, ermjail |
| `/delwarp` | 删除一个地标. | `/<command> <地标名称>` | - | edelwarp, remwarp, eremwarp, rmwarp, ermwarp |
| `/depth` | 查看你所在位置的海拔高度. | `/depth` | - | edepth, height, eheight |
| `/eco` | 调整玩家的经济状况(给钱|拿钱|设置|重置). | `/<command> <give|take|set|reset> <玩家> <数量>` | - | eeco, economy, eeconomy |
| `/enchant` | 附魔手中物品. | `/<command> <附魔名称> [附魔等级]` | - | eenchant, enchantment, eenchantment |
| `/enderchest` | 查看玩家的末影箱. 不输入则为自己. | `/<command> [玩家]` | - | echest, eechest, eenderchest, endersee, eendersee, ec, eec |
| `/essentials` | 重载Essentials插件. | `/<command>` | - | eessentials, ess, eess, essversion |
| `/exp` | 给予,设置,或查看一个玩家的经验值. | `/<command> [show|set|give] [玩家名称 [数量]]` | - | eexp, xp |
| `/ext` | 熄灭玩家身上的火. | `/<command> [玩家]` | - | eext, extinguish, eextinguish |
| `/feed` | 使玩家饱食度回复满. | `/<command> [玩家]` | - | eat, eeat, efeed |
| `/fly` | 开启/关闭飞行状态! | `/<command> [玩家] [on|off]` | - | efly |
| `/fireball` | 扔出一个火球. | `/<command> [small|skull]` | - | efireball, fireentity, efireentity, fireskull, efireskull |
| `/firework` | 允许你修改手中的烟花 | `/<command> <<meta param>|power [amount]|clear|fire [amount]>` | - | efirework |
| `/gamemode` | 改变某玩家的游戏模式. | `/<command> <survival|creative|adventure> [玩家]` | - | adventure, eadventure, adventuremode, eadventuremode, creative, eecreative, creativemode, ecreativemode, egamemode, gm, egm, gma, egma, gmc, egmc, gms, egms, gmt, egmt, survival, esurvival, survivalmode, esurvivalmode |
| `/gc` | 报告服务器剩余资源信息. | `/<command> [all]` | - | lag, elag, egc, mem, emem, memory, ememory, uptime, euptime, tps, etps, entities, eentities |
| `/getpos` | 查看你或其他玩家的坐标. | `/<command> [玩家]` | - | coords, egetpos, position, eposition, whereami, ewhereami, getlocation, egetlocation, getloc, egetloc |
| `/give` | 给某玩家一个物品. | `/<command> <玩家> <物品|物品ID> [数量 <附魔名称[:附魔等级]> ...]` | - | egive |
| `/god` | 开启/关闭上帝模式(不受伤害) | `/<command> [玩家] [on|off]` | - | egod, godmode, egodmode, tgm, etgm |
| `/hat` | 将手中物品佩戴头上 | `/<command> [remove]` | - | ehat, head, ehead |
| `/heal` | 治愈某玩家. | `/<command> [玩家]` | - | eheal |
| `/help` | 查看帮助命令列表. | `/<command> [搜索项目] [页数]` | - | ehelp |
| `/helpop` | 给在线的管理员发送信息. | `/<command> <文本>` | - | ac, eac, amsg, eamsg, ehelpop |
| `/home` | 传送回家. | `/<command> [玩家:][名称]` | - | ehome, homes, ehomes |
| `/ignore` | 忽略某玩家. | `/<command> <玩家>` | - | eignore |
| `/info` | 查看服务器信息. | `/<command> [章节] [页数]` | - | about, eabout, ifo, eifo, einfo, inform, einform, news, enews |
| `/invsee` | 查看某玩家背包. | `/<command> <玩家>` | - | einvsee |
| `/item` | 生成一个物品. | `/<command> <物品名称|物品ID> [数量 <附魔名称[:附魔等级]> ...]` | - | i, eitem, ei |
| `/itemdb` | 搜索物品. | `/<command> <物品|物品ID>` | - | dura, edura, durability, edurability, eitemdb, itemno, eitemno |
| `/jails` | 显示所有监狱的列表. | `/<command>` | - | ejails |
| `/jump` | 传送到视野尽头. | `/<command>` | - | j, ej, ejump, jumpto, ejumpto |
| `/kick` | 把某玩家以某理由从服务器踢出. | `/<command> <玩家> [理由]` | - | ekick |
| `/kickall` | 把所有玩家踢出服务器,除了OP. | `/<command> [理由]` | - | ekickall |
| `/kill` | 杀死某个玩家. | `/<command> <玩家>` | - | ekill |
| `/kit` | 获得指定的工具包,或查看可用的工具包. | `/<command> [工具包] [玩家]` | - | ekit, kits, ekits |
| `/kittycannon` | 向你的对手扔出一个爆炸的小猫. | `/<command>` | - | ekittycannon |
| `/lightning` | 神的力量！让闪电劈到准星处或玩家头顶. | `/<command> [玩家] [威力]` | - | elightning, shock, eshock, smite, esmite, strike, estrike, thor, ethor |
| `/list` | 查看指定组在线玩家. 忽略组则查看全部在线玩家 | `/<command> [组]` | - | elist, online, eonline, playerlist, eplayerlist, plist, eplist, who, ewho |
| `/mail` | 查看/清除/发送 邮件. | `/<command> [read|clear|send [to] [文本]|sendall [文本]]` | - | email, eemail |
| `/me` | 在接下来说的话中添加星号前缀. | `/<command> <描述>` | - | action, eaction, describe, edescribe, eme |
| `/more` | 让手中物品达到最大堆叠. | `/<command>` | - | emore |
| `/motd` | 查看今日服务器消息. | `/<command> [章节] [页面]` | - | emotd |
| `/msg` | 发送一条密语给某玩家. | `/<command> <玩家> <文本>` | - | w, m, t, emsg, tell, etell, whisper, ewhisper |
| `/mute` | 禁言或解禁玩家. | `/<command> <玩家> [时间]` | - | emute, silence, esilence |
| `/near` | 列出自己身边的玩家, 或列出某玩家附近的其它玩家. | `/<command> [玩家名称] [半径]` | - | enear, nearby, enearby |
| `/nick` | 改变自己或者别人的昵称. | `/<command> [玩家] <昵称|off>` | - | enick, nickname, enickname |
| `/nuke` | 发射核武器. 户外玩家均受影响, 慎用. | `/<command> [玩家]` | - | enuke |
| `/pay` | 从你的账户中转账付费给某玩家. | `/<command> <玩家> <钱数>` | - | epay |
| `/ping` | 啪啪啪啪啪啪啪啪啪! | `/<command>` | - | echo, eecho, eping, pong, epong |
| `/potion` | 为一个药水瓶添加自定义药水效果. | `/<command> <clear|apply|effect:<效果> power:<强度> duration:<持续时间>>` | - | epotion, elixer, eelixer |
| `/powertool` | 给手中物品指定一个命令. | `/<command> [l:|a:|r:|c:|d:][命令] [参数] - {玩家} 可以点击玩家的名字所取代.` | - | epowertool, pt, ept |
| `/powertooltoggle` | 开启或关闭当前所有的powertool. | `/<command>` | - | epowertooltoggle, ptt, eptt, pttoggle, epttoggle |
| `/ptime` | 专门调整某玩家客户端的时间. 添加 @ 前缀来修复. | `/<command> [list|reset|day|night|dawn|17:30|4pm|4000ticks] [玩家|*]` | - | playertime, eplayertime, eptime |
| `/pweather` | 修改一位玩家的天气 | `/<command> [list|reset|storm|sun|clear] [player|*]` | - | playerweather, eplayerweather, epweather |
| `/r` | 快速回复别人发给你的信息(邮件/私信). | `/<command> <文本>` | - | er, reply, ereply |
| `/realname` | 查看某玩家的真名(nick之前的名字). | `/<command> <昵称>` | - | erealname |
| `/recipe` | 显示物品的合成配方. | `/<command> <物品> [数字]` | - | formula, eformula, method, emethod, erecipe, recipes, erecipes |
| `/remove` | 删除指定世界中的实体(全部|驯服的|掉落的物品|箭|船|矿车|经验|挂画|展示框|末影水晶|怪物|动物|环境生物(目前只有蝙蝠)|怪物|怪物类型|). | `/<command> <all|tamed|drops|arrows|boats|minecarts|xp|paintings|itemframes|endercrystals|monsters|animals|ambient|mobs|[mobType]> [半径] [世界]` | - | eremove, butcher, ebutcher, killall, ekillall, mobkill, emobkill |
| `/repair` | 修复<手中|所有>的物品. | `/<command> [hand|all]` | - | fix, efix, erepair |
| `/rules` | 查看服务器规则. | `/<command> [章节] [页面]` | - | erules |
| `/seen` | 查看一位玩家|IP最后登出的时间. | `/<command> <玩家>` | - | eseen |
| `/sell` | 把(手中|背包|全部方块)物品出售给系统. | `/<command> <物品名称|物品ID|hand|inventory|blocks> [-][数量]` | - | esell |
| `/sethome` | 把你的家设置在这个位置. | `/<command> [[玩家:]名称]` | - | esethome, createhome, ecreatehome |
| `/setjail` | 在你所在位置设置一个监狱,名称叫 [监狱名称] | `/<command> <监狱名称>` | - | esetjail, createjail, ecreatejail |
| `/setwarp` | 创建一个新的地标. | `/<command> <地标名称>` | - | createwarp, ecreatewarp, esetwarp |
| `/setworth` | 设置某个物品的价值. | `/<command> [物品名称|物品ID] <价格>` | - | esetworth |
| `/socialspy` | 切换你是否可以看到其他[指定]玩家的私聊和邮件. | `/<command> [玩家] [on|off]` | - | esocialspy |
| `/spawner` | 改变一个刷怪笼的类型. | `/<command> <生物类型> [延迟]` | - | changems, echangems, espawner, mobspawner, emobspawner |
| `/spawnmob` | 生成一个生物. | `/<command> <生物类型>[:data][,<mount>[:data]] [数量] [玩家]` | - | mob, emob, spawnentity, espawnentity, espawnmob |
| `/speed` | 改变移动速度. | `/<command> [类型] <速度值> [玩家]` | - | flyspeed, eflyspeed, fspeed, efspeed, espeed, walkspeed, ewalkspeed, wspeed, ewspeed |
| `/sudo` | 让某玩家强制执行一个命令. | `/<command> <玩家> <命令 [参数]>` | - | esudo |
| `/suicide` | 自杀. | `/<command>` | - | esuicide |
| `/tempban` | 临时封禁一个玩家. | `/<command> <玩家> <时间>` | - | etempban |
| `/thunder` | 允许/禁止 自然雷击. | `/<command> <true/false> [持续时间]` | - | ethunder |
| `/time` | 显示/改变世界的时间,默认当前世界. | `/<command> [day|night|dawn|17:30|4pm|4000ticks] [世界名称|all]` | - | day, eday, night, enight, etime |
| `/togglejail` | 监禁/解禁一个玩家,并传送他到监狱. | `/<command> <玩家> <jailname> [datediff]` | - | jail, ejail, tjail, etjail, etogglejail, unjail, eunjail |
| `/top` | 传送到你所站坐标上的最高方块处. | `/<command>` | - | etop |
| `/tp` | 强行传送或传送到某玩家. | `/<command> <玩家> [另一个玩家]` | - | tele, etele, teleport, eteleport, etp, tp2p, etp2p |
| `/tpa` | 发送一条传送请求,让你传送到对象玩家的地点. | `/<command> <玩家>` | - | call, ecall, etpa, tpask, etpask |
| `/tpaall` | 发送一条传送请求,让所有玩家都传送到你这里. | `/<command> <玩家>` | - | etpaall |
| `/tpaccept` | 接受传送请求. | `/<command> [其他玩家]` | - | etpaccept, tpyes, etpyes |
| `/tpahere` | 发送一条传送请求,让对象玩家传送到你所在的地点. | `/<command> <玩家>` | - | etpahere |
| `/tpall` | 强制把所有在线玩家传送到自己的位置. | `/<command> <玩家>` | - | etpall |
| `/tpdeny` | 拒绝传送请求. | `/<command>` | - | etpdeny, tpno, etpno |
| `/tphere` | 强制把一个玩家传送到自己的位置. | `/<command> <玩家>` | - | s, etphere |
| `/tpo` | 强行传送到某玩家,无视拒绝传送. | `/<command> <玩家> [其他玩家]` | - | etpo |
| `/tpohere` | 强制把一个玩家传送到自己的位置,无视拒绝传送. | `/<command> <玩家>` | - | etpohere |
| `/tppos` | 把自己传送到某个坐标. | `/<command> <x坐标> <y坐标> <z坐标> [角度] [视角]` | - | etppos |
| `/tptoggle` | 拒绝所有传送. | `/<command> [玩家] [on|off]` | - | etptoggle |
| `/tree` | 在你准心所对的位置生成一颗大树. | `/<command> <tree|birch|redwood|redmushroom|brownmushroom|jungle|junglebush|swamp>` | - | etree |
| `/unban` | 解除封禁玩家. | `/<command> <玩家>` | - | pardon, eunban, epardon |
| `/unbanip` | 解除封禁IP地址. | `/<command> <address>` | - | eunbanip, pardonip, epardonip |
| `/unlimited` | 允许某玩家无限放置某方块. | `/<command> <list|item|clear> [玩家]` | - | eunlimited, ul, unl, eul, eunl |
| `/vanish` | 进入隐身模式,其他玩家将无法看到你. | `/<command> [玩家] [on|off]` | - | v, ev, evanish |
| `/warp` | 列出所有的地标,或传送到该地标. | `/<command> <pagenumber|warp> [玩家]` | - | ewarp, warps, ewarps |
| `/weather` | 设置所在世界的天气. | `/<command> <storm/sun> [持续时间]` | - | rain, erain, sky, esky, storm, estorm, sun, esun, eweather |
| `/whois` | 在昵称后面显示真名, 并列出玩家信息. | `/<command> <昵称>` | - | ewhois |
| `/workbench` | 随时随地开启一个工作台 | `/<command>` | - | craft, ecraft, wb, ewb, wbench, ewbench, eworkbench |
| `/world` | 在各个世界间同坐标转换. | `/<command> [世界]` | - | eworld |
| `/worth` | 查看某物品的价值. | `/<command> [物品] [数量]` | - | eprice, price, eworth |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `essentials.*` | Give players with op everything by default | op |

## 如何使用

1. 下载下方插件文件 `Essentials-Pre2.13.1.2.jar`。
2. 放入服务器 `plugins/` 目录(其它服务端)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `essentials`
- **edition**: bedrock
- **server_type**: `other`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: unknown
- **plugin_version**: `Pre2.13.1.2`
- **author**: unknown
- **main**: `com.earth2me.essentials.Essentials`
- **website**: http://tiny.cc/EssentialsCommands
- **license**: NOASSERTION (unknown)
- **tags**: admin, library

## 下载

- `Essentials-Pre2.13.1.2.jar`(**954052** 字节,sha256 `afdbcf091cbc20ea4a20f9770159990eb07901777069c77c151118f9c243a836`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/other/unknown/essentials/Essentials-Pre2.13.1.2.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
