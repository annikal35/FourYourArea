from boardforlocal import *
from userTwo import *
from userOne import *
from cmu_112_graphics import *
from buttons import *
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
    
def appStarted(app):
    app.boardlistLocal = createBoard(app)
    app.player1 = UserOne()
    app.player2 = UserTwo()
    app.image1 = app.loadImage('Deck_of_Cards.png')
    app.cardDeck = app.scaleImage(app.image1, 0.4)
    app.image2 = app.loadImage('rockbag.png')
    app.rockBag = app.scaleImage(app.image2, 0.1)
    app.buttons = [
      Button(270, 680, 520, 750, "STOP!"),
      Button(1250, 680, 1500, 750, "STOP!")
    #   Button(insert, params, here, pls, "Goodbye!", thisIsAnotheFunction),
   ]
    app.status = 'Player 1'

def mousePressed(app, event):
    if (270 <= event.x <=520) and (680 <= event.y <=750):
        app.status = 'Player 2'
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
    if (1250 <= event.x <=1500) and (680 <= event.y <=750):
        app.status = 'Player 1'
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
        # if (726 <= event.x and event.x<= 974) and (80<=event.y and event.y<=380):
        #     app.user.placingCard = getRandomPlacingScore()
        #     app.user.pickingCard = getRandomPickingScore()
        #     app.user.numBlue = random.randint(0,8)
        #     app.user.numRed = random.randint(0,8)
        #     app.user.numGreen = random.randint(0,8)
        #     app.user.numPink = random.randint(0,8)

        # if (1010 <= event.x and event.x<= 1190) and (128 <= event.y and
        #                                                 event.y<=332):
        #     rockNum = int(app.getUserInput('How many rocks do you want?'))
        #     if rockNum >3 or rockNum <1:
        #         app.showMessage('Please pick 1~3 rocks at a time!')
        #     else:
        #         currBlue = random.randint(0, rockNum)
        #         app.user.blue += currBlue
        #         currRed = random.randint(0,rockNum-currBlue)
        #         app.user.red += currRed
        #         currGreen = random.randint(0,rockNum-currBlue-currRed)
        #         app.user.green += currGreen
        #         currPink = random.randint(0,rockNum-currBlue-currRed-currGreen)
        #         app.user.pink += currPink
        # i  = 0
        # while i < 52:
        #     currCube = app.boardlist[i]
        #     if ((currCube.x <= event.x <= currCube.x + 90) and 
        #         (currCube.y-0.5*50<= event.y <= currCube.y + 1.5*50)):
        #         if (((currCube.x < event.x < currCube.x+1.5*30) and 
        #                     (currCube.y < event.y < currCube.y-0.5*50)) or
        #             ((currCube.x+1.5*30 < event.x < currCube.x+90) and 
        #                     (currCube.y < event.y < currCube.y-0.5*50)) or
        #             ((currCube.x < event.x < currCube.x+1.5*30) and 
        #                     (currCube.y+50 < event.y < currCube.y+1.5*50)) or
        #             ((currCube.x+1.5*30 < event.x < currCube.x+90) and 
        #                     (currCube.y+50 < event.y < currCube.y+1.5*50))):
        #             continue
        #         else:
        #             currColor = app.getUserInput('What color of \
        #                                         rock do you want to put?')
        #             if currCube.color != 'white':
        #                 app.showMessage('This area has been already placed')
        #                 break
        #             elif currColor == 'blue':
        #                 if app.user.blue == 0:
        #                     app.showMessage("You don't have blue anymore")
        #                 else:
        #                     currCube.color = 'blue'
        #                     app.user.blue -=1
        #                 break
        #             elif currColor == 'red':
        #                 if app.user.red == 0:
        #                     app.showMessage("You don't have red anymore")
        #                 else:
        #                     currCube.color = 'red'
        #                     app.user.red -=1
        #                 break
        #             elif currColor == 'green':
        #                 if app.user.green == 0:
        #                     app.showMessage("You don't have green anymore")
        #                 else:
        #                     currCube.color = 'green'
        #                     app.user.green -=1
        #                 break
        #             elif currColor == 'pink':
        #                 if app.user.pink == 0:
        #                     app.showMessage("You don't have pink anymore")
        #                 else:
        #                     currCube.color = 'pink'
        #                     app.user.pink -=1
        #                 break
        #             else:
        #                 app.showMessage('Please place within given color!')
        #                 break
        #     i +=1


def redrawAll(app, canvas):
    canvas.create_rectangle(0,0,app.width, app.height,
                            fill = '#FFFFCC')
    for cube in app.boardlistLocal:
        cube.drawAcube(canvas)
    app.player1.player1(canvas)
    app.player1.frontCard(canvas)
    app.player1.backCard(canvas)
    app.player1.currentRocks(canvas)
    app.player2.player2(canvas)
    app.player2.frontCard(canvas)
    app.player2.backCard(canvas)
    app.player2.currentRocks(canvas)
    canvas.create_image(300,500,image=ImageTk.PhotoImage(app.cardDeck))
    canvas.create_image(440,500,image=ImageTk.PhotoImage(app.rockBag))
    canvas.create_image(1300,500,image=ImageTk.PhotoImage(app.cardDeck))
    canvas.create_image(1440,500,image=ImageTk.PhotoImage(app.rockBag))
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
    canvas.create_text(780,700, text=f'Current: {app.status}',fill='purple',
                       font = 'Helvetica 25 bold italic')
    for button in app.buttons:
        button.render(canvas)

    
runApp(width=1550, height=800)