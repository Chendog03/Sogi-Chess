from tkinter import *
from tkinter.ttk import Progressbar
from validMovesFile import *
from PIL import Image, ImageTk
import promotionMessage
import copy, time
import os

print('running')

grid = None
pieces = []

#-----------------#

# CLIENT CODE

from twisted.internet import reactor, protocol
import threading

playerNumber = 0

clientProtocol = None

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        global clientProtocol
        self.transport.write("!JOIN {name}".format(name = clientName).encode('ascii'))
        clientProtocol = self
        
    def dataReceived(self, data):
        data = str(data.decode('ascii'))

        print(data)

        if data.startswith('[MESSAGE] Hello'):
            global playerNumber
            playerNumber = int(data[len(data)-2]) - 1

        if data.startswith('[MOVE]'):
            global grid, validMoves, pieceLocation, newLocation, moveNumber, FEN, fenList, pieceSelected, pieceInHand, pieces
            
            textList = data.split(' ')

            pieceLocation = [int(textList[1]), int(textList[2])]
            newLocation = [int(textList[3]), int(textList[4])]
            pieceInHand = textList[5]
            
            # IDENTICAL TO LEFT CLICK (ELSE CLAUSE) W/O broadcastMove()
            FEN = gridToFEN(grid)
            
            validMoves = getValidMoves(pieceLocation, pieceInHand)

            # placePiece() equivalent
            row = newLocation[0]
            col = newLocation[1]

            grid[row][col] = pieceInHand
                    
            row = pieceLocation[0]
            col = pieceLocation[1]

            grid[row][col] = '0'
            # end
            
            movePiece()
            addMove(1)

            while len(fenList) > moveNumber:
                fenList.pop()
                
            fenList.append(FEN)

            checkForCheck()
            
            cancelSelection()

    def connectionLost(self, reason):
        print("Connection lost.")
        


class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, *args, **kwargs):
        p = EchoClient()
        p.factory = self
        
        return p
        
    def clientConnectionFailed(self, connector, reason):
        print("Connection failed.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost.")
        reactor.stop()

    def threadSafeMessage(self, message):
        global clientProtocol
        clientProtocol.transport.write(message)

    def sendMessage(self, text):        
        reactor.callFromThread(self.threadSafeMessage, text)


clientName = 'username'

FACTORY = EchoFactory()
reactor.connectTCP("localhost", 8000, FACTORY)

threading.Thread(target=reactor.run, args=(False,)).start()


#-----------------#

root = Tk()
backgroundColour = '#333'
root.configure(bg=backgroundColour)

buffer = Label(root, bg=backgroundColour)
buffer.pack()

sogiText = Label(root, text='SOGI CHESS', font="Arial 30 bold", bg=backgroundColour, fg='white')
sogiText.pack(fill=BOTH, expand=1)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

pxWidth = screen_width*0.65
pxHeight = pxWidth*0.75

boardWidth = 16
boardHeight = 12

gridSize = min(pxWidth/boardWidth, pxHeight/boardHeight)

fontSize = int(gridSize/2)
colourOutline = '#ccc'
whiteColour = '#1CDECB'
blackColour = '#faafc9'

whiteColour = '#fff'
blackColour = '#000'

pawnPromotions = ['n', 'v', 'r', 'q']

promotablePieces = {"c" : 'k',
                    "g" : 'q',
                    "o" : 'r',
                    "h" : 'ĥ',
                    "f" : 'x'}

grid = None
pieces = []

whiteInCheck = False
blackInCheck = False

whiteKingSideCastle = False
whiteQueenSideCastle = False
blackKingSideCastle = False
blackQueenSideCastle = False

whiteAttackingSquares = []
blackAttackingSquares = []

canvas = Canvas(root, width=pxWidth, height=pxHeight, borderwidth=0, highlightthickness=0)
canvas.pack(padx=20, pady=20)
canvas.pack_propagate(False)

squareHighlight = None
checkHighlights = []

pieceSelected = False
pieceLocation = None
pieceInHand = None
newLocation = None

validMoves = []
validObjects = []
locations = []

moveNumber = 0

readout = Canvas(root, bg=backgroundColour, highlightthickness=0)
readout.pack()

moveText = Label(readout, text='Move Number: 0', bg=backgroundColour, fg='white', pady=5)
moveText.pack()


#FEN = 'r2q1rk1/1p1nbppp/p2pbn2/4p3/4P3/1NN1BP2/PPPQ2PP/2KR1B1R w - - 5 11'
FEN = 'rnvfsaxqkmasfvnr/2goc2hh2cog2/pppppppppppppppp/b14b/16/16/16/16/B14B/PPPPPPPPPPPPPPPP/2GOC2HH2COG2/RNVFSAXQKMASFVNR KQkq'
#FEN = 'rnv5k6r/2goc2hh2cog2/pppppppppppppppp/b14b/////B14B/PPPPPPPPPPPPPPPP/2GOC2HH2COG2/RNV5K6R KQkq'

FENText = Label(readout, text=FEN, bg=backgroundColour, fg='white')
FENText.pack()

buffer = Label(root, bg='white')
buffer.pack(pady=20)

fenList = [FEN]

for col in range(boardHeight):
    for row in range(boardWidth):
        if (col + row) %2 == 0:
            colour = "#c4a77a" # light
        else:
            colour = "#8f6733" # dark
            
        canvas.create_rectangle(gridSize*row,
                                gridSize*col,
                                gridSize*(row+1),
                                gridSize*(col+1),
                                fill=colour,
                                outline='')

pieceImages = None

progress = None


class Splash(Toplevel):
    def __init__(self, parent, size):
        global progress
        Toplevel.__init__(self, parent, width=size, height=size*4/5)
        self.title("LOADING")
        self.pack_propagate(False)

        titleText = Label(self, text='SOGI CHESS IS LOADING...', font="Arial 30 bold")
        titleText.pack(fill=BOTH, expand=1)

        frame = Frame(self)

        progress = Progressbar(frame, orient = HORIZONTAL, length=size/2, mode = 'determinate')

        frame.pack(fill=BOTH, expand=1)
        frame.pack_propagate(False)
        progress.place(anchor="c", relx=.5, rely=.5)


def preload():
    root.withdraw()

    windowSize = 500
    loadingScreen = Splash(root, windowSize)
    x = screen_width/2 - windowSize/2
    y = screen_height/2 - windowSize/2
    loadingScreen.geometry("+%d+%d" % (x, y))
    loadingScreen.update()
    
    loadImages(loadingScreen)

    drawPieces(FEN)

    loadingScreen.destroy()
        
    root.deiconify()
    root.attributes('-fullscreen', True)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def loadImages(win):
    global pieceImages

    pieceImages = {"BA" : None,
                   "BB" : None,
                   "BC" : None,
                   "BF" : None,
                   "BG" : None,
                   "BH" : None,
                   "BI" : None,
                   "BK" : None,
                   "BM" : None,
                   "BN" : None,
                   "BO" : None,
                   "BP" : None,
                   "BQ" : None,
                   "BR" : None,
                   "BS" : None,
                   "BV" : None,
                   "BX" : None,
                   "WA" : None,
                   "WB" : None,
                   "WC" : None,
                   "WF" : None,
                   "WG" : None,
                   "WH" : None,
                   "WI" : None,
                   "WK" : None,
                   "WM" : None,
                   "WN" : None,
                   "WO" : None,
                   "WP" : None,
                   "WQ" : None,
                   "WR" : None,
                   "WS" : None,
                   "WV" : None,
                   "WX" : None}

    stepValue = 100/len(pieceImages.keys())
    
    for piece in pieceImages.keys():
        image = Image.open(resource_path('assets/' + piece + '.png'))

        if piece[1] == 'P':
            resize_img = image.resize((int(gridSize*0.8), int(gridSize*0.8)))
        else:
            resize_img = image.resize((int(gridSize), int(gridSize)))

        pieceImg = ImageTk.PhotoImage(resize_img)
        pieceImages[piece] = pieceImg

        progress['value'] += stepValue
        win.update()


def addMove(change):
    global moveNumber, FEN
    moveNumber += change
    moveText.config(text = 'Move Number: ' + str(moveNumber))
    FENText.config(text = FEN)

def getMousePos(e):
    return [e.x, e.y]

def findGridPos(e):
    mousePos = getMousePos(e)
    gridX = mousePos[0] - (mousePos[0] % gridSize)
    gridY = mousePos[1] - (mousePos[1] % gridSize)
    return [int(gridX/gridSize), int(gridY/gridSize)]

def setHighlightedSquare(e):
    global squareHighlight, pieceSelected, pieceLocation, pieceInHand, moveNumber
    canvas.delete(squareHighlight)
    
    gridPos = findGridPos(e)
    row = gridPos[0]
    col = gridPos[1]

    if row not in range(boardWidth) or col not in range(boardHeight):
        return

    if grid[row][col] != '0':
        if moveNumber%2 == playerNumber:
            if (grid[row][col] == grid[row][col].upper() and moveNumber%2 == 0) or (grid[row][col] == grid[row][col].lower() and moveNumber%2 == 1):
                squareHighlight = canvas.create_rectangle(row * gridSize +1,
                                                      col * gridSize +1,
                                                      row * gridSize +gridSize,
                                                      col * gridSize +gridSize,
                                                      outline=colourOutline,
                                                      fill='',
                                                      width=fontSize/5)

                pieceSelected = True
                pieceInHand = grid[row][col]
                pieceLocation = [row, col]


def setHighlightedCheck(pos):
    global checkHighlights
    
    # canvas.delete(checkHighlight)
    
    outlineColour = '#e55'
        
    row = pos[0]
    col = pos[1]
    
    checkHighlights.append(canvas.create_rectangle(row * gridSize +1,
                                             col * gridSize +1,
                                             row * gridSize +gridSize,
                                             col * gridSize +gridSize,
                                             outline=outlineColour,
                                             fill='',
                                             width=fontSize/5))
def moveRook(pLoc, pInHand, newLoc):
    # placePiece() EQUIVALENT
    global grid, pieces

    row = newLoc[0]
    col = newLoc[1]

    grid[row][col] = pInHand
            
    row = pLoc[0]
    col = pLoc[1]

    grid[row][col] = '0'


    # movePiece() EQUIVALENT

    canvas.delete(pieces[row][col])
    pieces[row][col] = '0'

    row = newLoc[0]
    col = newLoc[1]
        
    if pInHand == pInHand.lower():
        colour = blackColour
    else:
        colour = whiteColour
        
    #pieces[row][col] = (canvas.create_text(row*gridSize+gridSize/2, col*gridSize+gridSize/2, fill=colour, font="Arial " + str(fontSize) + " bold", text=pInHand.upper()))
    pieces[row][col] = drawPieceImage(row, col, pInHand)
    
    FEN = gridToFEN(grid)

    updateAttackingSquares()


    

def placePiece(e):
    global grid, pieceSelected, pieceLocation, pieceInHand, newLocation
    
    gridPos = findGridPos(e)
    row = gridPos[0]
    col = gridPos[1]

    checkPromotion(gridPos)

    grid[row][col] = pieceInHand

    newLocation = [row, col]

    pieceSelected = False
            
    row = pieceLocation[0]
    col = pieceLocation[1]

    grid[row][col] = '0'

def checkPromotion(gridPos):
    global pieceInHand, pieceLocation

    col = gridPos[1]
    
    if pieceInHand == pieceInHand.lower():
        if col >= 8:
            if pieceInHand in promotablePieces.keys():
                suggestPromotion()
                
            elif col == boardHeight-1 and pieceInHand == 'p':
                promotePawn()
            
    else:
        if col <= 3:
            if pieceInHand.lower() in promotablePieces.keys():
                suggestPromotion()

            elif col == 0 and pieceInHand == 'P':
                promotePawn()


def promotePawn():
    global pieceInHand

    choice = promotionMessage.multiOptionWindow('Promote pawn to ____?', 'n','v','r','q')
    
    if choice == 'n':
        if pieceInHand == pieceInHand.lower():
            pieceInHand = 'n'
        else:
            pieceInHand = 'N'
    elif choice == 'v':
        if pieceInHand == pieceInHand.lower():
            pieceInHand = 'v'
        else:
            pieceInHand = 'V'
    elif choice == 'r':
        if pieceInHand == pieceInHand.lower():
            pieceInHand = 'r'
        else:
            pieceInHand = 'R'
    elif choice == 'q':
        if pieceInHand == pieceInHand.lower():
            pieceInHand = 'q'
        else:
            pieceInHand = 'Q'
    

                
def suggestPromotion():
    global pieceInHand

    promotesTo = promotablePieces[pieceInHand.lower()]

    if promotesTo == 'r':

        # boolPromote = promotionMessage.messageWindow(message='Promote to rook?')
        boolPromote = promotionMessage.popupWindow(root, message='Promote to rook?')

        if boolPromote == 1:
            if pieceInHand == pieceInHand.lower():
                pieceInHand = 'r'
            else:
                pieceInHand = 'R'
                
    elif promotesTo == 'q':

        boolPromote = promotionMessage.popupWindow(root, message='Promote to queen?')

        if boolPromote == 1:
            if pieceInHand == pieceInHand.lower():
                pieceInHand = 'q'
            else:
                pieceInHand = 'Q'

    elif promotesTo == 'ĥ':

        boolPromote = promotionMessage.popupWindow(root, message='Promote to master vertical horse?')

        if boolPromote == 1:
            if pieceInHand == pieceInHand.lower():
                pieceInHand = 'ĥ'
            else:
                pieceInHand = 'Ĥ'

    elif promotesTo == 'x':

        boolPromote = promotionMessage.popupWindow(root, message='Promote to cross master?')
        
        if boolPromote == 1:
            if pieceInHand == pieceInHand.lower():
                pieceInHand = 'x'
            else:
                pieceInHand = 'X'

    elif promotesTo == 'k':

        boolPromote = promotionMessage.popupWindow(root, message='Promote to KING?!?!?!?')

        if boolPromote == 1:
            if pieceInHand == pieceInHand.lower():
                pieceInHand = 'k'
            else:
                pieceInHand = 'K'

def castlingMoves():
    global whiteAttackingSquares, blackAttackingSquares, pieceLocation, grid
    global whiteKingSideCastle, whiteQueenSideCastle, blackKingSideCastle, blackQueenSideCastle

    valid = []
    
    if pieceInHand == 'k':
        
        offset = 1
        impeded = False
        
        if pieceLocation in whiteAttackingSquares:
            impeded = True
            
        while pieceLocation[0] + offset < boardWidth - 1 and not impeded:
            if blackKingSideCastle:
                impeded = True
                break
            
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece != '0':
                impeded = True

            if offset <= 4 and [locX, locY] in whiteAttackingSquares:
                impeded = True

            offset += 1

        if not impeded:
            valid.append([pieceLocation[0] + 4, pieceLocation[1]])
            #print('king side castling available')

        offset = 1
        impeded = False
        
        if pieceLocation in whiteAttackingSquares:
            impeded = True
            
        while pieceLocation[0] - offset > 0 and not impeded:
            if blackQueenSideCastle:
                impeded = True
                break

            # E
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece != '0':
                impeded = True

            if offset <= 4 and [locX, locY] in whiteAttackingSquares:
                impeded = True

            offset += 1

        if not impeded:
            valid.append([pieceLocation[0] - 4, pieceLocation[1]])
            #print('queen side castling available')

    if pieceInHand == 'K':
        
        offset = 1
        impeded = False
        
        if pieceLocation in blackAttackingSquares:
            impeded = True
            
        while pieceLocation[0] + offset < boardWidth - 1 and not impeded:
            if whiteKingSideCastle:
                impeded = True
                break
            
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece != '0':
                impeded = True

            if offset <= 4 and [locX, locY] in blackAttackingSquares:
                impeded = True

            offset += 1

        if not impeded:
            valid.append([pieceLocation[0] + 4, pieceLocation[1]])
            #print('king side castling available')

        offset = 1
        impeded = False
        
        if pieceLocation in blackAttackingSquares:
            impeded = True
            
        while pieceLocation[0] - offset > 0 and not impeded:
            if whiteQueenSideCastle:
                impeded = True
                break

            # E
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece != '0':
                impeded = True

            if offset <= 4 and [locX, locY] in blackAttackingSquares:
                impeded = True

            offset += 1

        if not impeded:
            valid.append([pieceLocation[0] - 4, pieceLocation[1]])
            #print('queen side castling available')

    return valid

        

def getAttackingMoves(pLoc, pInHand, g):
    global pieces
    
    valid = findAttackingMoves(pLoc, pInHand, pieces, boardWidth, boardHeight, g)

    temp = []
    for move in valid:
        pieceOnSquare = g[move[0]][move[1]]
        if pieceOnSquare != '0':
            temp.append(move)

    return temp


def getValidMoves(pLoc, pInHand):
    global pieces, grid
    
    valid = findValidMoves(pLoc, pInHand, pieces, boardWidth, boardHeight, grid)

    gridCopy = copy.deepcopy(grid)
    
    temp = []
    for move in valid:
        g = copy.deepcopy(gridCopy)
            
        g = simulateMove(move, g, pInHand, pLoc)

        if simCheckForCheck(g, pInHand):
            temp.append(move)

    valid = temp

    validCastleMoves = castlingMoves()
    if len(validCastleMoves) > 0:
        for move in validCastleMoves:
            valid.append(move)

    return valid


def simulateMove(move, g, pInHand, pLoc):
    row = move[0]
    col = move[1]

    g[row][col] = pInHand
            
    row = pLoc[0]
    col = pLoc[1]

    g[row][col] = '0'

    return g

def simCheckForCheck(g, pInHand):
    global pieces

    for i in range(len(g)):
        for j in range(len(g[i])):

            piece = g[i][j]
            if pInHand == pInHand.lower() and piece != '0' and piece == piece.upper():
                validMoves = getAttackingMoves([i, j], piece, g)
                
                for move in validMoves:
                    row = move[0]
                    col = move[1]

                    if g[row][col].lower() == 'k':
                        return False

            if pInHand == pInHand.upper() and piece != '0' and piece == piece.lower():
                validMoves = getAttackingMoves([i, j], piece, g)

                for move in validMoves:
                    row = move[0]
                    col = move[1]

                    if g[row][col].upper() == 'K':
                        return False

    return True

class CheckmateSplash(Toplevel):
    def __init__(self, parent, size, winner):
        Toplevel.__init__(self, parent, width=size, height=size*4/5)
        self.pack_propagate(False)

        titleText = Label(self, text='CHECKMATE - {x} wins!'.format(x = winner), font="Arial 30 bold")
        titleText.pack(fill=BOTH, expand=1)

def checkmateWindow(winner):
    root.attributes('-fullscreen', False)
    root.update()
    
    winSize = 500
    win = CheckmateSplash(root, winSize, winner)
    x = screen_width/2 - winSize/2
    y = screen_height/2 - winSize/2
    win.geometry("+%d+%d" % (x, y))
    win.update()

def checkForCheck():
    global pieceSelected, pieceLocation, pieceInHand, pieces, grid, whiteInCheck, blackInCheck, checkHighlights

    for obj in checkHighlights:
        canvas.delete(obj)
        
    if moveNumber == 0:
        return

    whiteInCheck = False
    blackInCheck = False
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):

            piece = grid[i][j]
            if pieceInHand == pieceInHand.upper() and piece != '0' and piece == piece.upper():

                validMoves = getAttackingMoves([i, j], piece, grid)
                
                for move in validMoves:
                    row = move[0]
                    col = move[1]

                    if grid[row][col].lower() == 'k':
                        blackInCheck = True
                        setHighlightedCheck([i, j])
                        print('check')

            if pieceInHand == pieceInHand.lower() and piece != '0' and piece == piece.lower():

                validMoves = getAttackingMoves([i, j], piece, grid)

                for move in validMoves:
                    row = move[0]
                    col = move[1]

                    if grid[row][col].upper() == 'K':
                        whiteInCheck = True
                        setHighlightedCheck([i, j])
                        print('check')

    # CHECK FOR CHECKMATE
    
    if whiteInCheck:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                piece = grid[i][j]

                if piece == piece.upper() and piece != '0':
                
                    if len(getValidMoves([i, j], piece)) != 0:
                        print('white has a legal move from ', piece)
                        return


        print('CHECKMATE - BLACK WINS')
        checkmateWindow('black')

    if blackInCheck:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                piece = grid[i][j]

                if piece == piece.lower() and piece != '0':
                    
                    if len(getValidMoves([i, j], piece)) != 0:
                        print('black has a legal move from ', piece)
                        return

        print('CHECKMATE - WHITE WINS')
        checkmateWindow('white')



def showLocation(pos, colour = 'p'):
    if colour == True:
        outlineColour = whiteColour
    elif colour == False:
        outlineColour = blackColour
    else:
        outlineColour = '#e55'
        
    row = pos[0]
    col = pos[1]
    
    obj = canvas.create_rectangle(row * gridSize +1+gridSize/4,
                                  col * gridSize +1+gridSize/4,
                                  row * gridSize +3*gridSize/4,
                                  col * gridSize +3*gridSize/4,
                                  outline=outlineColour,
                                  fill='',
                                  width=fontSize/5)

    return obj
        

def setVar(x):
    global promoteVar
    promoteVar.set(x)
    

def validateMove(e):
    global validMoves     
    
    gridPos = findGridPos(e)
    row = gridPos[0]
    col = gridPos[1]

    if row not in range(boardWidth) or col not in range(boardHeight):
        # print('not on board')
        return False
    
    if [row, col] not in validMoves:
        # print('not in valid moves')
        return False

    

    return True
    

def drawValidMoves():
    global validObjects, validMoves, pieces

    for move in validMoves:
        row = move[0]
        col = move[1]

        if moveNumber%2 == 0:
            colour = whiteColour
        else:
            colour = blackColour

        if pieces[row][col] != '0':
            colour = '#f11'
            
        validObjects.append(canvas.create_text(row*gridSize+gridSize/2,
                                               col*gridSize+gridSize/2,
                                               fill=colour,
                                               font="Arial " + str(fontSize*2) + " bold",
                                               text='·'))

def broadcastMove():
    global pieceLocation, newLocation, FACTORY, moveNumber, pieceInHand

    text = '!MOVE {prev0} {prev1} {nxt0} {nxt1} {mN} {pIH}'.format(prev0 = pieceLocation[0], prev1 = pieceLocation[1], nxt0 = newLocation[0], nxt1 = newLocation[1], mN = moveNumber, pIH = pieceInHand).encode('ascii')    
    FACTORY.sendMessage(text)


def leftClick(e):
    global grid, validMoves, pieceLocation, moveNumber, FEN, fenList, pieceSelected, pieceInHand
    FEN = gridToFEN(grid)
    
    if pieceSelected == False:
        setHighlightedSquare(e)
        
        if pieceSelected:
            validMoves = getValidMoves(pieceLocation, pieceInHand)
            drawValidMoves()
    else:
        validMoves = getValidMoves(pieceLocation, pieceInHand)
        
        if validateMove(e):
            placePiece(e)
            movePiece()
            broadcastMove()
            addMove(1)

            while len(fenList) > moveNumber:
                fenList.pop()
                
            fenList.append(FEN)

            checkForCheck()
        
        cancelSelection()
            
def leftArrow(e):
    global pieces, FEN, fenList, moveNumber

    if moveNumber < 1:
        return
    
    newFEN = fenList[moveNumber-1]

    for pieceColumn in pieces:
        for piece in pieceColumn:
            canvas.delete(piece)

    for obj in checkHighlights:
        canvas.delete(obj)
        
    cancelSelection()

    drawPieces(newFEN)

    FEN = newFEN

    addMove(-1)


def rightArrow(e):
    global pieces, FEN, fenList, moveNumber

    if len(fenList) - 2 < moveNumber:
        return
    
    newFEN = fenList[moveNumber + 1]

    for pieceColumn in pieces:
        for piece in pieceColumn:
            canvas.delete(piece)

    for obj in checkHighlights:
        canvas.delete(obj)
        
    cancelSelection()

    drawPieces(newFEN)

    FEN = newFEN

    addMove(1)

    checkForCheck()

    
    

def FENtoGrid(fenParam):
    global whiteKingSideCastle, whiteQueenSideCastle, blackKingSideCastle, blackQueenSideCastle
    
    grid = [[]]
    fenParam = fenParam.split(' ')

    fen = fenParam[0]
    fen = list(fen)

    meta = fenParam[1]
    
    charNum = 0
    while charNum < len(fen):
        char = fen[charNum]
        try:
            nextChar = fen[charNum+1]
        except:
            nextChar = ''
        charNum += 1
        
        if char.isnumeric():
            if nextChar.isnumeric():
                char += nextChar
                charNum += 1
                
            char = int(char)
            
            for i in range(char):
                grid[len(grid)-1].append('0')
                
        elif char == "/":
            while len(grid[len(grid) - 1]) < boardWidth:
                grid[len(grid)-1].append('0')
                
            grid.append([])
            
        else:
            grid[len(grid)-1].append(char)

    while len(grid[len(grid) - 1]) < boardWidth:
        grid[len(grid)-1].append('0')

    while len(grid) < boardHeight:
        grid.append(['0'] * boardWidth)
    
    temp = []

    for i in range(len(grid[0])):
        temp.append([])
        for j in range(len(grid)):
            temp[i].append(grid[j][i])
            

    meta = list(meta)

    for char in meta:
        if char == 'K':
            whiteKingSideCastle = False
        elif char == 'Q':
            whiteQueenSideCastle = False
        elif char == 'k':
            blackKingSideCastle = False
        elif char == 'q':
            blackQueenSideCastle = False
    
    return temp

def gridToFEN(grid):
    global whiteKingSideCastle, whiteQueenSideCastle, blackKingSideCastle, blackQueenSideCastle
    
    fen = ''
    for i in range(len(grid[0])):
        jRange = iter(range(len(grid)))
        for j in jRange:
            char = grid[j][i]
            if char != '0':
                fen += char
            else:
                blanks = 1
                for x in range(boardWidth-j-1):
                    if grid[j+x+1][i] == '0':
                        next(jRange)
                        blanks += 1
                    else:
                        break
                        
                fen += str(blanks)

        fen += '/'

    fen = fen[:-1]

    meta = ''

    if not whiteKingSideCastle:
        meta = meta + 'K'
    if not whiteQueenSideCastle:
        meta = meta + 'Q'
    if not blackKingSideCastle:
        meta = meta + 'k'
    if not blackQueenSideCastle:
        meta = meta + 'q'

    if meta == '':
        meta = '-'

    fen = fen + ' ' + meta

    return fen
            

def drawPieces(fen):
    global grid, pieces
    grid = FENtoGrid(fen)
    pieces = copy.deepcopy(grid)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            char = grid[i][j]
            if char != '0':
                if char == char.lower():
                    colour = blackColour
                else:
                    colour = whiteColour
                #pieces[i][j] = (canvas.create_text(i*gridSize+gridSize/2, j*gridSize+gridSize/2, fill=colour, font="Arial " + str(fontSize) + " bold", text=char.upper()))
                pieces[i][j] = drawPieceImage(i, j, char)
                
    global moveNumber, fenList
    print('Displaying move number: ' +str(moveNumber)+ ' of ' +str(len(fenList)-1))

    checkForCheck()



def drawPieceImage(i, j, char):
    global pieceImages

    if char == 'Ĥ':
        char = 'I'

    if char == 'Ĥ'.lower():
        char = 'i'

        
    imgLabel = Label(canvas)

    if char == char.lower():
        charImage = pieceImages['B' + char.upper()]
    else:
        charImage = pieceImages['W' + char]

    imgLabel.image = charImage

    return canvas.create_image(i*gridSize+gridSize/2, j*gridSize+gridSize/2, image=charImage)
    

    
def movePiece():
    global pieces, pieceLocation, pieceInHand, newLocation, FEN
    global whiteKingSideCastle, whiteQueenSideCastle, blackKingSideCastle, blackQueenSideCastle

    row = pieceLocation[0]
    col = pieceLocation[1]

    canvas.delete(pieces[row][col])
    pieces[row][col] = '0'

    row = newLocation[0]
    col = newLocation[1]

    if pieces[row][col] != '0':
        canvas.delete(pieces[row][col])
        
        if pieceInHand.lower() == 'b':
            pieces[row][col] = '0'
            grid[row][col] = '0'
            
            FEN = gridToFEN(grid)
            return
        
    if pieceInHand == pieceInHand.lower():
        colour = blackColour
    else:
        colour = whiteColour
    #pieces[row][col] = (canvas.create_text(row*gridSize+gridSize/2, col*gridSize+gridSize/2, fill=colour, font="Arial " + str(fontSize) + " bold", text=pieceInHand.upper()))
    pieces[row][col] = drawPieceImage(row, col, pieceInHand)
    
    FEN = gridToFEN(grid)
    #print(FEN)

    updateAttackingSquares()

    if pieceInHand == 'r' and pieceLocation[0] == 0:
        blackQueenSideCastle = True
    elif pieceInHand == 'r' and pieceLocation[0] == boardWidth-1:
        blackKingSideCastle = True
    elif pieceInHand == 'R' and pieceLocation[0] == 0:
        whiteQueenSideCastle = True
    elif pieceInHand == 'R' and pieceLocation[0] == boardWidth-1:
        whiteKingSideCastle = True
        
    elif pieceInHand == 'k':
        blackQueenSideCastle = True
        blackKingSideCastle = True

        if pieceLocation[1] == 0:
            if row - pieceLocation[0] > 1:
                print('playing king side castling move')
                moveRook([boardWidth-1, 0], 'r', [boardWidth-5, 0])
                
            elif row - pieceLocation[0] < -1:
                print('playing queen side castling move')
                moveRook([0, 0], 'r', [5, 0])

                
    elif pieceInHand == 'K':
        whiteQueenSideCastle = True
        whiteKingSideCastle = True

        if pieceLocation[1] == boardHeight-1:
            if row - pieceLocation[0] > 1:
                print('playing king side castling move')
                moveRook([boardWidth-1, boardHeight-1], 'R', [boardWidth-5, boardHeight-1])
                
            elif row - pieceLocation[0] < -1:
                print('playing queen side castling move')
                moveRook([0, boardHeight-1], 'R', [5, boardHeight-1])
        
        

def updateAttackingSquares():
    global grid, pieceInHand, whiteAttackingSquares, blackAttackingSquares
    
    temp = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pInHand = grid[i][j]
            pLoc = [i, j]

            if pInHand == '0':
                continue

            if (pieceInHand == pieceInHand.upper() and pInHand == pInHand.upper()) or (pieceInHand == pieceInHand.lower() and pInHand == pInHand.lower()):
                for move in findAttackingMoves(pLoc, pInHand, pieces, boardWidth, boardHeight, grid):
                    if move not in temp:
                        temp.append(move)

    if pieceInHand == pieceInHand.upper():
        whiteAttackingSquares = temp
        c = True
    else:
        blackAttackingSquares = temp
        c = False

    '''
    # SHOW ATTACKING MOVES
    global locations
    
    for loc in locations:
        canvas.delete(loc)
        
    for move in temp:
        locations.append(showLocation(move, c))
    '''
            

def cancelSelection():
    global squareHighlight, pieceSelected, validObjects, validMoves, pieceInHand

    validMoves = []
    
    canvas.delete(squareHighlight)
    pieceSelected = False
    pieceInHand = '1'
    pieceLocation = None

    for obj in validObjects:
        canvas.delete(obj)


preload()

root.bind('<Motion>', getMousePos)
root.bind("<Button-1>", leftClick)
#root.bind("<Left>", leftArrow)
#root.bind("<Right>", rightArrow)
            
root.mainloop()


        
    






