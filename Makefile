.PHONY: clean test sdist all test

all: test sdist

clean:
	rm -rf `find . | grep \.pyc`
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

deps:
	pip install -r dev_requirements.txt
	python setup.py develop

test:
	@python setup.py test 

dist: sdist

sdist:
	@python setup.py sdist
