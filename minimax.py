from board import *
from userforAI import *
from cmu_112_graphics import *
from TopScoringAI import *
from BottomScoringAI import *
from buttons import *

def appStarted(app):
    app.image1 = app.loadImage('Deck_of_Cards.png')
    app.cardDeck = app.scaleImage(app.image1, 0.6)
    app.image2 = app.loadImage('rockbag.png')
    app.rockBag = app.scaleImage(app.image2, 0.15)
    app.user = User()
    app.AI = True
    app.AIScore = 0
    app.boardlist = createBoard(app)
    app.possibleMoves = []
    app.coloredCube = []
    app.status = 'User'
    app.round = 1

def getPossibleMoves(app,board):
    for cube in board:
        if cube.color == 'white':
            app.possibleMoves.append(cube.color)

def isLegal(app, currCube):
    index = app.boardlist.index(currCube)
    if index > 52 or index <0 or currCube.color != 'white':
        return False
    return True
    

def gameover(app):
    if app.round >= 4:
        return False
    for cube in app.boardlist:
        if cube.color == 'white':
            return False
    return True


def minimax(state,move, depth, maxPlayer,app):
    if (depth == 0) or gameover(state):
        score = evaluate(state,move,app)
        return score

    if maxPlayer == app.AI:
        maxValue = float('-inf')
        for move in app.possibleMoves:
            if isLegal(app, move):
                index = app.boardlist.index(move)
                #move.color = ?
                currValue = minimax(app.boardlist,move,depth-1,False,app)
                maxValue = max(maxValue,currValue)
        return maxValue
    else:
        minValue = float('inf')
        for move in app.possibleMoves:
            if isLegal(app, move):
                index = app.boardlist.index(move)
                #move.color = ?
                currValue = minimax(app.boardlist,move,depth-1,True,app)
                minValue = min(currValue, minValue)
        return minValue

def evaluate(state,move,app):
    userScore = app.user.score
    if isWin(state, move,userScore,app):
        return 1
    elif isLost(state,move, userScore,app):
        return -1
    else:
        return 0

def isWin(state, currCube, userScore,app):
    index = state.indeX(currCube)
    if 0 <= index <= 3:
        app.AIScore += belowAdjforTop(app,
                        currCube,index)
    if 4 <= index <= 29:
        app.AIScore += belowAdjforTop(app,
                        currCube,index)
        if app.AIScore == 0:
            app.AIScore += aboveAdjforTop(app,
                currCube,index)
        if app.AIScore == 0:
            app.AIScore += belowAdjforBottom(app,
                            currCube, index)
    if 30 <= index <= 47:
        app.AIScore += belowAdjforBottom(app,
                            currCube, index)
        if app.AIScore == 0:
            app.AIScore += aboveAdjforBottom(app, 
                            currCube, index)
    else:
        app.user.score += aboveAdjforBottom(app, 
                            currCube, index)
    return app.AIScore > userScore

def isLost(state, currCube, userScore,app):
    index = state.indeX(currCube)
    if 0 <= index <= 3:
        app.AIScore += belowAdjforTop(app,
                        currCube,index)
    if 4 <= index <= 29:
        app.AIScore += belowAdjforTop(app,
                        currCube,index)
        if app.AIScore == 0:
            app.AIScore += aboveAdjforTop(app,
                currCube,index)
        if app.AIScore == 0:
            app.AIScore += belowAdjforBottom(app,
                            currCube, index)
    if 30 <= index <= 47:
        app.AIScore += belowAdjforBottom(app,
                            currCube, index)
        if app.AIScore == 0:
            app.AIScore += aboveAdjforBottom(app, 
                            currCube, index)
    else:
        app.user.score += aboveAdjforBottom(app, 
                            currCube, index)
    return app.AIScore < userScore


    # if 0 <= index <= 3:
    #     app.AIScore += belowAdjforTop(app,
    #                     currCube,index)
    #     break
    # if 4 <= index <= 29:
    #     app.AIScore += belowAdjforTop(app,
    #                     currCube,index)
    #     if app.AIScore == 0:
    #         app.AIScore += aboveAdjforTop(app,
    #             currCube,index)
    #         break
    #     if app.AIScore == 0:
    #         app.AIScore += belowAdjforBottom(app,
    #                         currCube, index)
    #         break
    #     break 
    # if 30 <= index <= 47:
    #     app.AIScore += belowAdjforBottom(app,
    #                         currCube, index)
    #     if app.AIScore == 0:
    #         app.AIScore += aboveAdjforBottom(app, 
    #                         currCube, index)
    #         break
    #     break
    # else:
    #     app.AIScore += aboveAdjforBottom(app, 
    #                         currCube, index)
    #     break

# def isLegal(move):

# possibleMoves = getPossibleMoves(app.boardlist)

# def getPossibleMoves(board):
#     for cube in board:
#         if cube.color == 'white':
            # possibleMoves.append(cube.color)
#     return possibleMoves


# def minimax(state, depth, maxPlayer):
#     if (depth == 0) or gameover(state):
#         return score

#     if maxPlayer:
#         maxValue = float('-inf')
#         for move in possibleMoves:
#             if isLegal(move, board):
#                 currValue = minimax(move, depth-1,False)
#                 maxValue = max(maxValue,currValue)
#         return maxValue
#     else:
#         minValue = float('inf')
#         for move in possibleMoves:
#             if isLegal(move, board):
#                 currValue = minimax(move, depth-1,True)
#                 minValue = min(currValue, minValue)
#         return minValue

        
        #function minimax(node, depth, maximizingPlayer) is
        # if depth = 0 or node is a terminal node then
        #     return the heuristic value of node
        # if maximizingPlayer then
        #     value := −∞
        #     for each child of node do
        #         value := max(value, minimax(child, depth − 1, FALSE))
                #   maxEval = max(maxValue, value)
        #     return value
        # else (* minimizing player *)
        #     value := +∞
        #     for each child of node do
        #         value := min(value, minimax(child, depth − 1, TRUE))
        #         minEval = min(maxValue, value)
        #     return value