
from board import load_fen, debug
from decorators.bench import timeit

def rook_moves(pos,board):

    moves = []
    color = board[pos[0]][pos[1]]

    #upward
    i,j = pos
    i -= 1
    while i >= 0:
        
        if board[i][j] == "":
            moves.append((i,j))
            i -= 1
        elif board[i][j].isupper() == color.isupper():
            break
        else:
            moves.append((i,j))
            break

    #downward
    i,j = pos
    i += 1
    while i < 8:
        
        if board[i][j] == "":
            moves.append((i,j))
            i += 1
        elif board[i][j].isupper() == color.isupper():
            break
        else:
            moves.append((i,j))
            break
    #left
    i,j = pos
    j -= 1
    while j >= 0:
        
        if board[i][j] == "":
            moves.append((i,j))
            j -= 1
        elif board[i][j].isupper() == color.isupper():
            break
        else:
            moves.append((i,j))
            break
    #right
    i,j = pos
    j += 1
    while j < 8:
        
        if board[i][j] == "":
            moves.append((i,j))
            j += 1
        elif board[i][j].isupper() == color.isupper():
            break
        else:
            moves.append((i,j))
            break

    return moves

def bishop_moves(pos, board):

    moves = []
    color = board[pos[0]][pos[1]]

    #north-west
    i,j = pos
    i -= 1
    j -= 1
    while i >= 0 and j >=0:
        
        if board[i][j] == "":
            moves.append((i,j))
            i -= 1
            j -= 1
        elif board[i][j].isupper() == color.isupper():
            break
        else:
            moves.append((i,j))
            break
       

    #south-west
    i,j = pos
    i += 1
    j -= 1
    while i < 8 and j >= 0:
        
        if board[i][j] == "":
            moves.append((i,j))
            i += 1
            j -= 1
        elif board[i][j].isupper() == color.isupper():
            break
        else:
            moves.append((i,j))
            break

    #north-east
    i,j = pos
    i -= 1
    j += 1
    while i >= 0 and j < 8:
        
        if board[i][j] == "":
            moves.append((i,j))
            i -= 1
            j += 1
        elif board[i][j].isupper() == color.isupper():
            break
        else:
            moves.append((i,j))
            break
    
    #south-east
    i,j = pos
    i += 1
    j += 1
    while i < 8 and  j < 8:
        
        if board[i][j] == "":
            moves.append((i,j))
            i += 1
            j += 1
        elif board[i][j].isupper() == color.isupper():
            break
        else:
            moves.append((i,j))
            break
    
    return moves


def queen_moves(pos,board):
    moves = [*rook_moves(pos,board), *bishop_moves(pos,board)]
    return moves

def knight_moves(pos,board):
    
    moves = []
    color = board[pos[0]][pos[1]]

    i,j = pos

    if i-1 >= 0 and j-2 >= 0:
        if board[i-1][j-2] == "" or board[i-1][j-2].isupper() != color.isupper():
            moves.append((i-1,j-2))
    
    if i-2 >= 0 and j-1 >= 0:
        if board[i-2][j-1] == "" or board[i-2][j-1].isupper() != color.isupper():
            moves.append((i-2,j-1))
    
    if i+1 < 8 and j-2 >=0:
        if board[i+1][j-2] == "" or board[i+1][j-2].isupper() != color.isupper():
            moves.append((i+1,j-2))

    if i+2 < 8 and j-1 >= 0:
        if board[i+2][j-1] == "" or board[i+2][j-1].isupper() != color.isupper():
            moves.append((i+2,j-1))

    if i+2 < 8 and j+1 < 8:
        if board[i+2][j+1] == "" or board[i+2][j+1].isupper() != color.isupper():
            moves.append((i+2,j+1))
    
    if i+1 < 8 and j+2 < 8:
        if board[i+1][j+2] == "" or board[i+1][j+2].isupper() != color.isupper():
            moves.append((i+1,j+2))
    
    if i-2 >= 0 and j+1 < 8:
        if board[i-2][j+1] == "" or board[i-2][j+1].isupper() != color.isupper():
            moves.append((i-2,j+1))

    if i-1 >= 0 and j+2 < 8:
        if board[i-1][j+2] == "" or board[i-1][j+2].isupper() != color.isupper():
            moves.append((i-1,j+2))
    
    return moves

def pawn_moves(pos, board):
    moves = []
    color = board[pos[0]][pos[1]]

    i,j = pos

    if board[i][j].isupper():
        if i >= 1:
            if board[i-1][j] == "":
                moves.append((i-1,j))
                if i == 6:
                    if board[i-2][j] == "":
                        moves.append((i-2,j))

            if j-1 >=0:
                if board[i-1][j-1] != "" and board[i-1][j-1].isupper() != color.isupper():
                    moves.append((i-1,j-1))
            if j+1 < 8:
                if board[i-1][j+1] != "" and board[i-1][j+1].isupper() != color.isupper():
                    moves.append((i-1,j+1))

    else:
        if i <= 6:
            if board[i+1][j] == "":
                moves.append((i+1,j))
                if i == 1:
                    if board[i+2][j] == "":
                        moves.append((i+2,j))

            if j-1 >=0:
                if board[i+1][j-1] != "" and board[i+1][j-1].isupper() != color.isupper():
                    moves.append((i+1,j-1))
            if j+1 < 8:
                if board[i+1][j+1] != "" and board[i+1][j+1].isupper() != color.isupper():
                    moves.append((i+1,j+1))

    return moves

board = load_fen("a")
debug(pawn_moves((4,4),board))