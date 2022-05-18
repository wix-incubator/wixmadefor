SOURCES=$(shell python3 scripts/read-config.py --sources )
FAMILY=$(shell python3 scripts/read-config.py --family )
DRAWBOT_SCRIPTS=$(shell ls documentation/*.py)
DRAWBOT_OUTPUT=$(shell ls documentation/*.py | sed 's/\.py/.png/g')

help:
	@echo "###"
	@echo "# Build targets for $(FAMILY)"
	@echo "###"
	@echo
	@echo "  make build:  Builds the fonts and places them in the fonts/ directory"
	@echo "  make test:   Tests the fonts with fontbakery"
	@echo "  make proof:  Creates HTML proof documents in the proof/ directory"
	@echo "  make images: Creates PNG specimen images in the documentation/ directory"
	@echo

build: build.stamp

venv: venv/touchfile

build.stamp: venv .init.stamp sources/config.yaml sources/config_text.yaml sources/config_display.yaml $(SOURCES) generate-ttx-hinting.stamp
	. venv/bin/activate; rm -rf fonts/; \
	gftools builder sources/config.yaml; \
	gftools builder sources/config_text.yaml; \
	gftools builder sources/config_display.yaml; \
	mkdir fonts/otf; mv fonts/**/otf/* fonts/otf; \
	mkdir fonts/ttf; mv fonts/**/ttf/* fonts/ttf; \
	python3 scripts/create-webfonts.py; \
	rm -rf fonts/Text; rm -rf fonts/Display && touch build.stamp

.init.stamp: venv
	. venv/bin/activate; python3 scripts/first-run.py

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

test: venv build.stamp
	. venv/bin/activate; mkdir -p out/ out/fontbakery; fontbakery check-googlefonts -l WARN --succinct --badges out/badges --html out/fontbakery/fontbakery-report.html --ghmarkdown out/fontbakery/fontbakery-report.md $(shell find fonts/ttf -type f)

proof: venv build.stamp
	. venv/bin/activate; mkdir -p out/ out/proof; gftools gen-html proof $(shell find fonts/ttf -type f) -o out/proof

images: venv build.stamp $(DRAWBOT_OUTPUT)
	git add documentation/*.png && git commit -m "Rebuild images" documentation/*.png

%.png: %.py build.stamp
	python3 $< --output $@

clean:
	rm -rf venv
	find . -name "*.pyc" -delete

update-ufr:
	npx update-template https://github.com/googlefonts/Unified-Font-Repository/

update:
	pip install --upgrade $(dependency); pip freeze > requirements.txt

# Added to Wix project to generate hinting source files
generate-ttx-hinting: generate-ttx-hinting.stamp

generate-ttx-hinting.stamp: venv
	. venv/bin/activate; for source in sources/*.ufo; do \
		python3 -m vttLib dumpfile_from_ufo $$source ; ufonormalizer -m $$source ; \
	done && touch generate-ttx-hinting.stamp