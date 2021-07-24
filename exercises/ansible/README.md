# Ansible

Настроим Vagrant-окружение c помощью [Ansible Provisioning](https://www.vagrantup.com/docs/provisioning/ansible) и запустим внутри него Fastify-проект.

## Ссылки

* [Ansible Documentation](https://docs.ansible.com/ansible/latest/index.html)
* [Vagrant: Проброс портов](https://www.vagrantup.com/docs/networking/forwarded_ports)
* [Пример интеграции Vagrant и Ansible](https://github.com/hexlet-boilerplates/vagrant-ansible)
* [apt_key](https://docs.ansible.com/ansible/2.3/apt_key_module.html) — Модуль для работы с ключами apt
* [apt_repository](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_repository_module.html) — модуль для работы с репозиториями пакетного менеджера apt
* [apt](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html) — модуль для работы с пакетным менеджером apt. Позволяет обновлять кеш, устанавливать пакеты

## Задачи

* [Установите Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
* Инициализируйте Vagrant с образом `ubuntu/focal64`
* Создайте директорию *provisioning* и файл *playbook.yml*, который будет использовать Ansible
* Подготовьте *Vagrantfile*

  * Добавьте провижинг с помощью Ansible. Укажите созданный плейбук *provisioning/playbook.yml*
  * Пробросьте изнутри виртуальной машины наружу 3000 порт. На нем запустится приложение Fastify

В плейбуке *provisioning/playbook.yml* опишите следующие задачи:

* Добавление GPG-ключа для apt-репозитория *nodejs*

  * url ключа: `https://keyserver.ubuntu.com/pks/lookup?op=get&fingerprint=on&search=0x1655A0AB68576280`
  * id: `68576280`

* Добавление apt-репозитория *nodesource*

  * repo: `deb https://deb.nodesource.com/node_16.x focal main`
  * filename: `nodesource`

* Установка *nodejs* с помощью apt

* Инициализация Fastify (`npm init -y fastify`). Инициализация должна происходит только если проект ранее не был инициализирован. Для этого используйте модуль [shell](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/shell_module.html) и его параметр `creates`, в параметры укажите  *package.json*

Выполните вход в виртуальную машину и установите вручную зависимости для Fastify-проекта. Убедитесь что запускается и работает

    ```sh
    vagrant ssh
    cd /vagrant
    npm install
    FASTIFY_ADDRESS=0.0.0.0 npm run dev # запуск приложения
    # открываем в браузере http://localhost:3000 и проверяем, что всё работает
    ```

  Опишите команду `start` в *Makefile*. С помощью этой команды приложение будет запускаться

Результатом домашней работы будет Fastify-проект, который запускается внутри виртуальной машины VirtualBox с помощью Vagrant и доступен снаружи по адресу *http://localhost:3000*. А также файл *provisioning/playbook.yml*, в котором происходит добавление репозитория и установка необходимых пакетов.

## Самостоятельная работа

Добавьте переменную `FASTIFY_ADDRESS` в */etc/environment* с помощью Ansible. Тогда не придется ее указывать при запуске Fastify. Используйте для этого модуль *lineinfile*.
