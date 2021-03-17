from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_quote
from .forms import BlogForm, UpdateProfile
from ..models import Blog, User
from flask_login import login_required, current_user
from .. import db, photos
from sqlalchemy import desc


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = "Hunja | A personal blog"
    quote = get_quote()
    print(quote)
    form = BlogForm()
    blogs = Blog.query.order_by(desc(Blog.timestamp)).all()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        new_blog = Blog(title=title, body=body, user_id=current_user.id)
        new_blog.save_blog()

        return redirect(url_for('main.index'))
    return render_template('index.html', title=title, quote=quote, blog_form=form, blogs=blogs)


@ main.route('/user/<uname>')
@ login_required
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@ main.route('/user/<uname>/update', methods=['GET', 'POST'])
@ login_required
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


@ main.route('/user/<uname>/update/pic', methods=['POST'])
@ login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))
    return render_template('profile/update.html', form=form)
