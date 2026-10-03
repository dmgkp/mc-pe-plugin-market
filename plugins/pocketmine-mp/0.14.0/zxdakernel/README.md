# ZXDAKernel(极致整合)

## 功能简介

**极致整合(ZXDAKernel)** 是一款运行于 **PocketMine-MP** 的 Minecraft 基岩版插件,插件版本 `5.1.2.7`,作者 FENGberd。
主要功能方向:玩法。
原插件说明:查看指令使用帮助
本插件未在 plugin.yml 中声明命令,可能通过 GUI / 物品 / 事件触发。
共定义 **6** 个权限点位(见下表,可用于判断插件能力)。

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `ZXDAConnector.command.coupons.help` | 查看指令使用帮助 | op |
| `ZXDAConnector.command.coupons.set` | 通过指令设置玩家的点券数量 | op |
| `ZXDAConnector.command.coupons.add` | 通过指令添加玩家的点券 | op |
| `ZXDAConnector.command.coupons.take` | 通过指令拿走玩家的点券 | op |
| `ZXDAConnector.command.coupons.query` | 通过指令查询玩家的点券数量 | op |
| `ZXDAConnector.command.coupons.clear` | 通过指令清空所有点券数据 | false |

## 如何使用

1. 下载下方插件文件 `ZXDAKernel-5.1.2.7.phar`。
2. 放入服务器 `plugins/` 目录(PocketMine-MP)。
3. 重启或重载服务器,插件会自动加载。

## 元数据

- **id**: `zxdakernel`
- **edition**: bedrock
- **server_type**: `pocketmine-mp`
- **minecraft_version**: `0.14.0` (推断来源: api-inferred)
- **minecraft_versions**: 0.14.0
- **plugin_version**: `5.1.2.7`
- **author**: FENGberd
- **main**: `ZXDAKernel\Main`
- **license**: NOASSERTION (unknown)
- **tags**: gameplay

## 下载

- `ZXDAKernel-5.1.2.7.phar`(**247181** 字节,sha256 `64fe65d53d990a8c223efd397502f44ff14f6d4d64f73cd4c2aecee5d963b8e5`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/pocketmine-mp/0.14.0/zxdakernel/ZXDAKernel-5.1.2.7.phar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
