# Vagrant

Создадим изолированное окружение для разработки с помощью Vagrant и запустим внутри него [Fastify](https://github.com/fastify/fastify). Fastify – микрофреймворк на JavaScript, который позволяет создать простой сайт используя буквально 20 строк кода (скопированных из документации).

## Ссылки

* [Что такое Vagrant](https://guides.hexlet.io/vagrant/)
* [Vagrant: Проброс портов](https://www.vagrantup.com/docs/networking/forwarded_ports)
* [Что такое Makefile](https://guides.hexlet.io/makefile-as-task-runner/)

## Задачи

* Установите [VirtualBox](https://www.virtualbox.org/wiki/Linux_Downloads)
* Установите [Vagrant](https://www.vagrantup.com/docs/installation)
* Инициализируйте Vagrant-проект

    ```sh
    vagrant init ubuntu/focal64
    ```

* В *Vagrantfile* пробросьте изнутри виртуальной машины наружу 3000 порт. На нем запустится Fastify
* Запустите виртуальную машин командой `vagrant up`
* После запуска Vagrant создаст директорию *.vagrant*. В этой директории создаются приватные ключи, конфиги для созданной виртуальной машины. Добавьте эту директорию в *.gitignore*
* Войдите в виртуальную машину и установите Node.JS v16.x с помощью команд:

    ```sh
    vagrant ssh
    curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
    sudo apt-get install -y nodejs
    ```

* Инициализируйте Fastify-проект и убедитесь что он работает

    ```sh
    cd /vagrant
    npm init -y fastify
    npm install
    FASTIFY_ADDRESS=0.0.0.0 npm run dev
    # открываем в браузере http://localhost:3000 и проверяем что все работает
    ```

* Добавьте в *Makefile* часто используемые команды

Результатом домашней работы будет Fastify-проект, который запускается внутри виртуальной машины VirtualBox с помощью Vagrant и доступен снаружи по адресу [http://localhost:3000](http://localhost:3000).

## Подсказки

* При выполнении *vagrant ssh* терминал подключается к виртуальной машине в домашнюю директорию пользователя, то есть */home/vagrant*, а код проекта появляется в каталоге */vagrant*
* Если мы используем Vagrant, то работа с проектом происходит внутри виртуальной машины, а не снаружи. Например, `npm install` выполняется после подключения к виртуальной машине по ssh и перехода в каталог с проектом
