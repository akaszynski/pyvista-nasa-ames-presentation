BUILD = ./build

build:
	latexmk -pdflatex=lualatex -pdf nasa_pyvista_seminar_2025.tex -interaction=nonstopmode --shell-escape -outdir=$(BUILD) -use-make

clean:
	rm -rf $(BUILD)

watch:
	latexmk -pdflatex=lualatex -pdf nasa_pyvista_seminar_2025.tex -interaction=nonstopmode --shell-escape -outdir=$(BUILD) -pvc

.PHONY: build clean

all: build
