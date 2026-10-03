# _unsupported

非插件文件（服务端核心等），不是插件，不会被索引进 `catalog.json`。

- 小于 256KB 的文件按原始相对路径保留；较大的服务端核心仅登记在 `MANIFEST.json`（含 path/size/sha256），受镜像仓库体积限制不再内嵌，原始文件仍完整保留在源目录。
- Java 版 (Bukkit/Spigot) 插件已作为 `server_type: other` 收入 `plugins/other/`。
