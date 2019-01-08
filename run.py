import os 
import json
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "randomstring123"

""" variables"""
guesses = [] 
data = []
score=0
image_counter=0
@app.route("/")
def index():
        return render_template('index.html')

@app.route("/user",methods=["GET","POST"])
def user():
    if request.method == "POST":
        
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])
    return render_template("user.html")

@app.route("/<username>", methods=["GET","POST"])



def users(username):
   
    global score
    global image_counter
    
    
    with open("data/guess_data.json", "r") as json_data:
        data = json.load(json_data)
        answer= data[image_counter]['answer'] 
        img_src=data[image_counter]['img_source']
        
        guess=request.form['guess']
        
        if request.method == "POST":
          
            if guess == answer:
             score+=2
             image_counter+=1
             img_src=data[image_counter]['img_source']
             guesses[:]=[]
            else:    
             guesses.append(guess)
            
    return render_template("game.html", username=username, guess_data=data, score=score, guesses=guesses, img_src=img_src)       
        
app.run(host=os.getenv('IP'), port=int (os.getenv('PORT')), debug=True)



