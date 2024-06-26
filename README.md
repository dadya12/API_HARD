# articles

## Зависимости

Для запуска проекта установить python версии 3.10 и выше и pip

## Локальный запуск проекта

После клонирования проекта выполните команды:

### Создайте виртуальное окружение командой
```bash
python -m venv venv
```

### Активируйте виртуальное окружение командой
```bash
source venv/bin/activate
venv\Scripts\activate
```

### Установите зависимости командой
```bash
pip install -r requirements.txt
```

### Создайте файл .env и пропишите переменные по аналогии с env.example

### Перейдите в папку source командой
```bash
cd source
```

### Примените миграции командой
```bash
python manage.py migrate
```

### Запустите проект командой
```bash
python manage.py runserver
```

### Создайте администратора командой
```bash
python manage.py createsuperuser
```

Для доступа в панель администратора перейдите по ссылке http://localhost:8000/admin
