'''
PAWN - P
KNIGHT - N
VANGUARD - V
ROOK - R
QUEEN - Q
KING - K
BARREL - B
COCKREL - C
GENERAL - G
OPHANIM - O
VERTICAL HORSE - H
MASTER V. HORSE - Ĥ
ARCHBISHOP - A
STORK - S
FROG - F
CROSS MASTER - X
CENTRE MASTER - M
'''

def findValidMoves(pieceLocation, pieceInHand, pieces, boardWidth, boardHeight, grid):    
    valid = []

    #PAWN
    
    if pieceInHand == 'p':
        
        if pieceLocation[1] < boardHeight - 1:
            
            if grid[pieceLocation[0]][pieceLocation[1] + 1] == '0':
                valid.append([pieceLocation[0], pieceLocation[1] + 1])
                
                if pieceLocation[1] == 2:
                    offset = 2
                    while grid[pieceLocation[0]][pieceLocation[1] + offset] == '0' and offset <= 3:
                        valid.append([pieceLocation[0], pieceLocation[1] + offset])
                        offset += 1
                
            if pieceLocation[0] > 0:
                piece = grid[pieceLocation[0] - 1][pieceLocation[1] + 1]
                if piece != '0' and piece == piece.upper():
                    valid.append([pieceLocation[0] - 1, pieceLocation[1] + 1])
                    
            if pieceLocation[0] < boardWidth - 1:
                piece = grid[pieceLocation[0] + 1][pieceLocation[1] + 1]
                if piece != '0' and piece == piece.upper():
                    valid.append([pieceLocation[0] + 1, pieceLocation[1] + 1])

    if pieceInHand == 'P':
        
        if pieceLocation[1] > 0:
            
            if grid[pieceLocation[0]][pieceLocation[1] - 1] == '0':
                valid.append([pieceLocation[0], pieceLocation[1] - 1])
                
                if pieceLocation[1] == boardHeight - 3:
                    offset = 2
                    while grid[pieceLocation[0]][pieceLocation[1] - offset] == '0' and offset <= 3:
                        valid.append([pieceLocation[0], pieceLocation[1] - offset])
                        offset += 1
                
            if pieceLocation[0] > 0:
                piece = grid[pieceLocation[0] - 1][pieceLocation[1] - 1]
                if piece != '0' and piece == piece.lower():
                    valid.append([pieceLocation[0] - 1, pieceLocation[1] - 1])
                    
            if pieceLocation[0] < boardWidth - 1:
                piece = grid[pieceLocation[0] + 1][pieceLocation[1] - 1]
                if piece != '0' and piece == piece.lower():
                    valid.append([pieceLocation[0] + 1, pieceLocation[1] - 1])

    # KNIGHT

    if pieceInHand == 'n':
        
        if pieceLocation[0] > 0:
            # SSW
            if pieceLocation[1] > 1:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # NNW
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

        if pieceLocation[0] < boardWidth - 1:
            # SSE
            if pieceLocation[1] > 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # NNE
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

        if pieceLocation[1] > 0:
            # WSW
            if pieceLocation[0] > 1:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] - 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.upper():
                    valid.append([locX, locY])

            # ESE
            if pieceLocation[0] < boardWidth - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] - 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.upper():
                    valid.append([locX, locY])

        if pieceLocation[1] < boardHeight - 1:
            # WNW
            if pieceLocation[0] > 1:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] + 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.upper():
                    valid.append([locX, locY])

            # ENE
            if pieceLocation[0] < boardWidth - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] + 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.upper():
                    valid.append([locX, locY])

    if pieceInHand == 'N':
        
        if pieceLocation[0] > 0:
            # SSW
            if pieceLocation[1] > 1:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # NNW
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

        if pieceLocation[0] < boardWidth - 1:
            # SSE
            if pieceLocation[1] > 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # NNE
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

        if pieceLocation[1] > 0:
            # WSW
            if pieceLocation[0] > 1:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] - 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.lower():
                    valid.append([locX, locY])

            # ESE
            if pieceLocation[0] < boardWidth - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] - 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.lower():
                    valid.append([locX, locY])

        if pieceLocation[1] < boardHeight - 1:
            # WNW
            if pieceLocation[0] > 1:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] + 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.lower():
                    valid.append([locX, locY])

            # ENE
            if pieceLocation[0] < boardWidth - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] + 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.lower():
                    valid.append([locX, locY])
    
    # VANGUARD (bishop)

    if pieceInHand == 'v':

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'V':

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    

            
    # ROOK

    if pieceInHand == 'r':

        offset = -1
        while pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'R':

        offset = -1
        while pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1
                
    # QUEEN

    if pieceInHand == 'q':

        offset = -1
        while pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'Q':

        offset = -1
        while pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        
    # KING

    if pieceInHand == 'k':
        
        if pieceLocation[0] > 0:
            # W
            locX = pieceLocation[0] - 1
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

            # SW
            if pieceLocation[1] > 0:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # NW
            if pieceLocation[1] < boardHeight - 1:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

        if pieceLocation[0] < boardWidth - 1:
            # E
            locX = pieceLocation[0] + 1
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

            # SE
            if pieceLocation[1] > 0:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # NE
            if pieceLocation[1] < boardHeight - 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

        if pieceLocation[1] > 0:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] - 1
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

        if pieceLocation[1] < boardHeight - 1:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + 1
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

    if pieceInHand == 'K':
        
        if pieceLocation[0] > 0:
            # W
            locX = pieceLocation[0] - 1
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

            # SW
            if pieceLocation[1] > 0:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # NW
            if pieceLocation[1] < boardHeight - 1:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

        if pieceLocation[0] < boardWidth - 1:
            # E
            locX = pieceLocation[0] + 1
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

            # SE
            if pieceLocation[1] > 0:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # NE
            if pieceLocation[1] < boardHeight - 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

        if pieceLocation[1] > 0:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] - 1
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        if pieceLocation[1] < boardHeight - 1:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + 1
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

    # BARREL

    if pieceInHand == 'b':
        
        if pieceLocation[1] < boardHeight - 1:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + 1
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

                # 2N
                if piece == '0':
                    locX = pieceLocation[0]
                    locY = pieceLocation[1] + 2
                        
                    piece = grid[locX][locY]
                        
                    if piece == piece.upper():
                        valid.append([locX, locY])

            # NE
            if pieceLocation[0] < boardWidth - 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == '0':
                    valid.append([locX, locY])

            # NW
            if pieceLocation[0] > 0:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == '0':
                    valid.append([locX, locY])
                

    if pieceInHand == 'B':

        if pieceLocation[1] > 0:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] - 1
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

                # 2S
                if piece == '0':
                    locX = pieceLocation[0]
                    locY = pieceLocation[1] - 2
                        
                    piece = grid[locX][locY]
                        
                    if piece == piece.lower():
                        valid.append([locX, locY])

            # SW
            if pieceLocation[0] > 0:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == '0':
                    valid.append([locX, locY])

            # SE
            if pieceLocation[0] < boardWidth - 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == '0':
                    valid.append([locX, locY])

    # COCKREL

    if pieceInHand == 'c':

        offset = -1
        while pieceLocation[0] + offset > 0 and offset >= -4:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1
        
        
        if pieceLocation[0] > 0:
            # SW
            if pieceLocation[1] > 0:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # NW
            if pieceLocation[1] < boardHeight - 1:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

        offset = 1
        while pieceLocation[0] + offset < boardWidth and offset <= 4:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        if pieceLocation[0] < boardWidth - 1:
            # SE
            if pieceLocation[1] > 0:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # NE
            if pieceLocation[1] < boardHeight - 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])


        if pieceLocation[1] < boardHeight - 1:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + 1
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

    if pieceInHand == 'C':

        offset = -1
        while pieceLocation[0] + offset >= 0 and offset >= -4:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1
        
        
        if pieceLocation[0] > 0:
            # SW
            if pieceLocation[1] > 0:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # NW
            if pieceLocation[1] < boardHeight - 1:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

        offset = 1
        while pieceLocation[0] + offset < boardWidth and offset <= 4:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        if pieceLocation[0] < boardWidth - 1:
            # SE
            if pieceLocation[1] > 0:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # NE
            if pieceLocation[1] < boardHeight - 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])


        if pieceLocation[1] > 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] - 1
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])


    # GENERAL

    if pieceInHand == 'g':

        offset = -1
        while pieceLocation[0] + offset >= 0 and offset >= -2:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and offset <= 2:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        if pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
            

        offset = 1
        while pieceLocation[1] + offset < boardHeight and offset <= 3:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        if pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])


        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight and offset <= 3:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1
        
        offset = -1
        if pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0 and offset <= 3:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'G':

        offset = -1
        while pieceLocation[0] + offset >= 0 and offset >= -2:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and offset <= 2:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and offset >= -3:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        if pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0 and offset >= -3:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        if pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth and offset >= -3:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        if pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])


    # OPHANIM

    if pieceInHand == 'o':

        offset = -1
        if pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                

        offset = 1
        if pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                

        offset = -1
        while pieceLocation[1] + offset >= 0 and offset >= -2:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and offset <= 4:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'O':

        offset = -1
        if pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = 1
        if pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = -1
        while pieceLocation[1] + offset >= 0 and offset >= -4:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and offset <= 2:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    # VERTICAL HORSE

    if pieceInHand == 'h':

        offset = -1
        if pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset < boardHeight:
            # SW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] - offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                

        offset = 1
        if pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                

        offset = -1
        if pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])


        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'H':

        offset = -1
        if pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = 1
        if pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset >= 0:
            # NE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] - offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        if pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

    # MASTER VERTICAL HORSE

    if pieceInHand == 'ĥ':

        offset = -1
        if pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

        offset = 1
        if pieceLocation[0] + offset < boardWidth and pieceLocation[1] - offset >= 0:
            # NE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] - offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

        offset = -1
        if pieceLocation[0] + offset >= 0 and pieceLocation[1] - offset < boardHeight:
            # SW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] - offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                

        offset = 1
        if pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'Ĥ':

        offset = -1
        if pieceLocation[0] + offset > 0 and pieceLocation[1] + offset > 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = 1
        if pieceLocation[0] + offset < boardWidth and pieceLocation[1] - offset > 0:
            # NE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] - offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = -1
        if pieceLocation[0] + offset >= 0 and pieceLocation[1] - offset < boardHeight:
            # SW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] - offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                

        offset = 1
        if pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1


    # ARCHBISHOP

    if pieceInHand == 'a':

        if pieceLocation[0] > 0:
            # SSW
            if pieceLocation[1] > 1:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # NNW
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

        if pieceLocation[0] < boardWidth - 1:
            # SSE
            if pieceLocation[1] > 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # NNE
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

        if pieceLocation[1] > 0:
            # WSW
            if pieceLocation[0] > 1:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] - 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.upper():
                    valid.append([locX, locY])

            # ESE
            if pieceLocation[0] < boardWidth - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] - 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.upper():
                    valid.append([locX, locY])

        if pieceLocation[1] < boardHeight - 1:
            # WNW
            if pieceLocation[0] > 1:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] + 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.upper():
                    valid.append([locX, locY])

            # ENE
            if pieceLocation[0] < boardWidth - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] + 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.upper():
                    valid.append([locX, locY])


        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'A':

        if pieceLocation[0] > 0:
            # SSW
            if pieceLocation[1] > 1:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # NNW
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

        if pieceLocation[0] < boardWidth - 1:
            # SSE
            if pieceLocation[1] > 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # NNE
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

        if pieceLocation[1] > 0:
            # WSW
            if pieceLocation[0] > 1:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] - 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.lower():
                    valid.append([locX, locY])

            # ESE
            if pieceLocation[0] < boardWidth - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] - 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.lower():
                    valid.append([locX, locY])

        if pieceLocation[1] < boardHeight - 1:
            # WNW
            if pieceLocation[0] > 1:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] + 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.lower():
                    valid.append([locX, locY])

            # ENE
            if pieceLocation[0] < boardWidth - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] + 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.lower():
                    valid.append([locX, locY])

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    # STORK

    if pieceInHand == 's':

        offset = -1
        while pieceLocation[0] + offset >= 0 and offset >= -3:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and offset <= 3:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and offset >= -4:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        if pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
            

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1


        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1
        


    if pieceInHand == 'S':
        
        offset = -1
        while pieceLocation[0] + offset >= 0 and offset >= -3:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and offset <= 3:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        if pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = 1
        while pieceLocation[1] + offset < boardHeight and offset <= 4:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1


        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

    # FROG/PEPEGA

    if pieceInHand == 'f':
        
        if pieceLocation[0] >= 2:
            # 2SW
            if pieceLocation[1] >= 2:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # 2NW
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])


            if pieceLocation[0] >= 4:
                # 4SW
                if pieceLocation[1] >= 4:
                    locX = pieceLocation[0] - 4
                    locY = pieceLocation[1] - 4
                    
                    piece = grid[locX][locY]
                        
                    if piece == piece.upper():
                        valid.append([locX, locY])

                # 4NW
                if pieceLocation[1] < boardHeight - 4:
                    locX = pieceLocation[0] - 4
                    locY = pieceLocation[1] + 4
                    
                    piece = grid[locX][locY]
                    
                    if piece == piece.upper():
                        valid.append([locX, locY])

        
        if pieceLocation[0] < boardWidth - 2:
            # 2SE
            if pieceLocation[1] >= 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # 2NE
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])


            if pieceLocation[0] < boardWidth - 4:
                # 4SE
                if pieceLocation[1] >= 4:
                    locX = pieceLocation[0] + 4
                    locY = pieceLocation[1] - 4
                    
                    piece = grid[locX][locY]
                        
                    if piece == piece.upper():
                        valid.append([locX, locY])

                # 4NE
                if pieceLocation[1] < boardHeight - 4:
                    locX = pieceLocation[0] + 4
                    locY = pieceLocation[1] + 4
                    
                    piece = grid[locX][locY]
                    
                    if piece == piece.upper():
                        valid.append([locX, locY])

        # N
        if pieceLocation[1] < boardHeight - 1:

            locX = pieceLocation[0]
            locY = pieceLocation[1] + 1

            piece = grid[locX][locY]

            if grid[locX][locY] != '0' and piece == piece.upper():
                
                valid.append([locX, locY])

        # S
        if pieceLocation[1] > 0:

            locX = pieceLocation[0]
            locY = pieceLocation[1] - 1

            piece = grid[locX][locY]
            
            if grid[locX][locY] != '0' and piece == piece.upper():
                
                valid.append([locX, locY])

        # W
        if pieceLocation[0] < boardWidth - 1:

            locX = pieceLocation[0] + 1
            locY = pieceLocation[1]

            piece = grid[locX][locY]
            
            if grid[locX][locY] != '0' and piece == piece.upper():
                
                valid.append([locX, locY])

        # E
        if pieceLocation[0] > 0:

            locX = pieceLocation[0] - 1
            locY = pieceLocation[1]

            piece = grid[locX][locY]
            
            if grid[locX][locY] != '0' and piece == piece.upper():
                
                valid.append([locX, locY])
        

    if pieceInHand == 'F':
        
        if pieceLocation[0] >= 2:
            # 2SW
            if pieceLocation[1] >= 2:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # 2NW
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])


            if pieceLocation[0] >= 4:
                # 4SW
                if pieceLocation[1] >= 4:
                    locX = pieceLocation[0] - 4
                    locY = pieceLocation[1] - 4
                    
                    piece = grid[locX][locY]
                        
                    if piece == piece.lower():
                        valid.append([locX, locY])

                # 4NW
                if pieceLocation[1] < boardHeight - 4:
                    locX = pieceLocation[0] - 4
                    locY = pieceLocation[1] + 4
                    
                    piece = grid[locX][locY]
                    
                    if piece == piece.lower():
                        valid.append([locX, locY])

        
        if pieceLocation[0] < boardWidth - 2:
            # 2SE
            if pieceLocation[1] >= 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # 2NE
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])


            if pieceLocation[0] < boardWidth - 4:
                # 4SE
                if pieceLocation[1] >= 4:
                    locX = pieceLocation[0] + 4
                    locY = pieceLocation[1] - 4
                    
                    piece = grid[locX][locY]
                        
                    if piece == piece.lower():
                        valid.append([locX, locY])

                # 4NE
                if pieceLocation[1] < boardHeight - 4:
                    locX = pieceLocation[0] + 4
                    locY = pieceLocation[1] + 4
                    
                    piece = grid[locX][locY]
                    
                    if piece == piece.lower():
                        valid.append([locX, locY])


        # N
        if pieceLocation[1] < boardHeight - 1:

            locX = pieceLocation[0]
            locY = pieceLocation[1] + 1

            piece = grid[locX][locY]
            
            if grid[locX][locY] != '0' and piece == piece.lower():
                
                valid.append([locX, locY])

        # S
        if pieceLocation[1] > 0:

            locX = pieceLocation[0]
            locY = pieceLocation[1] - 1

            piece = grid[locX][locY]
            
            if grid[locX][locY] != '0' and piece == piece.lower():
                
                valid.append([locX, locY])

        # W
        if pieceLocation[0] < boardWidth - 1:

            locX = pieceLocation[0] + 1
            locY = pieceLocation[1]

            piece = grid[locX][locY]
            
            if grid[locX][locY] != '0' and piece == piece.lower():
                
                valid.append([locX, locY])

        # E
        if pieceLocation[0] > 0:

            locX = pieceLocation[0] - 1
            locY = pieceLocation[1]

            piece = grid[locX][locY]
            
            if grid[locX][locY] != '0' and piece == piece.lower():
                
                valid.append([locX, locY])
                

    # CROSS MASTER

    if pieceInHand == 'x':

        offset = -3
        if pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

        offset = 3
        if pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

        offset = -3
        if pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

        offset = 3
        if pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])


        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'X':

        offset = -3
        if pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = 3
        if pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = -3
        if pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = 3
        if pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    # CENTRE MASTER

    if pieceInHand == 'm':

        offset = -1
        while pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        # JUMPS
        offset = 2
        if pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # 2SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                if [locX, locY] not in valid:
                    valid.append([locX, locY])

        offset = 2
        if pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                if [locX, locY] not in valid:
                    valid.append([locX, locY])

        offset = -2
        if pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                if [locX, locY] not in valid:
                    valid.append([locX, locY])
            

    if pieceInHand == 'M':
        
        offset = -1
        while pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1
        
        # JUMPS
        offset = -2
        if pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # 2NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                if [locX, locY] not in valid:
                    valid.append([locX, locY])

        offset = -2
        if pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                if [locX, locY] not in valid:
                    valid.append([locX, locY])

        offset = 2
        if pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                if [locX, locY] not in valid:
                    valid.append([locX, locY])


    return valid




# THE FUNCTION BELOW REMOVES MOVES FOR THE PAWN AND THE BARREL WHERE MOVEMENT SQUARES ARE NOT ATTACKING SQUARES.

def findAttackingMoves(pieceLocation, pieceInHand, pieces, boardWidth, boardHeight, grid):    
    valid = []


    #PAWN
    
    if pieceInHand == 'p':
        
        if pieceLocation[1] < boardHeight - 1:
                
            if pieceLocation[0] > 0:
                piece = grid[pieceLocation[0] - 1][pieceLocation[1] + 1]
                #if piece != '0' and piece == piece.upper():
                if piece == piece.upper():
                    valid.append([pieceLocation[0] - 1, pieceLocation[1] + 1])
                    
            if pieceLocation[0] < boardWidth - 1:
                piece = grid[pieceLocation[0] + 1][pieceLocation[1] + 1]
                #if piece != '0' and piece == piece.upper():
                if piece == piece.upper():
                    valid.append([pieceLocation[0] + 1, pieceLocation[1] + 1])

    if pieceInHand == 'P':
        
        if pieceLocation[1] > 0:
            
            if pieceLocation[0] > 0:
                piece = grid[pieceLocation[0] - 1][pieceLocation[1] - 1]
                #if piece != '0' and piece == piece.lower():
                if piece == piece.lower():
                    valid.append([pieceLocation[0] - 1, pieceLocation[1] - 1])
                    
            if pieceLocation[0] < boardWidth - 1:
                piece = grid[pieceLocation[0] + 1][pieceLocation[1] - 1]
                #if piece != '0' and piece == piece.lower():
                if piece == piece.lower():
                    valid.append([pieceLocation[0] + 1, pieceLocation[1] - 1])

    # KNIGHT

    if pieceInHand == 'n':
        
        if pieceLocation[0] > 0:
            # SSW
            if pieceLocation[1] > 1:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # NNW
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

        if pieceLocation[0] < boardWidth - 1:
            # SSE
            if pieceLocation[1] > 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # NNE
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

        if pieceLocation[1] > 0:
            # WSW
            if pieceLocation[0] > 1:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] - 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.upper():
                    valid.append([locX, locY])

            # ESE
            if pieceLocation[0] < boardWidth - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] - 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.upper():
                    valid.append([locX, locY])

        if pieceLocation[1] < boardHeight - 1:
            # WNW
            if pieceLocation[0] > 1:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] + 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.upper():
                    valid.append([locX, locY])

            # ENE
            if pieceLocation[0] < boardWidth - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] + 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.upper():
                    valid.append([locX, locY])

    if pieceInHand == 'N':
        
        if pieceLocation[0] > 0:
            # SSW
            if pieceLocation[1] > 1:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # NNW
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

        if pieceLocation[0] < boardWidth - 1:
            # SSE
            if pieceLocation[1] > 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # NNE
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

        if pieceLocation[1] > 0:
            # WSW
            if pieceLocation[0] > 1:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] - 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.lower():
                    valid.append([locX, locY])

            # ESE
            if pieceLocation[0] < boardWidth - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] - 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.lower():
                    valid.append([locX, locY])

        if pieceLocation[1] < boardHeight - 1:
            # WNW
            if pieceLocation[0] > 1:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] + 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.lower():
                    valid.append([locX, locY])

            # ENE
            if pieceLocation[0] < boardWidth - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] + 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.lower():
                    valid.append([locX, locY])
    
    # VANGUARD (bishop)

    if pieceInHand == 'v':

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'V':

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    

            
    # ROOK

    if pieceInHand == 'r':

        offset = -1
        while pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'R':

        offset = -1
        while pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1
                
    # QUEEN

    if pieceInHand == 'q':

        offset = -1
        while pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'Q':

        offset = -1
        while pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        
    # KING

    if pieceInHand == 'k':
        
        if pieceLocation[0] > 0:
            # W
            locX = pieceLocation[0] - 1
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

            # SW
            if pieceLocation[1] > 0:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # NW
            if pieceLocation[1] < boardHeight - 1:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

        if pieceLocation[0] < boardWidth - 1:
            # E
            locX = pieceLocation[0] + 1
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

            # SE
            if pieceLocation[1] > 0:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # NE
            if pieceLocation[1] < boardHeight - 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

        if pieceLocation[1] > 0:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] - 1
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

        if pieceLocation[1] < boardHeight - 1:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + 1
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
            

    if pieceInHand == 'K':
        
        if pieceLocation[0] > 0:
            # W
            locX = pieceLocation[0] - 1
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

            # SW
            if pieceLocation[1] > 0:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # NW
            if pieceLocation[1] < boardHeight - 1:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

        if pieceLocation[0] < boardWidth - 1:
            # E
            locX = pieceLocation[0] + 1
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

            # SE
            if pieceLocation[1] > 0:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # NE
            if pieceLocation[1] < boardHeight - 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

        if pieceLocation[1] > 0:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] - 1
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        if pieceLocation[1] < boardHeight - 1:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + 1
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

    # BARREL

    if pieceInHand == 'b':
        
        if pieceLocation[1] < boardHeight - 1:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + 1
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

                # 2N
                if piece == '0':
                    locX = pieceLocation[0]
                    locY = pieceLocation[1] + 2
                        
                    piece = grid[locX][locY]
                        
                    if piece == piece.upper():
                        valid.append([locX, locY])
                

    if pieceInHand == 'B':

        if pieceLocation[1] > 0:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] - 1
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

                # 2S
                if piece == '0':
                    locX = pieceLocation[0]
                    locY = pieceLocation[1] - 2
                        
                    piece = grid[locX][locY]
                        
                    if piece == piece.lower():
                        valid.append([locX, locY])

    # COCKREL

    if pieceInHand == 'c':

        offset = -1
        while pieceLocation[0] + offset > 0 and offset >= -4:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1
        
        
        if pieceLocation[0] > 0:
            # SW
            if pieceLocation[1] > 0:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # NW
            if pieceLocation[1] < boardHeight - 1:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

        offset = 1
        while pieceLocation[0] + offset < boardWidth and offset <= 4:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        if pieceLocation[0] < boardWidth - 1:
            # SE
            if pieceLocation[1] > 0:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # NE
            if pieceLocation[1] < boardHeight - 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])


        if pieceLocation[1] < boardHeight - 1:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + 1
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

    if pieceInHand == 'C':

        offset = -1
        while pieceLocation[0] + offset >= 0 and offset >= -4:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1
        
        
        if pieceLocation[0] > 0:
            # SW
            if pieceLocation[1] > 0:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # NW
            if pieceLocation[1] < boardHeight - 1:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

        offset = 1
        while pieceLocation[0] + offset < boardWidth and offset <= 4:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        if pieceLocation[0] < boardWidth - 1:
            # SE
            if pieceLocation[1] > 0:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] - 1
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # NE
            if pieceLocation[1] < boardHeight - 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] + 1
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])


        if pieceLocation[1] > 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] - 1
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])


    # GENERAL

    if pieceInHand == 'g':

        offset = -1
        while pieceLocation[0] + offset >= 0 and offset >= -2:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and offset <= 2:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        if pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
            

        offset = 1
        while pieceLocation[1] + offset < boardHeight and offset <= 3:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        if pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])


        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight and offset <= 3:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1
        
        offset = -1
        if pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0 and offset <= 3:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'G':

        offset = -1
        while pieceLocation[0] + offset >= 0 and offset >= -2:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and offset <= 2:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and offset >= -3:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        if pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0 and offset >= -3:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        if pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth and offset >= -3:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        if pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])


    # OPHANIM

    if pieceInHand == 'o':

        offset = -1
        if pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                

        offset = 1
        if pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                

        offset = -1
        while pieceLocation[1] + offset >= 0 and offset >= -2:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and offset <= 4:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'O':

        offset = -1
        if pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = 1
        if pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = -1
        while pieceLocation[1] + offset >= 0 and offset >= -4:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and offset <= 2:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    # VERTICAL HORSE

    if pieceInHand == 'h':

        offset = -1
        if pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset < boardHeight:
            # SW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] - offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                

        offset = 1
        if pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                

        offset = -1
        if pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])


        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'H':

        offset = -1
        if pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = 1
        if pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset >= 0:
            # NE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] - offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        if pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

    # MASTER VERTICAL HORSE

    if pieceInHand == 'ĥ':

        offset = -1
        if pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset > 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

        offset = 1
        if pieceLocation[0] + offset < boardWidth and pieceLocation[1] - offset > 0:
            # NE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] - offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

        offset = -1
        if pieceLocation[0] + offset >= 0 and pieceLocation[1] - offset < boardHeight:
            # SW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] - offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                

        offset = 1
        if pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'Ĥ':

        offset = -1
        if pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = 1
        if pieceLocation[0] + offset < boardWidth and pieceLocation[1] - offset >= 0:
            # NE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] - offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = -1
        if pieceLocation[0] + offset >= 0 and pieceLocation[1] - offset < boardHeight:
            # SW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] - offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                

        offset = 1
        if pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1


    # ARCHBISHOP

    if pieceInHand == 'a':

        if pieceLocation[0] > 0:
            # SSW
            if pieceLocation[1] > 1:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # NNW
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

        if pieceLocation[0] < boardWidth - 1:
            # SSE
            if pieceLocation[1] > 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # NNE
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

        if pieceLocation[1] > 0:
            # WSW
            if pieceLocation[0] > 1:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] - 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.upper():
                    valid.append([locX, locY])

            # ESE
            if pieceLocation[0] < boardWidth - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] - 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.upper():
                    valid.append([locX, locY])

        if pieceLocation[1] < boardHeight - 1:
            # WNW
            if pieceLocation[0] > 1:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] + 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.upper():
                    valid.append([locX, locY])

            # ENE
            if pieceLocation[0] < boardWidth - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] + 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.upper():
                    valid.append([locX, locY])


        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'A':

        if pieceLocation[0] > 0:
            # SSW
            if pieceLocation[1] > 1:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # NNW
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] - 1
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

        if pieceLocation[0] < boardWidth - 1:
            # SSE
            if pieceLocation[1] > 1:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # NNE
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] + 1
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

        if pieceLocation[1] > 0:
            # WSW
            if pieceLocation[0] > 1:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] - 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.lower():
                    valid.append([locX, locY])

            # ESE
            if pieceLocation[0] < boardWidth - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] - 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.lower():
                    valid.append([locX, locY])

        if pieceLocation[1] < boardHeight - 1:
            # WNW
            if pieceLocation[0] > 1:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] + 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.lower():
                    valid.append([locX, locY])

            # ENE
            if pieceLocation[0] < boardWidth - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] + 1
                    
                piece = grid[locX][locY]
                    
                if piece == piece.lower():
                    valid.append([locX, locY])

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    # STORK

    if pieceInHand == 's':

        offset = -1
        while pieceLocation[0] + offset >= 0 and offset >= -3:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and offset <= 3:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and offset >= -4:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        if pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
            

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1


        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1
        


    if pieceInHand == 'S':
        
        offset = -1
        while pieceLocation[0] + offset >= 0 and offset >= -3:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and offset <= 3:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        if pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = 1
        while pieceLocation[1] + offset < boardHeight and offset <= 4:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1


        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

    # FROG/PEPEGA

    if pieceInHand == 'f':
        
        if pieceLocation[0] >= 2:
            # 2SW
            if pieceLocation[1] >= 2:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # 2NW
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])


            if pieceLocation[0] >= 4:
                # 4SW
                if pieceLocation[1] >= 4:
                    locX = pieceLocation[0] - 4
                    locY = pieceLocation[1] - 4
                    
                    piece = grid[locX][locY]
                        
                    if piece == piece.upper():
                        valid.append([locX, locY])

                # 4NW
                if pieceLocation[1] < boardHeight - 4:
                    locX = pieceLocation[0] - 4
                    locY = pieceLocation[1] + 4
                    
                    piece = grid[locX][locY]
                    
                    if piece == piece.upper():
                        valid.append([locX, locY])

        
        if pieceLocation[0] < boardWidth - 2:
            # 2SE
            if pieceLocation[1] >= 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])

            # 2NE
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.upper():
                    valid.append([locX, locY])


            if pieceLocation[0] < boardWidth - 4:
                # 4SE
                if pieceLocation[1] >= 4:
                    locX = pieceLocation[0] + 4
                    locY = pieceLocation[1] - 4
                    
                    piece = grid[locX][locY]
                        
                    if piece == piece.upper():
                        valid.append([locX, locY])

                # 4NE
                if pieceLocation[1] < boardHeight - 4:
                    locX = pieceLocation[0] + 4
                    locY = pieceLocation[1] + 4
                    
                    piece = grid[locX][locY]
                    
                    if piece == piece.upper():
                        valid.append([locX, locY])

        # N
        if pieceLocation[1] < boardHeight - 1:

            locX = pieceLocation[0]
            locY = pieceLocation[1] + 1

            piece = grid[locX][locY]

            if grid[locX][locY] != '0' and piece == piece.upper():
                
                valid.append([locX, locY])

        # S
        if pieceLocation[1] > 0:

            locX = pieceLocation[0]
            locY = pieceLocation[1] - 1

            piece = grid[locX][locY]
            
            if grid[locX][locY] != '0' and piece == piece.upper():
                
                valid.append([locX, locY])

        # W
        if pieceLocation[0] < boardWidth - 1:

            locX = pieceLocation[0] + 1
            locY = pieceLocation[1]

            piece = grid[locX][locY]
            
            if grid[locX][locY] != '0' and piece == piece.upper():
                
                valid.append([locX, locY])

        # E
        if pieceLocation[0] > 0:

            locX = pieceLocation[0] - 1
            locY = pieceLocation[1]

            piece = grid[locX][locY]
            
            if grid[locX][locY] != '0' and piece == piece.upper():
                
                valid.append([locX, locY])
        

    if pieceInHand == 'F':
        
        if pieceLocation[0] >= 2:
            # 2SW
            if pieceLocation[1] >= 2:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # 2NW
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] - 2
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])


            if pieceLocation[0] >= 4:
                # 4SW
                if pieceLocation[1] >= 4:
                    locX = pieceLocation[0] - 4
                    locY = pieceLocation[1] - 4
                    
                    piece = grid[locX][locY]
                        
                    if piece == piece.lower():
                        valid.append([locX, locY])

                # 4NW
                if pieceLocation[1] < boardHeight - 4:
                    locX = pieceLocation[0] - 4
                    locY = pieceLocation[1] + 4
                    
                    piece = grid[locX][locY]
                    
                    if piece == piece.lower():
                        valid.append([locX, locY])

        
        if pieceLocation[0] < boardWidth - 2:
            # 2SE
            if pieceLocation[1] >= 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] - 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])

            # 2NE
            if pieceLocation[1] < boardHeight - 2:
                locX = pieceLocation[0] + 2
                locY = pieceLocation[1] + 2
                
                piece = grid[locX][locY]
                
                if piece == piece.lower():
                    valid.append([locX, locY])


            if pieceLocation[0] < boardWidth - 4:
                # 4SE
                if pieceLocation[1] >= 4:
                    locX = pieceLocation[0] + 4
                    locY = pieceLocation[1] - 4
                    
                    piece = grid[locX][locY]
                        
                    if piece == piece.lower():
                        valid.append([locX, locY])

                # 4NE
                if pieceLocation[1] < boardHeight - 4:
                    locX = pieceLocation[0] + 4
                    locY = pieceLocation[1] + 4
                    
                    piece = grid[locX][locY]
                    
                    if piece == piece.lower():
                        valid.append([locX, locY])


        # N
        if pieceLocation[1] < boardHeight - 1:

            locX = pieceLocation[0]
            locY = pieceLocation[1] + 1

            piece = grid[locX][locY]
            
            if grid[locX][locY] != '0' and piece == piece.lower():
                
                valid.append([locX, locY])

        # S
        if pieceLocation[1] > 0:

            locX = pieceLocation[0]
            locY = pieceLocation[1] - 1

            piece = grid[locX][locY]
            
            if grid[locX][locY] != '0' and piece == piece.lower():
                
                valid.append([locX, locY])

        # W
        if pieceLocation[0] < boardWidth - 1:

            locX = pieceLocation[0] + 1
            locY = pieceLocation[1]

            piece = grid[locX][locY]
            
            if grid[locX][locY] != '0' and piece == piece.lower():
                
                valid.append([locX, locY])

        # E
        if pieceLocation[0] > 0:

            locX = pieceLocation[0] - 1
            locY = pieceLocation[1]

            piece = grid[locX][locY]
            
            if grid[locX][locY] != '0' and piece == piece.lower():
                
                valid.append([locX, locY])
                

    # CROSS MASTER

    if pieceInHand == 'x':

        offset = -3
        if pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

        offset = 3
        if pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

        offset = -3
        if pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])

        offset = 3
        if pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])


        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    if pieceInHand == 'X':

        offset = -3
        if pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = 3
        if pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = -3
        if pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = 3
        if pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

    # CENTRE MASTER

    if pieceInHand == 'm':

        offset = -1
        while pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        # JUMPS
        offset = 2
        if pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # 2SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                if [locX, locY] not in valid:
                    valid.append([locX, locY])

        offset = 2
        if pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                if [locX, locY] not in valid:
                    valid.append([locX, locY])

        offset = -2
        if pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.upper():
                if [locX, locY] not in valid:
                    valid.append([locX, locY])
            

    if pieceInHand == 'M':
        
        offset = -1
        while pieceLocation[0] + offset >= 0:
            # W
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth:
            # E
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1]
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0:
            # N
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[0] + offset < boardWidth and pieceLocation[1] + offset < boardHeight:
            # SE
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1

        offset = -1
        while pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += -1

        offset = 1
        while pieceLocation[1] + offset < boardHeight and pieceLocation[0] - offset >= 0:
            # SW
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                valid.append([locX, locY])
                if piece != '0':
                    break
            else:
                break

            offset += 1
        
        # JUMPS
        offset = -2
        if pieceLocation[1] + offset >= 0 and pieceLocation[0] - offset < boardWidth:
            # 2NE
            locX = pieceLocation[0] - offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                if [locX, locY] not in valid:
                    valid.append([locX, locY])

        offset = -2
        if pieceLocation[0] + offset >= 0 and pieceLocation[1] + offset >= 0:
            # NW
            locX = pieceLocation[0] + offset
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                if [locX, locY] not in valid:
                    valid.append([locX, locY])

        offset = 2
        if pieceLocation[1] + offset < boardHeight:
            # S
            locX = pieceLocation[0]
            locY = pieceLocation[1] + offset
                
            piece = grid[locX][locY]
                
            if piece == piece.lower():
                if [locX, locY] not in valid:
                    valid.append([locX, locY])
                

    return valid
