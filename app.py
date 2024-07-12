from flask import Flask,render_template
from database import get_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/base')
def base():
    return render_template('base.html')
if __name__=="main":
    app.run()