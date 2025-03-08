# SABPN ТВ4

## Описание:
Дипломная работа ТВ4 - сервис авторизации по номеру телефона. 
Работа включает в себя разработку веб-сервиса с использованием Django и DRF, PostgreSQL в качестве БД, Docker для контейнеризации приложения.

## Запуск проекта

1. Клонируйте репозиторий:
   ```
   git clone <https://github.com/aleksanderslepow97/SABPN>
   cd phone_auth
   ```

2. Создайте виртуальное окружение и активируйте его:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

4. Запустите Docker:
   ```
   docker-compose up --build
   ```

5. Откройте [http://localhost:8000/swagger/](http://localhost:8000/swagger/) для доступа к документации API.

## Разработчики:

За дополнительной информацией обращайтесь: `sanya.slepow2015@yandex.ru`
Работа лицензирована.