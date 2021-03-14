from flask import render_template
from app import app
from.request import get_quote
# Views


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    quote = get_quote()
    print(quote)
    title = "Hunja | A personal blog"

    return render_template('index.html', title=title, quote=quote)


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html', id=movie_id)
