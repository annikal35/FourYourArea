from cmu_112_graphics import *
from buttons import *
# from main import *
# from mainforlocal import *

def appStarted(app):
    app.buttons = [
        Button(200, 550, 420, 620, "1 Player"),
        Button(200, 670, 420, 740, "2 Players")
    ]
    app.image3 = app.loadImage('hexagon1.png')
    app.hexagon1 = app.scaleImage(app.image3, 0.6)
    app.image4 = app.loadImage('hexagon2.png')
    app.hexagon2 = app.scaleImage(app.image4, 0.6)

def mousePressed(app, event):
    if (200 <= event.x <= 420) and (550 <= event.y <= 620):
        app.mode = 'mode1'
    elif (200 <= event.x <= 420) and (670 <= event.y <= 740):
        app.mode = 'mode2'

# def timerFired(app, canvas):
#     if app.timePassed == 500:
#         canvas.create_image(50,50, image=ImageTk.PhotoImage(app.hexagon1))
#     app.timePassed = 0

def redrawAll(app, canvas):
    for button in app.buttons:
        button.render(canvas)
    # canvas.create_text()


runApp(width=1550, height=800)