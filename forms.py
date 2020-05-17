from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import DataRequired, Length


class TextForm(FlaskForm):
    message = TextField('Message',[
        DataRequired(),
        Length(max=160, message=('Your message cannot be more than 160 characters'))])