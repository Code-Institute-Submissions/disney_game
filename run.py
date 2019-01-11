import os 
import json
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "randomstring123"

""" variables"""
guesses=[]
data = []
score=0
image_counter=0
hint_score=0


@app.route("/")
def index():
        return render_template('index.html')

@app.route("/user",methods=["GET","POST"])
def user():
    """set session cookie"""
    if request.method == "POST":
        
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])
    return render_template("user.html")

@app.route("/<username>", methods=["GET","POST"])

def users(username):
   
    global score
    global image_counter
    global hint_score
    hint=""
    
    """ get quiz data"""
    with open("data/guess_data.json", "r") as json_data:
        data = json.load(json_data)
        answer= data[image_counter]['answer'] 
        img_src=data[image_counter]['img_source']
        
      
        """ check answers"""
        if request.method == "POST":
          guess=request.form['guess']
          
          if guess == answer:
             score+=2 - hint_score
             image_counter+=1
             img_src=data[image_counter]['img_source']
             guesses[:]=[]
             hint_score=0
             
          elif guess=="hint":
              
           hint=data[image_counter]['hint']
           hint_score=1
           
          else:    
             guesses.append(guess)
            
    return render_template("game.html", username=username, guess_data=data, score=score, guesses=guesses, img_src=img_src, hint=hint)       
        
@app.route('/end_game/<username>')
    
def end_game(username):
    return render_template('end_game.html', score=score, username=username)



app.run(host=os.getenv('IP'), port=int (os.getenv('PORT')), debug=True)



