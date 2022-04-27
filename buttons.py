class Button(object):
  def __init__(self, x0, y0, x1, y1, text):
     self.x0 = x0
     self.y0 = y0
     self.x1 = x1
     self.y1 = y1
     self.text = text

     
  def render(self, canvas):
     # Draw the button on the canvas using self.x0, self.y0, self.x1, self.y1
      canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill='white',
                           outline = 'purple')
      canvas.create_text((self.x1+self.x0)/2, (self.y1+self.y0)/2, 
                          text=self.text, fill='purple', 
                        font='Helvetica 20 bold italic')

