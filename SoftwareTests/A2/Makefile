.PHONY: all setup test cleanup

DB_CONTAINER_NAME=test_mongo

all: setup test cleanup

setup:
	docker run -d --name $(DB_CONTAINER_NAME) -p 27017:27017 mongo:latest
	sleep 5

test:
	python3 -m coverage run -m unittest discover -s . -p 'test.py'
	python3 -m coverage report -m

cleanup:
	docker stop $(DB_CONTAINER_NAME)
	docker rm $(DB_CONTAINER_NAME)
	rm -f .coverage
	rm -rf __pycache__
