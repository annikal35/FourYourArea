class UserOne():
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
        self.r2 = 22.5
        self.cardColor = 'white'
        self.bluecir = 'blue'
        self.redcir = 'red'
        self.greencir = 'green'
        self.pinkcir = 'pink'
        self.score = 0

    def player1(self, canvas):
        canvas.create_text(265, 50, text='Player 1', fill='purple',
                           font = 'Helvetica 30 bold italic')
                           
    def frontCard(self,canvas):
        # creates the front of a card
        canvas.create_rectangle(70,100,230,350,fill=self.cardColor, 
                                outline='black', width = 5)
        canvas.create_oval(110-self.r2, 140-self.r2, 110+self.r2, 140+self.r2, 
                           fill=self.bluecir, outline=self.bluecir)
        canvas.create_text(180,140, text = f'{self.numBlue}', fill='black',
                           font = 'Helvetica 30 bold')
        canvas.create_oval(110-self.r2, 200-self.r2, 110+self.r2, 200+self.r2, 
                           fill=self.redcir, outline=self.redcir)
        canvas.create_text(180,200, text = f'{self.numRed}', fill='black',
                           font = 'Helvetica 30 bold')
        canvas.create_oval(110-self.r2, 260-self.r2, 110+self.r2, 260+self.r2, 
                           fill=self.greencir, outline=self.greencir)
        canvas.create_text(180,260, text = f'{self.numGreen}', fill='black',
                           font = 'Helvetica 30 bold')
        canvas.create_oval(110-self.r2, 320-self.r2, 110+self.r2, 320+self.r2, 
                           fill=self.pinkcir, outline = self.pinkcir)
        canvas.create_text(180,320, text = f'{self.numPink}', fill='black',
                           font = 'Helvetica 30 bold')
        
    
    def backCard(self, canvas):
        # creates the back of a card
        canvas.create_rectangle(280,100,440,350, outline='black',
                                fill = self.cardColor, width=5)
        canvas.create_text(320,120, text='Picking', fill='black',
                           font = 'Times 13 bold underline')
        firstScore = self.pickingCard['1']
        canvas.create_text(320,145, text=f'1: {firstScore}', fill='black',
                           font = 'Times 17 bold')
        secondScore = self.pickingCard['2']
        canvas.create_text(320,175, text=f'2: {secondScore}', fill='black',
                           font = 'Times 17 bold')
        thirdScore = self.pickingCard['3']
        canvas.create_text(320,205, text=f'3: {thirdScore}', fill='black',
                           font = 'Times 17 bold')
        fourthScore = self.pickingCard['4']
        canvas.create_text(320,235, text=f'4: {fourthScore}', fill='black',
                           font = 'Times 17 bold')
        fifthScore = self.pickingCard['5']
        canvas.create_text(320,265, text=f'5: {fifthScore}', fill='black',
                           font = 'Times 17 bold')
        sixthScore = self.pickingCard['6']
        canvas.create_text(320,295, text=f'6: {sixthScore}', fill='black',
                           font = 'Times 17 bold')
        seventhScore = self.pickingCard['7']
        canvas.create_text(320,325, text=f'7: {seventhScore}', fill='black',
                           font = 'Times 17 bold')
        canvas.create_line(360,105,360,345, fill='black')
        canvas.create_text(400,120, text='Placing', fill='black',
                           font = 'Times 13 bold underline')
        firstPlacing = self.placingCard['1']
        canvas.create_text(400,170, text=f'1: {firstPlacing}', fill='black',
                           font = 'Times 20 bold')
        secondPlacing = self.placingCard['2']
        canvas.create_text(400,220, text=f'2: {secondPlacing}', fill='black',
                           font = 'Times 20 bold')
        thirdPlacing = self.placingCard['3']
        canvas.create_text(400,270, text=f'3: {thirdPlacing}', fill='black',
                           font = 'Times 20 bold')
        fourthPlacing = self.placingCard['4']
        canvas.create_text(400,320, text=f'4: {fourthPlacing}', fill='black',
                           font = 'Times 20 bold')

    def currentRocks(self, canvas):
        # creates the current rocks
        canvas.create_text(100,400, text='Your Current\n Rocks', fill='purple',
                           font = 'Helvetica 16 bold italic')
        canvas.create_oval(60-self.r, 480-self.r, 60+self.r, 480+self.r, 
                           fill='blue',outline='blue')
        canvas.create_text(120, 480, text = f' : {self.blue}',fill='black',
                           font = 'Helvetica 25')
        canvas.create_oval(60-self.r, 550-self.r, 60+self.r, 550+self.r, 
                           fill='red', outline='red')
        canvas.create_text(120, 550, text = f' : {self.red}',fill='black',
                           font = 'Helvetica 25')
        canvas.create_oval(60-self.r, 620-self.r, 60+self.r, 620+self.r, 
                           fill='green', outline='green')
        canvas.create_text(120, 620, text = f' : {self.green}',fill='black',
                           font = 'Helvetica 25')
        canvas.create_oval(60-self.r, 690-self.r, 60+self.r, 690+self.r, 
                           fill='pink', outline='pink')
        canvas.create_text(120, 690, text = f' : {self.pink}',fill='black',
                           font = 'Helvetica 25')