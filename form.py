from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')
