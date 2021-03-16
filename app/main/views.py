from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_quote
from .forms import BlogForm
from ..models import Blog


# Views


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = "Hunja | A personal blog"
    quote = get_quote()
    print(quote)

    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        quote = form.quote.data
        author = form.author.data
        new_blog = Blog(title, quote, author)
        new_blog.save_blog()
        return redirect(url_for('main.index'))
    return render_template('index.html', title=title, quote=quote, blog_form=form)


# Views


@main.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html', id=movie_id)
