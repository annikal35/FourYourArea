from turtle import color
from board import *
from cmu_112_graphics import *
import random

class User():
    def __init__(self):
        self.blue = 0
        self.red = 0
        self.green = 0
        self.pink = 0
        self.numBlue = 0
        self.numRed = 0
        self.numGreen = 0
        self.numPink = 0
        self.placingCard = {'1':0,'2':0,'3':0,'4':0}
        self.pickingCard = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0}
        self.r = 25
        self.score = 0
        self.currSameColor = 0
        # self.i = random.randint(0,20)

    def frontCard(self,canvas):
        canvas.create_rectangle(750,450,950,750,fill='white', 
                                outline='black', width = 5)
        canvas.create_oval(810-self.r, 500-self.r, 810+self.r, 500+self.r, 
                           fill='blue', outline='blue')
        canvas.create_text(900,500, text = f'{self.numBlue}', fill='black',
                           font = 'Helvetica 30 bold')
        canvas.create_oval(810-self.r, 570-self.r, 810+self.r, 570+self.r, 
                           fill='red', outline='red')
        canvas.create_text(900,570, text = f'{self.numRed}', fill='black',
                           font = 'Helvetica 30 bold')
        canvas.create_oval(810-self.r, 640-self.r, 810+self.r, 640+self.r, 
                           fill='green', outline='green')
        canvas.create_text(900,640, text = f'{self.numGreen}', fill='black',
                           font = 'Helvetica 30 bold')
        canvas.create_oval(810-self.r, 710-self.r, 810+self.r, 710+self.r, 
                           fill='pink', outline = 'pink')
        canvas.create_text(900,710, text = f'{self.numPink}', fill='black',
                           font = 'Helvetica 30 bold')
        

    def backCard(self, canvas):
        canvas.create_rectangle(980,450,1180,750, outline='black',
                                fill = 'white', width=5)
        canvas.create_text(1025,470, text='Picking', fill='black',
                           font = 'Times 16 bold underline')
        firstScore = self.pickingCard['1']
        canvas.create_text(1010,505, text=f'1: {firstScore}', fill='black',
                           font = 'Times 17 bold')
        secondScore = self.pickingCard['2']
        canvas.create_text(1010,540, text=f'2: {secondScore}', fill='black',
                           font = 'Times 17 bold')
        thirdScore = self.pickingCard['3']
        canvas.create_text(1010,575, text=f'3: {thirdScore}', fill='black',
                           font = 'Times 17 bold')
        fourthScore = self.pickingCard['4']
        canvas.create_text(1010,610, text=f'4: {fourthScore}', fill='black',
                           font = 'Times 17 bold')
        fifthScore = self.pickingCard['5']
        canvas.create_text(1010,645, text=f'5: {fifthScore}', fill='black',
                           font = 'Times 17 bold')
        sixthScore = self.pickingCard['6']
        canvas.create_text(1010,680, text=f'6: {sixthScore}', fill='black',
                           font = 'Times 17 bold')
        seventhScore = self.pickingCard['7']
        canvas.create_text(1010,715, text=f'7: {seventhScore}', fill='black',
                           font = 'Times 17 bold')
        canvas.create_line(1080,460,1080,740, fill='black')
        canvas.create_text(1125,470, text='Placing', fill='black',
                           font = 'Times 16 bold underline')
        firstPlacing = self.placingCard['1']
        canvas.create_text(1120,530, text=f'1: {firstPlacing}', fill='black',
                           font = 'Times 20 bold')
        secondPlacing = self.placingCard['2']
        canvas.create_text(1120,590, text=f'2: {secondPlacing}', fill='black',
                           font = 'Times 20 bold')
        thirdPlacing = self.placingCard['3']
        canvas.create_text(1120,650, text=f'3: {thirdPlacing}', fill='black',
                           font = 'Times 20 bold')
        fourthPlacing = self.placingCard['4']
        canvas.create_text(1120,710, text=f'4: {fourthPlacing}', fill='black',
                           font = 'Times 20 bold')
    def currentScore(self, canvas):
        canvas.create_text(1350,50, text='Your Current Rocks', fill='purple',
                           font = 'Helvetica 20 bold italic')
        canvas.create_oval(1300-self.r, 110-self.r, 1300+self.r, 110+self.r, 
                           fill='blue',outline='blue')
        canvas.create_text(1350, 110, text = f' : {self.blue}',fill='black',
                           font = 'Helvetica 25')
        canvas.create_oval(1300-self.r, 170-self.r, 1300+self.r, 170+self.r, 
                           fill='red', outline='red')
        canvas.create_text(1350, 170, text = f' : {self.red}',fill='black',
                           font = 'Helvetica 25')
        canvas.create_oval(1300-self.r, 230-self.r, 1300+self.r, 230+self.r, 
                           fill='green', outline='green')
        canvas.create_text(1350, 230, text = f' : {self.green}',fill='black',
                           font = 'Helvetica 25')
        canvas.create_oval(1300-self.r, 290-self.r, 1300+self.r, 290+self.r, 
                           fill='pink', outline='pink')
        canvas.create_text(1350, 290, text = f' : {self.pink}',fill='black',
                           font = 'Helvetica 25')
        
        # self.pickingCard = getRandomPickingScore()

def getRandomPlacingScore():
        placingSet = [  {'1':2,'2':4,'3':6,'4':7}, {'1':1,'2':3,'3':5,'4':7}, 
                        {'1':1,'2':3,'3':6,'4':8}, {'1':3,'2':4,'3':5,'4':6},
                        {'1':1,'2':2,'3':3,'4':4}, {'1':2,'2':3,'3':5,'4':7},
                        {'1':2,'2':3,'3':4,'4':6}, {'1':2,'2':4,'3':6,'4':7},
                        {'1':3,'2':5,'3':7,'4':9}, {'1':1,'2':2,'3':5,'4':7}, 
                        {'1':0.5,'2':2,'3':4,'4':5}, {'1':2,'2':3,'3':4,'4':5},
                        {'1':1,'2':3,'3':5,'4':6}, {'1':2,'2':4,'3':6,'4':8},
                        {'1':3,'2':4,'3':6,'4':6}, {'1':1,'2':2,'3':4,'4':6},
                        {'1':2,'2':3,'3':5,'4':6}, {'1':1,'2':3,'3':4,'4':6},
                        {'1':0.5,'2':2,'3':3,'4':5}, {'1':2,'2':4,'3':5,'4':6}]
        return random.choice(placingSet)
    
def getRandomPickingScore():
    pickingSet = [  {'1':1,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6},
                    {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7},
                    {'1':1,'2':1,'3':2,'4':4,'5':6,'6':7,'7':8},
                    {'1':1,'2':1,'3':2,'4':4,'5':7,'6':8,'7':10},
                    {'1':1,'2':3,'3':4,'4':5,'5':8,'6':11,'7':15},
                    {'1':2,'2':2,'3':4,'4':6,'5':8,'6':10,'7':12},
                    {'1':1,'2':3,'3':5,'4':7,'5':9,'6':11,'7':13},
                    {'1':2,'2':2,'3':4,'4':8,'5':9,'6':10,'7':14},
                    {'1':1,'2':2,'3':3,'4':6,'5':8,'6':9,'7':11},
                    {'1':1,'2':2,'3':4,'4':5,'5':7,'6':9,'7':12},
                    {'1':1,'2':1,'3':3,'4':4,'5':6,'6':7,'7':9},
                    {'1':2,'2':3,'3':6,'4':7,'5':9,'6':11,'7':13},
                    {'1':1,'2':1,'3':2,'4':4,'5':6,'6':7,'7':8}, 
                    {'1':3,'2':5,'3':6,'4':8,'5':11,'6':13,'7':16},
                    {'1':1,'2':1,'3':2,'4':4,'5':6,'6':7,'7':10},
                    {'1':1,'2':2,'3':2,'4':4,'5':5,'6':8,'7':11},
                    {'1':2,'2':3,'3':4,'4':4,'5':8,'6':10,'7':13},
                    {'1':1,'2':1,'3':2,'4':3,'5':6,'6':8,'7':12},
                    {'1':1,'2':3,'3':5,'4':6,'5':9,'6':13,'7':16},
                    {'1':1,'2':1,'3':2,'4':4,'5':6,'6':7,'7':10}]
    return random.choice(pickingSet)

def appStarted(app):
    app.image1 = app.loadImage('Deck_of_Cards.png')
    app.cardDeck = app.scaleImage(app.image1, 0.6)
    app.image2 = app.loadImage('rockbag.png')
    app.rockBag = app.scaleImage(app.image2, 0.15)
    app.user = User()
    app.boardlist = createBoard(app)

def belowAdjacentCubes(app,cube,index):
    redColor = blueColor = greenColor = pinkColor = 0
    colorList = []
    left = app.boardlist[index-1]
    right = app.boardlist[index+1]
    adjacentY = cube.y+(1.02/11)+50
    for cubeElem in app.boardlist:
        if ((cubeElem.x == cube.x-(0.8/28)+30) and 
                               (cubeElem.y == adjacentY)):
            bottomColor = cubeElem.color
        if ((cubeElem.x == cube.x-(0.8/28)) and 
                               (cubeElem.y == adjacentY)):
            bottomLeftColor = cubeElem.color
        if ((cubeElem.x == cube.x-(1.6/28)+90) and 
                               (cubeElem.y == cube.y+(1.02*2/11)+50)):
            belowColor = cubeElem.color
        if ((cubeElem.x == cube.x-(0.8/28)+90) and 
                               (cubeElem.y == adjacentY)):
            anotherbottomColor = cubeElem.color
    # 1) left adjacent three 
    if ((cube.color != 'white') and (left.color!='white') and 
       (bottomColor!='white') and (bottomLeftColor!='white')):
       colorList.append(cube.color)
       colorList.append(left.color)
       colorList.append(bottomColor)
       colorList.append(bottomLeftColor)
       if 1 < colorList.count("red") < 5:
           redColor += colorList.count("red")
       if 1 < colorList.count("blue") < 5:
           blueColor += colorList.count("blue")
       if 1 < colorList.count("green") < 5:
           greenColor += colorList.count("green")
       if 1 < colorList.count("pink") < 5:
           pinkColor += colorList.count("pink")
    # 2) below adjacent three
    # if ((cube.color != 'white') and (belowColor!='white') and 
    #    (bottomColor!='white') and (anotherbottomColor!='white')):
    # 3) right adjacent three

    if redColor == blueColor == greenColor == pinkColor == 1:
        return 1
    elif ((redColor == 3) or (blueColor == 3) or 
           (greenColor == 3) or (pinkColor == 3)):
           return 3
    elif ((redColor == 4) or (blueColor == 4) or 
           (greenColor == 4) or (pinkColor == 4)):
           return 4
    else:
        return 2



def mousePressed(app, event):
        if (726 <= event.x and event.x<= 974) and (80<=event.y and event.y<=380):
            app.user.placingCard = getRandomPlacingScore()
            app.user.pickingCard = getRandomPickingScore()
            app.user.numBlue = random.randint(0,8)
            app.user.numRed = random.randint(0,8)
            app.user.numGreen = random.randint(0,8)
            app.user.numPink = random.randint(0,8)

        if (1010 <= event.x and event.x<= 1190) and (128 <= event.y and
                                                        event.y<=332):
            rockNum = int(app.getUserInput('How many rocks do you want?'))
            if rockNum >3 or rockNum <1:
                app.showMessage('Please pick 1~3 rocks at a time!')
            else:
                currBlue = random.randint(0, rockNum)
                app.user.blue += currBlue
                currRed = random.randint(0,rockNum-currBlue)
                app.user.red += currRed
                currGreen = random.randint(0,rockNum-currBlue-currRed)
                app.user.green += currGreen
                currPink = random.randint(0,rockNum-currBlue-currRed-currGreen)
                app.user.pink += currPink
        i  = 0
        while i < 52:
            currCube = app.boardlist[i]
            if ((currCube.x <= event.x <= currCube.x + 90) and 
                (currCube.y-0.5*50<= event.y <= currCube.y + 1.5*50)):
                if (((currCube.x < event.x < currCube.x+1.5*30) and 
                            (currCube.y < event.y < currCube.y-0.5*50)) or
                    ((currCube.x+1.5*30 < event.x < currCube.x+90) and 
                            (currCube.y < event.y < currCube.y-0.5*50)) or
                    ((currCube.x < event.x < currCube.x+1.5*30) and 
                            (currCube.y+50 < event.y < currCube.y+1.5*50)) or
                    ((currCube.x+1.5*30 < event.x < currCube.x+90) and 
                            (currCube.y+50 < event.y < currCube.y+1.5*50))):
                    continue
                else:
                    currColor = app.getUserInput('What color of \
                                                rock do you want to put?')
                    if currCube.color != 'white':
                        app.showMessage('This area has been already placed')
                        break
                    elif currColor == 'blue':
                        if app.user.blue == 0:
                            app.showMessage("You don't have blue anymore")
                        else:
                            currCube.color = 'blue'
                            app.user.blue -=1
                            # if i <= 29:
                            #     app.user.score += belowAdjacentCubes(app,currCube,i)
                                # app.user.score += aboveAdjacentCubes(app,currCube,i)
                            # else:

                    elif currColor == 'red':
                        if app.user.red == 0:
                            app.showMessage("You don't have red anymore")
                        else:
                            currCube.color = 'red'
                            app.user.red -=1
                    elif currColor == 'green':
                        if app.user.green == 0:
                            app.showMessage("You don't have green anymore")
                        else:
                            currCube.color = 'green'
                            app.user.green -=1
                    elif currColor == 'pink':
                        if app.user.pink == 0:
                            app.showMessage("You don't have pink anymore")
                        else:
                            currCube.color = 'pink'
                            app.user.pink -=1
                    else:
                        app.showMessage('Please place within given color!')
            i +=1

                

        

def redrawAll(app, canvas):
    canvas.create_rectangle(0,0,app.width, app.height,
                            fill = '#FFFFCC')
    for cube in app.boardlist:
        cube.drawAcube(canvas)
    canvas.create_text(950, 400, text='Current Card',fill='purple',
                       font = 'Helvetica 30 bold italic')
    # user = User()
    app.user.frontCard(canvas)
    app.user.backCard(canvas)
    app.user.currentScore(canvas)
    canvas.create_text(1350, 400, text='Scores',fill='purple',
                       font = 'Helvetica 30 bold italic')
    canvas.create_text(1350, 550, text=f'{app.user.score}',fill='purple',
                       font = 'Helvetica 30 bold italic')
    canvas.create_text(950,50, text='Pick!',fill='purple',
                       font = 'Helvetica 25 bold italic')
    canvas.create_image(850,230,image=ImageTk.PhotoImage(app.cardDeck))
    # imageWidth, imageHeight = app.rockBag.size #248 *300
    canvas.create_image(1100,230,image=ImageTk.PhotoImage(app.rockBag))

        
    
            
runApp(width=1550, height=800)