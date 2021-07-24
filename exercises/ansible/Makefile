test:
	vagrant -v
	test -e Vagrantfile || exit
	make lint

lint:
	ansible-lint provisioning

# BEGIN

# END

.PHONY: test
