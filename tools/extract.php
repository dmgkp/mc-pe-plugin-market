<?php
// SPDX-License-Identifier: AGPL-3.0-or-later
// Reads a list of archive paths (one per line) and emits one JSON object per line.
$list = file($argv[1], FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
foreach ($list as $f) {
    $out = ["path" => $f, "ok" => false, "kind" => null];
    $low = strtolower($f);
    try {
        if (substr($low, -5) === '.phar') {
            $out['kind'] = 'phar';
            $p = new Phar($f);
            $yml = null; $best = 999; $names = [];
            $ico = null;
            foreach (new RecursiveIteratorIterator($p) as $fi) {
                $rel = str_replace("phar://" . $f . "/", "", $fi->getPathname());
                $d = substr_count($rel, '/');
                if ($d == 0) $names[] = $rel;
                $b = strtolower(basename($rel));
                if (($b === 'plugin.yml' || $b === 'plugin.yaml') && $d < $best) { $best = $d; $yml = $fi->getContent(); }
                if ($b === 'icon.png' && $ico === null) $ico = $rel;
            }
            $out['plugin_yml'] = $yml;
            $out['icon_entry'] = $ico;
            $out['top_entries'] = array_slice($names, 0, 20);
            $out['entry_count'] = count($names);
        } else {
            $out['kind'] = 'zip';
            $z = new ZipArchive();
            if ($z->open($f) === true) {
                $yml = $z->getFromName('plugin.yml');
                if ($yml === false) $yml = $z->getFromName('plugin.yaml');
                if ($yml === false) $yml = $z->getFromName('nukkit.yml');
                $out['plugin_yml'] = ($yml === false) ? null : $yml;
                $mf = $z->getFromName('META-INF/MANIFEST.MF');
                $out['manifest'] = ($mf === false) ? null : trim($mf);
                $hasNukkit = false; $hasBukkit = false; $hasPmmp = false; $top = [];
                for ($i = 0; $i < $z->numFiles; $i++) {
                    $nm = $z->getNameIndex($i);
                    if (substr_count($nm, '/') === 0 && $nm !== '') $top[] = $nm;
                    if (strpos($nm, 'cn/nukkit/') === 0) $hasNukkit = true;
                    if (strpos($nm, 'org/bukkit/') === 0 || strpos($nm, 'net/minecraft/') === 0) $hasBukkit = true;
                    if (strpos($nm, 'pocketmine/') === 0) $hasPmmp = true;
                }
                $out['has_nukkit'] = $hasNukkit;
                $out['has_bukkit'] = $hasBukkit;
                $out['has_pmmp'] = $hasPmmp;
                $out['top_entries'] = array_slice($top, 0, 20);
                $z->close();
            } else {
                $out['error'] = 'zip open failed';
            }
        }
        $out['ok'] = true;
    } catch (Throwable $e) {
        $out['error'] = get_class($e) . ': ' . $e->getMessage();
    }
    echo json_encode($out, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_INVALID_UTF8_SUBSTITUTE) . "\n";
}
