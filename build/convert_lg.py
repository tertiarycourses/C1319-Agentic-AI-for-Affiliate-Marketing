"""C1319 Learner Guide from the WSQ LG: strip assessment alignment/preparation, one-day overview, lab minutes, LO-only alignment."""
import re, sys
from docx import Document
sys.path.insert(0, 'build'); from docxutil import *
SRC = "source-built/LG-Agentic AI for Affiliate Marketing.docx"
OUT = "courseware/LG-Agentic AI for Affiliate Marketing.docx"
d = Document(SRC)
T = list(d.tables)
global_subs(d, [("This guide supports the 2-day, 16-hour WSQ course Agentic AI for Affiliate Marketing (TGS-2025060552).",
                 "This guide supports the one-day, 7.5-hour course Agentic AI for Affiliate Marketing (C1319).")])
version_table(T[0], "One-day edition: offer economics, research Skills, MCP-assisted partner research, campaign controls and reporting across six connected labs.")
drop_toc(d, "Assessment Alignment"); drop_toc(d, "Assessment Preparation")
assert drop_section(d, "Assessment Alignment", "Heading2", keep_tables=True) == 4
assert drop_section(d, "Assessment Preparation", "Heading1") == 3
n = 0
for t in T[1:]:
    rows = {r.cells[0].text: r for r in t.rows}
    if "Duration" in rows and "Alignment" in rows:
        n += 1
        set_cell(rows["Duration"].cells[1], f"{LAB_MIN[n]} minutes")
        set_cell(rows["Alignment"].cells[1], rows["Alignment"].cells[1].text.split(' |')[0])
assert n == 6
d.core_properties.title = "Agentic AI for Affiliate Marketing"
d.save(OUT); print("wrote", OUT)
