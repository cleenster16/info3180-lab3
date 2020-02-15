from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' #2525
app.config['MAIL_USERNAME'] = '01279a928d290f'
app.config['MAIL_PASSWORD'] = 'ad4ea00c7037a1'

mail = Mail(app)
from app import views