BUILD = ./build

build:
	mkdir -p build
	lualatex -interaction=nonstopmode --shell-escape -output-directory=$(BUILD) nasa_pyvista_seminar_2025.tex || true
	latexmk -pdflatex=lualatex -pdf nasa_pyvista_seminar_2025.tex -interaction=nonstopmode --shell-escape -outdir=$(BUILD)

clean:
	rm -rf $(BUILD)

watch:
	latexmk -pdflatex=lualatex -pdf nasa_pyvista_seminar_2025.tex -interaction=nonstopmode --shell-escape -outdir=$(BUILD) -pvc

.PHONY: build clean

all: build
