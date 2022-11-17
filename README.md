# Battleboats !

This is my third portfolio project for Code Institute.

I chose to build a classic game of Battleships using Python and the CI python template.

This site is **not** tablet or mobile responsive.

Link to my [Github Repo](https://github.com/Rasmus-Dahlkvist/Battleboats)

Link to my [Live Site](https://new-battleboats-rd.herokuapp.com/)

![Full screen heroku image](/readme-images/heroku-full-screen.png)

---

## Design

### Workflow

Once the terminal has started my code :
* You are in a menu with three choices.
1. Easy Mode starts a new game with 15 turns.
2. Hard Mode starts a new game with 10 turns.
* When game is won click enter and you will come back to the menu.
* When game is lost click enter and you will be back in the menu.
3. Rule Book takes you to the rules section.
* When you are done reading about the rules press enter to go back to the menu.

Check out my flowchart below.

![Flowchart image](/readme-images/flowchart.png)

### Users pov

This does not belong in this project but i changed some colors on the live site and gave the run program button a new margin just to make it a little easier on the eyes.
For this i used [ColorSpace](https://mycolor.space/)
![Color palette](/readme-images/colorspace-palette.png)

0. At the top you will see a simple "logo" in both the menu and in the game screen but **not** in rule book.

1. This is what you will experience when you start this program
    * You will see a menu with three choices.
      * Use the **Arrow** keys to **navigate** and **Enter** key on your keyboard to **Select**.
        * These "arrows" **> <** will show you where you are in the menu. 
        
      * Menu options :
        * Easy Mode starts the game with 15 Turns.
        * Hard Mode starts the game with 10 turns.
        * Rule Book leads to a page that only shows the rules.

![Game menu](/readme-images/menu.png)

2. This is what you will see when you have selected either **Easy mode** or **Hard Mode** (except for Turn) in the menu.
    * The controls.
    * Reminders of what the "graphics" mean.
    * The statistics of what has happened so far in the game.
    * The gamespace.
      * The gamespace is five columns and five rows big.
        * The cursor/sight is a plus sign and starts in the center of the gamespace. 
        * You can "shoot" anywhere in the gamespace using the **Arrow keys** and **Space key**.
        * When "shot" the stats will change and the gamespace will be updated.
        * If you shoot in the same spot twice or press an invalid button you will get a message and "Turn" will **not** update.
        * Rinse and repeat and you will eventually win or lose.
          * When you win or lose the cursor/sight will dissappear to reveal the full gamespace and you will be greeted a message and prompted to press the **Enter key**
            * When **Enter key** is pressed you go back to the menu. 

![Gameplay image of new game](/readme-images/new-game.png)
![Gameplay image of won game](/readme-images/easy-win.png)
![Gameplay image of lost game](/readme-images/easy-lost.png)

3. This is what you will see when you have selected **Rule Book** in the menu.
    * The game controls and rules.
    * A message that prompts you to press **Enter key** to go back to the menu.

![Rule book image](/readme-images/rules.png)

4. You have the freedom to check the rules or play the game as many times as you like.

---

## Testing

* For testing the functionality of this code i mainly used [Replit](https://replit.com/) just because it is fast and easy and i have some experience with python code in [Replit](https://replit.com/) from before
  * I also tested the functionality in the [Gitpod](https://www.gitpod.io/) terminal.
  * This type of functional testing was done everytime i changed something or added something new in the code.

For testing the code for spelling errors etcetera i used [Pythonchecker](https://www.pythonchecker.com/)

And when i heard that Code institute had created their own [CI Python Linter](https://pep8ci.herokuapp.com/) i started using that instead.

![CI Python Test](/readme-images/python-test.png)

### Bugs :

* Potential bug:

	I believe that this "graphical bug" has something to do with me clearing the terminal.
	When testing in replit and gitpod terminals it is barely a problem.

	Replit and Gitpod symptoms: Every seventh buttonclick (or so) makes all the text in the terminal dissappear for maybe half a second and then reappear.

	In Heroko this is much more present and happens more often.

	Also in Heroku the "graphics" get "messy" for half a second sometimes.

  With that said, I have not experienced any error message or crash because of this problem.

All of the bugs i found (except for the potential bug) was fixed while building this program due to the nature of python code in general (if something goes wrong the program will most likely stop working).

---

## Deployment

This program was deployed using [Heroku](https://www.heroku.com/platform) together with [GitHub](https://github.com/)

This is how to deploy to [Heroku](https://www.heroku.com/platform) :
1. Create an account and log in.
2. Find the dropdown menu that says "new" and click it.
3. Click on "Create new app" 
4. Choose a name for your app.
5. Choose a region.
6. Click "create app"
7. In the settings tab click on Reveal Config Vars.
8. In the key-section write "PORT".
9. In the value-section write "8000".
* There were no credentials required for this app.
10. Click Add buildpack and choose python and nodejs in that order.
11. Find the deploy tab and click it. 
12. Select Github-Connect to Github.
13. Enter your repository name and click Search.
14. Click connect.
* You get the choice of manual or automatic deployment
15. I chose manual deployment because automatic did not seem to be reliable for me.
* For **manual deployment** remember that you need to deploy again **every time** you **push** your code to github.
* Once you choose a deployment method your app will be built and a "open app" button will appear.
16. Click the button to open your app.
* After this you can find several ways to open your app.

### Fork Repo :

When you are in the repository you want to fork:

Locate the "Fork" button on the top right of the page and click it

### Create Local Clone :

1. Under the repository name, click on the ‘code’ tab
2. In the clone box, HTTPS tab, click on the clipboard icon
3. In your IED open GitBash
4. Changed the current working directory to the location you want the cloned directory to be made
5. Type ‘git clone’ and then paste the URL copied from GitHub
6. Press enter and the local clone will be created


---

## Technologies used

* For changing colors and margin in layout.html
  * ColorSpace
  * Devtools
  * Html
  * Css

* For installing import modules to workspace
  * Pip3

* For making the flowchart
  * LibreOffice Draw

* For Testing
  * Replit
  * Pythonchecker
  * CI Python Linter

* For this readme
  * Markdown

* For Writing, Saving, and Deploying workspace
  * Gitpod
  * GitHub
  * Git
  * Heroku
  * Python

* Python libraries and imports
  * import os was used for clearing the terminal
  * from random import randint was used to randomize where the boats were located
  * import numpy as np was used to create the matrix
  * from getkey import getkey, keys was used to make the arrow keys, space key and enter key work

---

## Credits

This project was really hard but it would have been a lot harder if i had no experience in python from before.

* I learned lot of tricks i used for this project in "programming 1 python" on Hermods.
* I used [Copyassignment](https://copyassignment.com/battleship-game-code-in-python/) to get an idea of the logic used to build a program like this.
* I used the matrix found at [Tutorialspoint](https://www.tutorialspoint.com/python_data_structure/python_matrix.htm)
* For problemsolving i used [W3Schools](https://www.w3schools.com/python/)
* Inspiration for this readme and the deployment section in particular [cmikedev](https://github.com/cmikedev/battleship)
* Help with flowchart [Programiz](https://www.programiz.com/article/flowchart-programming)

---

### Special thanks

* To my mentor Harry for feedback and tips.
* To the people in slack channel # ask-us-anything.
* To my friend Martin for support and help with avoiding imposter-syndrome.

