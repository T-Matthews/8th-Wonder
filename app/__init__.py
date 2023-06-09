from flask import Flask
from config import Config
#Auth Blueprint import
from .auth.routes import auth


#imports for DB
from .models import db, login
from flask_migrate import Migrate



app=Flask(__name__)
app.config.from_object(Config)

#register blueprints
app.register_blueprint(auth)

#set up ORM and migrate comms with app and each other
db.init_app(app)
migrate=Migrate(app,db)

#Login Manager setup
login.init_app(app)
login.login_view ='auth.login'
login.login_message='Please log in to access this page.'
login.login_message_category = 'danger'



from . import routes