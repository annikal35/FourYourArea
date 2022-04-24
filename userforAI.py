import random

class AI():
    def __init__(self):
        self.blue = 0
        self.red = 0
        self.green = 0
        self.pink = 0
        self.numBlue = 0
        self.numRed = 0
        self.numGreen = 0
        self.numPink = 0
        self.placingCard = {'1':0,'2':0,'3':0,'4':0}
        self.pickingCard = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0}
        self.r = 25
        self.score = 0
        self.currSameColor = 0
        self.coloredCube = []
        self.colors = {'blue': self.blue, 'red':self.red, 
                        'green':self.green,'pink':self.pink}
        self.rockNumAI = 0

class User():
    def __init__(self):
        self.blue = 0
        self.red = 0
        self.green = 0
        self.pink = 0
        self.numBlue = 0
        self.numRed = 0
        self.numGreen = 0
        self.numPink = 0
        self.placingCard = {'1':0,'2':0,'3':0,'4':0}
        self.pickingCard = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0}
        self.r = 25
        self.score = 0
        self.currSameColor = 0
        self.coloredCube = []
        # self.i = random.randint(0,20)

    def frontCard(self,canvas):
        canvas.create_rectangle(750,450,950,750,fill='white', 
                                outline='black', width = 5)
        canvas.create_oval(810-self.r, 500-self.r, 810+self.r, 500+self.r, 
                           fill='blue', outline='blue')
        canvas.create_text(900,500, text = f'{self.numBlue}', fill='black',
                           font = 'Helvetica 30 bold')
        canvas.create_oval(810-self.r, 570-self.r, 810+self.r, 570+self.r, 
                           fill='red', outline='red')
        canvas.create_text(900,570, text = f'{self.numRed}', fill='black',
                           font = 'Helvetica 30 bold')
        canvas.create_oval(810-self.r, 640-self.r, 810+self.r, 640+self.r, 
                           fill='green', outline='green')
        canvas.create_text(900,640, text = f'{self.numGreen}', fill='black',
                           font = 'Helvetica 30 bold')
        canvas.create_oval(810-self.r, 710-self.r, 810+self.r, 710+self.r, 
                           fill='pink', outline = 'pink')
        canvas.create_text(900,710, text = f'{self.numPink}', fill='black',
                           font = 'Helvetica 30 bold')
        

    def backCard(self, canvas):
        canvas.create_rectangle(980,450,1180,750, outline='black',
                                fill = 'white', width=5)
        canvas.create_text(1025,470, text='Picking', fill='black',
                           font = 'Times 16 bold underline')
        firstScore = self.pickingCard['1']
        canvas.create_text(1010,505, text=f'1: {firstScore}', fill='black',
                           font = 'Times 17 bold')
        secondScore = self.pickingCard['2']
        canvas.create_text(1010,540, text=f'2: {secondScore}', fill='black',
                           font = 'Times 17 bold')
        thirdScore = self.pickingCard['3']
        canvas.create_text(1010,575, text=f'3: {thirdScore}', fill='black',
                           font = 'Times 17 bold')
        fourthScore = self.pickingCard['4']
        canvas.create_text(1010,610, text=f'4: {fourthScore}', fill='black',
                           font = 'Times 17 bold')
        fifthScore = self.pickingCard['5']
        canvas.create_text(1010,645, text=f'5: {fifthScore}', fill='black',
                           font = 'Times 17 bold')
        sixthScore = self.pickingCard['6']
        canvas.create_text(1010,680, text=f'6: {sixthScore}', fill='black',
                           font = 'Times 17 bold')
        seventhScore = self.pickingCard['7']
        canvas.create_text(1010,715, text=f'7: {seventhScore}', fill='black',
                           font = 'Times 17 bold')
        canvas.create_line(1080,460,1080,740, fill='black')
        canvas.create_text(1125,470, text='Placing', fill='black',
                           font = 'Times 16 bold underline')
        firstPlacing = self.placingCard['1']
        canvas.create_text(1120,530, text=f'1: {firstPlacing}', fill='black',
                           font = 'Times 20 bold')
        secondPlacing = self.placingCard['2']
        canvas.create_text(1120,590, text=f'2: {secondPlacing}', fill='black',
                           font = 'Times 20 bold')
        thirdPlacing = self.placingCard['3']
        canvas.create_text(1120,650, text=f'3: {thirdPlacing}', fill='black',
                           font = 'Times 20 bold')
        fourthPlacing = self.placingCard['4']
        canvas.create_text(1120,710, text=f'4: {fourthPlacing}', fill='black',
                           font = 'Times 20 bold')
    def currentScore(self, canvas):
        canvas.create_text(1350,50, text='Your Current Rocks', fill='purple',
                           font = 'Helvetica 20 bold italic')
        canvas.create_oval(1300-self.r, 110-self.r, 1300+self.r, 110+self.r, 
                           fill='blue',outline='blue')
        canvas.create_text(1350, 110, text = f' : {self.blue}',fill='black',
                           font = 'Helvetica 25')
        canvas.create_oval(1300-self.r, 170-self.r, 1300+self.r, 170+self.r, 
                           fill='red', outline='red')
        canvas.create_text(1350, 170, text = f' : {self.red}',fill='black',
                           font = 'Helvetica 25')
        canvas.create_oval(1300-self.r, 230-self.r, 1300+self.r, 230+self.r, 
                           fill='green', outline='green')
        canvas.create_text(1350, 230, text = f' : {self.green}',fill='black',
                           font = 'Helvetica 25')
        canvas.create_oval(1300-self.r, 290-self.r, 1300+self.r, 290+self.r, 
                           fill='pink', outline='pink')
        canvas.create_text(1350, 290, text = f' : {self.pink}',fill='black',
                           font = 'Helvetica 25')

def getRandomPlacingScore():
        placingSet = [  {'1':2,'2':4,'3':6,'4':7}, {'1':1,'2':3,'3':5,'4':7}, 
                        {'1':1,'2':3,'3':6,'4':8}, {'1':3,'2':4,'3':5,'4':6},
                        {'1':1,'2':2,'3':3,'4':4}, {'1':2,'2':3,'3':5,'4':7},
                        {'1':2,'2':3,'3':4,'4':6}, {'1':2,'2':4,'3':6,'4':7},
                        {'1':3,'2':5,'3':7,'4':9}, {'1':1,'2':2,'3':5,'4':7}, 
                        {'1':0.5,'2':2,'3':4,'4':5}, {'1':2,'2':3,'3':4,'4':5},
                        {'1':1,'2':3,'3':5,'4':6}, {'1':2,'2':4,'3':6,'4':8},
                        {'1':3,'2':4,'3':6,'4':6}, {'1':1,'2':2,'3':4,'4':6},
                        {'1':2,'2':3,'3':5,'4':6}, {'1':1,'2':3,'3':4,'4':6},
                        {'1':0.5,'2':2,'3':3,'4':5}, {'1':2,'2':4,'3':5,'4':6}]
        return random.choice(placingSet)
    
def getRandomPickingScore():
    pickingSet = [  {'1':1,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6},
                    {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7},
                    {'1':1,'2':1,'3':2,'4':4,'5':6,'6':7,'7':8},
                    {'1':1,'2':1,'3':2,'4':4,'5':7,'6':8,'7':10},
                    {'1':1,'2':3,'3':4,'4':5,'5':8,'6':11,'7':15},
                    {'1':2,'2':2,'3':4,'4':6,'5':8,'6':10,'7':12},
                    {'1':1,'2':3,'3':5,'4':7,'5':9,'6':11,'7':13},
                    {'1':2,'2':2,'3':4,'4':8,'5':9,'6':10,'7':14},
                    {'1':1,'2':2,'3':3,'4':6,'5':8,'6':9,'7':11},
                    {'1':1,'2':2,'3':4,'4':5,'5':7,'6':9,'7':12},
                    {'1':1,'2':1,'3':3,'4':4,'5':6,'6':7,'7':9},
                    {'1':2,'2':3,'3':6,'4':7,'5':9,'6':11,'7':13},
                    {'1':1,'2':1,'3':2,'4':4,'5':6,'6':7,'7':8}, 
                    {'1':3,'2':5,'3':6,'4':8,'5':11,'6':13,'7':16},
                    {'1':1,'2':1,'3':2,'4':4,'5':6,'6':7,'7':10},
                    {'1':1,'2':2,'3':2,'4':4,'5':5,'6':8,'7':11},
                    {'1':2,'2':3,'3':4,'4':4,'5':8,'6':10,'7':13},
                    {'1':1,'2':1,'3':2,'4':3,'5':6,'6':8,'7':12},
                    {'1':1,'2':3,'3':5,'4':6,'5':9,'6':13,'7':16},
                    {'1':1,'2':1,'3':2,'4':4,'5':6,'6':7,'7':10}]
    return random.choice(pickingSet)