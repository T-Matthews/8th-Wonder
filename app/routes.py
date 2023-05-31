from flask import render_template
from . import app


@app.route('/')
def home():
    
    return render_template('index.html')
    #can pass variables into render template, allowing for variable to be used in jinja template
