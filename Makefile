.PHONY: build
build:
	python3 build.py
	latexmk -pdf main

.PHONY: open
open: build
	open main.pdf

.PHONY: check
check:
	git diff-index --quiet HEAD -- || (echo "There are uncommitted changes."; exit 1)
	if git ls-files . --exclude-standard --others --error-unmatch; then \
		echo "There are untracked files."; \
		exit 1; \
	else \
		echo "Ignore the \"error: pathspec '.'...\""; \
		exit 0; \
	fi

.PHONY: promote
promote: build check
	mv main.tex main-template.tex

.PHONY: clean
clean:
	latexmk -C
