import os

#from config import basedir
from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.login import LoginManager
#from flask.ext.openid import OpenID


#Configuring app stuff
app = Flask(__name__)
#app.config.from_object('config')
#db = SQLAlchemy(app)

#Login stuff
#lm = LoginManager()
#lm.init_app(app)
#lm.login_view = 'signin'
#oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views
