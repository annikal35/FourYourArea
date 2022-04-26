from board import *
from userforAI import *
from cmu_112_graphics import *
from TopScoringAI import *
from BottomScoringAI import *
from minimax import *
from buttons import *
from mainforlocal import *
import random
import copy

def intro_redrawAll(app, canvas):
    canvas.create_rectangle(0,0,app.width, app.height,
                            fill = '#5e7296')
    for button in app.introButtons:
        button.render(canvas)
    canvas.create_text(860, 180, text='4', fill='#801315',
                    font ='Calibri 350 bold')
    canvas.create_text(750, 200, text='Four', fill='lightblue',
                    font ='Calibri 85 bold')
    canvas.create_text(600, 390, text='Your ', fill='lightgreen',
                    font ='Calibri 85 bold')
    canvas.create_text(850, 390, text='  Area', fill='lightgreen',
                    font ='Calibri 90 bold')
    canvas.create_image(200, 100, image=ImageTk.PhotoImage(app.hexagon1))

def intro_mousePressed(app, event):
    if (200 <= event.x <= 750) and (550 <= event.y <= 700):
        app.mode = 'mode1'
    elif (780 <= event.x <= 1350) and (550 <= event.y <= 700):
        app.mode = 'mode2'

def appStarted(app):
    # app.hexCount = 0
    # app.timePassed = 0
    app.mode = 'intro'
    app.introButtons = [
        Button(200, 550, 750, 700, "1 Player"),
        Button(780, 550, 1330, 700, "2 Players")
    ]
    app.timerDelay = 5000
    app.image1 = app.loadImage('Deck_of_Cards.png')
    app.cardDeck = app.scaleImage(app.image1, 0.6)
    app.cardDeck2 = app.scaleImage(app.image1, 0.4)
    app.image2 = app.loadImage('rockbag.png')
    app.rockBag = app.scaleImage(app.image2, 0.15)
    app.rockBag2 = app.scaleImage(app.image2, 0.1)
    app.image3 = app.loadImage('hexagon1.png')
    app.hexagon1 = app.scaleImage(app.image3, 0.6)
    app.image4 = app.loadImage('hexagon2.png')
    app.hexagon2 = app.scaleImage(app.image4, 0.6)
    app.user = User()
    app.AI = AI()
    app.player1 = UserOne()
    app.player2 = UserTwo()
    app.boardlist = createBoard(app)
    app.boardlist2 = createBoard2(app)
    app.coloredCube = []
    app.coloredCube1 = []
    app.buttons = [
      Button(1250, 680, 1500, 750, "STOP!"),
      Button(600, 40, 720, 140, "Finish\nPicking!")
    ]
    app.buttons2 = [
      Button(270, 680, 520, 750, "STOP!"),
      Button(1250, 680, 1500, 750, "STOP!"),
      Button(450, 40, 570, 140, "Finish\nPicking!"),
      Button(1000, 40, 1120, 140, "Finish\nPicking!")
   ]
    app.status2 = 'Player 1'
    app.possibleMoves = []
    app.status = 'User'
    app.round = 1
    app.isGameOver = False


def mode1_mousePressed(app, event):
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

        if (600<=event.x<=720) and (40<=event.y<=140):
            total=app.user.blue+app.user.red+app.user.green\
                              +app.user.pink
            if total == 1:
                app.user.score += app.user.pickingCard['1']
            elif total == 2:
                app.user.score += app.user.pickingCard['2']
            elif total == 3:
                app.user.score += app.user.pickingCard['3']
            elif total == 4:
                app.user.score += app.user.pickingCard['4']
            elif total == 5:
                app.user.score += app.user.pickingCard['5']
            elif total == 6:
                app.user.score += app.user.pickingCard['6']
            elif total == 7:
                app.user.score += app.user.pickingCard['7']

        for currCube in app.boardlist:
            # index = app.boardlist.index(currCube)
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
                    total=app.user.blue+app.user.red+app.user.green\
                              +app.user.pink
                    if total == 1:
                        app.user.score += app.user.pickingCard['1']
                    elif total == 2:
                        app.user.score += app.user.pickingCard['2']
                    elif total == 3:
                        app.user.score += app.user.pickingCard['3']
                    elif total == 4:
                        app.user.score += app.user.pickingCard['4']
                    elif total == 5:
                        app.user.score += app.user.pickingCard['5']
                    elif total == 6:
                        app.user.score += app.user.pickingCard['6']
                    elif total == 7:
                        app.user.score += app.user.pickingCard['7']
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
                                index = app.boardlist.index(currCube)
                                # print(index)
                                if 0 <= index <= 3:
                                    app.user.score += belowAdjforTopAI(app,
                                                    currCube,index)
                                    break
                                if 4 <= index <= 29:
                                    app.user.score += belowAdjforTopAI(app,
                                                    currCube,index)
                                    # if app.user.score == 0:
                                    app.user.score += aboveAdjforTopAI(app,
                                        currCube,index)
                                    # if app.user.score == 0:
                                    app.user.score += belowAdjforBottomAI(app,
                                                    currCube, index)
                                    # print(app.user.score)
                                    break 
                                if 30 <= index <= 47:
                                    app.user.score += belowAdjforBottomAI(app,
                                                       currCube, index)
                                    # if app.user.score == 0:
                                    app.user.score += aboveAdjforBottomAI(app, 
                                                    currCube, index)
                                    # print(app.user.score)
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
                                index = app.boardlist.index(currCube)
                                # print(index)
                                if 0 <= index <= 3:
                                    app.user.score += belowAdjforTopAI(app,
                                                    currCube,index)
                                    # print(app.user.score)
                                    break
                                if 4 <= index <= 29:
                                    app.user.score += belowAdjforTopAI(app,
                                                    currCube,index)
                                    # if app.user.score == 0:
                                    app.user.score += aboveAdjforTopAI(app,
                                        currCube,index)
                                    # if app.user.score == 0:
                                    app.user.score += belowAdjforBottomAI(app,
                                                    currCube, index)
                                    # print(app.user.score)
                                    break
                                if 30 <= index <= 47:
                                    app.user.score += belowAdjforBottomAI(app,
                                                       currCube, index)
                                    # if app.user.score == 0:
                                    app.user.score += aboveAdjforBottomAI(app, 
                                                    currCube, index)
                                    # print(app.user.score)
                                    break
                                else:
                                    app.user.score += aboveAdjforBottomAI(app, 
                                                       currCube, index)
                                    # print(app.user.score)
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
                                index = app.boardlist.index(currCube)
                                # print(index)
                                if 0 <= index <= 3:
                                    app.user.score += belowAdjforTopAI(app,
                                                    currCube,index)
                                    break
                                if 4 <= index <= 29:
                                    app.user.score += belowAdjforTopAI(app,
                                                    currCube,index)
                                    # if app.user.score == 0:
                                    app.user.score += aboveAdjforTopAI(app,
                                        currCube,index)
                                    # if app.user.score == 0:
                                    app.user.score += belowAdjforBottomAI(app,
                                                    currCube, index)
                                    # print(app.user.score)
                                    break 
                                if 30 <= index <= 47:
                                    app.user.score += belowAdjforBottomAI(app,
                                                       currCube, index)
                                    # if app.user.score == 0:
                                    app.user.score += aboveAdjforBottomAI(app, 
                                                    currCube, index)
                                    # print(app.user.score)
                                    break
                                else:
                                    app.user.score += aboveAdjforBottomAI(app, 
                                                       currCube, index)
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
                                index = app.boardlist.index(currCube)
                                if 0 <= index <= 3:
                                    app.user.score += belowAdjforTopAI(app,
                                                    currCube,index)
                                    break
                                if 4 <= index <= 29:
                                    app.user.score += belowAdjforTopAI(app,
                                                    currCube,index)
                                    # if app.user.score == 0:
                                    app.user.score += aboveAdjforTopAI(app,
                                        currCube,index)
                                    # if app.user.score == 0:
                                    app.user.score += belowAdjforBottomAI(app,
                                                    currCube, index)
                                    # print(app.user.score)
                                    break 
                                if 30 <= index <= 47:
                                    app.user.score += belowAdjforBottomAI(app,
                                                       currCube, index)
                                    # if app.user.score == 0:
                                    app.user.score += aboveAdjforBottomAI(app, 
                                                    currCube, index)
                                    # print(app.user.score)
                                    break
                                else:
                                    app.user.score += aboveAdjforBottomAI(app, 
                                                       currCube, index)
                                                
                        break
                    else:
                        app.showMessage('Please place within given color!')
    else:
        app.user.blue = app.user.red = app.user.green = app.user.pink = 0
        if app.round ==1:
            app.AI.placingCard = getRandomPlacingScore()
            app.AI.pickingCard = getRandomPickingScore()
            app.AI.numBlue = random.randint(1,4)
            app.AI.numRed = random.randint(1,4)
            app.AI.numGreen = random.randint(1,4)
            app.AI.numPink = random.randint(1,4)
        # app.AI.numBlue = random.randint(0,4)
        # app.AI.numRed = random.randint(0,4)
        # app.AI.numGreen = random.randint(0,4)
        # app.AI.numPink = random.randint(0,4)
        print(app.AI.numBlue,app.AI.numRed,app.AI.numGreen,app.AI.numPink)
        app.AI.rockNumAI += random.randint(1,3)
        # print(app.AI.rockNumAI)
        currBlueAI = random.randint(1, app.AI.rockNumAI)
        app.AI.blue += currBlueAI
        currRedAI = random.randint(0,app.AI.rockNumAI-currBlueAI)
        app.AI.red += currRedAI
        currGreenAI = random.randint(0,app.AI.rockNumAI-currBlueAI-currRedAI)
        app.AI.green += currGreenAI
        limit = app.AI.rockNumAI-currBlueAI-currRedAI-currGreenAI
        currPinkAI = random.randint(0,limit)
        app.AI.pink += currPinkAI
        # print(app.AI.blue, app.AI.red, app.AI.green, app.AI.pink)
        if ((app.AI.blue == 0 and app.AI.red == 0 and app.AI.green==0 and
         app.AI.pink==0) and ((app.AI.blue > app.AI.numBlue) or
         (app.AI.red>app.AI.numRed)or(app.AI.green > app.AI.numGreen) 
         or (app.AI.pink > app.AI.numPink))):
            while ((app.AI.blue > 0 and app.AI.red > 0 and app.AI.green>0 and
         app.AI.pink>0) and (app.AI.blue <= app.AI.numBlue) and
         (app.AI.red<=app.AI.numRed)and(app.AI.green <= app.AI.numGreen) and
          (app.AI.pink <= app.AI.numPink)):
        #   and ((app.AI.blue>0) or (app.AI.red>0) or (app.AI.green>0) or 
        #   (app.AI.pink>0))):
                app.AI.rockNumAI += random.randint(1,3)
                # print(app.AI.rockNumAI)
                currBlueAI = random.randint(0, app.AI.rockNumAI)
                app.AI.blue += currBlueAI
                if app.AI.blue == 0:
                    currRedAI = random.randint(0,app.AI.rockNumAI-currBlueAI)
                else:
                    currRedAI = random.randint(0,app.AI.rockNumAI-currBlueAI)
                app.AI.red += currRedAI
                if app.AI.red == 0 and app.AI.blue == 0:
                    currGreenAI = random.randint(1,app.AI.rockNumAI-currBlueAI-currRedAI)
                else:
                    currGreenAI = random.randint(0,app.AI.rockNumAI-currBlueAI-currRedAI)
                app.AI.green += currGreenAI
                limit = app.AI.rockNumAI-currBlueAI-currRedAI-currGreenAI
                if app.AI.green == 0 and app.AI.red == 0 and app.AI.blue == 0:
                    currPinkAI = random.randint(1,limit)
                else:
                    currPinkAI = random.randint(0,limit)
                app.AI.pink += currPinkAI
        print(app.AI.blue,app.AI.red,app.AI.green,app.AI.pink)
        # minimax(state,currCube,depth, maxPlayer,app)
        app.AI.score += minimax(app.boardlist,None,1,True,app)
        # app.AI.blue=app.AI.red=app.AI.green=app.AI.pink=0
        app.status = 'User'
        app.round += 1
        if app.round > 4:
            app.isGameOver = True


def getPossibleMoves(state):
    res = []
    for cube in state:
        if cube.color == 'white':
            res.append(cube)           
    return res

def isLegal(app, currCube):
    index = app.boardlist.index(currCube)
    print(index)
    if index > 52 or index <0 or currCube.color != 'white':
        return False
    return True
    

def gameover(app):
    if app.round <= 4:
        return False
    # if (app.AI.blue==app.AI.red==app.AI.green==app.AI.pink==0):
    #     return True
    for cube in app.boardlist:
        if cube.color != 'white':
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
            # if app.AI.score == 0:
            app.AI.score +=  aboveAdjforTopAI(app,
                currCube,index)
            # if app.AI.score == 0:
            app.AI.score += belowAdjforBottomAI(app,
                            currCube, index)
        if 30 <= index <= 47:
            app.AI.score +=belowAdjforBottomAI(app,
                                currCube, index)
            # if app.AI.score == 0:
            app.AI.score += aboveAdjforBottomAI(app, 
                                currCube, index)
        else:
            app.AI.score += aboveAdjforBottomAI(app, 
                                currCube, index)
    
    return app.AI.score > userScore

def isLost(currCube, userScore,app,color):
    index = app.boardlist.index(currCube)
    app.AI.coloredCube.append(color)
    if len(app.AI.coloredCube) >= 4:
        if 0 <= index <= 3:
            app.AI.score += belowAdjforTopAI(app,
                            currCube,index)
        if 4 <= index <= 29:
            app.AI.score += belowAdjforTopAI(app,
                            currCube,index)
        # if app.AI.score == 0:
            app.AI.score +=  aboveAdjforTopAI(app,
                currCube,index)
        # if app.AI.score == 0:
            app.AI.score += belowAdjforBottomAI(app,
                            currCube, index)
        if 30 <= index <= 47:
            app.AI.score +=belowAdjforBottomAI(app,
                                currCube, index)
            # if app.AI.score == 0:
            app.AI.score += aboveAdjforBottomAI(app, 
                                currCube, index)
        else:
            app.AI.score += aboveAdjforBottomAI(app, 
                                currCube, index)
    return app.AI.score < userScore

def putColor(app):
    res = []
    currDict = {'blue': app.AI.blue, 'red':app.AI.red, 
                'green':app.AI.green,'pink':app.AI.pink}
    print(currDict)
    if app.AI.blue > 0:
        res.append("blue")
    if app.AI.green > 0:
        res.append("green")
    if app.AI.red > 0:
        res.append("red")
    if app.AI.pink > 0:
        res.append("pink")
    print(res)
    currColor = random.choice(res)
    currDict[currColor] -=1
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
        print(maxValue)
        for move in app.boardlist: # possibleMoves = number of uncolored area
            newBoardlist = copy.deepcopy(app.boardlist)
            print(move.color)
            if isLegal(app, move):
                # index = app.boardlist.index(move)
                move.color = putColor(app)
                # if currCube == None:
                currCube = move
                # newBoardlist = copy.copy(app.boardlist)
                currValue = minimax(newBoardlist,currCube,depth-1,False,app)
                if currValue > maxValue:
                    maxValue = currValue
                    # if move.color == 'blue':
                    #     app.AI.blue -=1
                    # elif move.color == 'red':
                    #     app.AI.red -=1
                    # elif move.color == 'green':
                    #     app.AI.green -=1
                    # else:
                    #     app.AI.pink -=1
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
                print(move)
                # if currCube == None:
                currCube = move
                currValue = minimax(newBoardlist,currCube,depth-1,True,app)
                if currValue < minValue:
                    minValue = currValue
                    # if move.color == 'blue':
                    #     app.AI.blue -=1
                    # elif move.color == 'red':
                    #     app.AI.red -=1
                    # elif move.color == 'green':
                    #     app.AI.green -=1
                    # else:
                    #     app.AI.pink -=1
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

def mode1_timerFired(app):
    if app.isGameOver:
        return

def mode1_redrawAll(app, canvas):
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
    if app.isGameOver:
        if app.user.score > app.AI.score:
            canvas.create_rectangle(app.width/3, app.height/3,
                      app.width*(2/3),app.height*(2/3),fill = 'white')
            canvas.create_text(app.width/2, app.height/2, text="You won!",
                            font = "Arial 60 bold", fill = 'black')
        else:
            canvas.create_rectangle(app.width/3, app.height/3,
                      app.width*(2/3),app.height*(2/3),fill = 'white')
            canvas.create_text(app.width/2, app.height/2, text="AI won!",
                            font = "Arial 60 bold", fill = 'black')

            
runApp(width=1550, height=800)