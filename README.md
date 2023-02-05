# Django REST API for music albums with Docker

### Stack: Django, Djangorestframework, Swagger, Docker

## Инструкция по запуску

1. Клонируем репозиторий `git clone https://github.com/](https://github.com/KozyrevAndrey/djangoMusicApiRest.git`
2. Создаем свой `.env`, где прописываем необходимые переменные окружения
3. Генерируем `DJANGO_SECRET_KEY` через команду в консоли `python3 generate_secret_key.py`, полученный ключ копируем и вставляем в `.env` 
4. Запускаем проект командой `docker compose up`

## Переменные окружения 
```
DJANGO_SECRET_KEY=your_key
DEBUG=TRUE
```

