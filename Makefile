build: clean
	python3 setup.py build_ext --inplace

test:
	python3 -c 'import hello_ext; hello_ext.greet()'

clean:
	rm -rf build/
	rm *.so

.PHONY: *