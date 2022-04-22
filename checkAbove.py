def putColor(cube,color1,color2,color3,colorList):
    colorList.append(cube.color)
    colorList.append(color1)
    colorList.append(color2)
    colorList.append(color3)
    return colorList

def aboveFarRight(cube,rightColor,anotherAboveColor,aboveRightColor,colorList):
    if ((cube.color != 'white') and (rightColor!='white') and 
    (aboveRightColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    anotherAboveColor,aboveRightColor,[])
    return colorList

def checkAt5(cube,leftColor,rightColor, aboveColor,
                  anotherAboveColor,aboveRightColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,leftColor,
                                    aboveColor,anotherAboveColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveColor,anotherAboveColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
       (aboveRightColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveRightColor,anotherAboveColor,[])
    return colorList

def checkAt7(cube,leftColor,rightColor, aboveColor,
                  anotherAboveColor,aboveLeftColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,leftColor,
                                    aboveColor,anotherAboveColor,[])
    if ((cube.color != 'white') and (leftColor!='white') and 
       (aboveColor!='white') and (aboveLeftColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveColor,aboveLeftColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveColor,anotherAboveColor,[])
    return colorList

def checkAt6(cube,leftColor,rightColor, aboveColor,aboveRightColor,
                  anotherAboveColor,aboveLeftColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
       (aboveColor!='white') and (aboveLeftColor!='white')):
        colorList = putColor(cube,leftColor,
                                    aboveColor,aboveLeftColor,[])
    if ((cube.color != 'white') and (leftColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveColor,anotherAboveColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveColor,anotherAboveColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
       (aboveRightColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveRightColor,anotherAboveColor,[])
    return colorList

def aboveleftCol(cube,leftColor,rightColor, aboveColor,aboveTwoColor,
                  anotherAboveColor,aboveRightColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,leftColor,
                                    aboveColor,anotherAboveColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveColor,anotherAboveColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
       (aboveRightColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveRightColor,anotherAboveColor,[])
    if ((cube.color != 'white') and (aboveTwoColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,aboveTwoColor,
                                    aboveColor,anotherAboveColor,[])
    return colorList
    
def aboveRightCol(cube,leftColor,rightColor, aboveColor,aboveTwoColor,
                  anotherAboveColor,aboveLeftColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,leftColor,
                                    aboveColor,anotherAboveColor,[])
    if ((cube.color != 'white') and (leftColor!='white') and 
       (aboveColor!='white') and (aboveLeftColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveColor,aboveLeftColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveColor,anotherAboveColor,[])
    if ((cube.color != 'white') and (aboveTwoColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,aboveTwoColor,
                                    aboveColor,anotherAboveColor,[])
    return colorList  
          

def aboveFarLeft(cube, leftColor,aboveLeftColor,aboveColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
    (aboveLeftColor!='white') and (aboveColor!='white')):
        colorList = putColor(cube,leftColor,
                                    aboveLeftColor,aboveColor,[])
    return colorList

def aboveElse(cube,leftColor,rightColor, aboveColor,aboveRightColor,
                aboveTwoColor,anotherAboveColor,aboveLeftColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
       (aboveColor!='white') and (aboveLeftColor!='white')):
        colorList = putColor(cube,leftColor,
                                    aboveColor,aboveLeftColor,[])
    if ((cube.color != 'white') and (leftColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveColor,anotherAboveColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveColor,anotherAboveColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
       (aboveRightColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveRightColor,anotherAboveColor,[])
    if ((cube.color != 'white') and (aboveTwoColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,aboveTwoColor,
                                    aboveColor,anotherAboveColor,[])
    return colorList