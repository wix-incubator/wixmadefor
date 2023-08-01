from __future__ import annotations

import argparse
from pathlib import Path

import ufoLib2
import vttLib.transfer
from fontTools.ttLib import TTFont
import sys

parser = argparse.ArgumentParser()
parser.add_argument("ufo", type=Path)
args = parser.parse_args()
ufo_path: Path = args.ufo
vtt_data_path = ufo_path.parent / "vtt_data"
ttx_path_source = vtt_data_path / Path(ufo_path.stem).with_suffix(".ttx")
ttx_path_target = ufo_path.with_name(ufo_path.stem + "_VTT_Hinting").with_suffix(".ttx")

if ufo_path.name in (
    "WixMadeforText-SemiBold.ufo",
    "WixMadeforText-SemiBoldItalic.ufo",
    "WixMadeforDisplay-SemiBold.ufo",
    "WixMadeforDisplay-Medium.ufo",
):
    print("This UFO is currently unhinted. Skipping")
    sys.exit()

ufo = ufoLib2.Font.open(ufo_path)
production_names: dict[str, str] = ufo.lib["public.postscriptNames"]

ttx = TTFont()
ttx.importXML(ttx_path_source)

renamed_tsi1_programs = {
    production_names.get(k, k): v for k, v in ttx["TSI1"].glyphPrograms.items()
}
ttx["TSI1"].glyphPrograms = renamed_tsi1_programs
renamed_tsi3_programs = {
    production_names.get(k, k): v for k, v in ttx["TSI3"].glyphPrograms.items()
}
ttx["TSI3"].glyphPrograms = renamed_tsi3_programs
renamed_glyph_grouping = {
    production_names.get(k, k): v for k, v in ttx["TSI5"].glyphGrouping.items()
}
ttx["TSI5"].glyphGrouping = renamed_glyph_grouping

vttLib.transfer.dump_to_file(ttx, ttx_path_target)
