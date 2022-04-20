from boardforlocal import *
from userTwo import *
from userOne import *
from cmu_112_graphics import *
import random

def appStarted(app):
    app.boardlistLocal = createBoard(app)
    app.player1 = UserOne()
    app.player2 = UserTwo()
    app.image1 = app.loadImage('Deck_of_Cards.png')
    app.cardDeck = app.scaleImage(app.image1, 0.4)
    app.image2 = app.loadImage('rockbag.png')
    app.rockBag = app.scaleImage(app.image2, 0.1)

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

    
runApp(width=1550, height=800)