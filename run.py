import os 
import json
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "randomstring123"

""" variables"""
content=""
data = []

image_counter=0
hint_score=0
high_score=[]

@app.route("/")
def index():
        return render_template('index.html', high_score=high_score)

@app.route("/user",methods=["GET","POST"])
def user():
    """set session cookie"""
    if request.method == "POST":
        session['score']=0
        session["username"] = request.form["username"]
        x=session['username']
       
        open(x+'.txt',"w+")
    if "username" in session:
        return redirect(session["username"])
       
    return render_template("user.html")

@app.route("/<username>", methods=["GET","POST"])

def users(username):
    global  guess
   
    global image_counter
    global hint_score
    global content
    
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
             
            
             
             session['score'] = session.get('score') + 2  # reading and updating session data
             session.modified = True
          
             
             x=session['username']
             image_counter+=1
             img_src=data[image_counter]['img_source']
             open(x+".txt", "w").close()
             file = open (x+".txt", "r")
             content=file.read()
             file.close
             hint_score=0
         
         elif guess =="hint":
              
           hint=data[image_counter]['hint']
           hint_score=1
           
         else: 
          x=session['username']
          
          file = open (x+".txt", "a")
          file.write("\n"+guess)
          file.close
          file = open (x+".txt", "r")
          content=file.read()
          file.close
          
          
        

         
    return render_template("game.html", username=username, guess_data=data,  guess=content, img_src=img_src, hint=hint, score=session['score'])       
        
@app.route('/end_game/<username>')
    
def end_game(username):
    global high_score
    x=session['username']
  
    high_score.sort()
 
    os.remove(x+".txt")
    session['username'].clear()
    return render_template('end_game.html', username=username, high_score=high_score)



app.run(host=os.getenv('IP'), port=int (os.getenv('PORT')), debug=True)



