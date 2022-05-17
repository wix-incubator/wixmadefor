# We manually generate webfonts because the googlefonts
# builder process doesn't contain hints

import os
import shutil
from pathlib import Path
from fontTools.ttLib.woff2 import main as woff2_main

fonts_path = Path(os.path.dirname(__file__)) / "../fonts"
input_path = fonts_path / "ttf"
output_path = fonts_path / "webfonts"

if os.path.exists(output_path):
    shutil.rmtree(output_path)

os.mkdir(output_path)

for ttf in os.listdir(input_path):
    input_font = input_path / ttf
    output_font = output_path / ttf
    shutil.copyfile(input_font, output_font)
    woff2_main(['compress', str(output_font)])
    os.remove(output_font)
