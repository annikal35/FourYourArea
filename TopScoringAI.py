from checkBelow import *
from checkAbove import *

def belowAdjforTopAI(app,cube,index):
    redColor = blueColor = greenColor = pinkColor = 0
    colorList = []
    bottomColor = bottomLeftColor = belowColor = ''
    anotherbottomColor = bottomRightColor = ''
    if 0 <= index <= 3:
        belowColor = app.boardlist[index+10].color
        bottomColor = app.boardlist[index+4].color
        anotherbottomColor = app.boardlist[index+5].color
        if index <= 2:
            right = app.boardlist[index+1]
            bottomRightColor = app.boardlist[index+6].color
        if 1 <= index:
            left = app.boardlist[index-1]
            bottomLeftColor = app.boardlist[index+3].color
        if index == 0:
            colorList = checkAt0(cube, right.color,anotherbottomColor, 
                        bottomRightColor,belowColor,bottomColor,colorList)
        elif index == 3:
            colorList = checkAt3(cube,left.color,anotherbottomColor,
                                    bottomLeftColor, belowColor,bottomColor,colorList)
        elif index ==1 or index ==2:
            right = app.boardlist[index+1]
            left = app.boardlist[index-1]
            colorList = checkElse(cube,right.color,left.color,bottomLeftColor,
        anotherbottomColor,bottomRightColor, belowColor,bottomColor,colorList)
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)

    if 4 <= index <= 8:
        belowColor = app.boardlist[index+12].color
        bottomColor = app.boardlist[index+5].color
        anotherbottomColor = app.boardlist[index+6].color
        if index == 4:
            right = app.boardlist[index+1]
            bottomRightColor = app.boardlist[index+7].color
            colorList = checkAtFour(cube, right.color,anotherbottomColor,
                            bottomRightColor,belowColor,bottomColor,colorList)
        elif index == 8:
            left = app.boardlist[index-1]
            bottomLeftColor = app.boardlist[index+4].color
            colorList = checkAtEight(cube, left.color,anotherbottomColor,
                            bottomLeftColor,belowColor,bottomColor,colorList)
        else:
            right = app.boardlist[index+1]
            left = app.boardlist[index-1]
            bottomRightColor = app.boardlist[index+7].color
            bottomLeftColor = app.boardlist[index+4].color
            colorList = checkElse(cube, right.color, left.color,bottomLeftColor,
            anotherbottomColor,bottomRightColor, belowColor,bottomColor,colorList)
        print(colorList)
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)
    
    if 9 <= index <= 14:
        belowColor = app.boardlist[index+14].color
        bottomColor = app.boardlist[index+6].color
        anotherbottomColor = app.boardlist[index+7].color
        if index == 9:
            right = app.boardlist[index+1]
            bottomRightColor = app.boardlist[index+8].color
            colorList = checkAtFour(cube, right.color,anotherbottomColor,
                            bottomRightColor,belowColor,bottomColor,colorList)
        elif index == 14:
            left = app.boardlist[index-1]
            bottomLeftColor = app.boardlist[index+5].color
            colorList = checkAtEight(cube, left.color,anotherbottomColor,
                            bottomLeftColor,belowColor,bottomColor,colorList)
        else:
            bottomLeftColor = app.boardlist[index+5].color
            bottomRightColor = app.boardlist[index+8].color
            right = app.boardlist[index+1]
            left = app.boardlist[index-1]
            colorList = checkElse(cube, right.color, left.color,bottomLeftColor,
            anotherbottomColor,bottomRightColor, belowColor,bottomColor,colorList)
        print(colorList)
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)

    if 15 <= index <=21:
        belowColor = app.boardlist[index+15].color
        bottomColor = app.boardlist[index+7].color
        bottomRightColor = app.boardlist[index+9].color
        anotherbottomColor = app.boardlist[index+8].color
        if index == 15:
            right = app.boardlist[index+1]
            bottomLeftColor = app.boardlist[index+6].color
            colorList = checkAtFour(cube, right.color,anotherbottomColor,
                            bottomRightColor,belowColor,bottomColor,colorList)
        elif index == 21:
            left = app.boardlist[index-1]
            bottomLeftColor = app.boardlist[index+6].color
            colorList = checkAtEight(cube, left.color,anotherbottomColor,
                            bottomLeftColor,belowColor,bottomColor,colorList)
        else:
            bottomLeftColor = app.boardlist[index+6].color
            bottomRightColor = app.boardlist[index+9].color
            right = app.boardlist[index+1]
            left = app.boardlist[index-1]
            colorList=checkElse(cube, right.color, left.color, bottomLeftColor,
            anotherbottomColor,bottomRightColor, belowColor,bottomColor,colorList)
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)

    # print(redColor, blueColor, greenColor, pinkColor)
    if redColor == blueColor == greenColor == pinkColor == 1:
        if app.status == 'User':
            return app.user.placingCard['1']
        else:
            return app.AI.placingCard['1']
    elif ((redColor == 2) or (blueColor == 2) or 
        (greenColor == 2) or (pinkColor == 2)):
        if app.status == 'User':
            return app.user.placingCard['2']
        else:
            return app.AI.placingCard['2']
    elif ((redColor == 3) or (blueColor == 3) or 
        (greenColor == 3) or (pinkColor == 3)):
        if app.status == 'User':
            return app.user.placingCard['3']
        else:
            return app.AI.placingCard['3']
    elif ((redColor == 4) or (blueColor == 4) or 
        (greenColor == 4) or (pinkColor == 4)):
        if app.status == 'User':
            return app.user.placingCard['4']
        else:
            return app.AI.placingCard['4']
    else:
        return 0

def aboveAdjforTopAI(app, cube, index):
    redColor = blueColor = greenColor = pinkColor = 0
    colorList = []
    aboveLeftColor = aboveTwoColor = aboveColor = ''
    anotherAboveColor = aboveRightColor = ''
    if 4 <= index <= 8:
        if index <= 7:
            anotherAboveColor = app.boardlist[index-4].color
            right = app.boardlist[index+1]
        if index <=6:
            aboveRightColor = app.boardlist[index-3].color
        if 5 <= index <= 8:
            aboveColor = app.boardlist[index-5].color
            left = app.boardlist[index-1]
        if 6 <= index:
            aboveLeftColor = app.boardlist[index-6].color
        if index == 4:
            colorList =aboveFarRight(cube,right.color,anotherAboveColor, 
                                aboveRightColor,colorList)
        elif index == 5:
            colorList = checkAt5(cube,left.color,right.color, 
                        aboveColor,anotherAboveColor,aboveRightColor,colorList)
        elif index  == 6:
            colorList = checkAt6(cube,left.color,right.color,aboveColor,
                                aboveRightColor,anotherAboveColor,
                                    aboveLeftColor,colorList)
        elif index == 7:
            colorList = checkAt7(cube,left.color,right.color,aboveColor,
            anotherAboveColor,aboveLeftColor,colorList)
        elif index == 8:
            colorList = aboveFarLeft(cube,left.color,aboveLeftColor,
                            aboveColor,colorList)
        else:
            colorList=aboveElse(cube,left.color,right.color,aboveColor,
                  aboveRightColor,aboveTwoColor,anotherAboveColor,
                  aboveLeftColor,colorList)
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)

    if 9 <= index <= 14:
        if index <= 13:
            anotherAboveColor = app.boardlist[index-5].color
            right = app.boardlist[index+1]
        if 9 <= index <= 12:
            aboveRightColor = app.boardlist[index-4].color
        if 10 <= index <= 14:
            aboveColor = app.boardlist[index-6].color
            left = app.boardlist[index-1]
        if 11 <= index:
            aboveLeftColor = app.boardlist[index-7].color
        if 10 <=index<=13:
            aboveTwoColor = app.boardlist[index-10].color
        if index ==9:
            colorList =aboveFarRight(cube,right.color,anotherAboveColor, 
                                aboveRightColor,colorList)
        elif index ==10:
            colorList = aboveleftCol(cube,left.color,right.color, 
        aboveTwoColor,aboveColor,anotherAboveColor,aboveRightColor,colorList)
        elif index ==13:
            colorList = aboveRightCol(cube,left.color,right.color, 
                            aboveColor,aboveTwoColor,anotherAboveColor,
                                            aboveLeftColor,colorList)
        elif index == 14:
            colorList = aboveFarLeft(cube,left.color,aboveLeftColor,
                            aboveColor,colorList)
        else:
            colorList=aboveElse(cube,left.color,right.color,aboveColor,
                  aboveRightColor,aboveTwoColor,anotherAboveColor,
                  aboveLeftColor,colorList)
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)
    
    if 15 <= index <= 21:
        if index <= 20:
            anotherAboveColor = app.boardlist[index-6].color
            right = app.boardlist[index+1]
        if 15 <= index <= 19:
            aboveRightColor = app.boardlist[index-5].color
        if 16 <= index < 20:
            aboveTwoColor = app.boardlist[index-12].color
        if 16 <= index <= 21:
            aboveColor = app.boardlist[index-7].color
            left = app.boardlist[index-1]
        if 17 <= index:
            aboveLeftColor = app.boardlist[index-8].color
        if index ==15:
            colorList = aboveFarRight(cube,right.color,
                    anotherAboveColor, aboveRightColor,colorList)
        elif index == 16:
            colorList = aboveleftCol(cube,left.color,right.color, 
                            aboveTwoColor,aboveColor,anotherAboveColor,
                            aboveRightColor,colorList)
        elif index ==20:
            colorList = aboveRightCol(cube,left.color,right.color, 
                            aboveColor,aboveTwoColor,anotherAboveColor,
                                            aboveLeftColor,colorList)
        elif index == 21:
            colorList = aboveFarLeft(cube,left.color,aboveLeftColor,
                            aboveColor,colorList)
        else:
            colorList=aboveElse(cube,left.color,right.color,aboveColor,
                  aboveRightColor,aboveTwoColor,anotherAboveColor,
                  aboveLeftColor,colorList)
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)
    
    if 22 <= index <= 29:
        if index <= 28:
            anotherAboveColor = app.boardlist[index-7].color
            right = app.boardlist[index+1]
        if 22 <= index <= 27:
            aboveRightColor = app.boardlist[index-6].color
        if 23 <= index <=28:
            aboveTwoColor = app.boardlist[index-14].color
        if 23 <= index <= 29:
            aboveColor = app.boardlist[index-7].color
            left = app.boardlist[index-1]
        if 24 <= index:
            aboveLeftColor = app.boardlist[index-9].color
        if index ==22:
            colorList = aboveFarRight(cube,right.color,
                            anotherAboveColor, aboveRightColor,colorList)
        elif index == 23:
            colorList = aboveleftCol(cube,left.color,right.color, 
                                aboveTwoColor,aboveColor,anotherAboveColor,
                                    aboveRightColor,colorList)
        elif index  == 28:
            colorList = aboveRightCol(cube,left.color,right.color, 
                            aboveColor,aboveTwoColor,anotherAboveColor,
                                            aboveLeftColor,colorList)
        elif index == 29:
            colorList = aboveFarLeft(cube,left.color,aboveLeftColor,
                            aboveColor,colorList)
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)
    
    # print(redColor , blueColor,greenColor,pinkColor)
    if redColor == blueColor == greenColor == pinkColor == 1:
        if app.status == 'User':
            return app.user.placingCard['1']
        else:
            return app.AI.placingCard['1']
    elif ((redColor == 2) or (blueColor == 2) or 
        (greenColor == 2) or (pinkColor == 2)):
        if app.status == 'User':
            return app.user.placingCard['2']
        else:
            return app.AI.placingCard['2']
    elif ((redColor == 3) or (blueColor == 3) or 
        (greenColor == 3) or (pinkColor == 3)):
        if app.status == 'User':
            return app.user.placingCard['3']
        else:
            return app.AI.placingCard['3']
    elif ((redColor == 4) or (blueColor == 4) or 
        (greenColor == 4) or (pinkColor == 4)):
        if app.status == 'User':
            return app.user.placingCard['4']
        else:
            return app.AI.placingCard['4']
    else:
        return 0