test:
	test -f Dockerfile
	test -f docker-compose.yml

compose-install:
	docker-compose run application make install
	docker-compose run frontend npm ci

compose-start:
	docker-compose up --abort-on-container-exit

compose-setup: compose-down compose-build compose-install

compose-build:
	docker-compose build

compose-down:
	docker-compose down || true

compose-stop:
	docker-compose stop || true

compose-restart:
	docker-compose restart

compose-bash:
	docker-compose application run bash
