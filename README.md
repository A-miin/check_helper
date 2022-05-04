# Check helper
Для запуска проекта установите python версии 3.7 и выше, pip и virualenv


Для того чтобы клонировать содержимое репозитория выполните команду:
```bash
git clone https://github.com/A-miin/check_helper.git
```

После клонирования перейдите в склонированную папку и вывполните следующие команды:

Создайте виртуальное окружение командой
```bash
python3 -m virtualenv -p python3 venv
```
либо
```bash
virtualenv -p python3 venv
```

Активируйте виртуальное окружение командой
```bash
source venv/bin/activate
```

Установите зависимости командой
```bash
pip install -r requirements.txt
```

Создайте файл .env для хранения переменных окружения
```bash
touch .env
```
Заполните её по примеру из файла  .envexample

Примените миграции командой
```bash
python manage.py migrate
```

Загрузите фикстуры командой
```bash
python manage.py loaddata fixtures/dump.json
```
Для запуска сервера
```bash
python manage.py runserver
```

Данные для входа:
admin@admin.admin: admin  (superuser)

