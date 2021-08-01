test:
	test -f host_vars/localhost.yml
	test -f inventory.ini
	make install
	ansible-playbook -i inventory.ini test.yml --check

# BEGIN

# END

.PHONY: test
