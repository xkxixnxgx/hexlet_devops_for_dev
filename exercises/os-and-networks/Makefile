test:
	vagrant -v
	test -e Vagrantfile || exit

run:
	export FLASK_APP=webapp && export FLASK_ENV=development && flask run
