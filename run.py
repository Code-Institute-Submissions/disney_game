import os 
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/user')
def user():
    return render_template("user.html")

@app.route('/user/<name>')
def username(name):
     return render_template("game.html",name=name)
    
app.run(host=os.getenv('IP'), port=int (os.getenv('PORT')), debug=True)


