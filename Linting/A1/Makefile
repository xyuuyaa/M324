.PHONY: linting

linting: coverage.xml
	docker run --rm \
		-e SONAR_HOST_URL="http://sonarqube:9000" \
		-e SONAR_SCANNER_OPTS="-Dsonar.projectKey=house" \
		-e SONAR_TOKEN="your_token" \
		--network sonar-net \
		-v .:/usr/src \
		-u $(id -u):$(id -g) \
		sonarsource/sonar-scanner-cli

	rm -f coverage.xml

coverage.xml: src/house.py tests/test.py
	python3 -m coverage run -m unittest discover tests
	python3 -m coverage report
	python3 -m coverage xml -i

	rm -rf src/__pycache__
	rm -rf tests/__pycache__
	rm -f .coverage