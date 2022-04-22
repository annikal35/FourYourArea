from board import *
from userforAI import *
from cmu_112_graphics import *
from TopScoring import *
from checkBelowForBottom import *
import random

def appStarted(app):
    app.image1 = app.loadImage('Deck_of_Cards.png')
    app.cardDeck = app.scaleImage(app.image1, 0.6)
    app.image2 = app.loadImage('rockbag.png')
    app.rockBag = app.scaleImage(app.image2, 0.15)
    app.user = User()
    app.boardlist = createBoard(app)
    app.coloredCube = []

def belowAdjforBottom(app, cube, index):
    redColor = blueColor = greenColor = pinkColor = 0
    colorList = []
    bottomColor = bottomLeftColor = belowTwoColor = ''
    anotherbottomColor = bottomRightColor = ''
    if 22 <= index <= 29:
        if index <= 28:
            anotherbottomColor = app.boardlist[index+8].color
            right = app.boardlist[index+1]
            if index <=27:
                bottomRightColor = app.boardlist[index+9].color
                if index == 22:
                    colorList =belowLeftCol(cube,right.color,anotherbottomColor, 
                                bottomRightColor,[])

        if 23 <= index <= 29:
            bottomColor = app.boardlist[index+7]
            left = app.boardlist[index-1]
            if 24 <= index:
                bottomLeftColor = app.boardlist[index+6].color
                if index == 23:
                    colorList = checkAt23(cube, left.color, right.color, 
                               anotherbottomColor, bottomColor,
                                 belowTwoColor,bottomRightColor,[])
                if index == 28:
                    colorList = checkAt28(cube, left.color, right.color, 
                               anotherbottomColor, bottomColor,
                                 belowTwoColor,bottomLeftColor,[])
                if index == 29:
                    colorList = belowRightCol(cube,left.color,bottomLeftColor, 
                                bottomColor,[])
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)

    if 30 <= index <= 36:
        if index <= 35:
            anotherbottomColor = app.boardlist[index+7].color
            right = app.boardlist[index+1]
            if index <=34:
                bottomRightColor = app.boardlist[index+8].color
                if index == 30:
                    colorList =belowLeftCol(cube,right.color,anotherbottomColor, 
                                bottomRightColor,[])

        if 31 <= index <= 36:
            bottomColor = app.boardlist[index+6]
            left = app.boardlist[index-1]
            if 32 <= index:
                bottomLeftColor = app.boardlist[index+6].color
                if index == 31:
                    colorList = checkAt23(cube, left.color, right.color, 
                               anotherbottomColor, bottomColor,
                                 belowTwoColor,bottomRightColor,[])
                if index == 35:
                    colorList = checkAt28(cube, left.color, right.color, 
                               anotherbottomColor, bottomColor,
                                 belowTwoColor,bottomLeftColor,[])
                if index == 36:
                    colorList = belowRightCol(cube,left.color,bottomLeftColor, 
                                bottomColor,[])
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)
    
    if 37 <= index <= 42:
        if index <= 35:
            anotherbottomColor = app.boardlist[index+7].color
            right = app.boardlist[index+1]
            if index <=34:
                bottomRightColor = app.boardlist[index+8].color
                if index == 30:
                    colorList =belowLeftCol(cube,right.color,anotherbottomColor, 
                                bottomRightColor,[])

        if 31 <= index <= 36:
            bottomColor = app.boardlist[index+6]
            left = app.boardlist[index-1]
            if 32 <= index:
                bottomLeftColor = app.boardlist[index+6].color
                if index == 31:
                    colorList = checkAt23(cube, left.color, right.color, 
                               anotherbottomColor, bottomColor,
                                 belowTwoColor,bottomRightColor,[])
                if index == 35:
                    colorList = checkAt28(cube, left.color, right.color, 
                               anotherbottomColor, bottomColor,
                                 belowTwoColor,bottomLeftColor,[])
                if index == 36:
                    colorList = belowRightCol(cube,left.color,bottomLeftColor, 
                                bottomColor,[])
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)
    
    if 22 <= index <= 29:
        if index <= 28:
            anotherAboveColor = app.boardlist[index-7].color
            right = app.boardlist[index+1]
            if 22 <= index <= 27:
                aboveRightColor = app.boardlist[index-6].color
                if index ==22:
                    colorList = aboveFarRight(cube,right.color,
                                 anotherAboveColor, aboveRightColor,[])
                if 23 <= index <=28:
                    aboveTwoColor = app.boardlist[index-14].color
                if index == 23:
                    colorList = aboveleftCol(cube,left.color,right.color, 
                                     aboveTwoColor,aboveColor,anotherAboveColor,
                                           aboveRightColor,[])
        if 23 <= index <= 29:
            aboveColor = app.boardlist[index-7].color
            left = app.boardlist[index-1]
            if 24 <= index:
                aboveLeftColor = app.boardlist[index-9].color
                if index  == 28:
                    colorList = aboveRightCol(cube,left.color,right.color, 
                                    aboveColor,aboveTwoColor,anotherAboveColor,
                                                    aboveLeftColor,[])
                if index == 29:
                    colorList = aboveFarLeft(cube,left.color,aboveLeftColor,
                                    aboveColor,[])
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)
    right = app.boardlist[index+1]
    left = app.boardlist[index-1]
    colorList =aboveElse(cube,left.color,right.color,aboveColor,aboveRightColor,
                aboveTwoColor,anotherAboveColor,aboveLeftColor,colorList)

    redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                redColor, blueColor, greenColor, pinkColor)
    if redColor == blueColor == greenColor == pinkColor == 1:
        return app.user.placingCard['1']
    elif ((redColor == 2) or (blueColor == 2) or 
        (greenColor == 2) or (pinkColor == 2)):
        return app.user.placingCard['2']
    elif ((redColor == 3) or (blueColor == 3) or 
        (greenColor == 3) or (pinkColor == 3)):
        return app.user.placingCard['3']
    elif ((redColor == 4) or (blueColor == 4) or 
        (greenColor == 4) or (pinkColor == 4)):
        return app.user.placingCard['4']
    else:
        return 0


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
        for currCube in app.boardlist:
            index = app.boardlist.index(currCube)
            # currCube = app.boardlist[i]
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
                            if len(app.coloredCube) % 4 == 0:
                                if index <= 29:
                                    app.user.score += belowAdjforTop(app,
                                                    currCube,index)
                                    # if app.user.score == 0:
                                    app.user.score += aboveAdjforTop(app,
                                            currCube,index)  
                                else:
                                    app.user.score += belowAdjforBottom(app,
                                                       currCube, index)
                        break
                    elif currColor == 'red':
                        if app.user.red == 0:
                            app.showMessage("You don't have red anymore")
                        else:
                            currCube.color = 'red'
                            app.user.red -=1
                            app.coloredCube.append(currCube.color)
                            print(app.coloredCube)
                            if len(app.coloredCube) % 4 == 0:
                                if index <= 29:
                                    app.user.score += belowAdjforTop(app,
                                                    currCube,index)
                                    app.user.score += aboveAdjforTop(app,
                                                     currCube,index)
                        break
                    elif currColor == 'green':
                        if app.user.green == 0:
                            app.showMessage("You don't have green anymore")
                        else:
                            currCube.color = 'green'
                            app.user.green -=1
                            app.coloredCube.append(currCube.color)
                            print(app.coloredCube)
                            if len(app.coloredCube) % 4 == 0:
                                if index <= 29:
                                    app.user.score += belowAdjforTop(app,
                                                    currCube,index)
                                    app.user.score += aboveAdjforTop(app,
                                            currCube,index)
                                # app.user.score += aboveAdjacentCubes(app,currCube,i)
                        break
                    elif currColor == 'pink':
                        if app.user.pink == 0:
                            app.showMessage("You don't have pink anymore")
                        else:
                            currCube.color = 'pink'
                            app.user.pink -=1
                            app.coloredCube.append(currCube.color)
                            print(app.coloredCube)
                            if len(app.coloredCube) % 4 == 0:
                                if index <= 29:
                                    app.user.score += belowAdjforTop(app,
                                                    currCube,index)
                                    app.user.score += aboveAdjforTop(app,
                                                currCube,index)
                                # app.user.score += aboveAdjacentCubes(app,currCube,i)
                        break
                    else:
                        app.showMessage('Please place within given color!')


                

        

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