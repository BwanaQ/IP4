from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_quote
from .forms import BlogForm, UpdateProfile
from ..models import Blog, User
from flask_login import login_required
from .. import db, photos
# Views


@main.route('/')
@login_required
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


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)
# Views


@main.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html', id=movie_id)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))
    return render_template('profile/update.html', form=form)
