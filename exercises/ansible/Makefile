test:
	vagrant -v
	test -e Vagrantfile || exit
	make lint

lint:
	ansible-lint provisioning

# BEGIN
start:
	vagrant ssh
	cd /vagrant
	FASTIFY_ADDRESS=0.0.0.0 npm run dev
# END

.PHONY: test
