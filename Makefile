run-dev-container:
	docker stop dev-container || true && docker rm dev-container || true
	docker run --name=dev-container -p 80:80 -d -v "$(pwd):/app" dev-container

rebuild-and-run-dev-container:
	docker stop dev-container || true && docker rm dev-container || true
	docker build -t dev-container .
	docker run --name=dev-container -p 80:80 -d -v "$(pwd):/app" dev-container

stop-dev-container:
	docker stop dev-container || true && docker rm dev-container || true