run-dev-container:
	docker stop dev-container || true && docker rm dev-container || true
	docker run -d --name=dev-container -p 80:80 dev-container

rebuild-and-run-dev-container:
	docker stop dev-container || true && docker rm dev-container || true
	docker build -t dev-container .
	docker run -d --name=dev-container -p 80:80 dev-container

stop-dev-container:
	docker stop dev-container || true && docker rm dev-container || true