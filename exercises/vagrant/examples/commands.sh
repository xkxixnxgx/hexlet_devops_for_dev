cd /vagrant # переход в директорию
pwd # печать пути текущей директории
curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash - # curl скачивает скрипт, а bash выполняет этот скрипт через pipeline оператор
sudo apt-get install -y nodejs # Установка пакетов через системный пакетный менеджер apt. Флаг -y автоматом подтверждает установку

vagrant init <box_name> # Инициализация
vagrant up # Запуск виртуальной машины
vagrant ssh # Подключение к машине
vagrant halt # Остановка машины
vagrant reload # Перезапуск машины halt & up


# Удаляет директорию .vagrant (техническую директорию для созданной виртуальной машины)
vagrant destroy
