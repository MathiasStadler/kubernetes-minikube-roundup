init:
	pip3 install -r requirements.txt
	pip3 install --upgrade setuptools

install: init

test:
	py.test tests

clean:
	rm -rf package/__pycache__/ tests/__pycache__/

.PHONY: init test
