from flask import render_template, request, redirect, url_for, flash

from app.models.movie import MovieModel


class MovieController:
    def __init__(self):
        self.model = MovieModel()

    def index(self):
        movies = self.model.get_all_movies()
        return render_template('movies/index.html', movies=movies)

    def store(self):
        title = request.form.get('title', '')
        director = request.form.get('director', '')
        try:
            year = int(request.form.get('year', ''))
            rating = float(request.form.get('rating', ''))
        except ValueError:
            flash('Рік та рейтинг мають бути числами!', 'error')
            return redirect(url_for('index'))

        if self.model.add_movie(title, director, year, rating):
            flash('Фільм додано!', 'success')
        else:
            flash('Не вдалося додати фільм: перевірте назву, режисера, рік та рейтинг (0-10)', 'error')

        return redirect(url_for('index'))

    def mark_watched(self, movie_id: int):
        if self.model.mark_watched(movie_id):
            flash('Фільм позначено як переглянутий!', 'success')
        else:
            flash('Фільм не знайдено', 'error')
        return redirect(url_for('index'))

    def delete(self, movie_id: int):
        self.model.delete_movie(movie_id)
        flash('Фільм видалено!', 'success')
        return redirect(url_for('index'))
