test:
	vagrant -v
	test -e Vagrantfile || exit

run:
	export FLASK_APP=webapp && export FLASK_ENV=development && flask run

lint:
	ansible-lint provisioning

init:
	vagrant up
	vagrant provision
	vagrant halt

start:
	vagrant up;
	vagrant ssh -- -t ' \
	export FLASK_APP=webapp && \
	export FLASK_ENV=development && \
	flask run '

stop:
	vagrant halt

restart:
	vagrant reload

remove:
	vagrant destroy

.PHONY: test