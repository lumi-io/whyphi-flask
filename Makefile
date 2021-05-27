run-container:
	docker stop testing_container || true && docker rm testing_container || true
	docker build -t testing_container tests
	docker run -d --name=testing_container -p 80:80 testing_container

test-container: run-container
	pipenv run pytest

start-dev-container:
	docker-compose -f ./docker-compose.yml up

stop-dev-container:
	docker-compose -f ./docker-compose.yml down