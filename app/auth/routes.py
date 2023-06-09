from flask import Blueprint, render_template,request,flash,redirect,url_for
from app.models import User
auth = Blueprint('auth',__name__,template_folder='auth_templates',url_prefix='/auth',static_folder='auth_static')
from flask_login import login_user, current_user, login_required, logout_user
from .authforms import LoginForm,RegistrationForm
from werkzeug.security import check_password_hash
from app.models import db

@auth.route('/login',methods=['GET','POST'])
def login():

    #ADD LATER

    #  if current_user:
    #     flash(f'You are already logged in as {current_user.username}. Logout before attempting login.','danger')
    #     return(redirect(url_for('home')))


    
    lform=LoginForm()
    if request.method =='POST':
        if lform.validate_on_submit():

        #either the form data is proper
            username= lform.username.data
            form_password= lform.password.data
            #query our database for a user with that username
            user = User.query.filter_by(username = lform.username.data.title()).first()
            if user and check_password_hash(user.password,form_password):
                login_user(user)
                print(current_user.__dict__)
                flash(f'Welcome, {username}! You have been signed in.',category='primary')
                return redirect(url_for('home'))
        #or the username is incorrect - we dont want to sign the user in
        flash(f'Incorrect username or password, please try again.','danger')
        return redirect(url_for('auth.login'))
    return render_template('signin.html',form=lform)



@auth.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if request.method =="POST":
        if form.validate_on_submit():
            newuser = User(form.username.data, form.email.data, form.password.data, form.first_name.data, form.last_name.data)
            try:
                db.session.add(newuser)
                db.session.commit()
            except:
                flash('Username or Email already in use. Please try a different one.', 'danger')
                return redirect(url_for('auth.register'))
            if newuser.first_name:
                flash(f'Welcome, {newuser.first_name}! Thank you for registering.','info')
            else:
                flash(f'Welcome! Thank you for registering.','info')
            return redirect(url_for('home'))
        else:
            flash('Sorry, your passwords do not match. Please try again.','danger')
            return redirect(url_for('auth.register'))


    #implied else, activated upon GET request
    return render_template('register.html',form=form)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been signed out.','primary')
    return redirect(url_for('home'))



    