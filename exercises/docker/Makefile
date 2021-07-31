test:
	test -f Dockerfile
	make lint
	make build

lint:
	hadolint Dockerfile

build:
	docker build . -t fastify

run:
	docker run -it -p 3000:3000 fastify
