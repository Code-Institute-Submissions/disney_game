# Disney Game

This project is a character guessing game aimed at 5-12 year olds. The site is built in such a way to enable other disney games to be added in the future. Users can logon select a user name and then play the game. The user is presented with a picture of a disney character and they have to guess the name. Their guesses and scores are recorded and top 5 user scores are displayed on a scoreboard. There is a clue button but this deducts a point from the score.

The site will be developed in flask. A pssword will not be required to access the site. The finshed project will be displayed to heroku.


## UX
The site is aimed at children and is a fun and fairly easy game children can play unsupervised. There is no requirement to login or exchane any personal information. The site should be easy to navigate, bright and blocky design and lots of images. The home page should have animation and movement to help create excitement

### User stories

-I want to see games available to me to play and be connected with them in minimal clicks on any device type and playing the game with minimal instructions

-I an young and may not understand longwords and complicated dialouge

-I want to be able to record my scores and compare my knowledge to other players as well as play at the same time as my friends

-I want game play to be quick and easy to pick up

-I want to have my own user name and receive instant feedback on game progress.

-I want to be able to quit the game easily

-I want to see nice pictures of my favourite disney characters

-I want my parents to understand what I am doing

### Wire Frames
Home page - https://app.moqups.com/tidders2000@gmail.com/VL6zsKhB4b/view/page/a95b9e01a
Login Page - https://app.moqups.com/tidders2000@gmail.com/VL6zsKhB4b/view/page/ae2789af3
Game page - https://app.moqups.com/tidders2000@gmail.com/VL6zsKhB4b/view/page/a0d06493c




## Features

### Existing Features
-Index pages allows users to connect to a game of their choice

-The index page also displays top score by users

-On the login page jquery is used to focus the cursor so its easy to type in a user name

-The game pages displays a disney character picking up the src from a json file

-The game page allows users to enter a guess and see instant feedback by increasing score or printing guesses

-Instructions can be accessed from the game play screen

-If users are stuck they can type in hint and get a clue

-When users exit the game their score is captured and added to the high score json. This is trimmed to six entries and written to json. The index page reads the json file, orders the scores and displays on the scoreboard

-Game data should be saved locally to enable simultaneous play

### features to add

-Search to allow searching of the site
-Allow users to post information and cheats
-more games to be added
-Check username form to ensure names are not duplicated during simultaneous play
-list of active players to be displayed on game screen



## Technologies Used
Flask for app development: http://flask.pocoo.org/
python for game play coding: https://www.python.org/
JQuery for page interaction: https://jquery.com/
bootstrap4 for css layout: https://getbootstrap.com/
CSS animation library: http://devtuts.online/how-to-use-css3-animate-it/
CSS3 for layout
HTML 5 for page coding


## Testing
Basic page template
Tested links – contribute and search not wired up 
Media links show as links
Login goes to login page 
Click logo to return to home, not working
X has no impact
Scoreboard displays in order
Page is responsive

INdex
Images good definition
Login page
No entry, reverts to home page, add required to html
Special chars and numbers work
Responsive
Back button returns to index fine 
Cursor in text field, not working on safari ios

Game page
Cursor in text field, not working on safari ios
Instructions I does not work on ios
User name displayed
Score correct for start, normal and hint
Close button works to score
If user clicks x and comes back session is cleared
All images are displayed
All images are clean and good def
Reverts to score page on array number 24 
X out at random points seems to work ok
Responsive pushes the x down on small views a line
Incorrect answers display
Hint text works
Leaving and retunring to app causes image counter session bug
Closing window causes session issue
Back button works and aloows erturn to session
Session deleted when accessing score page
Close x still leaves text file – manual fix at moment
Scorte page
Correct score displayed
Home page link wortks
Correct scores displayed in correct order
Txt file delted
Score file trimmed to 6 entires
Occasional bug file wiped for score – no fix yet

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment
The site was developed in clodd 9 using flask and intially tested here. When the site was stable I made a heroku app and published to there. This then showed a problem with the json sort feature. I had to improve the code and sort using a custom function. I also noticed the image counter stored as a variable did not work with multiple players so live code had this stored in a session. Cofig and all other files remained the same between dev and production.

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:


## Credits
### Content
Ouroborus for the fancy line:https://stackoverflow.com/questions/40669689/horizontal-line-but-with-the-shadow-at-the-bottom
jack for the animation library: http://devtuts.online/how-to-use-css3-animate-it/
alecxe for solving the json sort issue: https://stackoverflow.com/questions/26924812/python-sort-list-of-json-by-value

### Media
The photos used in this site were obtained from  disney characters https://characters.disney.com/ and various google image searches

#### Acknowledgements
I received inspiration for this project from swiss air for the simple layout and animation, The actual game idea came from assortment of similar games