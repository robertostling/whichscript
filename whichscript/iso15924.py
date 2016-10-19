"""Functions to parse ISO 15924-related files from the Unicode project

The most important thing here is the UNICODE_ISO and UNICODE_SCRIPT tables,
which are dict objects mapping integer code points to ISO 15924 codes and full
names, respectively.
"""

import re
import os
from collections import Counter, defaultdict

def _parse_variants():
    path = os.path.join(
            os.path.dirname(__file__), '..', 'data', 'Unihan_Variants.txt')
    re_variant = re.compile(r'U\+([0-9A-F]+)\t(\w+)\tU\+([0-9A-F]+)')
    simplified = defaultdict(set)
    traditional = defaultdict(set)
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            m = re_variant.match(line)
            if not m: continue
            variant = m.group(2)
            u = int(m.group(3), 16)
            w = int(m.group(1), 16)
            if variant == 'kSimplifiedVariant':
                simplified[w].add(u)
            elif variant == 'kTraditionalVariant':
                traditional[w].add(u)
    return traditional, simplified


def _parse_conversion():
    path = os.path.join(
            os.path.dirname(__file__), '..', 'data', 'PropertyValueAliases.txt')
    re_entry = re.compile(r'sc\s+;\s+([A-Z][a-z]{3})\s+;\s+(\w+)\s+')
    table = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            m = re_entry.match(line)
            if not m: continue
            table[m.group(2)] = m.group(1)
    return table

def _parse_data():
    path = os.path.join(
            os.path.dirname(__file__), '..', 'data', 'Scripts.txt')
    re_range = re.compile(r'([0-9A-F]+)(?:\.\.([0-9A-F]+))\s+;\s+(.+?)\s+#')
    point_script = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            m = re_range.match(line)
            if not m: continue
            if not m.group(2):
                point_script[int(m.group(1), 16)] = m.group(3)
            else:
                for x in range(int(m.group(1), 16), int(m.group(2), 16)+1):
                    point_script[x] = m.group(3)
    return point_script

def _parse_mappings():
    path = os.path.join(
            os.path.dirname(__file__), '..', 'data',
            'Unihan_OtherMappings.txt')
    re_mapping = re.compile(r'U\+([0-9A-F]+)\t(\w+)\t')
    hant = set()
    hans = set()
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            m = re_mapping.match(line)
            if not m: continue
            u = int(m.group(1), 16)
            std = m.group(2)
            if std  == 'kBigFive': hant.add(u)
            elif std == 'kMainlandTelegraph': hans.add(u)

    counts = Counter(tuple(hant) + tuple(hans))
    multiple = {u for u,n in counts.items() if n > 1}
    hant = hant - multiple
    hans = hans - multiple

    return hant, hans

def _add_disambiguation(table):
    hant, hans = _parse_mappings()
    for u in hant: table[u] = 'Hant'
    for u in hans: table[u] = 'Hans'


SCRIPT_TO_ISO = _parse_conversion()
UNICODE_SCRIPT = _parse_data()
UNICODE_ISO = {u:SCRIPT_TO_ISO[name] for u,name in UNICODE_SCRIPT.items()}
UNICODE_TRADITIONAL, UNICODE_SIMPLIFIED = _parse_variants()

_add_disambiguation(UNICODE_ISO)

