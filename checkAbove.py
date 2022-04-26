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
                                    anotherAboveColor,aboveRightColor,colorList)
    return colorList

def checkAt5(cube,leftColor,rightColor, aboveColor,
                  anotherAboveColor,aboveRightColor,colorList):
   #  print(aboveColor, anotherAboveColor, aboveRightColor)
    if ((cube.color != 'white') and (leftColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,leftColor,
                                    aboveColor,anotherAboveColor,colorList)
    if ((cube.color != 'white') and (rightColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveColor,anotherAboveColor,colorList)
    if ((cube.color != 'white') and (rightColor!='white') and 
       (aboveRightColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveRightColor,anotherAboveColor,colorList)
    return colorList

def checkAt7(cube,leftColor,rightColor, aboveColor,
                  anotherAboveColor,aboveLeftColor,colorList):
   # print(aboveColor, anotherAboveColor,aboveLeftColor)
   if ((cube.color != 'white') and (leftColor!='white') and 
      (aboveColor!='white') and (anotherAboveColor!='white')):
      colorList = putColor(cube,leftColor,
                                 aboveColor,anotherAboveColor,colorList)
   if ((cube.color != 'white') and (leftColor!='white') and 
      (aboveColor!='white') and (aboveLeftColor!='white')):
      colorList = putColor(cube,rightColor,
                                 aboveColor,aboveLeftColor,colorList)
   if ((cube.color != 'white') and (rightColor!='white') and 
      (aboveColor!='white') and (anotherAboveColor!='white')):
      colorList = putColor(cube,rightColor,
                                 aboveColor,anotherAboveColor,colorList)
   return colorList

def checkAt6(cube,leftColor,rightColor, aboveColor,aboveRightColor,
                  anotherAboveColor,aboveLeftColor,colorList):
   # print(aboveColor, aboveRightColor, anotherAboveColor,aboveLeftColor)
   if ((cube.color != 'white') and (leftColor!='white') and 
      (aboveColor!='white') and (aboveLeftColor!='white')):
      colorList = putColor(cube,leftColor,
                                 aboveColor,aboveLeftColor,colorList)
   if ((cube.color != 'white') and (leftColor!='white') and 
      (aboveColor!='white') and (anotherAboveColor!='white')):
      colorList = putColor(cube,rightColor,
                                 aboveColor,anotherAboveColor,colorList)
   if ((cube.color != 'white') and (rightColor!='white') and 
      (aboveColor!='white') and (anotherAboveColor!='white')):
      colorList = putColor(cube,rightColor,
                                 aboveColor,anotherAboveColor,colorList)
   if ((cube.color != 'white') and (rightColor!='white') and 
      (aboveRightColor!='white') and (anotherAboveColor!='white')):
      colorList = putColor(cube,rightColor,
                                 aboveRightColor,anotherAboveColor,colorList)
   return colorList

def aboveleftCol(cube,leftColor,rightColor, aboveColor,aboveTwoColor,
                  anotherAboveColor,aboveRightColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,leftColor,
                                    aboveColor,anotherAboveColor,colorList)
    if ((cube.color != 'white') and (rightColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveColor,anotherAboveColor,colorList)
    if ((cube.color != 'white') and (rightColor!='white') and 
       (aboveRightColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveRightColor,anotherAboveColor,colorList)
    if ((cube.color != 'white') and (aboveTwoColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,aboveTwoColor,
                                    aboveColor,anotherAboveColor,colorList)
    return colorList
    
def aboveRightCol(cube,leftColor,rightColor, aboveColor,aboveTwoColor,
                  anotherAboveColor,aboveLeftColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,leftColor,
                                    aboveColor,anotherAboveColor,colorList)
    if ((cube.color != 'white') and (leftColor!='white') and 
       (aboveColor!='white') and (aboveLeftColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveColor,aboveLeftColor,colorList)
    if ((cube.color != 'white') and (rightColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveColor,anotherAboveColor,colorList)
    if ((cube.color != 'white') and (aboveTwoColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,aboveTwoColor,
                                    aboveColor,anotherAboveColor,colorList)
    return colorList  
          

def aboveFarLeft(cube, leftColor,aboveLeftColor,aboveColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
    (aboveLeftColor!='white') and (aboveColor!='white')):
        colorList = putColor(cube,leftColor,
                                    aboveLeftColor,aboveColor,colorList)
    return colorList

def aboveElse(cube,leftColor,rightColor, aboveColor,aboveRightColor,
                aboveTwoColor,anotherAboveColor,aboveLeftColor,colorList):
   # print(aboveColor, anotherAboveColor, aboveRightColor,aboveTwoColor,aboveLeftColor)
   if ((cube.color != 'white') and (leftColor!='white') and 
       (aboveColor!='white') and (aboveLeftColor!='white')):
        colorList = putColor(cube,leftColor,
                                    aboveColor,aboveLeftColor,colorList)
   if ((cube.color != 'white') and (leftColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveColor,anotherAboveColor,colorList)
   if ((cube.color != 'white') and (rightColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveColor,anotherAboveColor,colorList)
   if ((cube.color != 'white') and (rightColor!='white') and 
       (aboveRightColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,rightColor,
                                    aboveRightColor,anotherAboveColor,colorList)
   if ((cube.color != 'white') and (aboveTwoColor!='white') and 
       (aboveColor!='white') and (anotherAboveColor!='white')):
        colorList = putColor(cube,aboveTwoColor,
                                    aboveColor,anotherAboveColor,colorList)
   return colorList