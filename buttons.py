class Button(object):
  def __init__(self, x0, y0, x1, y1, text, onClick):
     # Takes in the bounding x/y coordinates, the test that is displayed on the button,
     self.x0 = x0
     self.y0 = y0
     self.x1 = x1
     self.y1 = y1
     self.text = text
     self.onClick = coverCard()
     # a function that gets called when the button is clicked, and stores them 
     # (you can add other stuff like colors)

  def click(self, x, y):
      if 
     # Calls self.onClick if (x, y) is inside of the box defined by (self.x0, self.y0, self.x1, self.y1)
     
  def render(self, canvas):
     # Draw the button on the canvas using self.x0, self.y0, self.x1, self.y1, etc.

def appStarted(app):
   # Defines a list of button objects
   app.buttons = [
      Button(insert, params, here, pls, "Hello!", thisIsAFunction),
      Button(insert, params, here, pls, "Goodbye!", thisIsAnotheFunction),
   ]

def mousePressed(app, event):
   # Loops over each button and calls its click method, which will call the corresponding onClick function
   # but only if the mouse was pressed on the button

def redrawAll(app, canvas):
   # Loops over each button and calls its render method, drawing each of them on the canvas.