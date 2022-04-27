from checkBelowForBottom import *
from checkBelowForAbove import *

def addColor(colorList, redColor, blueColor, greenColor, pinkColor):
    redColor += colorList.count("red")
    blueColor += colorList.count("blue")
    greenColor += colorList.count("green")
    pinkColor += colorList.count("pink")
    return (redColor, blueColor, greenColor, pinkColor)

# function that checks the availiable group of four cube areas below the given 
# index, get the colors and return the points based on the number of same 
# colors in a group
def belowAdjforBottomAI(app, cube, index):
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
        if 23 <= index <= 29:
            bottomColor = app.boardlist[index+7].color
            left = app.boardlist[index-1]
        if 24 <= index:
            bottomLeftColor = app.boardlist[index+6].color
        if 23 <= index <= 28:
            belowTwoColor = app.boardlist[index+14].color
        if index == 22:
                colorList =belowLeftCol(cube,right.color,anotherbottomColor, 
                            bottomRightColor,[])
        elif index == 23:
            colorList = checkAt23(cube, left.color, right.color, 
                        anotherbottomColor, bottomColor,
                            belowTwoColor,bottomRightColor,[])
        elif index == 28:
            colorList = checkAt28(cube, left.color, right.color, 
                        anotherbottomColor, bottomColor,
                            belowTwoColor,bottomLeftColor,[])
        elif index == 29:
            colorList = belowRightCol(cube,left.color,bottomLeftColor, 
                        bottomColor,[])
        else:
            right = app.boardlist[index+1]
            left = app.boardlist[index-1]
            colorList =belowElse(cube, left.color, right.color, 
             anotherbottomColor,belowTwoColor,bottomColor,
             bottomLeftColor,bottomRightColor,[])
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)

    if 30 <= index <= 36:
        if index <= 35:
            anotherbottomColor = app.boardlist[index+7].color
            right = app.boardlist[index+1]
        if index <=34:
            bottomRightColor = app.boardlist[index+8].color
        if 31 <= index <= 36:
            bottomColor = app.boardlist[index+6].color
            left = app.boardlist[index-1]
        if 32 <= index:
            bottomLeftColor = app.boardlist[index+5].color
        if 31 <= index <=35:
            belowTwoColor = app.boardlist[index+12].color
        if index == 30:
            colorList =belowLeftCol(cube,right.color,anotherbottomColor, 
                        bottomRightColor,[])
        elif index == 31:
            colorList = checkAt23(cube, left.color, right.color, 
                        anotherbottomColor, bottomColor,
                            belowTwoColor,bottomRightColor,[])
        elif index == 35:
            colorList = checkAt28(cube, left.color, right.color, 
                        anotherbottomColor, bottomColor,
                            belowTwoColor,bottomLeftColor,[])
        elif index == 36:
            colorList = belowRightCol(cube,left.color,bottomLeftColor, 
                        bottomColor,[])
        else:
            right = app.boardlist[index+1]
            left = app.boardlist[index-1]
            colorList =belowElse(cube, left.color, right.color, 
             anotherbottomColor,belowTwoColor,bottomColor,
             bottomLeftColor,bottomRightColor,[])
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)
    
    if 37 <= index <= 42:
        if index <= 41:
            anotherbottomColor = app.boardlist[index+6].color
            right = app.boardlist[index+1]
        if index <=40:
            bottomRightColor = app.boardlist[index+7].color
        if 38 <= index <= 42:
            bottomColor = app.boardlist[index+5].color
            left = app.boardlist[index-1]
        if 39 <= index:
            bottomLeftColor = app.boardlist[index+4].color
        if 38 <= index <= 41:
            belowTwoColor=app.boardlist[index+10].color
        if index == 37:
            colorList =belowLeftCol(cube,right.color,anotherbottomColor, 
                        bottomRightColor,[])
        elif index == 38:
            colorList = checkAt23(cube, left.color, right.color, 
                        anotherbottomColor, bottomColor,
                            belowTwoColor,bottomRightColor,[])
        elif index == 41:
            colorList = checkAt28(cube, left.color, right.color, 
                        anotherbottomColor, bottomColor,
                            belowTwoColor,bottomLeftColor,[])
        elif index == 42:
            colorList = belowRightCol(cube,left.color,bottomLeftColor, 
                        bottomColor,[])
        else:
            right = app.boardlist[index+1]
            left = app.boardlist[index-1]
            colorList =belowElse(cube, left.color, right.color, 
             anotherbottomColor,belowTwoColor,bottomColor,
             bottomLeftColor,bottomRightColor,[])
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)
    
    if 43 <= index <= 47:
        if index <= 46:
            anotherbottomColor = app.boardlist[index+5].color
            right = app.boardlist[index+1]
        if index <=45:
            bottomRightColor = app.boardlist[index+6].color
        if 44 <= index <= 47:
            bottomColor = app.boardlist[index+4].color
            left = app.boardlist[index-1]
        if 45 <= index:
            bottomLeftColor = app.boardlist[index+3].color
        if index == 43:
            colorList =belowLeftCol(cube,right.color,anotherbottomColor, 
                        bottomRightColor,[])
        elif index == 44:
            colorList = checkAt44(cube,left.color,right.color, 
                        anotherbottomColor, bottomColor,
                            bottomRightColor,[])
        elif index == 45:
            colorList = checkAt45(cube, left.color, right.color, 
                        anotherbottomColor, bottomColor,
                        bottomLeftColor,bottomRightColor,[])
        elif index == 46:
            colorList = checkAt46(cube,left.color,right.color,
               anotherbottomColor,bottomColor,bottomLeftColor,[])
        elif index == 47:
            colorList = belowRightCol(cube,left.color,bottomLeftColor, 
                        bottomColor,[])
        else:
            right = app.boardlist[index+1]
            left = app.boardlist[index-1]
            colorList =belowElse(cube, left.color, right.color, 
             anotherbottomColor,belowTwoColor,bottomColor,
             bottomLeftColor,bottomRightColor,[])
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)
    
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

# function that checks the availiable group of four cube areas above the given 
# index, get the colors and return the points based on the number of same 
# colors in a group
def aboveAdjforBottomAI(app, cube, index):
    redColor = blueColor = greenColor = pinkColor = 0
    colorList = []
    aboveLeftColor = aboveTwoColor = aboveColor = ''
    anotherAboveColor = aboveRightColor = ''
    if 30 <= index <= 36:
        aboveColor = app.boardlist[index-8].color
        anotherAboveColor = app.boardlist[index-7].color
        aboveTwoColor = app.boardlist[index-15].color
        if index <= 35:
            right = app.boardlist[index+1]
        if index <=34:
            aboveRightColor = app.boardlist[index-6].color
        if 31 <= index <= 36:
            left = app.boardlist[index-1]
        if 31 <= index:
            aboveLeftColor = app.boardlist[index-9].color
        if index == 30:
            colorList =aboveLeftColbelow(cube,right.color,aboveColor,
                        anotherAboveColor,aboveRightColor,aboveTwoColor,[])
        elif index == 36:
            colorList = aboveRightColbelow(cube,left.color,aboveColor,
                        anotherAboveColor,aboveLeftColor,aboveTwoColor,[])
        else:
            right = app.boardlist[index+1]
            left = app.boardlist[index-1]
            colorList =aboveElse(cube, left.color, right.color, aboveColor,
                  aboveRightColor,aboveTwoColor,anotherAboveColor,
                  aboveLeftColor,[])
    redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)

    if 37 <= index <= 42:
        aboveColor = app.boardlist[index-7].color
        anotherAboveColor = app.boardlist[index-6].color
        aboveTwoColor = app.boardlist[index-14].color
        if index <= 41:
            right = app.boardlist[index+1]
        if index <=40:
            aboveRightColor = app.boardlist[index-5].color
        if 38 <= index <= 42:
            left = app.boardlist[index-1]
        if 38 <= index:
            aboveLeftColor = app.boardlist[index-8].color
        if index == 37:
            colorList =aboveLeftColbelow(cube,right.color,aboveColor,
                        anotherAboveColor,aboveRightColor,aboveTwoColor,[])
        elif index == 42:
            colorList = aboveRightColbelow(cube,left.color,aboveColor,
                        anotherAboveColor,aboveLeftColor,aboveTwoColor,[])
        else:
            right = app.boardlist[index+1]
            left = app.boardlist[index-1]
            colorList =aboveElse(cube, left.color, right.color,aboveColor,
                  aboveRightColor,aboveTwoColor,anotherAboveColor,
                  aboveLeftColor,[])
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)
    
    if 43 <= index <= 47:
        aboveColor = app.boardlist[index-6].color
        anotherAboveColor = app.boardlist[index-5].color
        aboveTwoColor = app.boardlist[index-12].color
        if index <= 46:
            right = app.boardlist[index+1]
        if index <=45:
            aboveRightColor = app.boardlist[index-4].color
        if 44 <= index <= 47:
            left = app.boardlist[index-1]
        if 44 <= index:
            aboveLeftColor = app.boardlist[index-7].color
        if index == 43:
            colorList =aboveLeftColbelow(cube,right.color,aboveColor,
                        anotherAboveColor,aboveRightColor,aboveTwoColor,[])
        elif index == 47:
            colorList = aboveRightColbelow(cube,left.color,aboveColor,
                        anotherAboveColor,aboveLeftColor,aboveTwoColor,[])
        else:
            right = app.boardlist[index+1]
            left = app.boardlist[index-1]
            colorList =aboveElse(cube, left.color, right.color,aboveColor,
                  aboveRightColor,aboveTwoColor,anotherAboveColor,
                  aboveLeftColor,[])
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)
    
    if 48 <= index <= 51:
        aboveColor = app.boardlist[index-5].color
        anotherAboveColor = app.boardlist[index-4].color
        aboveTwoColor = app.boardlist[index-10].color
        if index <= 50:
            right = app.boardlist[index+1]
        if index <=49:
            aboveRightColor = app.boardlist[index-3].color
        if 49 <= index <= 51:
            left = app.boardlist[index-1]
        if 49 <= index:
            aboveLeftColor = app.boardlist[index-6].color
        if index == 48:
            colorList =aboveLeftColbelow(cube,right.color,aboveColor,
                        anotherAboveColor,aboveRightColor,aboveTwoColor,[])
        elif index == 51:
            colorList = aboveRightColbelow(cube,left.color,aboveColor,
                        anotherAboveColor,aboveLeftColor,aboveTwoColor,[])
        else:
            right = app.boardlist[index+1]
            left = app.boardlist[index-1]
            colorList =aboveElse(cube, left.color,right.color,aboveColor,
                  aboveRightColor,aboveTwoColor,anotherAboveColor,
                  aboveLeftColor,[])
        redColor, blueColor, greenColor, pinkColor = addColor(colorList, 
                                    redColor, blueColor, greenColor, pinkColor)

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