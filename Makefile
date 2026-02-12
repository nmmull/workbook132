.PHONY: build
build:
	latexmk -pdf main

.PHONY: open
open: build
	open main.pdf

.PHONY: clean
clean:
	latexmk -C
