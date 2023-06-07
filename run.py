#file to give terminal and flask shell access to the components of my app \
#so that I can test them through the shell/cli and not worry about templating or routing

#when you want to do testing through the flask shell with this context processor
#change the FLASK_APP variable in .env to run.py


from app import app
from app.models import db, User

@app.shell_context_processor
def shell_context():
    return {'db': db, 'User':User}