"""C1319: scrub the WSQ layer from the LG Markdown mirror and the labs (code, version, K/A criteria, minutes, assessment, URL)."""
import json, re, sys, pathlib
sys.path.insert(0, 'build'); from docxutil import OLD_C, NEW_C, OLD_URL, NEW_URL, LAB_MIN
OLD_MIN = {1: 75, 2: 90, 3: 120, 4: 90, 5: 90, 6: 135}

def sub_common(s):
    s = s.replace(OLD_URL, NEW_URL).replace(OLD_C, NEW_C)
    return re.sub(r'(LO\d) \| [KA0-9, |]*[KA]\d', r'\1', s)          # keep LO#, strip K#/A# criteria

lg = pathlib.Path("LG-Agentic AI for Affiliate Marketing (C1319).md")
s = sub_common(lg.read_text())
s = s.replace("**Version:** v2.0 (5 September 2026)", "**Version:** v1.0 (3 October 2026)")
s = s.replace("into prompts, screenshots or assessment evidence.", "into prompts, screenshots or lab evidence.")
s = re.sub(r"## Assessment preparation\n\n.*?\n\n(?=## )", "", s, flags=re.S)
labs = list(re.finditer(r"### Lab (\d):", s))
for m in reversed(labs):                                             # per-lab duration
    n = int(m.group(1)); seg = s[m.start():]
    seg = seg.replace(f"**Duration:** {OLD_MIN[n]} minutes", f"**Duration:** {LAB_MIN[n]} minutes", 1)
    s = s[:m.start()] + seg
lg.write_text(s)

r = pathlib.Path("labs/README.md"); s = sub_common(r.read_text())
for n in LAB_MIN: s = re.sub(rf"(\[Lab {n}:.*?)\({OLD_MIN[n]} minutes\)", rf"\1({LAB_MIN[n]} minutes)", s)
r.write_text(s)
for d in sorted(pathlib.Path("labs").glob("lab-0*")):
    n = int(d.name[5]); f = d / "README.md"; s = sub_common(f.read_text())
    s = s.replace(f"Duration: {OLD_MIN[n]} minutes", f"Duration: {LAB_MIN[n]} minutes")
    f.write_text(s)
m = pathlib.Path("labs/LAB-MANIFEST.json"); s = m.read_text()
s = re.sub(r'"criteria": "(LO\d) \|[^"]*"', r'"criteria": "\1"', s); json.loads(s); m.write_text(s)
print("ok")
