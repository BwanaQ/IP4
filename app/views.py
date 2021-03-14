from flask import render_template
from app import app

# Views


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    posts = [
        {
            "title": "Start", "body": "Index Post"
        },
        {
            "title": "Test", "body": "Coding is fun"
        }
    ]
    return render_template('index.html', posts=posts)


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html', id=movie_id)
