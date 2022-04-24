def putColor(cube,color1,color2,color3,colorList):
    colorList.append(cube.color)
    colorList.append(color1)
    colorList.append(color2)
    colorList.append(color3)
    return colorList

def belowLeftCol(cube,rightColor,anotherbottomColor, 
                                bottomRightColor,colorList):
    if ((cube.color != 'white') and (rightColor!='white') and 
    (anotherbottomColor!='white') and (bottomRightColor!='white')):
        colorList = putColor(cube, rightColor, 
                            anotherbottomColor, bottomRightColor,[])
    return colorList

def belowRightCol(cube,leftColor,bottomLeftColor, 
                                bottomColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
    (bottomLeftColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, leftColor, 
                            bottomLeftColor, bottomColor,[])
    return colorList

def checkAt23(cube, leftColor, rightColor, anotherbottomColor,
              bottomColor,belowTwoColor,bottomRightColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
    (anotherbottomColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, leftColor, 
                            anotherbottomColor, bottomColor,[])
    if ((cube.color != 'white') and (belowTwoColor!='white') and 
    (anotherbottomColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, belowTwoColor, 
                            anotherbottomColor, bottomColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
    (anotherbottomColor!='white') and (bottomRightColor!='white')):
        colorList = putColor(cube, rightColor, 
                            anotherbottomColor, bottomRightColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
    (anotherbottomColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, rightColor, 
                            anotherbottomColor, bottomColor,[])
    return colorList

def checkAt28(cube, leftColor, rightColor, anotherbottomColor,buttomLeftColor,
              bottomColor,belowTwoColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
    (anotherbottomColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, leftColor, 
                            anotherbottomColor, bottomColor,[])
    if ((cube.color != 'white') and (belowTwoColor!='white') and 
    (anotherbottomColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, belowTwoColor, 
                            anotherbottomColor, bottomColor,[])
    if ((cube.color != 'white') and (leftColor!='white') and 
    (bottomColor!='white') and (buttomLeftColor!='white')):
        colorList = putColor(cube, leftColor, 
                            bottomColor, buttomLeftColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
    (anotherbottomColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, rightColor, 
                            anotherbottomColor, bottomColor,[])
    return colorList

def checkAt44(cube, leftColor, rightColor, anotherbottomColor,
              bottomColor,bottomRightColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
    (anotherbottomColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, leftColor, 
                            anotherbottomColor, bottomColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
    (anotherbottomColor!='white') and (bottomRightColor!='white')):
        colorList = putColor(cube, rightColor, 
                            anotherbottomColor,bottomRightColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
    (anotherbottomColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, rightColor, 
                            anotherbottomColor, bottomColor,[])
    return colorList

def checkAt45(cube, leftColor, rightColor, anotherbottomColor,
              bottomColor,bottomLeftColor,bottomRightColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
    (anotherbottomColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, leftColor, 
                            anotherbottomColor, bottomColor,[])
    if ((cube.color != 'white') and (leftColor!='white') and 
    (bottomLeftColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, leftColor, 
                            bottomLeftColor, bottomColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
    (anotherbottomColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, rightColor, 
                            anotherbottomColor, bottomColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
    (anotherbottomColor!='white') and (bottomRightColor!='white')):
        colorList = putColor(cube, rightColor, 
                            anotherbottomColor, bottomRightColor,[])
    return colorList

def checkAt46(cube, leftColor, rightColor, anotherbottomColor,
              bottomColor,bottomLeftColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
    (anotherbottomColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, leftColor, 
                            anotherbottomColor, bottomColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
    (anotherbottomColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, rightColor, 
                            anotherbottomColor,bottomColor,[])
    if ((cube.color != 'white') and (leftColor!='white') and 
    (bottomLeftColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, rightColor, 
                            anotherbottomColor, bottomColor,[])
    return colorList

def belowElse(cube, leftColor, rightColor, anotherbottomColor,belowTwoColor,
              bottomColor,bottomLeftColor,bottomRightColor,colorList):
    if ((cube.color != 'white') and (leftColor!='white') and 
    (anotherbottomColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, leftColor, 
                            anotherbottomColor, bottomColor,[])
    if ((cube.color != 'white') and (leftColor!='white') and 
    (bottomLeftColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, leftColor, 
                            bottomLeftColor, bottomColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
    (anotherbottomColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, rightColor, 
                            anotherbottomColor, bottomColor,[])
    if ((cube.color != 'white') and (rightColor!='white') and 
    (anotherbottomColor!='white') and (bottomRightColor!='white')):
        colorList = putColor(cube, rightColor, 
                            anotherbottomColor, bottomRightColor,[])
    if ((cube.color != 'white') and (belowTwoColor!='white') and 
    (anotherbottomColor!='white') and (bottomColor!='white')):
        colorList = putColor(cube, belowTwoColor, 
                            anotherbottomColor, bottomColor,[])
    return colorList
    