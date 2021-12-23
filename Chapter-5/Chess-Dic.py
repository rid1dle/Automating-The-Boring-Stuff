def isValidChessBoard(chessBoard):
    toReturn = True
    for pos in chessBoard.keys():
        if (pos < '1a' and pos > '8h'):
            toReturn = False

    for pieces in chessBoard.values():
        if (pieces[:1] != 'w' and pieces[:1] != 'b'):
            toReturn = False

        elif (pieces[1:] != 'pawn' and pieces[1:] != 'knight' and pieces[1:] != 'bishop' and pieces[1:] != 'rook' and pieces[1:] != 'queen' and pieces[1:] != 'king'):
            toReturn = False

    return toReturn


# print(isValidChessBoard(dict(input('Enter your Board').split())))
val = {'1h': 'bking', '6c': 'wqueen',
       '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

print(isValidChessBoard(val))
