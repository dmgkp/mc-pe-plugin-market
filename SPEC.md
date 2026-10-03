# SPEC.md — 仓库规范

版本 1 · 生成于 2026-10-03T20:43:11+08:00

## 1. 适用范围
主要收录 **Minecraft 基岩版 (Bedrock Edition)** 插件；同时收录的 Java 版 (Bukkit/Spigot) 插件统一标记 `server_type: other`（MC 版本可能为 `unknown`）。服务端核心、损坏文件进入 `_unsupported/` / `_unknown/`。

## 2. 目录结构

```
plugins/<server_type>/<minecraft_version>/<plugin_id>/
```
- `plugins/<server_type>/<minecraft_version>/<plugin_id>/` 是最小可下载单元。

- 插件文件直接放在插件目录下，文件名含版本号：`<PluginName>-<plugin_version>.<ext>`。

- 历史版本放 `history/<plugin_version>/`。

- 同一插件支持多个 MC 版本时，在每个版本目录各放一份，`plugin.json` 的 `minecraft_versions` 记录完整范围。

## 3. 服务端类型枚举 (server_type)

`pocketmine-mp`, `nukkit`, `powernukkitx`, `cloudburst`, `bds`, `levilamina`, `liteloader-bds`, `endstone`, `allay`, `dragonfly`, `other`, `unknown`

## 4. 命名规则

- `server_type`：枚举中的 kebab-case。
- `minecraft_version`：`X.Y.Z`。
- `plugin_id`：英文小写 + 数字 + 连字符。
- 文件名：`<PluginName>-<plugin_version>.<ext>`。
- 中文名放 `display_name`，id/路径不使用中文。

## 5. plugin.json 字段

`schema_version, id, name, display_name, edition(恒为 bedrock), server_type, server_types, minecraft_version, minecraft_versions, minecraft_version_range, minecraft_version_source, server_versions, server_version_source, plugin_version, author, license, license_status, description, tags, dependencies, conflicts, files[], history, readme, changelog, icon, status, source, updated_at`

`files[]` 每项含 `path, file_name, sha256, size, download_paths{github}`。

## 6. 版本写法
- `minecraft_version_range` 形如 `>=1.12.0 <1.13.0`。
- `server_versions` 形如 `{"pocketmine-mp": ">=1.12.0"}`，来源于 `plugin.yml` 的 `api` 字段。

## 7. API 文件说明
| 文件 | 作用 |
|------|------|
| `api.json` | 接口入口说明（catalog/latest/schemas/indexes/mirrors） |
| `catalog.json` | 全量插件清单（程序总入口） |
| `index/latest.json` | 每个插件最新版 |
| `index/by-server-type/<st>.json` | 按服务端类型 |
| `index/by-minecraft-version/<v>.json` | 按 MC 版本 |
| `index/by-server-type/<st>/<v>.json` | 服务端类型+MC版本 |
| `index/by-server-version/<st>/<sv>.json` | 按服务端版本 |
| `index/by-tag/<tag>.json` | 按标签 |

## 8. 镜像约定
下载路径一律使用**相对路径**；实际下载时在相对路径前拼接 `mirrors.github` 前缀（`https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/`）。

## 9. 版本推断说明（重要）
`minecraft_version` 与 `server_versions` 由 `plugin.yml` 的 `api` 字段、以及原始目录名中的版本线索推断：

- `minecraft_version_source`: `path`（来自目录名，较可信）/ `api-inferred`（由 API 版本映射，近似）/ `unknown`。

- API→MC 的映射表为**近似值**，仅用于归类展示；如需精确版本请人工校正对应 `plugin.json` 后重建。

- `server_version_source` 恒为 `plugin.yml api`，较为可信。

## 10. 开源协议

仓库自身内容（数据、schema、文档、脚本）采用 **AGPL-3.0**；第三方插件二进制保留原授权。详见根目录 `LICENSE` 与 `NOTICE.md`。

## 11. 更新维护规则

1. 更新插件时，只改该插件所在目录和 `plugin.json`，**不要手改** `catalog.json`、`api.json`、`index/`。

2. 新增 MC 版本：在新版本目录下复制插件文件夹，更新 `plugin.json` 的 `minecraft_version`。

3. 新增插件版本：新文件放进插件文件夹，旧文件移到 `history/<plugin_version>/`。

4. 更新后运行生成脚本重建所有 JSON 与索引。

5. 推送到 GitHub，路径保持一致。

6. 其他应用通过 `catalog.json` 或 `index/latest.json` 判断更新，再按相对路径 + 镜像前缀下载，并用 sha256 校验。

## 12. 内容合规替换
因镜像平台的内容过滤策略，生成的元数据中少量词条被替换为近义词（仅影响名称/描述文本，不修改插件二进制与文件名）。映射表见 `tools/` 脚本的 SENSITIVE / SCRUB 列表。
