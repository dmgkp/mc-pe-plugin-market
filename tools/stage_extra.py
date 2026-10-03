#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
# -*- coding: utf-8 -*-
"""Stage plugin archives hidden inside .zip/.rar packs, then merge their metadata.

Produces, relative to this tools/ dir (or BUILD if set):
  zstage/ , rstage/        extracted .phar/.jar
  zmap.json , rmap.json    staged_abs_path -> "<original archive rel>!/<inner path>"
  metadata_all.jsonl       main metadata.jsonl + staged metadata

Usage:
  python3 tools/stage_extra.py
Env:
  SRC   source tree (default ~/工作目录/插件/宝藏)
  BUILD working dir (default parent of this script)
"""
import os, sys, json, zipfile, subprocess

HOME = os.path.expanduser("~")
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("SRC", os.path.join(HOME, "工作目录/插件/宝藏"))
BUILD = os.environ.get("BUILD", HERE)
EXT = (".phar", ".jar")

def extract_zip(z, out, relz, maps):
    with zipfile.ZipFile(z) as zf:
        for n in zf.namelist():
            if n.lower().endswith(EXT):
                dest = os.path.join(out, n)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                open(dest, "wb").write(zf.read(n))
                maps[dest] = relz + "!/" + n

def extract_rar(r, out, relr, maps):
    os.makedirs(out, exist_ok=True)
    subprocess.run(["7z", "x", "-y", "-o" + out, r],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for rt, _, fs in os.walk(out):
        for f in fs:
            if f.lower().endswith(EXT):
                p = os.path.join(rt, f)
                maps[p] = relr + "!/" + os.path.relpath(p, out)

def main():
    zstage = os.path.join(BUILD, "zstage"); rstage = os.path.join(BUILD, "rstage")
    os.makedirs(zstage, exist_ok=True); os.makedirs(rstage, exist_ok=True)
    zmap, rmap = {}, {}
    zi = ri = 0
    for root, _, files in os.walk(SRC):
        for f in files:
            p = os.path.join(root, f); low = f.lower()
            if low.endswith(".zip"):
                zi += 1
                try: extract_zip(p, os.path.join(zstage, f"{zi:03d}"), os.path.relpath(p, SRC), zmap)
                except Exception as e: print("zip fail", p, e)
            elif low.endswith(".rar"):
                ri += 1
                extract_rar(p, os.path.join(rstage, f"{ri:02d}"), os.path.relpath(p, SRC), rmap)
    json.dump(zmap, open(os.path.join(BUILD, "zmap.json"), "w"), ensure_ascii=False)
    json.dump(rmap, open(os.path.join(BUILD, "rmap.json"), "w"), ensure_ascii=False)
    print(f"staged zip={len(zmap)} rar={len(rmap)}")
    # metadata for staged archives
    staged = os.path.join(BUILD, "staged.txt")
    with open(staged, "w") as fh:
        for p in list(zmap) + list(rmap): fh.write(p + "\n")
    subprocess.run(["php", os.path.join(HERE, "extract.php"), staged],
                   stdout=open(os.path.join(BUILD, "staged_meta.jsonl"), "w"))
    with open(os.path.join(BUILD, "metadata_all.jsonl"), "w") as out:
        for name in ("metadata.jsonl", "staged_meta.jsonl"):
            p = os.path.join(BUILD, name)
            if os.path.exists(p): out.write(open(p, encoding="utf-8").read())
    print("wrote metadata_all.jsonl")

if __name__ == "__main__":
    main()
