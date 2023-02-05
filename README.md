# Django REST API for music albums with Docker

### Stack: Django, Djangorestframework, Swagger, Docker

## Инструкция по запуску

1. Клонируем репозиторий `git clone https://github.com/KozyrevAndrey/djangoMusicApiRest.git`
2. Создаем свой `.env`, где прописываем необходимые переменные окружения
3. Переходим на сайт генерация ключа django `https://djecrety.ir/`
4. Вставляем полученный ключ в переменные окружения .env
5. Запускаем проект командой `docker-compose up -d --build`, если хотите пользоваться консолью, не открывая новое консольное окно, или `docker-compose up`, если хотите получать дополнительную информацию из консоли.
6. Получить доступ к сайту можно по `http://localhost`
7. Проверьте адрес `http://localhost/api/song`, если таблица не существует, проведите подготовительные команды:
```
docker-compose exec web python manage.py collectstatic
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```
Адреса:
`http://localhost/admin` - админ панель;
`http://localhost/swagger-ui/` - документация по api;
`http://localhost/api/performer` - доступ к исполнителям через api;
`http://localhost/api/album` - доступ к альбомам через api;
`http://localhost/api/song` - доступ к песням через api.

## Переменные окружения 
```
DJANGO_SECRET_KEY=your_key
DEBUG=TRUE
```

