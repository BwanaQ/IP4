from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):

    title = StringField('Title', validators=[Required()])
    body = TextAreaField('Body', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Add a Comment', validators=[Required()])
    submit = SubmitField('submit')
