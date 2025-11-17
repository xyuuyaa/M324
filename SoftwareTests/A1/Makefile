.PHONY: test

test: src/File.py tests/File_test.py
	# run tests with coverage
	python3 -m coverage run -m unittest discover tests
	python3 -m coverage report -m

	# remove coverage
	rm -f .coverage

	# clean __pycache__
	rm -rf src/__pycache__
	rm -rf tests/__pycache__