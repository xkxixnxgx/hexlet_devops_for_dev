# Dotfiles

Подготовка рабочего окружения — это весьма распространённая задача. И Ansible с ней отлично справляется. Установить Git, настроить его, установить нужные приложения — всё это мы можем выполнить, если опишем нужные действия в плейбуке. Однако программисты не были бы программистами, если бы не написали готовые модули для этого. В Ansible для этого существуют роли. А роли, которые находятся в свободном доступе и переиспользуются другими разработчиками находятся в Ansible Galaxy. Это специальный реестр ролей, где можно найти роль под нужную задачу.

В этом задании для вас уже подготовлен плейбук, который настраивает рабочее окружение. Его необходимо настроить с помощью переменных, установить зависимости и запустить. Вот список того, что устанавливается

* git и curl
* Docker и Docker Compose
* Менеджер версий [asdf](https://asdf-vm.com/)
* Командная оболочка [zsh](https://www.zsh.org/) и плагины для него (для Docker, Git, asdf)
* Интерпретаторы ruby и nodejs (версия управляется с помощью asdf)
* В конфиге Git устанавливается имя пользователя и почта. Добавляются алиасы и глобальный *.gitignore*

## Ссылки

* [Создание инвентори файла](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#assigning-a-variable-to-one-machine-host-variables)
* [Что такое Makefile](https://guides.hexlet.io/makefile-as-task-runner/)
* [dotfiles]( https://github.com/mokevnin/dotfiles)
* [Что такое "Менеджер версий"](https://guides.hexlet.io/version_managers)
* [asdf](https://asdf-vm.com/#/core-manage-asdf)
* [ohmyz.sh](https://ohmyz.sh/)
* [Установка ролей из Ansible Galaxy](https://galaxy.ansible.com/docs/using/installing.html)
* [Ansible Galaxy — community.general](https://galaxy.ansible.com/community/general)
* [Ansible Galaxy — gantsign.ansible-role-oh-my-zsh](https://galaxy.ansible.com/community/general)
* [Ansible Galaxy — markosamuli.asdf](https://galaxy.ansible.com/markosamuli/asdf)

## Задачи

* Создайте файл *inventory.ini*, укажите в нём хост `localhost` с локальным подключением
* Создайте файл *host_vars/localhost.yml*. Опишите в этом файле переменные

  * `user` — логин текущего пользователя (для которого настраивается окружение). Значение переменной можно задать динамически (взять текущего пользователя из фактов или из переменной окружения), так и статически (например `vagrant`)
  * `git_user_email` — email пользователя в коммитах Git
  * `git_user_name` — имя пользователя в коммитах Git
  * `zsh_theme` —  тема Oh My Zsh, например `murilasso`. Список тем и их названий можно посмотреть [здесь](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes)

* Создайте и запустите виртуальную машины на Ubuntu с помощью Vagrant, зайдите в неё и установите вручную `make` и `ansible`

* В плейбуке для настройки окружения используются роли и коллекции из Ansible Galaxy. Установите их

  ```shell
  ansible-galaxy collection install -r requirements.yml
  ansible-galaxy role install -r requirements.yml
  ```

  Создайте в *Makefile* команду под именем. `install`. Добавьте в нее команды для установки ролей и коллекций

* Выполните плейбук

  ```shell
  ansible-playbook -i inventory.yml playbook.yml -v
  ```

  Добавьте команду в *Makefile*

Чтобы проверить, что всё установилось корректно, перелогиньтесь в машине, на которой выполняли настройку окружения, вызовите docker, docker-compose, git. Для данных приложений должен работать автокомполит для команд. Командная оболочка изменится на zsh с выбранной темой.

```shell
docker --version
Docker version 20.10.7, build f0df350

docker-compose --version
docker-compose version 1.26.0, build d4451659

node -v
v16.3.0

git config user.name
Jon Snow

 $ git config user.email
jon@staks.com
```

### Подсказки

* По умолчанию в Vagrant для запроса root-доступа (sudo) не запрашивается пароль. При выполнении плейбука, в котором используется эскалация привилегий ([become](https://docs.ansible.com/ansible/latest/user_guide/become.html)) обычно передают опцию `--ask-become-password`, например

```shell
ansible-playbook -i inventory.ini playbook.yml --ask-become-pass
```

## Самостоятельная работа

Создайте на Github репозиторий и опишите в нём установку и настройку приложений, с которыми работаете в повседневной жизни.
