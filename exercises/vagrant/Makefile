test:
	vagrant -v
	test -e Vagrantfile || exit
	npm install --dry-run

init:
	vagrant up
	vagrant ssh -- -t ' \
		curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash - ; \
		sudo apt-get update -y ; \
		sudo apt-get install -y nodejs ; \
		cd /vagrant ; \
		npm init -y fastify ; \
		npm install -y '
	vagrant halt

run:
	vagrant up;
	vagrant ssh -- -t ' \
		cd /vagrant ; \
		FASTIFY_ADDRESS=0.0.0.0 npm run dev ; \
		/bin/bash '

stop:
	vagrant halt

restart:
	vagrant reload

remove:
	vagrant destroy