# Docker

В этом задании мы упакуем готовое приложение в образ.

## Ссылки

* [Введение в Docker](https://www.youtube.com/watch?v=dfXuTTV6TVo)
* [Как и для чего использовать Docker](https://guides.hexlet.io/docker/)
* [Docker Overview](https://docs.docker.com/get-started/overview/)

## Задачи

* Инициализируйте вручную проект на [Fastify](https://github.com/fastify/fastify#quick-start)
* Создайте *Dockerfile* и пропишите команды для упаковки приложения в образ
* Соберите образ с тегом. При старте контейнера должен запускаться веб-сервер и быть доступен снаружи на 3000 порту.

  ```shell
  docker build . -t <tag>
  ```

* Запустите контейнер и проверьте, что всё работает.

  ```shell
  docker run -it -p 3000:3000 <image>
  # открываем в браузере http://localhost:3000 и проверяем, что всё работает
  ```

* Залейте (запушьте) образ на [Docker Hub](https://hub.docker.com/)

  ```shell
  docker push <image>
  ```

* Добавьте в *Makefile* команду `build` для сборки образа
