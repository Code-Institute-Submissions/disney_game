import os 
import json
from flask import Flask, render_template, request, redirect, session

guesses = [] 
app = Flask(__name__)
app.secret_key = "randomstring123"


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
    data = []
    score = 0
    image_counter=0
     
    with open("data/guess_data.json", "r") as json_data:
        data = json.load(json_data)
        answer= data[image_counter]['answer'] 
  
        if request.method == "POST":
            
            add=request.form['guess']
            if add == answer:
             return("correct")
            else:    
             guesses.append(add)
            
    return render_template("game.html", username=username, guess_data=data, score=score, guesses=guesses, counter=image_counter)       
        
app.run(host=os.getenv('IP'), port=int (os.getenv('PORT')), debug=True)



