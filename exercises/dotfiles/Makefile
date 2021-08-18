test:
	test -f host_vars/localhost.yml
	test -f inventory.ini
	make install
	ansible-playbook -i inventory.ini test.yml --check

install:
	ansible-galaxy collection install -r requirements.yml
	ansible-galaxy role install -r requirements.yml

run-playbook:
	ansible-playbook -i inventory.yml playbook.yml -v

start:
	vagrant up;

stop:
	vagrant halt

into:
	vagrant ssh

restart:
	vagrant reload

remove:
	vagrant destroy



.PHONY: test
