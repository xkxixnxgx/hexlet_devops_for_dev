# В Makefile в качестве отступов используюбтся только табы
install:
	npm install

start:
	npm start

# Можем использовать Makefile как алиас для длинных команд или череды команд
vagrant-install:
	vagrant ssh -c "cd /vagrant && make install"

vagrant-start:
	vagrant ssh -c "cd /vagrant && make start"

# несколько команд make записываются в ту же строку, что и сама команда
upstart: install start
