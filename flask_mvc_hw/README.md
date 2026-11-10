# Flask MVC: колекція фільмів

Основа: https://github.com/sunmeat/python_flask. Модель `TaskModel` замінено на `MovieModel` (варіант «фільм»).

Поля сутності `Movie`: назва, режисер, рік, рейтинг, статус «переглянуто».

## Запуск

```bash
pip install -r requirements.txt
python run.py
```

Відкрити http://127.0.0.1:5000/

## Структура (MVC)

- `app/models/movie.py` — модель
- `app/controllers/movie_controller.py` — контролер
- `app/views/templates/` — подання
- `app/__init__.py` — маршрути

## Скріни

Знаходяться в папці `screenshots/`.
