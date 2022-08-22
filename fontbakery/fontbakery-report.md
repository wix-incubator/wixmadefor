## Fontbakery report

Fontbakery version: 0.8.8

<details><summary><b>[9] WixMadeforText-Italic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp">com.google.fonts/check/gasp</a>)</summary><div>


* ⚠ **WARN** The gasp table has a range of 8 that may be unneccessary. [code: non-ffff-range]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- commabelow
	- exclamdown.case 
	- And questiondown.case
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 
	- And Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* exclam (U+0021): X=32.0,Y=1.5 (should be at baseline 0?)
	* ampersand (U+0026): X=454.0,Y=714.0 (should be at cap-height 715?)
	* period (U+002E): X=30.0,Y=1.5 (should be at baseline 0?)
	* three (U+0033): X=156.5,Y=1.5 (should be at baseline 0?)
	* colon (U+003A): X=30.0,Y=1.5 (should be at baseline 0?)
	* question (U+003F): X=177.0,Y=1.5 (should be at baseline 0?)
	* Q (U+0051): X=485.0,Y=-1.0 (should be at baseline 0?)
	* i (U+0069): X=177.0,Y=714.5 (should be at cap-height 715?)
	* j (U+006A): X=175.5,Y=714.0 (should be at cap-height 715?)
	* braceleft (U+007B): X=171.0,Y=1.0 (should be at baseline 0?) and 16 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:
	* dollar (U+0024) contains a short segment B<<319.0,-6.0>-<316.0,-6.0>-<313.0,-6.0>>
	* asterisk (U+002A) contains a short segment B<<358.0,425.0>-<359.0,421.0>-<359.0,416.0>>
	* at (U+0040) contains a short segment B<<684.0,215.0>-<682.0,204.0>-<680.5,193.0>>
	* at (U+0040) contains a short segment B<<680.5,193.0>-<679.0,182.0>-<679.0,168.0>>
	* braceleft (U+007B) contains a short segment B<<137.0,209.0>-<139.0,216.0>-<140.0,222.5>>
	* braceleft (U+007B) contains a short segment B<<140.0,222.5>-<141.0,229.0>-<141.0,232.0>>
	* braceleft (U+007B) contains a short segment B<<168.0,-15.5>-<167.0,-23.0>-<167.0,-28.0>>
	* braceright (U+007D) contains a short segment B<<244.0,618.0>-<245.0,626.0>-<245.0,630.0>>
	* braceright (U+007D) contains a short segment B<<272.5,380.0>-<272.0,376.0>-<272.0,374.0>>
	* germandbls (U+00DF) contains a short segment L<<307.0,407.0>--<328.0,407.0>> and 4 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* nine (U+0039): B<<316.5,152.5>-<400.0,224.0>-<452.0,293.0>>/B<<452.0,293.0>-<394.0,245.0>-<312.0,245.0>> = 13.386785231777212 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[8] WixMadeforDisplay-ExtraBold.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp">com.google.fonts/check/gasp</a>)</summary><div>


* ⚠ **WARN** The gasp table has a range of 8 that may be unneccessary. [code: non-ffff-range]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Wix Madefor Display ExtraBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- hook
	- exclamdown.case
	- commabelow
	- uni031B.cap 
	- And questiondown.case
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 
	- And Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:
	* germandbls (U+00DF) contains a short segment L<<292.0,437.0>--<314.0,437.0>>
	* Euro (U+20AC) contains a short segment B<<79.0,336.0>-<79.0,347.0>-<79.0,358.0>>
	* Euro (U+20AC) contains a short segment B<<79.0,358.0>-<79.0,369.0>-<79.0,380.0>>
	* Euro (U+20AC) contains a short segment B<<241.0,380.0>-<240.0,369.0>-<240.0,358.0>>
	* Euro (U+20AC) contains a short segment B<<240.0,358.0>-<240.0,347.0>-<241.0,336.0>> and uni20BA (U+20BA) contains a short segment L<<627.0,318.0>--<627.0,308.0>> [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[10] WixMadeforText-ExtraBoldItalic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp">com.google.fonts/check/gasp</a>)</summary><div>


* ⚠ **WARN** The gasp table has a range of 8 that may be unneccessary. [code: non-ffff-range]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Wix Madefor Text ExtraBold' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- commabelow
	- exclamdown.case 
	- And questiondown.case
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 
	- And Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=457.0,Y=714.0 (should be at cap-height 715?)
	* asterisk (U+002A): X=276.0,Y=716.0 (should be at cap-height 715?)
	* S (U+0053): X=186.5,Y=1.5 (should be at baseline 0?)
	* y (U+0079): X=144.0,Y=1.0 (should be at baseline 0?)
	* braceleft (U+007B): X=257.0,Y=-2.0 (should be at baseline 0?)
	* braceleft (U+007B): X=301.0,Y=-2.0 (should be at baseline 0?)
	* braceright (U+007D): X=-15.0,Y=-2.0 (should be at baseline 0?)
	* braceright (U+007D): X=29.0,Y=-2.0 (should be at baseline 0?)
	* questiondown (U+00BF): X=412.0,Y=1.0 (should be at baseline 0?)
	* questiondown (U+00BF): X=412.0,Y=1.0 (should be at baseline 0?) and 50 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:
	* dollar (U+0024) contains a short segment B<<379.0,721.0>-<385.0,721.0>-<391.0,721.0>>
	* dollar (U+0024) contains a short segment B<<305.0,-6.0>-<302.0,-6.0>-<298.0,-6.0>>
	* at (U+0040) contains a short segment B<<683.0,245.0>-<682.0,238.0>-<680.5,229.0>>
	* at (U+0040) contains a short segment B<<680.5,229.0>-<679.0,220.0>-<679.0,212.0>>
	* at (U+0040) contains a short segment B<<679.0,212.0>-<679.0,196.0>-<686.5,183.5>>
	* at (U+0040) contains a short segment B<<686.5,183.5>-<694.0,171.0>-<713.0,171.0>>
	* m (U+006D) contains a short segment B<<661.0,301.0>-<663.0,313.0>-<664.0,321.5>>
	* m (U+006D) contains a short segment B<<664.0,321.5>-<665.0,330.0>-<665.0,336.0>>
	* m (U+006D) contains a short segment B<<367.0,301.0>-<369.0,313.0>-<370.0,321.5>>
	* m (U+006D) contains a short segment B<<370.0,321.5>-<371.0,330.0>-<371.0,336.0>> and 7 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni2079 (U+2079): B<<194.0,486.5>-<236.0,521.0>-<262.0,549.0>>/B<<262.0,549.0>-<242.0,536.0>-<212.0,536.0>> = 14.097228840864815 and uni2089 (U+2089): B<<89.0,-17.5>-<131.0,17.0>-<157.0,45.0>>/B<<157.0,45.0>-<137.0,32.0>-<107.0,32.0>> = 14.097228840864815 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[7] WixMadeforDisplay-Regular.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp">com.google.fonts/check/gasp</a>)</summary><div>


* ⚠ **WARN** The gasp table has a range of 8 that may be unneccessary. [code: non-ffff-range]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- hook
	- exclamdown.case
	- commabelow
	- uni031B.cap 
	- And questiondown.case
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 
	- And Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:
	* a (U+0061) contains a short segment L<<415.0,303.0>--<415.0,308.0>>
	* ordfeminine (U+00AA) contains a short segment L<<331.0,555.0>--<331.0,557.0>>
	* germandbls (U+00DF) contains a short segment L<<272.0,407.0>--<294.0,407.0>>
	* agrave (U+00E0) contains a short segment L<<415.0,303.0>--<415.0,308.0>>
	* aacute (U+00E1) contains a short segment L<<415.0,303.0>--<415.0,308.0>>
	* acircumflex (U+00E2) contains a short segment L<<415.0,303.0>--<415.0,308.0>>
	* atilde (U+00E3) contains a short segment L<<415.0,303.0>--<415.0,308.0>>
	* adieresis (U+00E4) contains a short segment L<<415.0,303.0>--<415.0,308.0>>
	* aring (U+00E5) contains a short segment L<<415.0,303.0>--<415.0,308.0>>
	* ae (U+00E6) contains a short segment L<<415.0,288.0>--<415.0,290.0>> and 20 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[8] WixMadeforText-BoldItalic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp">com.google.fonts/check/gasp</a>)</summary><div>


* ⚠ **WARN** The gasp table has a range of 8 that may be unneccessary. [code: non-ffff-range]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- commabelow
	- exclamdown.case 
	- And questiondown.case
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 
	- And Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* S (U+0053): X=191.5,Y=1.0 (should be at baseline 0?)
	* g (U+0067): X=219.0,Y=-2.0 (should be at baseline 0?)
	* dieresis (U+00A8): X=223.5,Y=716.5 (should be at cap-height 715?)
	* dieresis (U+00A8): X=440.5,Y=716.5 (should be at cap-height 715?)
	* micro (U+00B5): X=167.0,Y=-1.0 (should be at baseline 0?)
	* uni00B9 (U+00B9): X=260.0,Y=714.0 (should be at cap-height 715?)
	* adieresis (U+00E4): X=184.5,Y=716.5 (should be at cap-height 715?)
	* adieresis (U+00E4): X=401.5,Y=716.5 (should be at cap-height 715?)
	* aring (U+00E5): X=313.5,Y=714.5 (should be at cap-height 715?)
	* edieresis (U+00EB): X=216.5,Y=716.5 (should be at cap-height 715?) and 36 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:
	* dollar (U+0024) contains a short segment B<<388.0,721.0>-<392.0,721.0>-<396.0,721.0>>
	* dollar (U+0024) contains a short segment B<<310.0,-6.0>-<306.0,-6.0>-<303.0,-6.0>>
	* at (U+0040) contains a short segment B<<683.0,234.0>-<682.0,226.0>-<680.5,216.0>>
	* at (U+0040) contains a short segment B<<680.5,216.0>-<679.0,206.0>-<679.0,195.0>>
	* at (U+0040) contains a short segment B<<679.0,195.0>-<679.0,176.0>-<688.5,161.0>>
	* m (U+006D) contains a short segment B<<692.0,323.0>-<693.0,335.0>-<693.0,343.0>>
	* braceright (U+007D) contains a short segment B<<306.0,410.0>-<304.0,401.0>-<303.5,396.0>>
	* braceright (U+007D) contains a short segment B<<303.5,396.0>-<303.0,391.0>-<303.0,387.0>>
	* germandbls (U+00DF) contains a short segment L<<322.0,426.0>--<343.0,426.0>>
	* ae (U+00E6) contains a short segment L<<509.0,214.0>--<509.0,212.0>> and 4 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[8] WixMadeforText-Regular.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp">com.google.fonts/check/gasp</a>)</summary><div>


* ⚠ **WARN** The gasp table has a range of 8 that may be unneccessary. [code: non-ffff-range]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- hook
	- exclamdown.case
	- commabelow
	- uni031B.cap 
	- And questiondown.case
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 
	- And Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni031B (U+031B) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:
	* a (U+0061) contains a short segment L<<393.0,303.0>--<393.0,307.0>>
	* ordfeminine (U+00AA) contains a short segment L<<302.0,555.0>--<302.0,557.0>>
	* germandbls (U+00DF) contains a short segment L<<274.0,407.0>--<295.0,407.0>>
	* agrave (U+00E0) contains a short segment L<<393.0,303.0>--<393.0,307.0>>
	* aacute (U+00E1) contains a short segment L<<393.0,303.0>--<393.0,307.0>>
	* acircumflex (U+00E2) contains a short segment L<<393.0,303.0>--<393.0,307.0>>
	* atilde (U+00E3) contains a short segment L<<393.0,303.0>--<393.0,307.0>>
	* adieresis (U+00E4) contains a short segment L<<393.0,303.0>--<393.0,307.0>>
	* aring (U+00E5) contains a short segment L<<393.0,303.0>--<393.0,307.0>>
	* amacron (U+0101) contains a short segment L<<393.0,303.0>--<393.0,307.0>> and 24 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[10] WixMadeforText-Medium.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp">com.google.fonts/check/gasp</a>)</summary><div>


* ⚠ **WARN** The gasp table has a range of 8 that may be unneccessary. [code: non-ffff-range]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Wix Madefor Text Medium' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- hook
	- exclamdown.case
	- commabelow
	- uni031B.cap 
	- And questiondown.case
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 
	- And Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni031B (U+031B) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* exclam (U+0021): X=86.0,Y=713.5 (should be at cap-height 715?)
	* exclam (U+0021): X=168.5,Y=713.5 (should be at cap-height 715?)
	* Q (U+0051): X=520.0,Y=-0.5 (should be at baseline 0?)
	* y (U+0079): X=230.0,Y=-2.0 (should be at baseline 0?)
	* registered (U+00AE): X=262.0,Y=717.0 (should be at cap-height 715?)
	* germandbls (U+00DF): X=292.5,Y=-1.5 (should be at baseline 0?)
	* atilde (U+00E3): X=239.0,Y=717.0 (should be at cap-height 715?)
	* aring (U+00E5): X=298.5,Y=713.5 (should be at cap-height 715?)
	* aring (U+00E5): X=229.0,Y=713.5 (should be at cap-height 715?)
	* idieresis (U+00EF): X=166.5,Y=716.5 (should be at cap-height 715?) and 54 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:
	* germandbls (U+00DF) contains a short segment L<<280.0,415.0>--<301.0,415.0>>
	* uni20B4 (U+20B4) contains a short segment B<<339.0,327.0>-<336.0,325.0>-<333.0,322.5>>
	* uni20B4 (U+20B4) contains a short segment B<<333.0,322.5>-<330.0,320.0>-<327.0,318.0>> and uni20BA (U+20BA) contains a short segment L<<595.0,340.0>--<595.0,330.0>> [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[8] WixMadeforDisplay-Bold.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp">com.google.fonts/check/gasp</a>)</summary><div>


* ⚠ **WARN** The gasp table has a range of 8 that may be unneccessary. [code: non-ffff-range]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- hook
	- exclamdown.case
	- commabelow
	- uni031B.cap 
	- And questiondown.case
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 
	- And Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* Q (U+0051): X=542.0,Y=-1.5 (should be at baseline 0?)
	* g (U+0067): X=292.0,Y=-2.0 (should be at baseline 0?)
	* r (U+0072): X=291.5,Y=502.0 (should be at x-height 503?)
	* y (U+0079): X=232.0,Y=-1.0 (should be at baseline 0?)
	* micro (U+00B5): X=219.0,Y=-1.0 (should be at baseline 0?)
	* cedilla (U+00B8): X=203.5,Y=-250.5 (should be at descender -252?)
	* uni00B9 (U+00B9): X=172.0,Y=714.0 (should be at cap-height 715?)
	* germandbls (U+00DF): X=296.5,Y=-2.0 (should be at baseline 0?)
	* aring (U+00E5): X=318.5,Y=716.0 (should be at cap-height 715?)
	* aring (U+00E5): X=247.5,Y=716.0 (should be at cap-height 715?) and 59 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:
	* germandbls (U+00DF) contains a short segment L<<285.0,425.0>--<307.0,425.0>>
	* uni20B4 (U+20B4) contains a short segment B<<380.0,330.0>-<378.0,328.0>-<376.0,327.0>> and uni20BA (U+20BA) contains a short segment L<<627.0,330.0>--<627.0,320.0>> [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[9] WixMadeforText-Bold.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp">com.google.fonts/check/gasp</a>)</summary><div>


* ⚠ **WARN** The gasp table has a range of 8 that may be unneccessary. [code: non-ffff-range]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- hook
	- exclamdown.case
	- commabelow
	- uni031B.cap 
	- And questiondown.case
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 
	- And Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni031B (U+031B) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* g (U+0067): X=281.0,Y=-2.0 (should be at baseline 0?)
	* r (U+0072): X=298.5,Y=502.5 (should be at x-height 503?)
	* y (U+0079): X=227.0,Y=-1.0 (should be at baseline 0?)
	* cedilla (U+00B8): X=212.5,Y=-250.5 (should be at descender -252?)
	* uni00B9 (U+00B9): X=164.0,Y=714.0 (should be at cap-height 715?)
	* Oslash (U+00D8): X=530.5,Y=713.0 (should be at cap-height 715?)
	* Oslash (U+00D8): X=297.5,Y=2.0 (should be at baseline 0?)
	* aring (U+00E5): X=314.5,Y=716.0 (should be at cap-height 715?)
	* aring (U+00E5): X=245.5,Y=716.0 (should be at cap-height 715?)
	* ccedilla (U+00E7): X=222.5,Y=-250.5 (should be at descender -252?) and 45 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:
	* germandbls (U+00DF) contains a short segment L<<290.0,426.0>--<311.0,426.0>> and uni20BA (U+20BA) contains a short segment L<<595.0,329.0>--<595.0,319.0>> [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[9] WixMadeforText-MediumItalic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp">com.google.fonts/check/gasp</a>)</summary><div>


* ⚠ **WARN** The gasp table has a range of 8 that may be unneccessary. [code: non-ffff-range]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Wix Madefor Text Medium' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- commabelow
	- exclamdown.case 
	- And questiondown.case
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 
	- And Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* exclam (U+0021): X=179.0,Y=716.0 (should be at cap-height 715?)
	* ampersand (U+0026): X=461.0,Y=713.0 (should be at cap-height 715?)
	* Q (U+0051): X=707.0,Y=2.0 (should be at baseline 0?)
	* Q (U+0051): X=481.5,Y=-2.0 (should be at baseline 0?)
	* S (U+0053): X=194.0,Y=1.5 (should be at baseline 0?)
	* i (U+0069): X=172.5,Y=717.0 (should be at cap-height 715?)
	* j (U+006A): X=171.0,Y=717.0 (should be at cap-height 715?)
	* y (U+0079): X=165.0,Y=-1.0 (should be at baseline 0?)
	* dieresis (U+00A8): X=244.5,Y=714.0 (should be at cap-height 715?)
	* dieresis (U+00A8): X=443.5,Y=714.0 (should be at cap-height 715?) and 42 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:
	* dollar (U+0024) contains a short segment B<<398.0,721.0>-<400.0,721.0>-<403.0,721.0>>
	* dollar (U+0024) contains a short segment B<<315.0,-6.0>-<313.0,-6.0>-<310.0,-6.0>>
	* at (U+0040) contains a short segment B<<684.0,223.0>-<682.0,213.0>-<680.5,202.5>>
	* at (U+0040) contains a short segment B<<680.5,202.5>-<679.0,192.0>-<679.0,180.0>>
	* m (U+006D) contains a short segment B<<721.0,324.0>-<723.0,339.0>-<723.0,349.0>>
	* m (U+006D) contains a short segment B<<407.5,324.0>-<409.0,339.0>-<409.0,349.0>>
	* braceleft (U+007B) contains a short segment B<<125.0,203.0>-<127.0,210.0>-<128.0,216.5>>
	* braceleft (U+007B) contains a short segment B<<128.0,216.5>-<129.0,223.0>-<129.0,226.0>>
	* braceright (U+007D) contains a short segment B<<285.5,387.0>-<285.0,382.0>-<285.0,380.0>>
	* germandbls (U+00DF) contains a short segment L<<313.0,415.0>--<334.0,415.0>> and 5 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[10] WixMadeforText-ExtraBold.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp">com.google.fonts/check/gasp</a>)</summary><div>


* ⚠ **WARN** The gasp table has a range of 8 that may be unneccessary. [code: non-ffff-range]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Wix Madefor Text ExtraBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- hook
	- exclamdown.case
	- commabelow
	- uni031B.cap 
	- And questiondown.case
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: uogonek	Contours detected: 2	Expected: 1
	- Glyph name: Uogonek	Contours detected: 2	Expected: 1
	- Glyph name: aogonek	Contours detected: 3	Expected: 2
	- Glyph name: eogonek	Contours detected: 3	Expected: 2
	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 
	- And Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni031B (U+031B) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* asterisk (U+002A): X=177.5,Y=716.0 (should be at cap-height 715?)
	* asterisk (U+002A): X=256.5,Y=716.0 (should be at cap-height 715?)
	* d (U+0064): X=363.0,Y=508.0 (should be at x-height 510?)
	* r (U+0072): X=316.0,Y=511.0 (should be at x-height 510?)
	* y (U+0079): X=224.0,Y=-1.0 (should be at baseline 0?)
	* braceleft (U+007B): X=355.0,Y=-2.0 (should be at baseline 0?)
	* braceleft (U+007B): X=311.0,Y=-2.0 (should be at baseline 0?)
	* braceright (U+007D): X=39.0,Y=-2.0 (should be at baseline 0?)
	* braceright (U+007D): X=83.0,Y=-2.0 (should be at baseline 0?)
	* uni00B2 (U+00B2): X=198.5,Y=715.5 (should be at cap-height 715?) and 84 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:
	* germandbls (U+00DF) contains a short segment L<<297.0,437.0>--<318.0,437.0>>
	* Euro (U+20AC) contains a short segment B<<79.0,336.0>-<79.0,347.0>-<79.0,358.0>>
	* Euro (U+20AC) contains a short segment B<<79.0,358.0>-<79.0,369.0>-<79.0,380.0>>
	* Euro (U+20AC) contains a short segment B<<239.0,380.0>-<239.0,369.0>-<239.0,358.0>>
	* Euro (U+20AC) contains a short segment B<<239.0,358.0>-<239.0,347.0>-<239.0,336.0>>
	* uni20BA (U+20BA) contains a short segment L<<272.0,136.0>--<292.0,136.0>> and uni20BA (U+20BA) contains a short segment L<<595.0,318.0>--<595.0,308.0>> [code: found-short-segments]
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 0 | 96 | 1173 | 67 | 979 | 0 |
| 0% | 0% | 4% | 51% | 3% | 42% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
