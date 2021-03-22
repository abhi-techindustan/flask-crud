from flask import Flask
# from forms import ContactForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'a really really really really long secret key'

# manager = Manager(app)
db = SQLAlchemy(app)
