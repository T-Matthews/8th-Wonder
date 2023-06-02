from flask import Blueprint, render_template

auth = Blueprint('auth',__name__,template_folder='auth_templates',url_prefix='/auth',static_folder='auth_static')

from .authforms import LoginForm

@auth.route('/login',methods=['GET','POST'])
def login():
    lform=LoginForm()

    return render_template('signin.html',form=lform)