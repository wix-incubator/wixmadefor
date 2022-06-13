# Add nameid 25 to variable fonts

import os
from pathlib import Path
from fontTools.ttLib.woff2 import main as woff2_main


def add_nameid25(font_path, string: str):
    from fontTools.ttLib import TTFont
    from fontTools.ttLib.tables._n_a_m_e import makeName

    f = TTFont(font_path)
    f["name"].setName(string, 25, 3, 1, 0x409)
    f.save(font_path)

fonts_path = Path(os.path.dirname(__file__)) / "../fonts/variable"

for vf in os.listdir(fonts_path):
    font_path = fonts_path / vf
    if "Display" in vf:
        add_nameid25, (vf, "WixMadeforDisplay"),
    else:
        add_nameid25, (vf, "WixMadeforText")