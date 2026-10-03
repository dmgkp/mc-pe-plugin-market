# Minecraft 基岩版插件仓库 (Bedrock Plugin Repo)

一个托管在 **GitHub** 的 Minecraft 基岩版 (Bedrock Edition) 插件仓库，
提供结构化目录、机器可读的 `catalog.json` 与多维索引，应用可按服务端类型 / MC 版本 / 服务端版本 / 标签筛选下载。

## GitHub Raw 直链前缀

`https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/`

拼下载地址：`前缀 + plugins[].file 相对路径`。例如 `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/<相对路径>`。

## 开源协议

本仓库自身的**内容**（目录结构、`catalog.json`/`api.json`/`index/*` 等数据、JSON Schema、文档、`tools/` 脚本）以 **GNU AGPL-3.0** 授权，全文见 [`LICENSE`](LICENSE)。

⚠️ 仓库内打包的**第三方插件二进制文件**不属于 AGPL 授权范围，其权利仍归各自原作者，多数原始分发包未附带许可证（`plugin.json` 中 `license: NOASSERTION`）。详见 [`NOTICE.md`](NOTICE.md)。

若你是某插件作者并希望下架或变更授权，请提 Issue。

## 免责声明 (Disclaimer)

1. 本仓库为 **非官方** 的个人整理与归档项目，与 Mojang Studios / Microsoft、任何服务端核心或插件作者均无隶属、赞助或背书关系。
2. 仓库内所有插件及其二进制文件 **版权归各自原作者所有**；本仓库仅做收集、索引与分发，未对插件二进制或其功能做任何修改（仅生成的元数据文本做过少量合规性替换）。
3. 插件多来自网络公开的整合包，来源庞杂，无法逐一核实授权与出处；若你是权利人且不希望被收录，请提交 Issue，我们会尽快移除。
4. 本仓库 **不对插件的可用性、安全性、兼容性或合法性作任何担保**。请在下载后自行审查代码、校验 sha256，并自行承担使用风险（包括但不限于存档损坏、服务器故障、数据丢失）。
5. 因使用或无法使用本仓库内容而产生的任何直接或间接损失，作者及贡献者 **概不负责**。
6. 请勿将本仓库内容用于任何违法用途；使用者应遵守所在地法律法规及各插件自身的许可协议。
7. "Minecraft"、"我的世界" 等为 Mojang / Microsoft 的商标，本仓库与其无关。

完整免责声明见 [`DISCLAIMER.md`](DISCLAIMER.md)。

## 致敬插件作者

本仓库收录的 **1084** 个插件，凝结了众多社区作者的日夜心血。谨向以下作者，以及所有未能留下名字的作者，致以诚挚的感谢 🙏

| 作者 | 收录插件数 |
|------|-----------|
| onebone | 85 |
| MUedsa | 30 |
| Him188 | 24 |
| LDX | 18 |
| aliuly | 18 |
| Spiderman | 18 |
| zmdd | 17 |
| linger | 15 |
| FENGberd | 13 |
| FENGberd,Alcatraz_Du | 13 |
| happylife | 12 |
| fxxk | 11 |
| Mentha Haplocalyx Alcatraz_Du | 11 |
| EvolSoft | 11 |
| labi | 11 |
| Kevin | 11 |
| Mr_sky | 10 |
| 18wyj2 | 10 |
| [Praxthisnovcht] | 10 |
| Kirt | 10 |
| plus | 9 |
| Wshape1 | 9 |
| uuuuone | 8 |
| Smile | 8 |
| Orange | 8 |
| zzx | 8 |
| boybook | 8 |
| 64FF00 | 8 |
| MagicDroidX | 7 |
| Tethered_ | 7 |

共 **308** 位署名作者（部分老插件未署名）。全部版权归原作者所有；
若你是作者，希望调整署名、补充 License 或下架，请提 Issue，我们会尽快处理。

## 目录结构

```
.
├── README.md / SPEC.md / api.json / catalog.json / catalog.md / REPORT.md
├── schemas/{plugin.schema.json,catalog.schema.json}
├── index/{latest.json,by-server-type/,by-minecraft-version/,by-server-version/,by-tag/}
├── plugins/<server_type>/<minecraft_version>/<plugin_id>/
│     ├── plugin.json  README.md  CHANGELOG.md  LICENSE  icon.png(可选)
│     └── <PluginName>-<plugin_version>.<ext>
├── _unknown/      # 损坏/无法识别（原始文件保留）
└── _unsupported/  # 非插件（服务端核心等）
```

## 如何下载

1. 打开 `catalog.json`（或 `index/latest.json`），找到目标插件。
2. 取 `plugins[].file` 相对路径，例如 `plugins/nukkit/0.15.0/awtmessage/AwtMessage-0.0.2-SNAPSNOT.jar`。
3. 拼 GitHub 前缀即可下载，例如 `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/nukkit/0.15.0/awtmessage/AwtMessage-0.0.2-SNAPSNOT.jar`。
4. 用 `plugins[].sha256` 校验完整性。

## 接口 / API

全部为静态 JSON，拼 GitHub Raw 前缀即可拉取。入口说明见 [`api.json`](api.json)。

### 入口文件

| 文件 | 说明 |
|------|------|
| `catalog.json` | 全量插件清单（程序总入口） |
| `index/latest.json` | 每个插件的最新版 |
| `api.json` | 接口入口说明（catalog/latest/schemas/indexes/mirrors） |
| `schemas/plugin.schema.json` | 单个插件 `plugin.json` 的 JSON Schema |
| `schemas/catalog.schema.json` | `catalog.json` 的 JSON Schema |

### 条件筛选索引

| 需求 | 路径 | 示例 |
|------|------|------|
| 按服务端类型 | `index/by-server-type/<server_type>.json` | `index/by-server-type/pocketmine-mp.json` |
| 按 MC 版本 | `index/by-minecraft-version/<minecraft_version>.json` | `index/by-minecraft-version/0.11.1.json` |
| 服务端类型 + MC 版本 | `index/by-server-type/<server_type>/<minecraft_version>.json` | `index/by-server-type/nukkit/0.15.0.json` |
| 按服务端版本 | `index/by-server-version/<server_type>/<server_version>.json` | `index/by-server-version/pocketmine-mp/1.0.0.json` |
| 按标签 | `index/by-tag/<tag>.json` | `index/by-tag/economy.json` |

每个索引文件结构：`{schema_version, generated_at, index, count, plugins[]}`，`plugins[]` 项字段：
`id, name, display_name, server_type, minecraft_version, plugin_version, path, file, sha256, size, tags, download_paths`。

### plugin.json 字段

`schema_version, id, name, display_name, edition, server_type, server_types, minecraft_version, 
minecraft_versions, minecraft_version_range, minecraft_version_source, server_versions, server_version_source, 
plugin_version, author, license, license_status, description, tags, dependencies, conflicts, 
commands[]{name,description,usage,permission,aliases}, files[]{path,file_name,sha256,size,download_paths}, 
history, readme, changelog, icon, status, source, updated_at`。

### 调用与下载（伪代码）

```text
base = "https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/"
cat  = GET(base + "catalog.json")
item = 从 cat.plugins 里按 server_type / minecraft_version / tag 筛选
data = GET(base + item.file)
assert sha256(data) == item.sha256
```

> 每个插件目录内的 `README.md` 含中文**功能简介 / 命令列表 / 使用方法**，`plugin.json` 含机器可读的 `commands` 与全部字段。

## 推送到 GitHub

```bash
git remote add origin dmgkp/mc-pe-plugin-market.git
git push -u origin main
```

> 仓库地址与镜像前缀已固定为 `dmg666/mc-pe-plugin-market`；如需迁移，修改生成脚本中的 `USER` / `REPO` 后重新生成即可。

_Generated 2026-10-03T20:43:11+08:00. 1084 个插件条目。_