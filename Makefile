build: clean
	python3 setup.py build_ext --inplace

test:
	python3 -c 'import hello_ext; output = hello_ext.greet(); print(output)'

clean:
	rm -rf build/
	rm *.so

.PHONY: *