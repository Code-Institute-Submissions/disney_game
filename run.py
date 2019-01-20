import os 
import json

from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "randomstring123"

""" variables"""
content=""
data = []
highscores={}


image_counter=0
hint_score=0


@app.route("/")

def index():
 global highscores
 with open('data/highscores.json', 'r') as read_file:
            highscores = json.load(read_file)  # Read the json file.
            highscores.sort(reverse=True)

           
  

 return render_template('index.html',x=highscores)

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
         guess=request.form['guess'].lower()
          
         if guess == answer:
             
             intial_score=2
             score_number=intial_score-hint_score
             
             
             session['score'] = session.get('score') + score_number # reading and updating session data
             session.modified = True
          
             
             x=session['username']
             image_counter+=1
             if image_counter >=24:
              return redirect(url_for('end_game', username=username))
             else:
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
          content=file.readlines()
          file.close
          
          
        

         
    return render_template("game.html", username=username, guess_data=data,  guess=content, img_src=img_src, hint=hint, score=session['score'])       
        
@app.route('/end_game/<username>')
    
def end_game(username):
    global image_counter
    global highscores
    x=session['username']
    score=session['score']
    list_len=len(highscores)
    del highscores[5:list_len]

    highscores.insert(0,
        {'user':x,'score':score}
    )  
    
    data = highscores # limit the array to 5?
    
    with open('data/highscores.json','w') as f:
      json.dump(data, f)
   
    f.close
    
    image_counter=0 # reset image array to position 0
    os.remove(x+".txt") # remove user txt file
    session.pop('username', None) # delete visits
    session.pop('score', None) # delete visits
    
    return render_template('end_game.html', username=username,  score=score)



app.run(host=os.getenv('IP'), port=int (os.getenv('PORT')), debug=True)



