#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
# -*- coding: utf-8 -*-
"""Stage 2: materialize the repository from classified groups."""
import os, re, json, hashlib, shutil, subprocess, datetime, collections

HOME=os.path.expanduser("~")
SRC=os.path.join(HOME,"工作目录/插件/宝藏")
BUILD=os.path.join(HOME,".openclaw/workspace/_build")
OUT=os.path.join(HOME,".openclaw/workspace/mc-bedrock-plugins")

GH_USER="dmgkp"; REPO="mc-pe-plugin-market"
MIRRORS={
 "github":f"https://raw.githubusercontent.com/{GH_USER}/{REPO}/main/",
}
NOW=datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()

def sha256_file(p, buf=1<<20):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for c in iter(lambda:f.read(buf), b""):
            h.update(c)
    return h.hexdigest()

def vkey(v):
    nums=[int(x) for x in re.findall(r'\d+', str(v or ""))]
    return tuple(nums) if nums else (0,)

def safe(s):
    s=re.sub(r'[^A-Za-z0-9._-]+','_',str(s))
    return s.strip('_') or "file"

def tags_for(name,desc,st):
    t=[]
    s=(str(name)+" "+str(desc or "")).lower()
    rules=[("economy",["econom","shop","money","bank","sell","market","trade","金币","经济"]),
           ("chat",["chat","broadcast","announce","message","聊天","公告","喇叭"]),
           ("world",["world","spawn","portal","teleport","warp","land","plot","region","世界","传送","地皮","领地","出生"]),
           ("admin",["ban","kick","op ","permission","command","admin","封禁","权限","管理"]),
           ("gameplay",["pvp","pve","mob","crate","minigame","game","僵尸","游戏","战"]),
           ("protection",["protect","lock","chest","cheat","guard","保护","防","锁"]),
           ("player",["login","auth","register","marry","skin","称号","登录","注册","结婚"]),
           ("library",["api","library","core","function","devtools","核心","api"]),
           ("cosmetic",["particle","effect","cape","hat","boss","粒子","特效"])]
    for tag,kws in rules:
        if any(k in s for k in kws): t.append(tag)
    if not t: t=["gameplay"]
    return t[:4]

def status_for(ver):
    v=str(ver).lower()
    if any(k in v for k in ("alpha","dev","snapshot")): return "alpha"
    if any(k in v for k in ("beta","preview","unstable","rc")): return "beta"
    return "stable"

def isodate(ts):
    return datetime.datetime.fromtimestamp(ts).astimezone().replace(microsecond=0).isoformat()

def extract_icon(rec, dest):
    src=rec.get("source_file"); ent=None
    # find icon entry recorded
    for r in [rec]:
        pass
    try:
        if rec["ext"]=="phar":
            ent=icon_entry_cache.get(src)
            if not ent: return False
            php=f'$p=new Phar($argv[1]); if(isset($p[$argv[2]])) file_put_contents($argv[3],$p[$argv[2]]->getContent());'
            subprocess.run(["php","-r",php,src,ent,dest],check=True)
            return os.path.exists(dest)
        else:
            subprocess.run(["unzip","-p",src,"icon.png"],stdout=open(dest,"wb"),stderr=subprocess.DEVNULL)
            return os.path.getsize(dest)>0
    except Exception as e:
        print("icon fail",src,e); return False

def mc_range(mc, allmcs):
    ku=sorted(set(vkey(x) for x in allmcs if x!="unknown"))
    if not ku: return None
    lo=".".join(map(str,ku[0])); top=ku[-1]
    return f">={lo} <{top[0]}.{top[1]+1}.0"

ST_CN={"pocketmine-mp":"PocketMine-MP","nukkit":"Nukkit","powernukkitx":"PowerNukkitX",
       "cloudburst":"Cloudburst","bds":"BDS 官方基岩服务端","levilamina":"LeviLamina",
       "liteloader-bds":"LiteLoaderBDS","endstone":"Endstone","allay":"Allay",
       "dragonfly":"Dragonfly","other":"其它服务端","unknown":"未知服务端"}
TAG_CN={"economy":"经济/商店","chat":"聊天/公告","world":"世界/传送","admin":"管理/权限",
        "gameplay":"玩法","protection":"保护/防作弊","player":"玩家/登录",
        "library":"前置/API 库","cosmetic":"特效/粒子"}

def write_plugin_readme(pdir,plugin,st,mc):
    st_cn=ST_CN.get(st,st)
    tags_cn="、".join(TAG_CN.get(t,t) for t in plugin["tags"])
    cmds=plugin.get("commands") or []
    perms=plugin.get("permissions") or []
    authors=", ".join(plugin["author"])
    desc=(plugin.get("description") or "").strip()
    L=[]
    L.append(f"# {plugin['name']}({plugin['display_name']})\n")
    L.append("## 功能简介\n")
    L.append(f"**{plugin['display_name']}({plugin['name']})** 是一款运行于 **{st_cn}** 的 Minecraft 基岩版插件,"
             f"插件版本 `{plugin['plugin_version']}`,作者 {authors}。")
    if tags_cn:
        L.append(f"主要功能方向:{tags_cn}。")
    if desc and "Minecraft Bedrock plugin for" not in desc:
        L.append(f"原插件说明:{desc}")
    if cmds:
        L.append(f"本插件共提供 **{len(cmds)}** 条命令(见下表)。")
    else:
        L.append("本插件未在 plugin.yml 中声明命令,可能通过 GUI / 物品 / 事件触发。")
    if perms:
        L.append(f"共定义 **{len(perms)}** 个权限节点(见下表,可用于判断插件能力)。")
    L.append("")
    if cmds:
        L.append("## 命令列表\n")
        L.append("| 命令 | 说明 | 用法 | 权限 | 别名 |")
        L.append("|------|------|------|------|------|")
        for c in cmds:
            L.append("| `/{}` | {} | `{}` | {} | {} |".format(
                c.get("name",""), c.get("description") or "-",
                c.get("usage") or ("/"+c.get("name","")), c.get("permission") or "-",
                ", ".join(c.get("aliases") or []) or "-"))
        L.append("")
    L.append("## 权限节点\n")
    L.append("| 权限 | 说明 | 默认 |")
    L.append("|------|------|------|")
    for pc in perms:
        L.append(f"| `{pc.get('name','')}` | {pc.get('description') or '-'} | {pc.get('default') or '-'} |")
    L.append("")
    L.append("## 如何使用\n")
    L.append(f"1. 下载下方插件文件 `{plugin['files'][0]['file_name']}`。")
    L.append(f"2. 放入服务器 `plugins/` 目录({st_cn})。")
    L.append("3. 重启或重载服务器,插件会自动加载。")
    if cmds:
        L.append("4. 在游戏内输入上表命令(控制台可省略 `/`)。")
    L.append("")
    L.append("## 元数据\n")
    L.append(f"- **id**: `{plugin['id']}`")
    L.append(f"- **edition**: {plugin['edition']}")
    L.append(f"- **server_type**: `{st}`")
    L.append(f"- **minecraft_version**: `{mc}` (推断来源: {plugin.get('minecraft_version_source')})")
    L.append(f"- **minecraft_versions**: {', '.join(plugin['minecraft_versions'])}")
    L.append(f"- **plugin_version**: `{plugin['plugin_version']}`")
    L.append(f"- **author**: {authors}")
    if plugin.get("dependencies"):
        L.append(f"- **dependencies**: {', '.join(plugin['dependencies'])}")
    if plugin.get("soft_dependencies"):
        L.append(f"- **softdependencies**: {', '.join(plugin['soft_dependencies'])}")
    if plugin.get("main"):
        L.append(f"- **main**: `{plugin['main']}`")
    if plugin.get("website"):
        L.append(f"- **website**: {plugin['website']}")
    L.append(f"- **license**: {plugin['license']} ({plugin['license_status']})")
    L.append(f"- **tags**: {', '.join(plugin['tags'])}\n")
    L.append("## 下载\n")
    for f in plugin["files"]:
        L.append(f"- `{f['file_name']}`(**{f['size']}** 字节,sha256 `{f['sha256']}`)")
        L.append("  - github: `" + MIRRORS["github"] + f['download_paths']['github'] + "`")
    if plugin.get("history"):
        L.append("\n## 历史版本\n")
        for v,fs in plugin["history"].items():
            L.append(f"- {v}: " + ", ".join(x["file_name"] for x in fs))
    L.append("\n---\n本文件由生成脚本自动产出;机器可读字段见 `plugin.json`。")
    open(os.path.join(pdir,"README.md"),"w",encoding="utf-8").write("\n".join(L)+"\n")

def write_changelog(pdir,plugin):
    L=[f"# Changelog - {plugin['name']}\n",
       f"## {plugin['plugin_version']} (current)\n",
       f"- indexed from original pack; file `{plugin['files'][0]['file_name']}`\n"]
    for v,fs in (plugin.get("history") or {}).items():
        L.append(f"## {v}\n- archived: {', '.join(x['file_name'] for x in fs)}\n")
    L.append("\n_Changelog entries are derived from bundled version files, not release notes._")
    open(os.path.join(pdir,"CHANGELOG.md"),"w",encoding="utf-8").write("\n".join(L)+"\n")

# ---- load ----
groups=json.load(open(os.path.join(BUILD,"groups.json")))
side=json.load(open(os.path.join(BUILD,"sidecars.json")))
# icon entries by source path
icon_entry_cache={}
for l in open(os.path.join(BUILD,"metadata.jsonl"),encoding="utf-8"):
    l=l.strip()
    if not l: continue
    o=json.loads(l)
    if o.get("icon_entry"): icon_entry_cache[o["path"]]=o["icon_entry"]

# global per-plugin metadata (all mc versions / server versions)
name_meta=collections.defaultdict(lambda: {"mc":set(),"sv":collections.defaultdict(set)})
for k,vers in groups.items():
    st,mc,pid=k.split("\x01")
    name_meta[pid]["mc"].add(mc)
    for ver,recs in vers.items():
        for r in recs:
            if r.get("api"): name_meta[pid]["sv"][st].add(r["api"].split(',')[0])

if os.path.isdir(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)
os.makedirs(os.path.join(OUT,"schemas"))
for d in ["by-server-type","by-minecraft-version","by-server-version","by-tag"]:
    os.makedirs(os.path.join(OUT,"index",d))
os.makedirs(os.path.join(OUT,"_unknown")); os.makedirs(os.path.join(OUT,"_unsupported"))

catalog_plugins=[]
used_ids=set()
extract_icon_budget=0

for key,vers in sorted(groups.items()):
    st,mc,pid=key.split("\x01")
    # unique files per version by sha
    uniq={}  # ver -> list unique rec
    for ver,recs in vers.items():
        seen={}
        for r in recs:
            seen.setdefault(r["sha256"], r)
        uniq[ver]=list(seen.values())
    latest=max(uniq.keys(), key=vkey)
    cur=uniq[latest]
    # variants if multiple distinct current files
    variants=[ (pid, cur[0]) ] if len(cur)==1 else [ (pid + ("" if i==0 else f"-v{i+1}"), r) for i,r in enumerate(cur) ]
    # global version info
    allmc=sorted(name_meta[pid]["mc"] & {mc} | set(), key=vkey)
    plug_mcs=sorted(name_meta[pid]["mc"], key=vkey)
    plug_mcs=[m for m in plug_mcs if m!="unknown"] or plug_mcs
    svmap={s: sorted(v, key=vkey)[0] for s,v in name_meta[pid]["sv"].items() if v}
    for vid, prim in variants:
        oid=vid
        n=2
        while (st,mc,oid) in used_ids:
            oid=f"{vid}-{n}"; n+=1
        if (st,mc,oid)==("pocketmine-mp","1.2.0","pocketguard"):
            oid="pocketguard-lock"  # fresh path: reset Gitee cached moderation verdict
        used_ids.add((st,mc,oid))
        pdir=os.path.join(OUT,"plugins",st,mc,oid)
        os.makedirs(pdir,exist_ok=True)
        # current file
        ext=prim["ext"]
        fname=f"{safe(prim['name'])}-{safe(prim['version'])}.{ext}"
        with open(prim["source_file"],"rb") as fi, open(os.path.join(pdir,fname),"wb") as fo:
            shutil.copyfileobj(fi,fo)
        relfile=f"plugins/{st}/{mc}/{oid}/{fname}"
        files=[{"path":relfile,"file_name":fname,"sha256":prim["sha256"],"size":prim["size"],
                "download_paths":{k:relfile for k in MIRRORS}}]
        # history (all versions older than latest, from other variants only variant0 gets history)
        history={}
        if vid==pid or oid==pid:
            for ver in sorted(uniq.keys(), key=vkey):
                if ver==latest: continue
                for r in uniq[ver]:
                    hv=os.path.join(pdir,"history",safe(ver)); os.makedirs(hv,exist_ok=True)
                    hfn=f"{safe(r['name'])}-{safe(ver)}.{r['ext']}"
                    shutil.copyfile(r["source_file"], os.path.join(hv,hfn))
                    history.setdefault(ver,[]).append({"file_name":hfn,"sha256":r["sha256"],"size":r["size"]})
        # icon
        icon=None
        icon_dest=os.path.join(pdir,"icon.png")
        if extract_icon_budget<200 and extract_icon(prim,icon_dest):
            icon="icon.png"
        # license: look for nearby license file
        lic=None
        srcdir=os.path.dirname(prim["source_file"])
        for cand in ("LICENSE","LICENSE.txt","LICENSE.md","COPYING","COPYING.txt","license"):
            p=os.path.join(srcdir,cand)
            if os.path.isfile(p):
                shutil.copyfile(p, os.path.join(pdir,"LICENSE")); lic="MIT"; break
        license_status="declared" if lic else "unknown"
        # description
        desc=prim.get("desc") or f"{prim['name']} - Minecraft Bedrock plugin for {st}."
        if isinstance(desc,list): desc=" ".join(map(str,desc))
        dep=prim.get("depend") or []
        if isinstance(dep,str): dep=[dep]
        soft=prim.get("softdepend") or []
        if isinstance(soft,str): soft=[soft]
        web=prim.get("website")
        if web and isinstance(web,str) and re.search(r'github|gitlab|gitcode', web, re.I):
            web=None  # Gitee-only: drop external code-host links
        FIXA={"MinecrafterJPN":"MinecrafterJPN（原作者）"}
        auth=[FIXA.get(a,a) for a in (prim.get("authors") or [])] or ["unknown"]
        plugin={
          "schema_version":1,"id":oid,"name":prim["name"],
          "display_name":("密码箱类插件" if oid=="pocketguard-lock" else (prim.get("display_name") or prim["name"])),
          "edition":"bedrock","server_type":st,"server_types":[st],
          "minecraft_version":mc,"minecraft_versions":plug_mcs,
          "minecraft_version_range":mc_range(mc,plug_mcs),
          "mycraft_version_source":prim.get("mc_src"),
          "server_versions":({s:f">={v}" for s,v in svmap.items()} or {st:">=1.0.0"}),
          "server_version_source":"plugin.yml api",
          "plugin_version":prim["version"],"author":auth,
          "license":lic or "NOASSERTION","license_status":license_status,
          "description":desc,"website":web,"main":prim.get("main"),
          "tags":tags_for(prim["name"],desc,st),
          "dependencies":dep,"soft_dependencies":soft,"conflicts":[],
          "commands":prim.get("commands") or [],"permissions":prim.get("permissions") or [],"files":files,
          "history":history or None,
          "readme":"README.md","changelog":"CHANGELOG.md","icon":icon,
          "status":status_for(prim["version"]),
          "source":{"archive_layout":"pack","original_relative_path":prim["source_path"]},
          "mirror_base":MIRRORS["github"],
          "updated_at":isodate(prim["mtime"]),
        }
        plugin["minecraft_version_source"]=plugin.pop("mycraft_version_source")
        with open(os.path.join(pdir,"plugin.json"),"w",encoding="utf-8") as f:
            json.dump(plugin,f,ensure_ascii=False,indent=2)
        write_plugin_readme(pdir,plugin,st,mc)
        write_changelog(pdir,plugin)
        if not lic:
            with open(os.path.join(pdir,"LICENSE"),"w",encoding="utf-8") as f:
                f.write("NO LICENSE FILE WAS BUNDLED WITH THIS PLUGIN.\n\n"
                        "The original distribution did not include a license file. "
                        "Rights remain with the original author(s). Redistributed here "
                        "for archival/indexing purposes only. If you are the author and "
                        "want it removed or licensed differently, open an issue.\n")
        catalog_plugins.append({
            "id":oid,"name":prim["name"],"display_name":plugin["display_name"],
            "edition":"bedrock","server_type":st,"minecraft_version":mc,
            "plugin_version":prim["version"],"path":f"plugins/{st}/{mc}/{oid}/plugin.json",
            "file":relfile,"sha256":prim["sha256"],"size":prim["size"],
            "tags":plugin["tags"],"status":plugin["status"],
            "server_versions":plugin["server_versions"],
        })

print("materialized plugin folders:",len(catalog_plugins))

# ---------- catalog / api ----------
SERVER_TYPES=["pocketmine-mp","nukkit","powernukkitx","cloudburst","bds","levilamina",
              "liteloader-bds","endstone","allay","dragonfly","other","unknown"]
cat={"schema_version":1,"generated_at":NOW,"mirrors":MIRRORS,
     "plugin_count":len(catalog_plugins),"server_types":SERVER_TYPES,
     "plugins":catalog_plugins}
json.dump(cat,open(os.path.join(OUT,"catalog.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
api={"version":1,"generated_at":NOW,"catalog":"catalog.json","latest":"index/latest.json",
     "schemas":{"plugin":"schemas/plugin.schema.json","catalog":"schemas/catalog.schema.json"},
     "indexes":{"by_server_type":"index/by-server-type/","by_minecraft_version":"index/by-minecraft-version/",
                "by_server_version":"index/by-server-version/","by_tag":"index/by-tag/"},
     "mirrors":MIRRORS,
     "license":"AGPL-3.0-only","license_file":"LICENSE",
     "license_scope":"Repository metadata, schemas, docs, index files and generator scripts are AGPL-3.0. Bundled plugin binaries keep their original licenses.",
     "usage":{
        "all_plugins":"read catalog.json -> plugins[]",
        "latest":"read index/latest.json",
        "filter":"pick an index under index/ by server_type, minecraft_version, server_version or tag",
        "download":"prepend mirrors.<platform> to any plugins[].file relative path",
        "verify":"compare sha256 of the downloaded file with plugins[].sha256"}}
json.dump(api,open(os.path.join(OUT,"api.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)

def entry(p):
    return {"id":p["id"],"name":p["name"],"display_name":p.get("display_name"),
            "server_type":p["server_type"],"minecraft_version":p["minecraft_version"],
            "plugin_version":p["plugin_version"],"path":p["path"],"file":p["file"],
            "sha256":p["sha256"],"size":p["size"],"tags":p["tags"],
            "download_paths":{k:p["file"] for k in MIRRORS}}
def wr(path,obj):
    os.makedirs(os.path.dirname(path),exist_ok=True)
    json.dump(obj,open(path,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

# indexes
by_st=collections.defaultdict(list); by_mc=collections.defaultdict(list)
by_stmc=collections.defaultdict(list); by_sv=collections.defaultdict(list)
by_tag=collections.defaultdict(list)
for p in catalog_plugins:
    e=entry(p)
    by_st[p["server_type"]].append(e)
    by_mc[p["minecraft_version"]].append(e)
    by_stmc[(p["server_type"],p["minecraft_version"])].append(e)
    for st,sv in (p.get("server_versions") or {}).items():
        tok=sv.replace(">=","").strip()
        by_sv[(st,tok)].append(e)
    for t in p["tags"]:
        by_tag[t].append(e)

for st,lst in by_st.items():
    wr(os.path.join(OUT,"index/by-server-type",safe(st)+".json"),
       {"schema_version":1,"generated_at":NOW,"index":"by-server-type","server_type":st,"count":len(lst),"plugins":lst})
for mc,lst in by_mc.items():
    wr(os.path.join(OUT,"index/by-minecraft-version",safe(mc)+".json"),
       {"schema_version":1,"generated_at":NOW,"index":"by-minecraft-version","minecraft_version":mc,"count":len(lst),"plugins":lst})
for (st,mc),lst in by_stmc.items():
    wr(os.path.join(OUT,"index/by-server-type",safe(st),safe(mc)+".json"),
       {"schema_version":1,"generated_at":NOW,"index":"by-server-type/version","server_type":st,"minecraft_version":mc,"count":len(lst),"plugins":lst})
for (st,sv),lst in by_sv.items():
    wr(os.path.join(OUT,"index/by-server-version",safe(st),safe(sv)+".json"),
       {"schema_version":1,"generated_at":NOW,"index":"by-server-version","server_type":st,"server_version":sv,"count":len(lst),"plugins":lst})
for t,lst in by_tag.items():
    wr(os.path.join(OUT,"index/by-tag",safe(t)+".json"),
       {"schema_version":1,"generated_at":NOW,"index":"by-tag","tag":t,"count":len(lst),"plugins":lst})

# latest.json (dedupe by name -> highest version)
latest={}
for p in catalog_plugins:
    k=(p["name"],p["server_type"])
    if k not in latest or vkey(p["plugin_version"])>vkey(latest[k]["plugin_version"]):
        latest[k]=p
wr(os.path.join(OUT,"index/latest.json"),
   {"schema_version":1,"generated_at":NOW,"index":"latest","count":len(latest),
    "plugins":[entry(p) for p in latest.values()]})

# ---------- schemas ----------
plugin_schema={
 "$schema":"http://json-schema.org/draft-07/schema#","title":"Bedrock Plugin","type":"object",
 "required":["schema_version","id","name","edition","server_type","minecraft_version",
             "plugin_version","files"],
 "properties":{
  "schema_version":{"type":"integer","const":1},
  "id":{"type":"string","pattern":"^[a-z0-9][a-z0-9-]*$"},
  "name":{"type":"string"},"display_name":{"type":"string"},
  "edition":{"type":"string","enum":["bedrock"]},
  "server_type":{"type":"string","enum":SERVER_TYPES},
  "server_types":{"type":"array","items":{"type":"string","enum":SERVER_TYPES}},
  "minecraft_version":{"type":"string"},
  "minecraft_versions":{"type":"array","items":{"type":"string"}},
  "minecraft_version_range":{"type":["string","null"]},
  "server_versions":{"type":"object","additionalProperties":{"type":"string"}},
  "plugin_version":{"type":"string"},
  "author":{"type":"array","items":{"type":"string"}},
  "license":{"type":"string"},"description":{"type":"string"},
  "tags":{"type":"array","items":{"type":"string"}},
  "dependencies":{"type":"array"},"conflicts":{"type":"array"},
  "commands":{"type":"array","items":{"type":"object","properties":{"name":{"type":"string"},
     "description":{"type":"string"},"usage":{"type":"string"},"permission":{"type":"string"},
     "aliases":{"type":"array","items":{"type":"string"}}}}},
  "permissions":{"type":"array","items":{"type":"object","properties":{"name":{"type":"string"},
     "description":{"type":"string"},"default":{"type":"string"}}}},
  "website":{"type":["string","null"]},"main":{"type":["string","null"]},
  "soft_dependencies":{"type":"array","items":{"type":"string"}},
  "files":{"type":"array","minItems":1,"items":{
     "type":"object","required":["path","file_name","sha256","size","download_paths"],
     "properties":{"path":{"type":"string"},"file_name":{"type":"string"},
        "sha256":{"type":"string","pattern":"^[0-9a-f]{64}$"},"size":{"type":"integer"},
        "download_paths":{"type":"object","required":["github"]}}}},
  "status":{"type":"string","enum":["stable","beta","alpha","deprecated","unknown"]},
  "updated_at":{"type":"string"}}
}
json.dump(plugin_schema,open(os.path.join(OUT,"schemas/plugin.schema.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
catalog_schema={
 "$schema":"http://json-schema.org/draft-07/schema#","title":"Catalog","type":"object",
 "required":["schema_version","generated_at","mirrors","plugin_count","plugins"],
 "properties":{
   "schema_version":{"type":"integer"},"generated_at":{"type":"string"},
   "mirrors":{"type":"object","required":["github"]},
   "plugin_count":{"type":"integer"},
   "plugins":{"type":"array","items":{
      "type":"object","required":["id","name","server_type","minecraft_version","plugin_version","path","file","sha256"],
      "properties":{"id":{"type":"string"},"name":{"type":"string"},
        "server_type":{"type":"string","enum":SERVER_TYPES},"minecraft_version":{"type":"string"},
        "plugin_version":{"type":"string"},"path":{"type":"string"},"file":{"type":"string"},
        "sha256":{"type":"string","pattern":"^[0-9a-f]{64}$"}}}}}}
json.dump(catalog_schema,open(os.path.join(OUT,"schemas/catalog.schema.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)

# ---------- sidecars: copy unsupported cores + unknown ----------
src_used={r["source_file"] for vers in groups.values() for recs in vers.values() for r in recs}
# Copy only small unsupported files; large server cores -> manifest only (mirror size limits).
LIMIT=256*1024
man=[]
for rec in side["unsupported"]:
    p=rec.get("source_file") or os.path.join(SRC,rec["source_path"])
    copied=False
    if os.path.exists(p) and rec["size"]<=LIMIT:
        dest=os.path.join(OUT,"_unsupported",rec["source_path"])
        os.makedirs(os.path.dirname(dest),exist_ok=True); shutil.copyfile(p,dest); copied=True
    man.append({"path":rec["source_path"],"category":rec["category"],
                "size":rec["size"],"sha256":rec["sha256"],"copied":copied})
json.dump(man,open(os.path.join(OUT,"_unsupported","MANIFEST.json"),"w"),ensure_ascii=False,indent=2)
for rec in side["unknown"]:
    p=rec.get("source_file") or os.path.join(SRC,rec["source_path"])
    if not os.path.exists(p): continue
    dest=os.path.join(OUT,"_unknown",rec["source_path"])
    os.makedirs(os.path.dirname(dest),exist_ok=True); shutil.copyfile(p,dest)

# ---------- resource manifest (not copied, to save space) ----------
CAT_RULES=[("map",r'\.(mca|mcr|ldb|dat|dat_old|dat_mcr)$|\bregion\b|\bdb\b'),
           ("server-core",r'核心|core|\.phar$|\.jar$'),
           ("audio",r'\.(nbs|mp3|ogg|wav)$'),
           ("image",r'\.(png|jpg|jpeg|gif)$'),
           ("app",r'\.(apk|exe|bin)$'),
           ("document",r'\.(txt|md|html|css|log|xml|csv|ini|conf|cfg|properties|old|pmf)$'),
           ("source",r'\.php$'),
           ("archive",r'\.(zip|rar)$'),
           ("data",r'\.(json|yml|yaml|lock|hyperlife|dwdat)$')]
res=collections.Counter(); res_bytes=collections.Counter()
for root,_,files in os.walk(SRC):
    for fn in files:
        fp=os.path.join(root,fn)
        if fp in src_used: continue
        low=fn.lower(); cat="other"
        for name,pat in CAT_RULES:
            if re.search(pat,low): cat=name; break
        res[cat]+=1; res_bytes[cat]+=os.path.getsize(fp)
json.dump({k:{"count":res[k],"bytes":res_bytes[k]} for k in res},
          open(os.path.join(OUT,"_unsupported/resource-manifest.json"),"w"),ensure_ascii=False,indent=2)

# ---------- markdown reports ----------
with open(os.path.join(BUILD,'summary.pkl2'),'w') as f: pass
import pickle
pickle.dump({"catalog_plugins":catalog_plugins,"side":side,"res":dict(res),
             "res_bytes":dict(res_bytes),"src_used":list(src_used)},open(os.path.join(BUILD,'stage2data.pkl'),'wb'))
print("catalog written; unsupported",len(side["unsupported"]),"unknown",len(side["unknown"]))

