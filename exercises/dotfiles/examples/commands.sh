# Запуск adhoc команды
ansible localhost -m ping

# Запуск плейбука выполняется командой ansible-playbook
# Флаг -v, -vv, -vvv указывает на подробность вывода Ansible
# флаг -i указывает на файл инвентори в котором прописаны хосты для запуска
ansible-playbook -i inventory.ini playbook.yml -v

# флаг -K это сокращенная запись флага --ask-become-pass для указания пароля для sudo (когда указываем become: true для эскалации прав)
ansible-playbook -i inventory.ini playbook.yml -v -K

# Установка ролей и коллекций выполняется разными командами
ansible-galaxy collection install -r requirements.yml
ansible-galaxy role install -r requirements.yml
