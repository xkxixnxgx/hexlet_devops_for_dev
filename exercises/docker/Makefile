test:
	test -f Dockerfile
	make lint
	make build

lint:
	hadolint Dockerfile

build:
	docker build . -t fastify:0.0.1

push_hub:
	docker login
	docker tag fastify:0.0.1 xkxixnxgx/fastify:0.0.1
	docker push xkxixnxgx/fastify:0.0.1

build_hub: build push_hub

pull_hub:
	docker login
	docker pull xkxixnxgx/fastify:0.0.1

run:
	docker run -d -p 3000:3000 fastify:0.0.1

run_hub:
	docker run -d -p 3000:3000 xkxixnxgx/fastify:0.0.1
