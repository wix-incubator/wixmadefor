# Wix Madefor

![logo](assets/WixMadefor%20black%20logo.png)

## About

Wix Madefor is a compact font family of three weights for display setting, and four text weights for use in user interfaces. The text fonts also have matching italics, with shapes rooted in cursive forms, despite the typeface’s geometric structure, allowing Wix to have different expressions, from functional to more playful. 

The typeface was designed to carry subtle features with an engaging and clean appearance.

The display style was designed with strong geometric features – round characters are nearly circular, and the curvatures of f, j, and t are angular; stroke endings in letters such as c and s have a slight flaring; and the letter spacing is set tight for use at larger sizes.

### Supported scripts

Latin (uprights and italics), Cyrillic (uprights) and Vietnamese (uprights) scripts are supported.

Supported languages:
Afar, Afrikaans, Albanian, Asturian, Asu, Basque, Belarusian, Bemba,
Bena, Bini, Bosnian, Breton, Bube, Bulgarian, Catalan, Cebuano, Chiga,
Colognian, Cornish, Croatian, Czech, Danish, Dutch, Embu, English,
Estonian, Faroese, Filipino, Finnish, French, Friulian, Ga, Galician,
Ganda, German, Gusii, Hungarian, Icelandic, Inari Sami, Indonesian,
Interlingua, Irish, Italian, Javanese, Jenaama Bozo, Jju, Jola-Fonyi,
Kabuverdianu, Kalaallisut, Kalenjin, Kamba, Kikuyu, Kinyarwanda,
Latvian, Lithuanian, Low German, Lower Sorbian, Luo, Luxembourgish,
Luyia, Macedonian, Machame, Makhuwa-Meetto, Makonde, Malagasy, Maltese,
Manx, Meru, Morisyen, Nigerian Pidgin, North Ndebele, Northern Sami,
Northern Sotho, Norwegian Bokmål, Norwegian Nynorsk, Nyanja, Nyankole,
Occitan, Oromo, Polish, Portuguese, Quechua, Romanian, Romansh, Rombo,
Rundi, Russian, Rwa, Saho, Samburu, Sango, Sangu, Scottish Gaelic,
Sena, Serbian, Shambala, Shona, Sidamo, Slovak, Slovenian, Soga, Somali,
Soninke, South Ndebele, Southern Sotho, Spanish, Sranan Tongo, Swahili,
Swati, Swedish, Swiss German, Taita, Taroko, Teso, Tiv, Tsonga, Tswana,
Turkishm Tyap, Ukrainian, Upper Sorbian, Vietnamese, Vunjo, Walloon,
Walser, Welsh, Western Frisian, Wolof, Xhosa, Zulu

There are 721 glyphs in the upright weights, and 476 in the italics.

### Axes

The Text and Display families each have a Weight axis, `wght`, with a range from 400 (Regular) to 800 (ExtraBold).

The Text family has eight named instances: Regular, Medium, Bold, ExtraBold, Italic, Medium Italic, Bold Italic, ExtraBold Italic.

### Features

The following features are enabled:
- Catalan L dot
- Dutch ij
- Moldovan and Romanian cedilla
- Precomposed and built Fractions
- Ordinals
- Superiors
- Inferiors
- Subscripts
- Numerators
- Denominators
- Case punctuation
- Uprights have Bulgarian alternates for Cyrillic

## Building

Fonts are built automatically by GitHub Actions - take a look in the "Actions" tab for the latest build.

If you want to build fonts manually on your own computer:

* `make build` will produce font files.
* `make test` will run [FontBakery](https://github.com/googlefonts/fontbakery)'s quality assurance tests.
* `make proof` will generate HTML proof files.

The proof files and QA tests are also available automatically via GitHub Actions.

## Changelog

[Font Versioning](https://github.com/googlefonts/gf-docs/tree/main/Spec#font-versioning) is based on semver. 

**July 2022. Version 3.000**
- MAJOR Initial release on Google Fonts.

## License

This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at
https://scripts.sil.org/OFL

## Repository Layout

This font repository structure is inspired by [Unified Font Repository v0.3](https://github.com/unified-font-repository/Unified-Font-Repository), modified for the Google Fonts workflow.
