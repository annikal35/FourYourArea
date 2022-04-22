class Button(object):
  def __init__(self, x0, y0, x1, y1, text):
     # Takes in the bounding x/y coordinates, the test that is displayed on the button,
     self.x0 = x0
     self.y0 = y0
     self.x1 = x1
     self.y1 = y1
     self.text = text
     # a function that gets called when the button is clicked, and stores them 
     # (you can add other stuff like colors)

     
  def render(self, canvas):
      canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill='white',
                           outline = 'purple')
      canvas.create_text((self.x1+self.x0)/2, (self.y1+self.y0)/2, 
                          text=self.text, fill='purple', 
                        font='Helvetica 20 bold italic')
     # Draw the button on the canvas using self.x0, self.y0, self.x1, self.y1, etc.

