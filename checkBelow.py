def checkingBelow(cube, belowColor, bottomColor, anotherbottomColor,colorList):
    colorList.append(cube.color)
    colorList.append(belowColor)
    colorList.append(bottomColor)
    colorList.append(anotherbottomColor)
    return colorList

def checkRightMost(cube, rightColor, bottomRightColor,
                      anotherbottomColor,colorList):
    colorList.append(cube.color)
    colorList.append(rightColor)
    colorList.append(anotherbottomColor)
    colorList.append(bottomRightColor)
    return colorList
            
def checkLeftMost(cube, leftColor,bottomColor,bottomLeftColor, colorList):
    colorList.append(cube.color)
    colorList.append(leftColor)
    colorList.append(bottomColor)
    colorList.append(bottomLeftColor)
    return colorList

def checkRight(cube, rightColor, bottomColor, anotherBottomColor, colorList):
    colorList.append(cube.color)
    colorList.append(rightColor)
    colorList.append(bottomColor)
    colorList.append(anotherBottomColor)
    return colorList

def checkLeft(cube, leftColor, anotherbottomColor, bottomColor,colorList):
    colorList.append(cube.color)
    colorList.append(leftColor)
    colorList.append(anotherbottomColor)
    colorList.append(bottomColor)
    return colorList

def addColor(colorList, redColor, blueColor, greenColor, pinkColor):
    redColor += colorList.count("red")
    blueColor += colorList.count("blue")
    greenColor += colorList.count("green")
    pinkColor += colorList.count("pink")
    return (redColor, blueColor, greenColor, pinkColor)

def checkElse(cube, rightColor,leftColor,bottomLeftColor, 
              anotherbottomColor, bottomRightColor, belowColor,
            bottomColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
    (bottomLeftColor!='white') and (bottomColor!='white')):
            colorList = checkLeft(cube, leftColor, 
                            anotherbottomColor, bottomColor,[])
    elif ((cube.color != 'white') and (belowColor!='white') and 
    (bottomColor!='white') and (anotherbottomColor!='white')):
        print(belowColor, anotherbottomColor, bottomColor)
        colorList = checkingBelow(cube, belowColor, bottomColor, 
                    anotherbottomColor,[])
    elif ((cube.color != 'white') and (rightColor!='white') and 
    (anotherbottomColor!='white') and (bottomRightColor!='white')):
            colorList = checkRightMost(cube, rightColor, bottomRightColor,
                    anotherbottomColor,[])
    return colorList

def checkAt0(cube, rightColor,anotherbottomColor, bottomRightColor, 
            belowColor,bottomColor,colorList):
    if ((cube.color != 'white') and (rightColor!='white') and 
    (bottomColor!='white') and (anotherbottomColor!='white')):
        colorList = checkRight(cube, rightColor, bottomColor, 
                    anotherbottomColor,[])
    if ((cube.color != 'white') and (belowColor!='white') and 
        (bottomColor!='white') and (anotherbottomColor!='white')):
        colorList = checkingBelow(cube, belowColor, bottomColor, 
                anotherbottomColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
             (anotherbottomColor!='white') and (bottomRightColor!='white')):
        colorList = checkRightMost(cube, rightColor, bottomRightColor,
                anotherbottomColor,[])
    return colorList

def checkAt3(cube, leftColor,anotherbottomColor, bottomLeftColor, 
            belowColor,bottomColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
        (anotherbottomColor!='white') and (bottomColor!='white')):
        colorList = checkLeft(cube, leftColor, 
                            anotherbottomColor, bottomColor,[])
    if ((cube.color != 'white') and (belowColor!='white') and 
        (bottomColor!='white') and (anotherbottomColor!='white')):
        colorList = checkingBelow(cube, belowColor, bottomColor, 
                anotherbottomColor,[])
    if ((cube.color != 'white') and (leftColor!='white') and 
        (bottomColor!='white') and (bottomLeftColor!='white')):
        colorList = checkLeftMost(cube, leftColor,bottomColor,
                                    bottomLeftColor, [])
    return colorList

def checkAtFour(cube, rightColor,anotherbottomColor, bottomRightColor, 
            belowColor,bottomColor,colorList):
    if ((cube.color != 'white') and (rightColor!='white') and 
        (bottomColor!='white') and (anotherbottomColor!='white')):
        colorList = checkRight(cube, rightColor, bottomColor, 
                            anotherbottomColor,[])
    if ((cube.color != 'white') and (belowColor!='white') and 
(bottomColor!='white') and (anotherbottomColor!='white')):
        colorList = checkingBelow(cube, belowColor, bottomColor, 
                anotherbottomColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
(anotherbottomColor!='white') and (bottomRightColor!='white')):
        colorList = checkRightMost(cube, rightColor, bottomRightColor,
                anotherbottomColor,[])
    return colorList

def checkAtEight(cube, leftColor,anotherbottomColor,
                    bottomLeftColor,belowColor,bottomColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
    (anotherbottomColor!='white') and (bottomColor!='white')):
            colorList = checkLeft(cube, leftColor, 
                            anotherbottomColor, bottomColor,[])
    if ((cube.color != 'white') and (leftColor!='white') and 
        (bottomColor!='white') and (bottomLeftColor!='white')):
        colorList = checkLeftMost(cube, leftColor,bottomColor,
                                    bottomLeftColor, [])
    if ((cube.color != 'white') and (belowColor!='white') and 
        (bottomColor!='white') and (anotherbottomColor!='white')):
        colorList = checkingBelow(cube, belowColor, bottomColor, 
                anotherbottomColor,[])
    return colorList