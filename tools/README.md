# tools/ — 生成脚本 (AGPL-3.0)
从源插件目录重建整个仓库（catalog/api/index 自动生成，勿手改）。
```
php tools/extract.php archives.txt > metadata.jsonl
python3 tools/stage_extra.py   # 提取 zip/rar 内嵌插件 + metadata_all.jsonl
python3 tools/build.py
python3 tools/stage2.py
python3 tools/stage3.py
```
镜像：GitHub https://github.com/dmgkp/mc-pe-plugin-market
