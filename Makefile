docs-build:
	cd docs-quarto \
		&& quartodoc build --verbose \
		&& quarto render
