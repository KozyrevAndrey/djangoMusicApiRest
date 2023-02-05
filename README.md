# Django REST API for music albums with Docker

### Stack: Django, Djangorestframework, Swagger, Docker

## Инструкция по запуску

1. Клонируем репозиторий `git clone https://github.com/KozyrevAndrey/djangoMusicApiRest.git`
2. Создаем свой `.env`, где прописываем необходимые переменные окружения
3. Переходим на сайт генерация ключа django `https://djecrety.ir/`
4. Вставляем полученный ключ в переменные окружения .env
3. Запускаем проект командой `docker compose up`

## Переменные окружения 
```
DJANGO_SECRET_KEY=your_key
DEBUG=TRUE
```

