class BoardforLocal():
    def __init__(self,x,y,c,d,color):
        self.x = x
        self.y = y
        self.c = c
        self.d = d
        self.color = color 

    def drawAcube(self,canvas):
        # bottom surface
        canvas.create_polygon(self.x,self.y+self.d, 
                              self.x+1.5*self.c,self.y+0.5*self.d, 
                              self.x+3*self.c,self.y+self.d, 
                              self.x+1.5*self.c,self.y+1.5*self.d,
                              outline='black', fill=self.color)
        # left surface
        canvas.create_polygon(self.x, self.y, self.x,self.y+self.d, 
                              self.x+1.5*self.c,self.y+0.5*self.d, 
                              self.x+1.5*self.c,self.y-0.5*self.d, 
                              outline='black', fill=self.color)
        # right surface
        canvas.create_polygon(self.x+1.5*self.c,self.y+0.5*self.d, 
                              self.x+1.5*self.c,self.y-0.5*self.d, 
                              self.x+3*self.c,self.y, 
                              self.x+3*self.c,self.y+self.d,
                              outline='black',fill=self.color)

def createBoard(app):
    k = 10
    g = 9
    cubelist = []
    for i in range(g):
        if i <5:
            x = app.width *((5.0-(i*0.38))/13)
            y = app.height*((0.5+1.02*i)/11)
        else:
            x = app.width *((5.0-(g-i-1)*0.38)/13)
            y = app.height*((0.5+1.02*i)/11)
        for j in range(0,k,3):
            cube = BoardforLocal(x+j*30, y+50,30,50,'white')
            cubelist.append(cube)
        if i <4:
            k +=3
        else:
            k-=3
    return cubelist