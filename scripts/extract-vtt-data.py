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


if ufo_path.name in (
    "WixMadeforText-SemiBold.ufo",
    "WixMadeforText-SemiBoldItalic.ufo",
    "WixMadeforDisplay-SemiBold.ufo"
):
    print("SemiBold ufos are currently unhinted. Skipping")
    sys.exit()


ttx_path = ufo_path.with_name(ufo_path.stem + "_VTT_Hinting").with_suffix(".ttx")

ufo = ufoLib2.Font.open(ufo_path)
production_names: dict[str, str] = ufo.lib["public.postscriptNames"]
vttLib.transfer.copy_from_ufo_data_to_file(ufo, ttx_path)


ttx = TTFont()
ttx.importXML(ttx_path)

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

vttLib.transfer.dump_to_file(ttx, ttx_path)