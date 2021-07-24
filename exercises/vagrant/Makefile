test:
	vagrant -v
	test -e Vagrantfile || exit
	npm install --dry-run

init:
	vagrant up
	vagrant ssh
	curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
	sudo apt-get update
	sudo apt-get install -y nodejs
	cd /vagrant
	npm init -y fastify
	npm install

run:
	vagrant up
	vagrant ssh
	cd /vagrant
	FASTIFY_ADDRESS=0.0.0.0 npm run dev

stop:
	vagrant halt

reload:
	vagrant reload
