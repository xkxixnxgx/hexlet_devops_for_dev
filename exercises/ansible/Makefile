test:
	vagrant -v
	test -e Vagrantfile || exit
	make lint

lint:
	ansible-lint provisioning

init:
	vagrant up
	vagrant provision
	vagrant halt

start:
	vagrant up;
	vagrant ssh -- -t ' \
		cd /vagrant ; \
		npm run dev ; \
		/bin/bash '

stop:
	vagrant halt

restart:
	vagrant reload

remove:
	vagrant destroy

.PHONY: test
