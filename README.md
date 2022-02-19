# Calendar API

### Локальный запуск проекта

1. Установить docker, docker-compose.
2. Активировать виртуальное окружение.
3. Установить пакеты для подсказок IDE `pip install -r config/local/requirements.txt`.
4. Войти в контейнер джанго `docker-compose -f docker-compose-local.yml exec django bash
`. 
5. Создать админа `./manage.py createsuperuser --no-input`.

### Ссылки локальной/дев конфигурации проекта
- Django-admin: .../admin/
- Silk: .../silk/
- Swagger: .../docs/swagger/

### Команды для работы с проектом
- Получение JWT-токенов для пользователя по ID `./manage.py jwt 1`

### Документация API
В проекте используется модуль drf-spectacular (т.к. есть поддержка OpenAPI 3.0), который автоматически создает
документацию swagger (также redoc), с возможностью выполнения авторизованных запросов.