from flask import Blueprint, render_template,request,flash,redirect,url_for

auth = Blueprint('auth',__name__,template_folder='auth_templates',url_prefix='/auth',static_folder='auth_static')

from .authforms import LoginForm

@auth.route('/login',methods=['GET','POST'])
def login():
    lform=LoginForm()
    if request.method =='POST':
        flash(message="Thanks for logging in",category='message')
        return redirect(url_for('home'))

    return render_template('signin.html',form=lform)