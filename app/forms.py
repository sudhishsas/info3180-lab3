
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, InputRequired, Length


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),Length(min=4 ,max= 28),InputRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(),InputRequired()])
    subject = StringField('Subject', validators=[DataRequired(),InputRequired()])
    message = TextAreaField('Message', validators=[DataRequired(),InputRequired(),Length(max=200)])