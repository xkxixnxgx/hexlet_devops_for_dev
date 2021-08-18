# Docker Compose

Docker Compose позволяет управлять набором контейнеров, каждый из которых представляет собой один сервис проекта. Управление включает в себя сборку, запуск с учетом зависимостей и конфигурацию. Конфигурация Docker Compose описывается в файле docker-compose.yml, лежащем в корне проекта, и выглядит примерно так:

```yaml
# https://github.com/hexlet-basics/hexlet_basics

version: '3.3'

services:
  db:
    image: postgres
  app:
    build:
      context: services/app
      dockerfile: Dockerfile
    command: mix phx.server
    ports:
      - "${PORT}:${PORT}"
    env_file: '.env'
    volumes:
      - "./services/app:/app:cached"
      - "~/.bash_history:/root/.bash_history:cached"
      - ".bashrc:/root/.bashrc:cached"
      - "/var/tmp:/var/tmp:cached"
      - "/tmp:/tmp:cached"
    depends_on:
      - db
```

Создайте Docker Compose, поместив туда ваш проект, с которым вы обычно работаете в повседневной практике.

## Ссылки

* [Overview of Docker Compose](https://docs.docker.com/compose/)
* [Compose file version 3 reference](https://docs.docker.com/compose/compose-file/compose-file-v3/)
* [Code Basics](https://github.com/hexlet-basics/hexlet-basics)
* [Postgres Docker image](https://hub.docker.com/_/postgres)
* [Введение в Docker](https://www.youtube.com/watch?v=dfXuTTV6TVo)
* [Docker Overview](https://docs.docker.com/get-started/overview/)

## Задачи

* Установите [Docker Compose](https://docs.docker.com/compose/install/)
* Создайте файл *docker-compose.yml* в корневой директории проекта. Опишите в нем используемые сервисы - ваше приложение, база данных / webpack (в зависимости от того, что используется в проекте)
* Пропишите `volume` для вашего приложения
* Инициализируйте проект на вашем фреймворке, убедитесь что он работает. Если ваше приложение использует базу данных, используйте коннект к этой базе. Хостом будет являться имя сервиса базы, например `database`
* Войдите в контейнер с приложением командой `docker-compose exec bash`
* Выставьте наружу нужный порт и проверьте что запущенный сервер доступен из браузера
* Поэкспериментируйте с Docker Compose. Пересоздайте контейнеры, выполните команды внутри запущенного контейнера (exec) и в отдельном запуске
* В *Makefile* опишите команды для подготовки и запуска проекта

Результат выполнения задачи — приложение, которое работает внутри Docker Compose, а также доступно снаружи по определённому порту. Опишите команды, Которые необходимы для сборки и запуска приложения.
