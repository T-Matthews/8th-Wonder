from flask import Blueprint, render_template,request,flash,redirect,url_for

auth = Blueprint('auth',__name__,template_folder='auth_templates',url_prefix='/auth',static_folder='auth_static')

from .authforms import LoginForm,RegistrationForm

@auth.route('/login',methods=['GET','POST'])
def login():
    lform=LoginForm()
    if request.method =='POST':
        if lform.validate_on_submit():

        #either the form data is proper
            username= lform.username.data
            password= lform.password.data
            print('formdata: ',username,password)
            flash(message=f"Thanks for logging in, {username}",category='primary')
            #
            return redirect(url_for('home'))
        #or the username is incorrect - we dont want to sign the user in
        else:
            return redirect(url_for('auth.login'))
    return render_template('signin.html',form=lform)



@auth.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if request.method =="POST":
        if form.validate_on_submit():
            #check db
            # access form data
            print(form.data)
            flash('Welcome! Thank you for registering.','info')
            return redirect(url_for('home'))
        else:
            flash('Sorry, your passwords do not match. Please try again.','danger')
            return redirect(url_for('auth.register'))


    #implied else, activated upon GET request
    return render_template('register.html',form=form)
    