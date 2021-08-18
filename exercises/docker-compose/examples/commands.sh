# Собирает сервисы, описанные в конфигурационных файлах
docker-compose build
# Запускает собранные сервисы
docker-compose up
# Если какой-то из сервисов завершит работу,
# то будут остальные будут остановлены автоматически
docker-compose up --abort-on-container-exit
# Запустит сервис application и выполнит внутри команду make install
docker-compose run application make install
# А так мы можем запустить сервис и подключиться к нему с помощью bash
docker-compose run application bash
# Останавливает и удаляет все сервисы, которые были запущены с помощью up
docker-compose down
# Останавливает но не удаляет сервисы, запущенные с помощью up
# Их можно запустить снова с помощью docker-compose start
docker-compose stop
# Перезапускает все остановленные и запущенные сервисы
docker-compose restart

# пример Makefile:
# https://github.com/hexlet-basics/hexlet-basics/blob/master/make-compose.mk
