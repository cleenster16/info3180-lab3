from flask_wtf import Form
from wtforms.fields import TextField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email

class ContactForm(Form):

    name = TextField('Name', validators=[InputRequired("Please enter your full name")])
    email = TextField('Email', validators=[InputRequired("Please enter you email address"), Email()])
    subject = TextField('Subject', validators=[InputRequired("Please enter the subject for your message")])
    message = TextField('Message', validators=[InputRequired("Please enter the message you would like to send")])

