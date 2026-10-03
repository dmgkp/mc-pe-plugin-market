# AuthMe(基础插件)

## 功能简介

**基础插件(AuthMe)** 是一款运行于 **其它服务端** 的 Minecraft 基岩版插件,插件版本 `3.4`,作者 Xephi59。
主要功能方向:管理/权限、保护/防作弊、玩家/登录。
原插件说明:AuthMe prevents people, which aren't logged in, from doing stuff like placing blocks, moving, typing commands or seeing the inventory of the current player.
本插件共提供 **9** 条命令(见下表)。
共定义 **37** 个权限点位(见下表,可用于判断插件能力)。

## 命令列表

| 命令 | 说明 | 用法 | 权限 | 别名 |
|------|------|------|------|------|
| `/register` | Register an account | `/register password confirmpassword` | - | - |
| `/login` | Login into a account | `/login password` | - | - |
| `/changepassword` | Change password of a account | `/changepassword oldPassword newPassword` | - | - |
| `/logout` | Logout | `/logout` | - | - |
| `/unregister` | unregister your account | `/unregister password` | - | - |
| `/passpartu` | compare passpartu token | `/passpartu token` | - | - |
| `/authme` | AuthMe op commands | `/authme reload|register playername password|changepassword playername password|unregister playername|version` | - | - |
| `/email` | Add Email or recover password | `/email add your@email.com your@email.com|change oldEmail newEmail|recovery your@email.com` | - | - |
| `/captcha` | Captcha | `/captcha theCaptcha` | - | - |

## 权限点位

| 权限 | 说明 | 默认 |
|------|------|------|
| `authme.player.*` | Gives access to all authme player commands | true |
| `authme.admin.*` | Gives access to all authme admin commands | - |
| `authme.register` | Register an account | true |
| `authme.login` | Login into a account | true |
| `authme.changepassword` | Change password of a account | true |
| `authme.logout` | Logout | true |
| `authme.email` | Email | true |
| `authme.passpartu` | passpartu | true |
| `authme.allow2accounts` | allow more accounts for same ip | false |
| `authme.seeOtherAccounts` | display other accounts about a player when he logs in | false |
| `authme.unregister` | unregister your account | true |
| `authme.admin.reload` | AuthMe reload commands | op |
| `authme.admin.register` | AuthMe register command | op |
| `authme.admin.changepassword` | AuthMe changepassword command | op |
| `authme.admin.unregister` | AuthMe unregister command | op |
| `authme.admin.purge` | AuthMe unregister command | op |
| `authme.admin.convertflattosql` | Convert File to Sql method | op |
| `authme.admin.convertfromrakamak` | Convert from Rakamak database to AuthMe | op |
| `authme.admin.lastlogin` | Get last login date about a player | op |
| `authme.admin.getemail` | Get last email about a player | op |
| `authme.admin.chgemail` | Change a player email | op |
| `authme.admin.accounts` | Display Players Accounts | op |
| `authme.admin.xauthimport` | Import xAuth Database to AuthMe Database | op |
| `authme.captcha` | Captcha | true |
| `authme.admin.setspawn` | Set the AuthMe spawn point | op |
| `authme.admin.spawn` | Teleport to AuthMe spawn point | op |
| `authme.vip` | Allow vip slot when the server is full | op |
| `authme.admin.purgebannedplayers` | Purge banned players | op |
| `authme.admin.flattosqlite` | Convert File to Sqlite method | op |
| `authme.bypassforcesurvival` | Bypass all ForceSurvival features | false |
| `authme.admin.purgelastpos` | Purge last pos of players | op |
| `authme.admin.switchantibot` | Switch AntiBot mode on/off | op |
| `authme.bypassantibot` | Bypass the AntiBot check | op |
| `authme.admin.royalauth` | Import RoyalAuth database into AuthMe | op |
| `authme.admin.setfirstspawn` | Set the AuthMe First Spawn Point | op |
| `authme.admin.firstspawn` | Teleport to AuthMe First Spawn Point | op |
| `authme.admin.getip` | Get IP from a player ( fake and real ) | op |

## 如何使用

1. 下载下方插件文件 `AuthMe-3.4.jar`。
2. 放入服务器 `plugins/` 目录(其它服务端)。
3. 重启或重载服务器,插件会自动加载。
4. 在游戏内输入上表命令(控制台可省略 `/`)。

## 元数据

- **id**: `authme`
- **edition**: bedrock
- **server_type**: `other`
- **minecraft_version**: `unknown` (推断来源: unknown)
- **minecraft_versions**: unknown
- **plugin_version**: `3.4`
- **author**: Xephi59
- **softdependencies**: [Vault, ChestShop, Spout, Multiverse-Core, Notifications, Citizens, CombatTag, Essentials, EssentialsSpawn]
- **main**: `fr.xephi.authme.AuthMe`
- **website**: http://dev.bukkit.org/bukkit-plugins/authme-reloaded/
- **license**: NOASSERTION (unknown)
- **tags**: admin, protection, player

## 下载

- `AuthMe-3.4.jar`(**1076298** 字节,sha256 `0c7800f95da22e2d7e2dbf6255919d74cf20009a1ea06b3777ea19e32bba2733`)
  - github: `https://raw.githubusercontent.com/dmgkp/mc-pe-plugin-market/main/plugins/other/unknown/authme/AuthMe-3.4.jar`

---
本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。
