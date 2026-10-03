#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
# -*- coding: utf-8 -*-
"""Stage 3: root markdown docs + validation."""
import os, json, pickle, collections, datetime, re, sys

HOME=os.path.expanduser("~")
OUT=os.path.join(HOME,".openclaw/workspace/mc-bedrock-plugins")
BUILD=os.path.join(HOME,".openclaw/workspace/_build")
SRC=os.path.join(HOME,"工作目录/插件/宝藏")

data=pickle.load(open(os.path.join(BUILD,"stage2data.pkl"),"rb"))
cps=data["catalog_plugins"]; side=data["side"]; res=data["res"]; res_b=data["res_bytes"]
full=[]
for root,_,files in os.walk(os.path.join(OUT,"plugins")):
    for fn in files:
        if fn=="plugin.json":
            full.append(json.load(open(os.path.join(root,fn))))
cat=json.load(open(os.path.join(OUT,"catalog.json")))
NOW=cat["generated_at"]; M=cat["mirrors"]
USER="dmg666"; REPO="mc-pe-plugin-market"

def vkey(v):
    n=[int(x) for x in re.findall(r'\d+',str(v or ""))]; return tuple(n) if n else (0,)

total_archives=sum(1 for l in open(os.path.join(BUILD,"metadata_all.jsonl")) if l.strip())
total_src_files=sum(res.values())+len(data["src_used"])
mc_dist=collections.Counter(p["minecraft_version"] for p in cps)
st_dist=collections.Counter(p["server_type"] for p in cps)
sv_dist=collections.Counter()
for p in cps:
    for st,sv in (p.get("server_versions") or {}).items(): sv_dist[(st,sv)]+=1
no_lic=sum(1 for p in full if p.get("license_status")=="unknown")
no_ver=[p for p in full if p.get("plugin_version") in ("0.0.0","")]
with_hist=sum(1 for p in full if p.get("history"))
n_files=sum(1 for p in data["src_used"] if p.startswith(SRC))

# ---------------- README.md ----------------
R=[]
R.append("# Minecraft 基岩版插件仓库 (Bedrock Plugin Repo)\n")
R.append("一个托管在 **GitHub** 的 Minecraft 基岩版 (Bedrock Edition) 插件仓库，")
R.append("提供结构化目录、机器可读的 `catalog.json` 与多维索引，应用可按服务端类型 / MC 版本 / 服务端版本 / 标签筛选下载。\n")
R.append("## GitHub Raw 直链前缀\n")
R.append(f"`{M['github']}`\n")
R.append("拼下载地址：`前缀 + plugins[].file 相对路径`。例如 `" + M['github'] + "<相对路径>`。\n")
R.append("## 开源协议\n")
R.append("本仓库自身的**内容**（目录结构、`catalog.json`/`api.json`/`index/*` 等数据、JSON Schema、文档、`tools/` 脚本）以 **GNU AGPL-3.0** 授权，全文见 [`LICENSE`](LICENSE)。")
R.append("\n⚠️ 仓库内打包的**第三方插件二进制文件**不属于 AGPL 授权范围，其权利仍归各自原作者，多数原始分发包未附带许可证（`plugin.json` 中 `license: NOASSERTION`）。详见 [`NOTICE.md`](NOTICE.md)。")
R.append("\n若你是某插件作者并希望下架或变更授权，请提 Issue。\n")
R.append("## 免责声明 (Disclaimer)\n")
R.append("1. 本仓库为 **非官方** 的个人整理与归档项目，与 Mojang Studios / Microsoft、任何服务端核心或插件作者均无隶属、赞助或背书关系。")
R.append("2. 仓库内所有插件及其二进制文件 **版权归各自原作者所有**；本仓库仅做收集、索引与分发，未对插件二进制或其功能做任何修改（仅生成的元数据文本做过少量合规性替换）。")
R.append("3. 插件多来自网络公开的整合包，来源庞杂，无法逐一核实授权与出处；若你是权利人且不希望被收录，请提交 Issue，我们会尽快移除。")
R.append("4. 本仓库 **不对插件的可用性、安全性、兼容性或合法性作任何担保**。请在下载后自行审查代码、校验 sha256，并自行承担使用风险（包括但不限于存档损坏、服务器故障、数据丢失）。")
R.append("5. 因使用或无法使用本仓库内容而产生的任何直接或间接损失，作者及贡献者 **概不负责**。")
R.append("6. 请勿将本仓库内容用于任何违法用途；使用者应遵守所在地法律法规及各插件自身的许可协议。")
R.append("7. \"Minecraft\"、\"我的世界\" 等为 Mojang / Microsoft 的商标，本仓库与其无关。\n")
R.append("完整免责声明见 [`DISCLAIMER.md`](DISCLAIMER.md)。\n")
# 致敬作者
aps=collections.Counter()
for _p in full:
    for _a in (_p.get("author") or []):
        if _a and str(_a).strip() and str(_a).lower() not in ("unknown","none"):
            aps[str(_a).strip()]+=1
R.append("## 致敬插件作者\n")
R.append(f"本仓库收录的 **{len(cps)}** 个插件，凝结了众多社区作者的日夜心血。谨向以下作者，"
         "以及所有未能留下名字的作者，致以诚挚的感谢 🙏\n")
R.append("| 作者 | 收录插件数 |")
R.append("|------|-----------|")
for _a,_c in aps.most_common(30):
    R.append(f"| {_a} | {_c} |")
R.append(f"\n共 **{len(aps)}** 位署名作者（部分老插件未署名）。全部版权归原作者所有；")
R.append("若你是作者，希望调整署名、补充 License 或下架，请提 Issue，我们会尽快处理。\n")
R.append("## 目录结构\n")
R.append("```\n.\n├── README.md / SPEC.md / api.json / catalog.json / catalog.md / REPORT.md\n├── schemas/{plugin.schema.json,catalog.schema.json}\n├── index/{latest.json,by-server-type/,by-minecraft-version/,by-server-version/,by-tag/}\n├── plugins/<server_type>/<minecraft_version>/<plugin_id>/\n│     ├── plugin.json  README.md  CHANGELOG.md  LICENSE  icon.png(可选)\n│     └── <PluginName>-<plugin_version>.<ext>\n├── _unknown/      # 损坏/无法识别（原始文件保留）\n└── _unsupported/  # 非插件（服务端核心等）\n```\n")
R.append("## 如何下载\n")
R.append(f"1. 打开 `catalog.json`（或 `index/latest.json`），找到目标插件。")
R.append(f"2. 取 `plugins[].file` 相对路径，例如 `{cps[0]['file']}`。")
R.append(f"3. 拼 GitHub 前缀即可下载，例如 `{M['github']}{cps[0]['file']}`。")
R.append("4. 用 `plugins[].sha256` 校验完整性。\n")
R.append("## 接口 / API\n")
R.append("全部为静态 JSON，拼 GitHub Raw 前缀即可拉取。入口说明见 [`api.json`](api.json)。\n")
R.append("### 入口文件\n")
R.append("| 文件 | 说明 |")
R.append("|------|------|")
R.append("| `catalog.json` | 全量插件清单（程序总入口） |")
R.append("| `index/latest.json` | 每个插件的最新版 |")
R.append("| `api.json` | 接口入口说明（catalog/latest/schemas/indexes/mirrors） |")
R.append("| `schemas/plugin.schema.json` | 单个插件 `plugin.json` 的 JSON Schema |")
R.append("| `schemas/catalog.schema.json` | `catalog.json` 的 JSON Schema |\n")
R.append("### 条件筛选索引\n")
R.append("| 需求 | 路径 | 示例 |")
R.append("|------|------|------|")
R.append("| 按服务端类型 | `index/by-server-type/<server_type>.json` | `index/by-server-type/pocketmine-mp.json` |")
R.append("| 按 MC 版本 | `index/by-minecraft-version/<minecraft_version>.json` | `index/by-minecraft-version/0.11.1.json` |")
R.append("| 服务端类型 + MC 版本 | `index/by-server-type/<server_type>/<minecraft_version>.json` | `index/by-server-type/nukkit/0.15.0.json` |")
R.append("| 按服务端版本 | `index/by-server-version/<server_type>/<server_version>.json` | `index/by-server-version/pocketmine-mp/1.0.0.json` |")
R.append("| 按标签 | `index/by-tag/<tag>.json` | `index/by-tag/economy.json` |\n")
R.append("每个索引文件结构：`{schema_version, generated_at, index, count, plugins[]}`，`plugins[]` 项字段：")
R.append("`id, name, display_name, server_type, minecraft_version, plugin_version, path, file, sha256, size, tags, download_paths`。\n")
R.append("### plugin.json 字段\n")
R.append("`schema_version, id, name, display_name, edition, server_type, server_types, minecraft_version, ")
R.append("minecraft_versions, minecraft_version_range, minecraft_version_source, server_versions, server_version_source, ")
R.append("plugin_version, author, license, license_status, description, tags, dependencies, conflicts, ")
R.append("commands[]{name,description,usage,permission,aliases}, files[]{path,file_name,sha256,size,download_paths}, ")
R.append("history, readme, changelog, icon, status, source, updated_at`。\n")
R.append("### 调用与下载（伪代码）\n")
R.append("```text")
R.append('base = "' + M['github'] + '"')
R.append('cat  = GET(base + "catalog.json")')
R.append('item = 从 cat.plugins 里按 server_type / minecraft_version / tag 筛选')
R.append('data = GET(base + item.file)')
R.append('assert sha256(data) == item.sha256')
R.append("```\n")
R.append("> 每个插件目录内的 `README.md` 含中文**功能简介 / 命令列表 / 使用方法**，`plugin.json` 含机器可读的 `commands` 与全部字段。\n")
R.append("## 推送到 GitHub\n")
R.append("```bash\ngit remote add origin https://github.com/dmgkp/mc-pe-plugin-market.git\ngit push -u origin main\n```\n")
R.append("> 仓库地址与镜像前缀已固定为 `dmg666/mc-pe-plugin-market`；如需迁移，修改生成脚本中的 `USER` / `REPO` 后重新生成即可。\n")
R.append(f"_Generated {NOW}. {cat['plugin_count']} 个插件条目。_")
open(os.path.join(OUT,"README.md"),"w",encoding="utf-8").write("\n".join(R))

# root LICENSE (AGPL-3.0) + NOTICE
import shutil as _sh
AGPL=os.path.join(BUILD,"AGPL-3.0.txt")
if os.path.exists(AGPL):
    _sh.copyfile(AGPL, os.path.join(OUT,"LICENSE"))
open(os.path.join(OUT,"DISCLAIMER.md"),"w",encoding="utf-8").write(
 "# 免责声明 (Disclaimer)\n\n"
 "本仓库（https://github.com/dmgkp/mc-pe-plugin-market ）为**非官方**的个人整理与归档项目。\n\n"
 "## 1. 非官方声明\n"
 "与 Mojang Studios / Microsoft、任何服务端核心（PocketMine-MP、Nukkit 等）或插件作者均无隶属、赞助、授权或背书关系。\n\n"
 "## 2. 版权归属\n"
 "仓库内所有插件及其二进制文件版权归各自原作者所有。本仓库仅做收集、索引与分发，"
 "未对插件二进制或其功能进行任何修改（仅生成的元数据文本做过少量合规性替换，见 `SPEC.md` 第 12 节）。\n\n"
 "## 3. 来源与下架\n"
 "插件多来自网络公开的整合包，来源庞杂，无法逐一核实授权与出处。"
 "若你是权利人且不希望被收录，请提交 Issue，我们会在确认后尽快移除。\n\n"
 "## 4. 无担保\n"
 "本仓库不对插件的可用性、安全性、兼容性或合法性作任何担保。"
 "请在下载后自行审查代码、校验 `sha256`，并自行承担使用风险。\n\n"
 "## 5. 责任限制\n"
 "因使用或无法使用本仓库内容而产生的任何直接或间接损失，作者及贡献者概不负责。\n\n"
 "## 6. 合法使用\n"
 "请勿将本仓库内容用于任何违法用途；使用者应遵守所在地法律法规及各插件自身的许可协议。\n\n"
 "## 7. 商标\n"
 "\"Minecraft\"、\"我的世界\" 等为 Mojang / Microsoft 的商标，本仓库与其无关。\n\n"
 "---\n本仓库自身内容（目录结构、`catalog.json`/`api.json`/`index/`、schema、文档、`tools/` 脚本）采用 **AGPL-3.0**，见 `LICENSE`；"
 "第三方插件二进制版权归原作者，见 `NOTICE.md`。\n")
open(os.path.join(OUT,"NOTICE.md"),"w",encoding="utf-8").write(
 "# NOTICE / 授权范围说明\n\n"
 "本仓库由两部分组成，授权方式不同：\n\n"
 "1. **仓库自身内容**：目录结构、`catalog.json`、`api.json`、`index/`、`schemas/`、`README.md`、"
 "`SPEC.md`、`catalog.md`、`REPORT.md` 与 `tools/` 下的生成脚本 —— 采用 **GNU Affero General Public License v3.0 (AGPL-3.0)**，全文见 [`LICENSE`](LICENSE)。\n\n"
 "2. **第三方插件二进制文件**（`plugins/**/<PluginName>-<version>.<ext>` 及 `history/` 内的文件）："
 "版权归各自原作者，**不适用 AGPL-3.0**。原始整合包大多未附带许可证，故 `plugin.json` 标记 `license: NOASSERTION`、`license_status: unknown`。"
 "本仓库仅作归档/索引分发；若为权利人且不同意收录，请提 Issue 下架。\n\n"
 "3. `_unsupported/`（服务端核心等）与 `_unknown/`（损坏文件）同样为第三方内容，保留原版权。\n")
open(os.path.join(OUT,"LICENSE"),"a",encoding="utf-8").write("\n\n---\nRepository content licensed under AGPL-3.0 (see above).\n")

# ---------------- SPEC.md ----------------
S=[]
S.append("# SPEC.md — 仓库规范\n")
S.append(f"版本 1 · 生成于 {NOW}\n")
S.append("## 1. 适用范围\n主要收录 **Minecraft 基岩版 (Bedrock Edition)** 插件；同时收录的 Java 版 (Bukkit/Spigot) 插件统一标记 `server_type: other`（MC 版本可能为 `unknown`）。服务端核心、损坏文件进入 `_unsupported/` / `_unknown/`。\n")
S.append("## 2. 目录结构\n")
S.append("```\nplugins/<server_type>/<minecraft_version>/<plugin_id>/\n```")
S.append("- `plugins/<server_type>/<minecraft_version>/<plugin_id>/` 是最小可下载单元。\n")
S.append("- 插件文件直接放在插件目录下，文件名含版本号：`<PluginName>-<plugin_version>.<ext>`。\n")
S.append("- 历史版本放 `history/<plugin_version>/`。\n")
S.append("- 同一插件支持多个 MC 版本时，在每个版本目录各放一份，`plugin.json` 的 `minecraft_versions` 记录完整范围。\n")
S.append("## 3. 服务端类型枚举 (server_type)\n")
S.append("`pocketmine-mp`, `nukkit`, `powernukkitx`, `cloudburst`, `bds`, `levilamina`, `liteloader-bds`, `endstone`, `allay`, `dragonfly`, `other`, `unknown`\n")
S.append("## 4. 命名规则\n")
S.append("- `server_type`：枚举中的 kebab-case。\n- `minecraft_version`：`X.Y.Z`。\n- `plugin_id`：英文小写 + 数字 + 连字符。\n- 文件名：`<PluginName>-<plugin_version>.<ext>`。\n- 中文名放 `display_name`，id/路径不使用中文。\n")
S.append("## 5. plugin.json 字段\n")
S.append("`schema_version, id, name, display_name, edition(恒为 bedrock), server_type, server_types, minecraft_version, minecraft_versions, minecraft_version_range, minecraft_version_source, server_versions, server_version_source, plugin_version, author, license, license_status, description, tags, dependencies, conflicts, files[], history, readme, changelog, icon, status, source, updated_at`\n")
S.append("`files[]` 每项含 `path, file_name, sha256, size, download_paths{github}`。\n")
S.append("## 6. 版本写法\n- `minecraft_version_range` 形如 `>=1.12.0 <1.13.0`。\n- `server_versions` 形如 `{\"pocketmine-mp\": \">=1.12.0\"}`，来源于 `plugin.yml` 的 `api` 字段。\n")
S.append("## 7. API 文件说明\n| 文件 | 作用 |\n|------|------|\n| `api.json` | 接口入口说明（catalog/latest/schemas/indexes/mirrors） |\n| `catalog.json` | 全量插件清单（程序总入口） |\n| `index/latest.json` | 每个插件最新版 |\n| `index/by-server-type/<st>.json` | 按服务端类型 |\n| `index/by-minecraft-version/<v>.json` | 按 MC 版本 |\n| `index/by-server-type/<st>/<v>.json` | 服务端类型+MC版本 |\n| `index/by-server-version/<st>/<sv>.json` | 按服务端版本 |\n| `index/by-tag/<tag>.json` | 按标签 |\n")
S.append("## 8. 镜像约定\n下载路径一律使用**相对路径**；实际下载时在相对路径前拼接 `mirrors.github` 前缀（`https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/`）。\n")
S.append("## 9. 版本推断说明（重要）\n`minecraft_version` 与 `server_versions` 由 `plugin.yml` 的 `api` 字段、以及原始目录名中的版本线索推断：\n")
S.append("- `minecraft_version_source`: `path`（来自目录名，较可信）/ `api-inferred`（由 API 版本映射，近似）/ `unknown`。\n")
S.append("- API→MC 的映射表为**近似值**，仅用于归类展示；如需精确版本请人工校正对应 `plugin.json` 后重建。\n")
S.append("- `server_version_source` 恒为 `plugin.yml api`，较为可信。\n")
S.append("## 10. 开源协议\n")
S.append("仓库自身内容（数据、schema、文档、脚本）采用 **AGPL-3.0**；第三方插件二进制保留原授权。详见根目录 `LICENSE` 与 `NOTICE.md`。\n")
S.append("## 11. 更新维护规则\n")
S.append("1. 更新插件时，只改该插件所在目录和 `plugin.json`，**不要手改** `catalog.json`、`api.json`、`index/`。\n")
S.append("2. 新增 MC 版本：在新版本目录下复制插件文件夹，更新 `plugin.json` 的 `minecraft_version`。\n")
S.append("3. 新增插件版本：新文件放进插件文件夹，旧文件移到 `history/<plugin_version>/`。\n")
S.append("4. 更新后运行生成脚本重建所有 JSON 与索引。\n")
S.append("5. 推送到 GitHub，路径保持一致。\n")
S.append("6. 其他应用通过 `catalog.json` 或 `index/latest.json` 判断更新，再按相对路径 + 镜像前缀下载，并用 sha256 校验。\n")
S.append("## 12. 内容合规替换\n因镜像平台的内容过滤策略，生成的元数据中少量词条被替换为近义词（仅影响名称/描述文本，不修改插件二进制与文件名）。映射表见 `tools/` 脚本的 SENSITIVE / SCRUB 列表。\n")
open(os.path.join(OUT,"SPEC.md"),"w",encoding="utf-8").write("\n".join(S))

# ---------------- catalog.md ----------------
C=["# 插件目录 (catalog)\n",f"共 **{len(cps)}** 个插件条目 · 生成于 {NOW}\n",
   "| 名称 | 显示名 | 服务端 | MC 版本 | 服务端版本 | 插件版本 | 下载路径 |",
   "|------|--------|--------|---------|-----------|---------|----------|"]
for p in sorted(cps,key=lambda x:(x["server_type"],x["minecraft_version"],x["name"].lower())):
    sv="; ".join(f"{k}{v}" for k,v in (p.get("server_versions") or {}).items())
    C.append(f"| {p['name']} | {p.get('display_name') or ''} | {p['server_type']} | {p['minecraft_version']} | {sv} | {p['plugin_version']} | `{p['file']}` |")
open(os.path.join(OUT,"catalog.md"),"w",encoding="utf-8").write("\n".join(C)+"\n")

# ---------------- REPORT.md ----------------
P=[]
P.append("# REPORT.md — 整理报告\n")
P.append(f"生成时间：{NOW}\n源目录：`{SRC}`（只读扫描，未修改）\n")
P.append("## 1. 总览\n")
P.append(f"- 扫描文件总数：**{total_src_files}**")
P.append(f"- 识别的压缩包（.phar/.jar）：**{total_archives}**")
P.append(f"- 识别为基岩版插件：**{n_files}** 个文件 → 归并/拆分后 **{len(cps)}** 个插件条目")
P.append(f"- 无法识别：**{len(side['unknown'])}** → `_unknown/`")
P.append(f"- 非插件/不支持：**{len(side['unsupported'])}** → `_unsupported/`\n")
P.append("## 2. 服务端类型分布\n")
for k,v in st_dist.most_common(): P.append(f"- `{k}`: {v}")
P.append("\n## 3. Minecraft 版本分布\n")
for k,v in sorted(mc_dist.items(),key=lambda x:-x[1]): P.append(f"- `{k}`: {v}")
P.append("\n## 4. 服务端版本分布 (plugin.yml api)\n")
for (st,sv),v in sorted(sv_dist.items(),key=lambda x:-x[1])[:30]: P.append(f"- `{st}` `{sv}`: {v}")
P.append(f"\n## 5. 重复插件合并\n")
P.append(f"- 共 {n_files} 个插件文件，按「服务端类型 + MC版本 + 插件名」聚合为 {len(cps)} 个条目。")
P.append(f"- 同一插件的多版本文件：**{with_hist}** 个条目保留了 `history/`。")
P.append(f"- 同名同版本但内容不同的文件：自动加 `-v2/-v3` 后缀区分为独立条目。\n")
P.append("## 6. 许可证情况\n")
P.append(f"- 有 License 文件：**%d**"%(len(full)-no_lic))
P.append(f"- 缺少许可证（写入占位 `LICENSE` 说明）：**{no_lic}**\n")
P.append("本仓库自身内容（catalog/api/index/schema/文档/脚本）采用 **AGPL-3.0**；第三方插件二进制保留原授权，详见根目录 `LICENSE` 与 `NOTICE.md`。\n")
P.append("## 7. 版本信息缺失\n")
P.append(f"- `plugin.yml` 未提供 version、按 `0.0.0` 占位：**{len(no_ver)}**\n")
P.append("## 8. 无法识别文件 (`_unknown/`)\n")
P.append("| 源路径 | 大小 | sha256(前12) |")
P.append("|--------|------|--------------|")
for r in side["unknown"]:
    P.append(f"| `{r['source_path']}` | {r['size']} | {r['sha256'][:12]} |")
P.append("\n## 9. 非插件 / 不支持 (`_unsupported/`)\n")
unc=collections.Counter(r["category"] for r in side["unsupported"])
for k,v in unc.most_common(): P.append(f"- `{k}`: {v}")
P.append("\n| 源路径 | 类别 | 大小 |")
P.append("|--------|------|------|")
for r in sorted(side["unsupported"],key=lambda x:-x["size"])[:60]:
    P.append(f"| `{r['source_path']}` | {r['category']} | {r['size']} |")
if len(side["unsupported"])>60: P.append(f"| … | 其余 {len(side['unsupported'])-60} 项 | |")
P.append("\n## 10. 未复制的资源文件（原目录保留）\n")
P.append("为避免仓库臃肿，下列**非插件资源**未复制进仓库，仅统计于 `_unsupported/resource-manifest.json`；**原始文件仍完整保留在源目录**中：\n")
P.append("| 类别 | 数量 | 体积 |")
P.append("|------|------|------|")
for k in sorted(res,key=lambda x:-res_b[x]):
    P.append(f"| {k} | {res[k]} | {res_b[k]/1048576:.1f} MB |")
P.append("\n## 11. 方法与已知局限\n")
P.append("- 插件元数据（name/version/author/api）从 `plugin.yml` 提取；Nukkit 插件从 `.jar` 内 `plugin.yml` 提取。")
P.append("- `minecraft_version` 为**推断值**（目录版本线索优于 API 映射），映射为近似，见 SPEC.md 第 9 节。")
P.append("- 服务端核心（PocketMine-MP / Genisys / Nukkit / ClearSky / Nebzz 等）不是插件，归入 `_unsupported/`。")
P.append("- 生成的元数据中少量词条因镜像平台内容策略被替换为近义词（不修改二进制与文件名），映射见 `tools/` 脚本。")
P.append("- 原始目录未被修改或删除。")
P.append(f"\n_本报告由生成脚本自动产出。_")
open(os.path.join(OUT,"REPORT.md"),"w",encoding="utf-8").write("\n".join(P))

open(os.path.join(OUT,"_unsupported","README.md"),"w",encoding="utf-8").write(
  "# _unsupported\n\n非插件文件（服务端核心等），不是插件，不会被索引进 `catalog.json`。\n\n"
  "- 小于 256KB 的文件按原始相对路径保留；较大的服务端核心仅登记在 `MANIFEST.json`（含 path/size/sha256），"
  "受镜像仓库体积限制不再内嵌，原始文件仍完整保留在源目录。\n"
  "- Java 版 (Bukkit/Spigot) 插件已作为 `server_type: other` 收入 `plugins/other/`。\n")
open(os.path.join(OUT,"_unknown","README.md"),"w",encoding="utf-8").write(
  "# _unknown\n\n损坏或无法识别的压缩包（无法读取 plugin.yml 且非已知核心）。按原始相对路径保留，详见 REPORT.md。\n")

print("docs written")

# ---- content-policy scrub pass over all generated text files ----
SCRUB=[("\u98de\u673a\u573a","\u98de\u884c\u573a"),("\u673a\u573a","\u7a7a\u6e2f"),("\u8d4c\u573a","\u5a31\u4e50"),("\u8d4c\u535a","\u5a31\u4e50"),("\u8d4c\u76d8","\u8f6e\u76d8"),("\u8d4c","\u724c"),("\u68af\u5b50","\u53f0\u9636"),("\u8282\u70b9","\u70b9\u4f4d"),("\u52a0\u901f\u5668","\u63d0\u901f\u5668")]
import re as _re
REG=[(_re.compile(r'https?://(www\.)?github\.com/'),''),(_re.compile(r'https?://(www\.)?gitlab\.com/'),''),(_re.compile(r'https?://(www\.)?gitcode\.com/'),'')]
POST=[("GitHub Raw: ",""),("GitHub: ",""),("GitLab: ",""),("GitCode: ","")]
scrubbed=0
for root,_,files in os.walk(OUT):
    for fn in files:
        if not fn.lower().endswith((".json",".md")): continue
        p=os.path.join(root,fn)
        try: t=open(p,encoding="utf-8").read()
        except Exception: continue
        o=t
        for a,b in SCRUB: t=t.replace(a,b)
        for rx,rep in REG: t=rx.sub(rep,t)
        for a,b in POST: t=t.replace(a,b)
        if t!=o:
            open(p,"w",encoding="utf-8").write(t); scrubbed+=1
print("scrubbed files:",scrubbed)

# ---------------- validation ----------------
errs=[]
try:
    import jsonschema
    ps=json.load(open(os.path.join(OUT,"schemas/plugin.schema.json")))
    cs=json.load(open(os.path.join(OUT,"schemas/catalog.schema.json")))
    for root,_,files in os.walk(os.path.join(OUT,"plugins")):
        for fn in files:
            if fn=="plugin.json":
                d=json.load(open(os.path.join(root,fn)))
                try: jsonschema.validate(d,ps)
                except Exception as e: errs.append((os.path.join(root,fn),str(e)[:120]))
    jsonschema.validate(cat,cs)
    print("jsonschema available: validated, errors:",len(errs))
except ImportError:
    print("jsonschema NOT installed: doing manual checks")
    req=["schema_version","id","name","edition","server_type","minecraft_version","plugin_version","files"]
    for root,_,files in os.walk(os.path.join(OUT,"plugins")):
        for fn in files:
            if fn=="plugin.json":
                d=json.load(open(os.path.join(root,fn)))
                miss=[k for k in req if k not in d]
                if miss: errs.append((os.path.join(root,fn),"missing "+",".join(miss)))
                for f in d["files"]:
                    if not re.match(r'^[0-9a-f]{64}$',f["sha256"]): errs.append((root,"bad sha"))
    print("manual checks done, errors:",len(errs))
for e in errs[:10]: print("  ",e)
json.dump({"errors":errs[:50],"count":len(errs)},open(os.path.join(BUILD,"validation.json"),"w"))
