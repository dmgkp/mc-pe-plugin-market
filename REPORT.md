# REPORT.md — 整理报告

生成时间：2026-10-03T20:43:11+08:00
源目录：`/data/data/com.termux/files/home/工作目录/插件/宝藏`（只读扫描，未修改）

## 1. 总览

- 扫描文件总数：**4576**
- 识别的压缩包（.phar/.jar）：**1781**
- 识别为基岩版插件：**1193** 个文件 → 归并/拆分后 **1084** 个插件条目
- 无法识别：**9** → `_unknown/`
- 非插件/不支持：**66** → `_unsupported/`

## 2. 服务端类型分布

- `pocketmine-mp`: 965
- `nukkit`: 104
- `other`: 15

## 3. Minecraft 版本分布

- `0.14.0`: 349
- `0.11.1`: 150
- `1.8.0`: 134
- `0.11.0`: 85
- `1.1.0`: 83
- `0.16.0`: 46
- `1.12.0`: 46
- `1.6.0`: 46
- `unknown`: 33
- `1.5.0`: 29
- `0.15.0`: 23
- `1.4.0`: 20
- `1.2.0`: 12
- `1.9.0`: 10
- `1.0.0`: 9
- `1.7.0`: 8
- `1.11.0`: 1

## 4. 服务端版本分布 (plugin.yml api)

- `pocketmine-mp` `>=1.0.0`: 512
- `pocketmine-mp` `>=1.12.0`: 143
- `nukkit` `>=1.0.0`: 128
- `pocketmine-mp` `>=1.10.0`: 55
- `pocketmine-mp` `>=1.9.0`: 53
- `pocketmine-mp` `>=2.0.0`: 33
- `pocketmine-mp` `>=1.8.0`: 31
- `pocketmine-mp` `>=1.6.0`: 24
- `pocketmine-mp` `>=1.1.0`: 19
- `other` `>=1.0.0`: 15
- `pocketmine-mp` `>=1.2.0`: 15
- `pocketmine-mp` `>=1.11.0`: 12
- `pocketmine-mp` `>=3.0.0`: 10
- `pocketmine-mp` `>=1.4.0`: 9
- `pocketmine-mp` `>=1.4.1`: 8
- `pocketmine-mp` `>=1.13.0`: 8
- `pocketmine-mp` `>=3.0.0-ALPHA10`: 7
- `pocketmine-mp` `>=1.7.1`: 7
- `pocketmine-mp` `>=1.3.1`: 6
- `pocketmine-mp` `>=1.12`: 5
- `pocketmine-mp` `>=1.12.`: 4
- `pocketmine-mp` `>=1.3.0`: 3
- `pocketmine-mp` `>=1.0.1.5`: 3
- `pocketmine-mp` `>=3.0.0-ALPHA11`: 3
- `pocketmine-mp` `>=1.3.5`: 2
- `pocketmine-mp` `>=3.0.0-ALPHA7`: 2
- `nukkit` `>=1.0.5`: 1
- `pocketmine-mp` `>=1.0.5`: 1
- `pocketmine-mp` `>=1.13.1`: 1
- `pocketmine-mp` `>=2.1.0`: 1

## 5. 重复插件合并

- 共 1193 个插件文件，按「服务端类型 + MC版本 + 插件名」聚合为 1084 个条目。
- 同一插件的多版本文件：**79** 个条目保留了 `history/`。
- 同名同版本但内容不同的文件：自动加 `-v2/-v3` 后缀区分为独立条目。

## 6. 许可证情况

- 有 License 文件：**0**
- 缺少许可证（写入占位 `LICENSE` 说明）：**1084**

本仓库自身内容（catalog/api/index/schema/文档/脚本）采用 **AGPL-3.0**；第三方插件二进制保留原授权，详见根目录 `LICENSE` 与 `NOTICE.md`。

## 7. 版本信息缺失

- `plugin.yml` 未提供 version、按 `0.0.0` 占位：**0**

## 8. 无法识别文件 (`_unknown/`)

| 源路径 | 大小 | sha256(前12) |
|--------|------|--------------|
| `[1.6.3]Lunchs插件包更新！--有生之年____/1.6.3/PocketMine插件/Bolirongqi--玻璃容器展示柜[完美支持PHP7,PHP5慎用!]/Bolirongqi_vDeBe.ch 汉化cre--玻璃容器展示柜[完美支持PHP7,PHP5慎用!].phar` | 10950 | 7f07a331212c |
| `[1.6.3]Lunchs插件包更新！--有生之年____/1.6.3/PocketMine插件/WRand--抽奖插件/WRand_v1.0.0_2017-09-19--抽奖插件.phar` | 2943 | dd7eddaeefb1 |
| `[1.6.4] Lunchs插件包更新！-- LUGG/1.6.4/PocketMine插件/Fkz--浮空字显示服务器状态信息-自定义文本通过按钮翻页/Fkz_v1.2.0--浮空字显示服务器状态信息-自定义文本通过按钮翻页.phar` | 14602 | db4f7d715c59 |
| `[1.6.4] Lunchs插件包更新！-- LUGG/1.6.4/你们要的 [精湛补丁]/PocketMine插件/WsStationBlock--站在指定方块上执行指定命令/WsStationBlock_v1.0.0--站在指定方块上执行指定命令.phar` | 7598 | db385cce1b53 |
| `[官方正版]YuIoPluginBag0.1.4.1/YuIoPluginBag/插件/PocketMine插件/公会 - 研究用/[公会]Union.phar` | 210768 | cb535076d41d |
| `[官方正版]YuIoPluginBag0.1.4.1/YuIoPluginBag/插件/PocketMine插件/禁止物品/[禁止物品]BanItem.phar` | 7448 | a6f0c45d76f1 |
| `[官方正版]YuIoPluginBag0.1.4.1/YuIoPluginBag/插件/PocketMine插件/高原反应/[高原反应]HighStress.phar` | 678 | 973a1041ec64 |
| `流星插件包/PM插件/视频播放插件/视频播放插件.phar` | 35129 | c226ceacef54 |
| `百度贴吧/附魔(完整版).phar` | 1706851 | 2786f7024253 |

## 9. 非插件 / 不支持 (`_unsupported/`)

- `server-core`: 61
- `server-core-or-archive`: 5

| 源路径 | 类别 | 大小 |
|--------|------|------|
| `[1.6.3]Lunchs插件包更新！--有生之年____/1.6.3/核心/Nukkit/Nukkit-1.1.3-20170827.jar` | server-core-or-archive | 11611136 |
| `[1.6.3]Lunchs插件包更新！--有生之年____/1.6.3/核心/Nebzz/Nebzz-GP_alpha.4.phar` | server-core | 9573796 |
| `[1.6.3]Lunchs插件包更新！--有生之年____/1.6.3/核心/Nebzz/Nebzz-PMMP_alpha.4.phar` | server-core | 7745490 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/Nukkit v0.16.x/Nukkit v0.16.x.jar` | server-core-or-archive | 6651395 |
| `[1.6.4] Lunchs插件包更新！-- LUGG/1.6.4/核心/NightMoon/[1.2.3]NightMoon For MCPE 1.2.3.phar` | server-core | 5183291 |
| `[1.6.3]Lunchs插件包更新！--有生之年____/1.6.3/核心/GenisysPro/GenisysPro-20170827-稳定版.phar` | server-core | 4803008 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/PocketMine-MP1.5.phar` | server-core | 4711598 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/PocketMine-MP1.4.0.phar` | server-core | 4698838 |
| `[官方正版]YuIoPluginBag0.1.4.1/YuIoPluginBag/核心/GenisysPro/Genisys(1.0.5).phar` | server-core | 4614982 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/PocketMine-MP1.2.12.phar` | server-core | 4456812 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/PocketMine-MP1.0php5.phar` | server-core | 4371691 |
| `[官方正版]YuIoPluginBag0.1.4.1/YuIoPluginBag/核心/GenisysPro/GenisysPro(1.1.09).phar` | server-core | 4011108 |
| `[官方正版]YuIoPluginBag0.1.4.1/YuIoPluginBag/核心/GenisysPro/GenisysPro(1.0.07-1.0.4).phar` | server-core | 3908029 |
| `[官方正版]YuIoPluginBag0.1.4.1/YuIoPluginBag/核心/Tess/Tesseract(1.0.0.7-1.0.4).phar` | server-core | 3835009 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/PocketMine-MP1.1.phar` | server-core | 3652069 |
| `[1.6.3]Lunchs插件包更新！--有生之年____/1.6.3/核心/BuleLight/[1.0.X~1.1.5]BlueLight-PHP7-%23811--蓝灯 PHP7.phar` | server-core | 3633926 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/Genisys v0.14.x/ITXPHP7改5-渲紅#042.phar` | server-core | 3583305 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/Genisys v0.15.x/Genisys v0.15.x.phar` | server-core | 3509744 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/Nukkit v0.15.x/nukkit.jar` | server-core-or-archive | 2924621 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/Nukkit v0.14.x/Nukkit v0.14.x.jar` | server-core-or-archive | 2882774 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/ClearSky v0.14.x/ClearSky v0.14.x.phar` | server-core | 2681526 |
| `../../../.openclaw/workspace/_build/zstage/006/0.11.0插件地图核心大全（不含付费）/核心/核心（zhy）.phar` | server-core | 2649741 |
| `[1.6.3]Lunchs插件包更新！--有生之年____/1.6.3/核心/SteadFast2 - Lifeboat服务器的核心/SteadFast(1.2.beta).phar` | server-core | 2612065 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/我的世界0.14核心/ClearSky(0.14.X).phar` | server-core | 2165852 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/我的世界0.14核心/0.14核心(显示红色可进).phar` | server-core | 2125000 |
| `[官方正版]YuIoPluginBag0.1.4.1/YuIoPluginBag/核心/GenisysPro/GenisysPro(1.1.0.55-1.1.1).phar` | server-core | 1781427 |
| `[官方正版]YuIoPluginBag0.1.4.1/YuIoPluginBag/核心/DumpCore/DumpCore(1.0.5-1.0.9).phar` | server-core | 1764136 |
| `[官方正版]YuIoPluginBag0.1.4.1/YuIoPluginBag/核心/GenisysPro/GenisysPro(1.0.5-1.0.9).phar` | server-core | 1764136 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/Nukkit v0.13.x/Nukkit v0.13.x.jar` | server-core | 1709029 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/0.12/乌兰托娅改造fc核心.phar` | server-core | 1697601 |
| `[1.6.4] Lunchs插件包更新！-- LUGG/1.6.4/核心/Turanic/Turanic_1.2.8_3.0.1.phar` | server-core | 1506838 |
| `[1.6.4] Lunchs插件包更新！-- LUGG/1.6.4/核心/Turanic/Turanic_MCPE1.2.3_3.0.1.phar` | server-core | 1495343 |
| `[1.6.4] Lunchs插件包更新！-- LUGG/1.6.4/核心/Apollo-Legacy/Apollo_1.2.10_3.0.1 #990.phar` | server-core | 1474511 |
| `[1.6.4] Lunchs插件包更新！-- LUGG/1.6.4/核心/Turanic/Turanic_1.2.9_3.0.1.phar` | server-core | 1467532 |
| `[1.6.3]Lunchs插件包更新！--有生之年____/1.6.3/核心/GenisysPlus/GenisysPlus_v1.1.0.55 - 1.1.4.51_1.12.0 4.0.0.phar` | server-core | 1405330 |
| `[1.6.3]Lunchs插件包更新！--有生之年____/1.6.3/核心/Leveryl/Leveryl--MCPE1.X.phar` | server-core | 1394267 |
| `[1.6.4] Lunchs插件包更新！-- LUGG/1.6.4/核心/Apollo-Legacy/Apollo_v1.2.8_3.0.0-ALPHA10.phar` | server-core | 1370718 |
| `[1.6.4] Lunchs插件包更新！-- LUGG/1.6.4/核心/Apollo-Legacy/Apollo_MCPEv1.2.0.81_3.0.0-ALPHA9.phar` | server-core | 1354836 |
| `[1.6.4] Lunchs插件包更新！-- LUGG/1.6.4/核心/BuleLight/BlueLight_v1.2.7_3.0.0-ALPHA8 #105.phar` | server-core | 1324247 |
| `[1.6.3]Lunchs插件包更新！--有生之年____/1.6.3/核心/BuleLight/BlueLight_v1.2.0_3.0.0-ALPHA8 #85.phar` | server-core | 1322253 |
| `[1.6.4] Lunchs插件包更新！-- LUGG/1.6.4/核心/PocketMine-MP/PocketMine-MP_v1.2.10_3.0.0-ALPHA11.phar` | server-core | 1267305 |
| `[官方正版]YuIoPluginBag0.1.4.1/YuIoPluginBag/核心/Tess/Tesseract(1.1.0.55).phar` | server-core | 1236024 |
| `[1.6.4] Lunchs插件包更新！-- LUGG/1.6.4/核心/PocketMine-MP/PocketMine-MP_v1.2.0.81_3.0.0-ALPHA9.phar` | server-core | 1235996 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/Genisys v0.16.x/Genisys v0.16.x.phar` | server-core | 1210364 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/Genisys_1.1dev-legacy【4.27更新无更好地形】.phar` | server-core | 1175181 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/Genisys v0.14.x/Genisys v0.14.x.phar` | server-core | 1160011 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/Genisys v0.14.x/Genisys_1.1dev--------最终版本.phar` | server-core | 1160011 |
| `[1.6.3]Lunchs插件包更新！--有生之年____/1.6.3/核心/Cookie-MP/Cookie-MP_v1.1.0.55_3.0.0-ALPHA5.phar` | server-core | 1153691 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/Genisys v0.14.x/php5.phar` | server-core | 1124263 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/0.13/乌兰托娅万岁核心0.13.phar` | server-core | 1055285 |
| `../../../.openclaw/workspace/_build/zstage/006/0.11.0插件地图核心大全（不含付费）/核心/麦块PocketMine-MP.phar` | server-core | 1045294 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/我的世界0.14核心/0.14.1 ITX核心.phar` | server-core | 995070 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/我的世界0.14核心/[0.14]ITX-7(PHP5).phar` | server-core | 994267 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/Genisys v0.13.x/PocketMine_MP.phar` | server-core | 992722 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/我的世界0.14核心/0.14.0.b3核心.phar` | server-core | 986607 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/我的世界0.14核心/ITX核心开源PHP5 0.14.0正式版.phar` | server-core | 984648 |
| `../../../.openclaw/workspace/_build/zstage/006/0.11.0插件地图核心大全（不含付费）/核心/zxc核心PocketMine-MP.phar` | server-core | 925541 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/0.11.1/乌兰托娅万岁改造和谐核心 更新 (2).phar` | server-core | 914415 |
| `Go!极致插件包v2.3.0/相关资源/PE Server 核心/0.13/PocketMine-MP_1.7乌兰托娅万岁制造.phar` | server-core | 909282 |
| `[1.6.4] Lunchs插件包更新！-- LUGG/1.6.4/核心/Altay/Altay_1.2_3.0.1.phar` | server-core | 891840 |
| … | 其余 6 项 | |

## 10. 未复制的资源文件（原目录保留）

为避免仓库臃肿，下列**非插件资源**未复制进仓库，仅统计于 `_unsupported/resource-manifest.json`；**原始文件仍完整保留在源目录**中：

| 类别 | 数量 | 体积 |
|------|------|------|
| map | 809 | 494.5 MB |
| archive | 52 | 289.3 MB |
| server-core | 80 | 168.2 MB |
| image | 88 | 42.4 MB |
| app | 11 | 24.1 MB |
| document | 930 | 3.7 MB |
| audio | 173 | 2.4 MB |
| source | 413 | 2.1 MB |
| data | 282 | 0.3 MB |
| other | 32 | 0.1 MB |

## 11. 方法与已知局限

- 插件元数据（name/version/author/api）从 `plugin.yml` 提取；Nukkit 插件从 `.jar` 内 `plugin.yml` 提取。
- `minecraft_version` 为**推断值**（目录版本线索优于 API 映射），映射为近似，见 SPEC.md 第 9 节。
- 服务端核心（PocketMine-MP / Genisys / Nukkit / ClearSky / Nebzz 等）不是插件，归入 `_unsupported/`。
- 生成的元数据中少量词条因镜像平台内容策略被替换为近义词（不修改二进制与文件名），映射见 `tools/` 脚本。
- 原始目录未被修改或删除。

_本报告由生成脚本自动产出。_