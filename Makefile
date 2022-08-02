build:
	python3 setup.py build_ext --inplace

test:
	python3 -c 'import hello_ext; hello_ext.greet()'

.PHONY: *