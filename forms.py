from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import DataRequired, Length, Email
from wtforms.fields.html5 import EmailField, DateField


class TextForm(FlaskForm):
    message = TextField('Message',[
        DataRequired(),
        Length(max=160, message=('Your message cannot be more than 160 characters'))])

class ContactForm(FlaskForm):
    clastname = TextField('Last Name')
    cfirstname = TextField('First Name')
    caddress1 = TextField('Address')
    caddress2 = TextField('Address 2')
    ccity = TextField('City')
    cstate = TextField('State')
    czip = TextField('Zip')
    chomearea = TextField('Home area code')
    chomephone = TextField('Home phone')
    dbday = DateField('Birthday')
    cemail = EmailField('Email Address', [DataRequired(), Email()])
    ccellarea  = TextField('Cell area code')
    ccellphone = TextField('Cell phone')