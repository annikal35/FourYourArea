from boardforlocal import *
from userTwo import *
from userOne import *
from cmu_112_graphics import *
from buttons import *
from TopScoring import *
from BottomScoring import *
import random

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

#################################
# main page for 2 players
#################################

def mode2_keyPressed(app,event):
    if event.key == 'r':
        app.round2 = 1
        app.isGameOver2 = False
        app.player1.score = app.player2.score = 0
        app.player1.numBlue=app.player1.numRed=\
            app.player1.numGreen=app.player1.numPink=0
        app.player2.numBlue=app.player2.numRed=\
            app.player2.numGreen=app.player2.numPink=0
        app.player1.blue=app.player1.red=app.player1.green=app.player1.pink=0
        app.player2.blue=app.player2.red=app.player2.green=app.player2.pink=0
        app.player1.placingCard = {'1':0,'2':0,'3':0,'4':0}
        app.player2.placingCard = {'1':0,'2':0,'3':0,'4':0}
        app.player1.pickingCard = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0}
        app.player2.pickingCard = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0}
        app.player2.cardColor = 'white'
        app.player2.bluecir = 'blue'
        app.player2.redcir = 'red'
        app.player2.greencir = 'green'
        app.player2.pinkcir = 'pink'
        app.player1.cardColor = 'white'
        app.player1.bluecir = 'blue'
        app.player1.redcir = 'red'
        app.player1.greencir = 'green'
        app.player1.pinkcir = 'pink'
        for cube in app.boardlist2:
            cube.color = 'white'
    elif event.key == 'w':
        app.round2 ==4
        app.isGameOver2 = True

def mode2_mousePressed(app, event):
    if 0<=event.x<=150 and 0<=event.y<=50:
        #going back to intro resets the game
        app.mode = 'intro'
        app.round2 = 1
        app.isGameOver2 = False
        app.player1.score = app.player2.score = 0
        app.player1.numBlue=app.player1.numRed=\
            app.player1.numGreen=app.player1.numPink=0
        app.player2.numBlue=app.player2.numRed=\
            app.player2.numGreen=app.player2.numPink=0
        app.player1.blue=app.player1.red=app.player1.green=app.player1.pink=0
        app.player2.blue=app.player2.red=app.player2.green=app.player2.pink=0
        app.player1.placingCard = {'1':0,'2':0,'3':0,'4':0}
        app.player2.placingCard = {'1':0,'2':0,'3':0,'4':0}
        app.player1.pickingCard = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0}
        app.player2.pickingCard = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0}
        app.player2.cardColor = 'white'
        app.player2.bluecir = 'blue'
        app.player2.redcir = 'red'
        app.player2.greencir = 'green'
        app.player2.pinkcir = 'pink'
        app.player1.cardColor = 'white'
        app.player1.bluecir = 'blue'
        app.player1.redcir = 'red'
        app.player1.greencir = 'green'
        app.player1.pinkcir = 'pink'
        for cube in app.boardlist2:
            cube.color = 'white'
    
    # the previous player's card will be hidden
    if (270 <= event.x <=520) and (680 <= event.y <=750):
        app.status2 = 'Player 2'
        app.player1.cardColor = 'black'
        app.player1.bluecir = 'black'
        app.player1.redcir = 'black'
        app.player1.greencir = 'black'
        app.player1.pinkcir = 'black'
        app.player2.cardColor = 'white'
        app.player2.bluecir = 'blue'
        app.player2.redcir = 'red'
        app.player2.greencir = 'green'
        app.player2.pinkcir = 'pink'
        app.player1.blue=app.player1.red=app.player1.green=app.player1.pink=0
    if (1250 <= event.x <=1500) and (680 <= event.y <=750):
        app.status2 = 'Player 1'
        app.player2.cardColor = 'black'
        app.player2.bluecir = 'black'
        app.player2.redcir = 'black'
        app.player2.greencir = 'black'
        app.player2.pinkcir = 'black'
        app.player1.cardColor = 'white'
        app.player1.bluecir = 'blue'
        app.player1.redcir = 'red'
        app.player1.greencir = 'green'
        app.player1.pinkcir = 'pink'
        app.player2.blue=app.player2.red=app.player2.green=app.player2.pink=0
        if app.round2 == 4:
            app.isGameOver2 = True
        else:
            app.round2 +=1

    if app.status2 == 'Player 1':
        app.player2.blue=app.player2.red=app.player2.green=app.player2.pink=0
        if (176 <= event.x<= 424) and (350<=event.y<=650):
            app.player1.placingCard = getRandomPlacingScore()
            app.player1.pickingCard = getRandomPickingScore()
            app.player1.numBlue = random.randint(1,4)
            app.player1.numRed = random.randint(1,4)
            app.player1.numGreen = random.randint(1,4)
            app.player1.numPink = random.randint(1,4)

        if (350 <= event.x <= 530) and (378 <= event.y<=602):
            rockNum = app.getUserInput('How many rocks do you want?')
            if rockNum not in '0123456789':
                    app.showMessage('Please put proper numbers')
            else:
                rockNum = int(rockNum)
                if rockNum >3 or rockNum <1:
                    app.showMessage('Please pick 1~3 rocks at a time!')
                elif rockNum == 1:
                    colorList = ['blue', 'red','green','pink']
                    currCol = random.choice(colorList)
                    if currCol == 'blue':
                        app.user.blue +=1
                    if currCol == 'red':
                        app.user.red +=1
                    if currCol == 'green':
                        app.user.green +=1
                    if currCol == 'pink':
                        app.user.pink +=1
                else:
                    currBlue = random.randint(0, rockNum)
                    app.player1.blue += currBlue
                    currRed = random.randint(0,rockNum-currBlue)
                    app.player1.red += currRed
                    currGreen = random.randint(0,rockNum-currBlue-currRed)
                    app.player1.green += currGreen
                    if app.player1.blue==app.player1.red==app.player1.green==0:
                            currPink = rockNum
                    else:
                        currPink = random.randint(0,rockNum-currBlue-\
                        currRed-currGreen)
                    app.player1.pink += currPink

            if ((app.player1.blue > app.player1.numBlue)or
               (app.player1.red>app.player1.numRed)or
               (app.player1.green>app.player1.numGreen)or
               (app.player1.pink>app.player1.numPink)):
                app.showMessage("You went over the limit! Press stop to turn")

        if (450<=event.x<=570) and (40<=event.y<=140):
            #picking score
            total=app.player1.blue+app.player1.red+app.player1.green\
                              +app.player1.pink
            if total == 1:
                app.player1.score += app.player1.pickingCard['1']
            elif total == 2:
                app.player1.score += app.player1.pickingCard['2']
            elif total == 3:
                app.player1.score += app.player1.pickingCard['3']
            elif total == 4:
                app.player1.score += app.player1.pickingCard['4']
            elif total == 5:
                app.player1.score += app.player1.pickingCard['5']
            elif total == 6:
                app.player1.score += app.player1.pickingCard['6']
            elif total == 7:
                app.player1.score += app.player1.pickingCard['7']

        #placing score
        for currCube in app.boardlist2:
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
                    break
                else:
                    currColor = app.getUserInput('What color of \
                                                rock do you want to put?')
                    if currCube.color != 'white':
                        app.showMessage('This area has been already placed')
                        break
                    elif currColor == 'blue':
                        if app.player1.blue == 0:
                            app.showMessage("You don't have blue anymore")
                        else:
                            currCube.color = 'blue'
                            app.player1.blue -=1
                            app.coloredCube1.append(currCube.color)
                            if len(app.coloredCube1) >=4:
                                index = app.boardlist2.index(currCube)
                                if 0 <= index <= 3:
                                    app.player1.score += belowAdjforTop(app,
                                                    currCube,index)
                                    break
                                if 4 <= index <= 21:
                                    app.player1.score += belowAdjforTop(app,
                                                    currCube,index)
                                    
                                    app.player1.score += aboveAdjforTop(
                                            app,currCube,index)
                                if 22 <= index <= 29:
                                    app.player1.score += belowAdjforBottom(
                                        app,currCube, index)
                                    app.player1.score += aboveAdjforTop(
                                            app,currCube,index)
                                    break 
                                if 30 <= index <= 47:
                                    app.player1.score += belowAdjforBottom(
                                        app,currCube, index)
                                    app.player1.score += aboveAdjforBottom(
                                            app, currCube, index)
                                    break
                                else:
                                    app.player1.score += aboveAdjforBottom(app, 
                                                    currCube, index)
                                    break
                        break
                    elif currColor == 'red':
                        if app.player1.red == 0:
                            app.showMessage("You don't have red anymore")
                        else:
                            currCube.color = 'red'
                            app.player1.red -=1
                            app.coloredCube1.append(currCube.color)
                            if len(app.coloredCube1) >=4:
                                index = app.boardlist2.index(currCube)
                                if 0 <= index <= 3:
                                    app.player1.score += belowAdjforTop(app,
                                                    currCube,index)
                                    break
                                if 4 <= index <= 21:
                                    app.player1.score += belowAdjforTop(app,
                                                    currCube,index)
                                    
                                    app.player1.score += aboveAdjforTop(
                                            app,currCube,index)
                                if 22 <= index <= 29:
                                    app.player1.score += belowAdjforBottom(
                                        app,currCube, index)
                                    app.player1.score += aboveAdjforTop(
                                            app,currCube,index)
                                    break 
                                if 30 <= index <= 47:
                                    app.player1.score += belowAdjforBottom(
                                        app,currCube, index)
                                    app.player1.score += aboveAdjforBottom(
                                            app, currCube, index)
                                    break
                                else:
                                    app.player1.score += aboveAdjforBottom(app, 
                                                    currCube, index)
                                    break
                        break
                    elif currColor == 'green':
                        if app.player1.green == 0:
                            app.showMessage("You don't have green anymore")
                        else:
                            currCube.color = 'green'
                            app.player1.green -=1
                            app.coloredCube1.append(currCube.color)
                            if len(app.coloredCube1) >=4:
                                index = app.boardlist2.index(currCube)
                                if 0 <= index <= 3:
                                    app.player1.score += belowAdjforTop(app,
                                                    currCube,index)
                                    break
                                if 4 <= index <= 21:
                                    app.player1.score += belowAdjforTop(app,
                                                    currCube,index)
                                    
                                    app.player1.score += aboveAdjforTop(
                                            app,currCube,index)
                                if 22 <= index <= 29:
                                    app.player1.score += belowAdjforBottom(
                                        app,currCube, index)
                                    app.player1.score += aboveAdjforTop(
                                            app,currCube,index)
                                    break 
                                if 30 <= index <= 47:
                                    app.player1.score += belowAdjforBottom(
                                        app,currCube, index)
                                    app.player1.score += aboveAdjforBottom(
                                            app, currCube, index)
                                    break
                                else:
                                    app.player1.score += aboveAdjforBottom(app, 
                                                    currCube, index)
                                    break
                        break
                    elif currColor == 'pink':
                        if app.player1.pink == 0:
                            app.showMessage("You don't have pink anymore")
                        else:
                            currCube.color = 'pink'
                            app.player1.pink -=1
                            app.coloredCube1.append(currCube.color)
                            if len(app.coloredCube1) >=4:
                                index = app.boardlist2.index(currCube)
                                if 0 <= index <= 3:
                                    app.player1.score += belowAdjforTop(app,
                                                    currCube,index)
                                    break
                                if 4 <= index <= 21:
                                    app.player1.score += belowAdjforTop(app,
                                                    currCube,index)
                                    
                                    app.player1.score += aboveAdjforTop(
                                            app,currCube,index)
                                if 22 <= index <= 29:
                                    app.player1.score += belowAdjforBottom(
                                        app,currCube, index)
                                    app.player1.score += aboveAdjforTop(
                                            app,currCube,index)
                                    break 
                                if 30 <= index <= 47:
                                    app.player1.score += belowAdjforBottom(
                                        app,currCube, index)
                                    app.player1.score += aboveAdjforBottom(
                                            app, currCube, index)
                                    break
                                else:
                                    app.player1.score += aboveAdjforBottom(app, 
                                                    currCube, index)
                                    break
                        break
                    else:
                        app.showMessage('Please place within given color!')
    else:
        app.player1.blue=app.player1.red=app.player1.green=app.player1.pink=0
        if (1176 <= event.x<= 1424) and (350<=event.y<=650):
            app.player2.placingCard = getRandomPlacingScore()
            app.player2.pickingCard = getRandomPickingScore()
            app.player2.numBlue = random.randint(1,4)
            app.player2.numRed = random.randint(1,4)
            app.player2.numGreen = random.randint(1,4)
            app.player2.numPink = random.randint(1,4)

        if (1350 <= event.x <= 1530) and (398 <= event.y<=602):
            rockNum = app.getUserInput('How many rocks do you want?')
            if rockNum not in '0123456789':
                    app.showMessage('Please put proper numbers')
            else:
                rockNum = int(rockNum)
                if rockNum >3 or rockNum <1:
                    app.showMessage('Please pick 1~3 rocks at a time!')
                elif rockNum == 1:
                    colorList = ['blue', 'red','green','pink']
                    currCol = random.choice(colorList)
                    if currCol == 'blue':
                        app.user.blue +=1
                    if currCol == 'red':
                        app.user.red +=1
                    if currCol == 'green':
                        app.user.green +=1
                    if currCol == 'pink':
                        app.user.pink +=1
                else:
                    currBlue = random.randint(0, rockNum)
                    app.player2.blue += currBlue
                    currRed = random.randint(0,rockNum-currBlue)
                    app.player2.red += currRed
                    currGreen = random.randint(0,rockNum-currBlue-currRed)
                    app.player2.green += currGreen
                    if app.player2.blue==app.player2.red==app.player2.green==0:
                            currPink = rockNum
                    else:
                        currPink = random.randint(0,rockNum-currBlue-\
                        currRed-currGreen)
                    app.player2.pink += currPink
                    
            if ((app.player2.blue > app.player2.numBlue)or
               (app.player2.red>app.player2.numRed)or
               (app.player2.green>app.player2.numGreen)or
               (app.player2.pink>app.player2.numPink)):
                app.showMessage("You went over the limit! Press stop to turn")
        
        if (1000<=event.x<=1120) and (40<=event.y<=140):
            #picking score
            total=app.player2.blue+app.player2.red+app.player2.green\
                              +app.player2.pink
            if total == 1:
                app.player2.score += app.player2.pickingCard['1']
            elif total == 2:
                app.player2.score += app.player2.pickingCard['2']
            elif total == 3:
                app.player2.score += app.player2.pickingCard['3']
            elif total == 4:
                app.player2.score += app.player2.pickingCard['4']
            elif total == 5:
                app.player2.score += app.player2.pickingCard['5']
            elif total == 6:
                app.player2.score += app.player2.pickingCard['6']
            elif total == 7:
                app.player2.score += app.player2.pickingCard['7']

        for currCube in app.boardlist2:
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
                    break
                else:
                    currColor = app.getUserInput('What color of \
                                                rock do you want to put?')
                    if currCube.color != 'white':
                        app.showMessage('This area has been already placed')
                        break
                    elif currColor == 'blue':
                        if app.player2.blue == 0:
                            app.showMessage("You don't have blue anymore")
                        else:
                            currCube.color = 'blue'
                            app.player2.blue -=1
                            app.coloredCube1.append(currCube.color)
                            if len(app.coloredCube1) >=4:
                                index = app.boardlist2.index(currCube)
                                if 0 <= index <= 3:
                                    app.player2.score += belowAdjforTop(app,
                                                    currCube,index)
                                    break
                                if 4 <= index <= 21:
                                    app.player2.score += belowAdjforTop(app,
                                                    currCube,index)
                                    
                                    app.player2.score += aboveAdjforTop(
                                            app,currCube,index)
                                if 22 <= index <= 29:
                                    app.player2.score += belowAdjforBottom(
                                        app,currCube, index)
                                    app.player2.score += aboveAdjforTop(
                                            app,currCube,index)
                                    break 
                                if 30 <= index <= 47:
                                    app.player2.score += belowAdjforBottom(
                                        app,currCube, index)
                                    app.player2.score += aboveAdjforBottom(
                                            app, currCube, index)
                                    break
                                else:
                                    app.player2.score += aboveAdjforBottom(app, 
                                                    currCube, index)
                                    break
                        break
                    elif currColor == 'red':
                        if app.player2.red == 0:
                            app.showMessage("You don't have red anymore")
                        else:
                            currCube.color = 'red'
                            app.player2.red -=1
                            app.coloredCube1.append(currCube.color)
                            if len(app.coloredCube1) >=4:
                                index = app.boardlist2.index(currCube)
                                if 0 <= index <= 3:
                                    app.player2.score += belowAdjforTop(app,
                                                    currCube,index)
                                    break
                                if 4 <= index <= 21:
                                    app.player2.score += belowAdjforTop(app,
                                                    currCube,index)
                                    
                                    app.player2.score += aboveAdjforTop(
                                            app,currCube,index)
                                if 22 <= index <= 29:
                                    app.player2.score += belowAdjforBottom(
                                        app,currCube, index)
                                    app.player2.score += aboveAdjforTop(
                                            app,currCube,index)
                                    break 
                                if 30 <= index <= 47:
                                    app.player2.score += belowAdjforBottom(
                                        app,currCube, index)
                                    app.player2.score += aboveAdjforBottom(
                                            app, currCube, index)
                                    break
                                else:
                                    app.player2.score += aboveAdjforBottom(app, 
                                                    currCube, index)
                                    break
                        break
                    elif currColor == 'green':
                        if app.player2.green == 0:
                            app.showMessage("You don't have green anymore")
                        else:
                            currCube.color = 'green'
                            app.player2.green -=1
                            app.coloredCube1.append(currCube.color)
                            if len(app.coloredCube1) >=4:
                                index = app.boardlist2.index(currCube)
                                if 0 <= index <= 3:
                                    app.player2.score += belowAdjforTop(app,
                                                    currCube,index)
                                    break
                                if 4 <= index <= 21:
                                    app.player2.score += belowAdjforTop(app,
                                                    currCube,index)
                                    
                                    app.player2.score += aboveAdjforTop(
                                            app,currCube,index)
                                if 22 <= index <= 29:
                                    app.player2.score += belowAdjforBottom(
                                        app,currCube, index)
                                    app.player2.score += aboveAdjforTop(
                                            app,currCube,index)
                                    break 
                                if 30 <= index <= 47:
                                    app.player2.score += belowAdjforBottom(
                                        app,currCube, index)
                                    app.player2.score += aboveAdjforBottom(
                                            app, currCube, index)
                                    break
                                else:
                                    app.player2.score += aboveAdjforBottom(app, 
                                                    currCube, index)
                                    break
                        break
                    elif currColor == 'pink':
                        if app.player2.pink == 0:
                            app.showMessage("You don't have pink anymore")
                        else:
                            currCube.color = 'pink'
                            app.player2.pink -=1
                            app.coloredCube1.append(currCube.color)
                            if len(app.coloredCube1) >=4:
                                index = app.boardlist2.index(currCube)
                                if 0 <= index <= 3:
                                    app.player2.score += belowAdjforTop(app,
                                                    currCube,index)
                                    break
                                if 4 <= index <= 21:
                                    app.player2.score += belowAdjforTop(app,
                                                    currCube,index)
                                    
                                    app.player2.score += aboveAdjforTop(
                                            app,currCube,index)
                                if 22 <= index <= 29:
                                    app.player2.score += belowAdjforBottom(
                                        app,currCube, index)
                                    app.player2.score += aboveAdjforTop(
                                            app,currCube,index)
                                    break 
                                if 30 <= index <= 47:
                                    app.player2.score += belowAdjforBottom(
                                        app,currCube, index)
                                    app.player2.score += aboveAdjforBottom(
                                            app, currCube, index)
                                    break
                                else:
                                    app.player2.score += aboveAdjforBottom(app, 
                                                    currCube, index)
                                    break
                        break
                    else:
                        app.showMessage('Please place within given color!')

def mode2_timerFired(app):
    if app.isGameOver2:
        return

def mode2_redrawAll(app, canvas):
    canvas.create_rectangle(0,0,app.width, app.height,
                            fill = '#FFFFCC')
    for cube in app.boardlist2:
        cube.drawAcube(canvas)
    app.player1.player1(canvas)
    app.player1.frontCard(canvas)
    app.player1.backCard(canvas)
    app.player1.currentRocks(canvas)
    app.player2.player2(canvas)
    app.player2.frontCard(canvas)
    app.player2.backCard(canvas)
    app.player2.currentRocks(canvas)
    canvas.create_image(300,500,image=ImageTk.PhotoImage(app.cardDeck2))
    canvas.create_image(440,500,image=ImageTk.PhotoImage(app.rockBag2))
    canvas.create_image(1300,500,image=ImageTk.PhotoImage(app.cardDeck2))
    canvas.create_image(1440,500,image=ImageTk.PhotoImage(app.rockBag2))
    # cardDeck image is from 
    # https://clipartpng.com/?2722,deck-of-cards-png-clip-art-image
    # rockbag image is from https://www.pngwing.com/en/free-png-zgoig/download
    canvas.create_text(300, 630, text='Scores',fill='purple',
                       font = 'Helvetica 30 bold italic')
    canvas.create_text(1300, 630, text='Scores',fill='purple',
                       font = 'Helvetica 30 bold italic')
    canvas.create_text(390, 630, text=f' : {app.player1.score}',fill='purple',
                       font = 'Helvetica 30 bold italic')
    canvas.create_text(1390, 630, text=f' : {app.player2.score}',fill='purple',
                       font = 'Helvetica 30 bold italic')
    canvas.create_text(360,380, text='Pick!',fill='purple',
                       font = 'Helvetica 25 bold italic')
    canvas.create_text(1360,380, text='Pick!',fill='purple',
                       font = 'Helvetica 25 bold italic')
    canvas.create_text(780,700, text=f'Current: {app.status2}',fill='purple',
                       font = 'Helvetica 25 bold italic')
    canvas.create_text(780,750, text=f'Round: {app.round2}',fill='purple',
                       font = 'Helvetica 25 bold italic')
    for button in app.buttons2:
        button.render(canvas)
    if app.isGameOver2:
        if app.player1.score > app.player2.score:
            canvas.create_rectangle(app.width/3, app.height/3,
                      app.width*(2/3),app.height*(2/3),fill = 'white')
            canvas.create_text(app.width/2, app.height/2, text="Player1 won!",
                            font = "Arial 60 bold", fill = 'black')
        else:
            canvas.create_rectangle(app.width/3, app.height/3,
                      app.width*(2/3),app.height*(2/3),fill = 'white')
            canvas.create_text(app.width/2, app.height/2, text="Player2 won!",
                            font = "Arial 60 bold", fill = 'black')

    
