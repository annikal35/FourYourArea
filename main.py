from board import *
from userforAI import *
from cmu_112_graphics import *
from TopScoringAI import *
from BottomScoringAI import *
from minimax import *
from buttons import *
import random
import copy

def appStarted(app):
    app.image1 = app.loadImage('Deck_of_Cards.png')
    app.cardDeck = app.scaleImage(app.image1, 0.6)
    app.image2 = app.loadImage('rockbag.png')
    app.rockBag = app.scaleImage(app.image2, 0.15)
    app.user = User()
    app.AI = AI()
    app.boardlist = createBoard(app)
    app.coloredCube = []
    app.buttons = [
      Button(1250, 680, 1500, 750, "STOP!"),
    ]
    app.possibleMoves = []
    app.status = 'User'
    app.round = 1


def mousePressed(app, event):
    if 1250 <= event.x <= 1500 and 680 <= event.y <= 750:
        app.status = 'AI'
    
    if app.status == 'User':
        app.AI.blue = app.AI.red = app.AI.green = app.AI.pink = 0
        if (726 <= event.x and event.x<= 974) and (80<=event.y and event.y<=380):
            app.user.placingCard = getRandomPlacingScore()
            app.user.pickingCard = getRandomPickingScore()
            app.user.numBlue = random.randint(0,4)
            app.user.numRed = random.randint(0,4)
            app.user.numGreen = random.randint(0,4)
            app.user.numPink = random.randint(0,4)

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
        for currCube in app.boardlist:
            index = app.boardlist.index(currCube)
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
                        if app.user.blue == 0:
                            app.showMessage("You don't have blue anymore")
                        else:
                            currCube.color = 'blue'
                            app.user.blue -=1
                            app.coloredCube.append(currCube.color)
                            print(app.coloredCube)
                            if len(app.coloredCube) >= 4:
                                if 0 <= index <= 3:
                                    app.user.score += belowAdjforTopAI(app,
                                                    currCube,index)
                                    break
                                if 4 <= index <= 29:
                                    app.user.score += belowAdjforTopAI(app,
                                                    currCube,index)
                                    if app.user.score == 0:
                                        app.user.score += aboveAdjforTopAI(app,
                                            currCube,index)
                                        break
                                    if app.user.score == 0:
                                        app.user.score += belowAdjforBottomAI(app,
                                                       currCube, index)
                                        break
                                    break 
                                if 30 <= index <= 47:
                                    app.user.score += belowAdjforBottomAI(app,
                                                       currCube, index)
                                    if app.user.score == 0:
                                        app.user.score += aboveAdjforBottomAI(app, 
                                                       currCube, index)
                                        break
                                    break
                                else:
                                    app.user.score += aboveAdjforBottomAI(app, 
                                                       currCube, index)
                                    break
                        break
                    elif currColor == 'red':
                        if app.user.red == 0:
                            app.showMessage("You don't have red anymore")
                        else:
                            currCube.color = 'red'
                            app.user.red -=1
                            app.coloredCube.append(currCube.color)
                            print(app.coloredCube)
                            if len(app.coloredCube) >= 4:
                                if 0 <= index <= 3:
                                    app.user.score += belowAdjforTopAI(app,
                                                    currCube,index)
                                    break
                                if 4 <= index <= 29:
                                    app.user.score += belowAdjforTopAI(app,
                                                    currCube,index)
                                    if app.user.score == 0:
                                        app.user.score += aboveAdjforTopAI(app,
                                            currCube,index)
                                        break
                                    if app.user.score == 0:
                                        app.user.score += belowAdjforBottomAI(app,
                                                       currCube, index)
                                        break
                                    break
                                if 30 <= index <= 47:
                                    app.user.score += belowAdjforBottomAI(app,
                                                       currCube, index)
                                    if app.user.score == 0:
                                        app.user.score += aboveAdjforBottomAI(app, 
                                                       currCube, index)
                                        break
                                    break
                                else:
                                    app.user.score += aboveAdjforBottomAI(app, 
                                                       currCube, index)
                                    break
                        break
                    elif currColor == 'green':
                        if app.user.green == 0:
                            app.showMessage("You don't have green anymore")
                        else:
                            currCube.color = 'green'
                            app.user.green -=1
                            app.coloredCube.append(currCube.color)
                            print(app.coloredCube)
                            if len(app.coloredCube) >= 4:
                                if 0 <= index <= 3:
                                    app.user.score += belowAdjforTopAI(app,
                                                    currCube,index)
                                    break
                                if 4 <= index <= 29:
                                    app.user.score += belowAdjforTopAI(app,
                                                    currCube,index)
                                    if app.user.score == 0:
                                        app.user.score += aboveAdjforTopAI(app,
                                            currCube,index)
                                        break
                                    if app.user.score == 0:
                                        app.user.score += belowAdjforBottomAI(app,
                                                       currCube, index)
                                        break
                                    break 
                                if 30 <= index <= 47:
                                    app.user.score += belowAdjforBottomAI(app,
                                                       currCube, index)
                                    if app.user.score == 0:
                                        app.user.score += aboveAdjforBottomAI(app, 
                                                       currCube, index)
                                        break
                                    break
                                else:
                                    app.user.score += aboveAdjforBottomAI(app, 
                                                       currCube, index)
                                    break
                        break
                    elif currColor == 'pink':
                        if app.user.pink == 0:
                            app.showMessage("You don't have pink anymore")
                        else:
                            currCube.color = 'pink'
                            app.user.pink -=1
                            app.coloredCube.append(currCube.color)
                            print(app.coloredCube)
                            if len(app.coloredCube) >= 4:
                                if 0 <= index <= 3:
                                    app.user.score += belowAdjforTopAI(app,
                                                    currCube,index)
                                    break
                                if 4 <= index <= 29:
                                    app.user.score += belowAdjforTopAI(app,
                                                    currCube,index)
                                    if app.user.score == 0:
                                        app.user.score += aboveAdjforTopAI(app,
                                            currCube,index)
                                        break
                                    if app.user.score == 0:
                                        app.user.score += belowAdjforBottomAI(app,
                                                       currCube, index)
                                        break
                                    break 
                                if 30 <= index <= 47:
                                    app.user.score += belowAdjforBottomAI(app,
                                                       currCube, index)
                                    if app.user.score == 0:
                                        app.user.score += aboveAdjforBottomAI(app, 
                                                       currCube, index)
                                        break
                                    break
                                else:
                                    app.user.score += aboveAdjforBottomAI(app, 
                                                       currCube, index)
                                                
                                    break
                        break
                    else:
                        app.showMessage('Please place within given color!')
    else:
        app.user.blue = app.user.red = app.user.green = app.user.pink = 0
        if app.round ==1:
            app.AI.placingCard = getRandomPlacingScore()
            app.AI.pickingCard = getRandomPickingScore()
            app.AI.numBlue = random.randint(0,4)
            app.AI.numRed = random.randint(0,4)
            app.AI.numGreen = random.randint(0,4)
            app.AI.numPink = random.randint(0,4)
        # app.AI.numBlue = random.randint(0,4)
        # app.AI.numRed = random.randint(0,4)
        # app.AI.numGreen = random.randint(0,4)
        # app.AI.numPink = random.randint(0,4)
        while((app.AI.blue <= app.AI.numBlue) and(app.AI.red<=app.AI.numRed)and
          (app.AI.green <= app.AI.numGreen) and (app.AI.pink <= app.AI.numPink)):
            app.AI.rockNumAI += random.randint(1,3)
            currBlueAI = random.randint(1, app.AI.rockNumAI)
            app.AI.blue += currBlueAI
            currRedAI = random.randint(0,app.AI.rockNumAI-currBlueAI)
            app.AI.red += currRedAI
            currGreenAI = random.randint(0,app.AI.rockNumAI-currBlueAI-currRedAI)
            app.AI.green += currGreenAI
            currPinkAI = random.randint(0,app.AI.rockNumAI-currBlueAI-
                                        currRedAI-currGreenAI)
            app.AI.pink += currPinkAI
        app.AI.score += minimax(app.boardlist,None,1,True,app)
        app.status = 'User'
        app.round += 1


def getPossibleMoves(state):
    res = []
    for cube in state:
        if cube.color == 'white':
            res.append(cube)           
    return res

def isLegal(app, currCube):
    index = app.boardlist.index(currCube)
    if index > 52 or index <0 or currCube.color != 'white':
        return False
    return True
    

def gameover(app):
    if app.round >= 4:
        return False
    for cube in app.boardlist:
        if cube.color == 'white':
            return False
    return True

def isWin(currCube, userScore,app,color):
    index = app.boardlist.index(currCube)
    app.AI.coloredCube.append(color)
    if len(app.AI.coloredCube) >=4:
        if 0 <= index <= 3:
            app.AI.score += belowAdjforTopAI(app,
                            currCube,index)
        if 4 <= index <= 29:
            app.AI.score += belowAdjforTopAI(app,
                            currCube,index)
            if app.AI.score == 0:
                app.AI.score +=  aboveAdjforTopAI(app,
                    currCube,index)
            if app.AI.score == 0:
                app.AI.score += belowAdjforBottomAI(app,
                                currCube, index)
        if 30 <= index <= 47:
            app.AI.score +=belowAdjforBottomAI(app,
                                currCube, index)
            if app.AI.score == 0:
                app.AI.score += aboveAdjforBottomAI(app, 
                                currCube, index)
        else:
            app.AI.score += aboveAdjforBottomAI(app, 
                                currCube, index)
    
    return app.AI.score > userScore

def isLost(currCube, userScore,app,color):
    index = app.boardlist.index(currCube)
    app.AI.coloredCube.append(color)
    if len(app.AI.coloredCube) >=4:
        if 0 <= index <= 3:
            app.AI.score += belowAdjforTopAI(app,
                            currCube,index)
        if 4 <= index <= 29:
            app.AI.score += belowAdjforTopAI(app,
                            currCube,index)
            if app.AI.score == 0:
                app.AI.score +=  aboveAdjforTopAI(app,
                    currCube,index)
            if app.AI.score == 0:
                app.AI.score += belowAdjforBottomAI(app,
                                currCube, index)
        if 30 <= index <= 47:
            app.AI.score +=belowAdjforBottomAI(app,
                                currCube, index)
            if app.AI.score == 0:
                app.AI.score += aboveAdjforBottomAI(app, 
                                currCube, index)
        else:
            app.AI.score += aboveAdjforBottomAI(app, 
                                currCube, index)
    return app.AI.score < userScore

def putColor(app):
    res = []
    if app.AI.blue != 0:
        res.append("blue")
    if app.AI.green != 0:
        res.append("green")
    if app.AI.red != 0:
        res.append("red")
    if app.AI.pink != 0:
        res.append("pink")
    currColor = random.choice(res)
    app.AI.colors[currColor] -=1
    return currColor

def minimax(state,currCube,depth, maxPlayer,app):
    if (depth == 0) or gameover(app):
        score = evaluate(currCube,app)
        return score
    # print(app.boardlist)
    # newBoardlist = copy.copy(app.boardlist)
    # print(newBoardlist)
    # possibleMoves = getPossibleMoves(state)
    if maxPlayer:
        maxValue = float('-inf')
        for move in app.boardlist: # possibleMoves = number of uncolored area
            newBoardlist = copy.deepcopy(app.boardlist)
            if isLegal(app, move):
                # index = app.boardlist.index(move)
                move.color = putColor(app)
                # if currCube == None:
                currCube = move
                # newBoardlist = copy.copy(app.boardlist)
                currValue = minimax(newBoardlist,currCube,depth-1,False,app)
                if currValue > maxValue:
                    maxValue = currValue
                    if move.color == 'blue':
                        app.AI.blue -=1
                    elif move.color == 'red':
                        app.AI.red -=1
                    elif move.color == 'green':
                        app.AI.green -=1
                    else:
                        app.AI.pink -=1
                else:
                    move.color = 'white'
                # maxValue = max(maxValue,currValue)
        return maxValue
    else:
        minValue = float('inf')
        for move in app.boardlist:
            # print(move)
            newBoardlist = copy.deepcopy(app.boardlist)
            if isLegal(app, move):
                # index = app.boardlist.index(move)
                move.color = putColor(app)
                # if currCube == None:
                currCube = move
                currValue = minimax(newBoardlist,currCube,depth-1,True,app)
                if currValue < minValue:
                    minValue = currValue
                    if move.color == 'blue':
                        app.AI.blue -=1
                    elif move.color == 'red':
                        app.AI.red -=1
                    elif move.color == 'green':
                        app.AI.green -=1
                    else:
                        app.AI.pink -=1
                else:
                    move.color = 'white'
                # minValue = min(currValue, minValue)
        return minValue

def evaluate(currCube,app):
    userScore = app.user.score
    color = currCube.color
    if isWin(currCube,userScore,app,color):
        return app.AI.score
    elif isLost(currCube,userScore,app,color):
        return app.AI.score
    else:
        return 0

# def finishTheGame(app):
#     if app.round >= 4:
#         if app.user.score > app.AI.score:
#             app.showMessage("Game Over! You are the winner!")
#         else:
#             app.showMessage("Game Over! AI player wins!")


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
    canvas.create_text(1350, 390, text=f'Round:{app.round}',fill='purple',
                       font = 'Helvetica 30 bold italic')
    canvas.create_text(1350, 470, text='Scores',fill='purple',
                       font = 'Helvetica 30 bold italic')
    canvas.create_text(1350, 540, text=f'Your Score: {app.user.score}',
           fill='purple',font = 'Helvetica 30 bold italic')
    canvas.create_text(1350, 600, text=f'AI Score: {app.AI.score}',
           fill='purple',font = 'Helvetica 30 bold italic')
    canvas.create_text(950,50, text='Pick!',fill='purple',
                       font = 'Helvetica 25 bold italic')
    for button in app.buttons:
        button.render(canvas)
    canvas.create_image(850,230,image=ImageTk.PhotoImage(app.cardDeck))
    canvas.create_image(1100,230,image=ImageTk.PhotoImage(app.rockBag))
    # finishTheGame(app)
    # cardDeck image is from 
    # https://clipartpng.com/?2722,deck-of-cards-png-clip-art-image
    # rockbag image is from https://www.pngwing.com/en/free-png-zgoig/download

            
runApp(width=1550, height=800)