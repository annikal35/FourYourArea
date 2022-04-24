def putColor(cube,color1,color2,color3,colorList):
    colorList.append(cube.color)
    colorList.append(color1)
    colorList.append(color2)
    colorList.append(color3)
    return colorList

def aboveLeftColbelow(cube,rightColor,aboveColor,anotherAboveColor,
                                aboveRightColor,colorList):
    if ((cube.color != 'white') and (rightColor!='white') and 
    (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube, rightColor, 
                            aboveColor, anotherAboveColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
    (anotherAboveColor!='white') and (aboveRightColor!='white')):
        colorList = putColor(cube, rightColor, 
                            anotherAboveColor,aboveRightColor,[])
    return colorList

def aboveRightColbelow(cube,leftColor,aboveColor,anotherAboveColor,
                                aboveLeftColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
    (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube, leftColor, 
                            aboveColor, anotherAboveColor,[])
    if ((cube.color != 'white') and (leftColor!='white') and 
    (aboveColor!='white') and (aboveLeftColor!='white')):
        colorList = putColor(cube, leftColor, 
                            anotherAboveColor,aboveLeftColor,[])
    return colorList

def aboveElse(cube, leftColor, rightColor, anotheraboveColor,
          aboveTwoColor,aboveColor,aboveLeftColor,aboveRightColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
    (aboveColor!='white') and (aboveLeftColor!='white')):
        colorList = putColor(cube, leftColor, 
                            aboveColor, aboveLeftColor,[])
    if ((cube.color != 'white') and (aboveTwoColor!='white') and 
    (aboveColor!='white') and (anotheraboveColor!='white')):
        colorList = putColor(cube, aboveTwoColor, 
                            aboveColor, anotheraboveColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
    (anotheraboveColor!='white') and (aboveColor!='white')):
        colorList = putColor(cube, rightColor, 
                            anotheraboveColor, aboveColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
    (anotheraboveColor!='white') and (aboveRightColor!='white')):
        colorList = putColor(cube, rightColor, 
                            anotheraboveColor, aboveRightColor,[])
    if ((cube.color != 'white') and (leftColor!='white') and 
    (aboveColor!='white') and (anotheraboveColor!='white')):
        colorList = putColor(cube, leftColor, 
                            aboveColor, anotheraboveColor,[])
    return colorList