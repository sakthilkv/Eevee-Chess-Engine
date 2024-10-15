
from board import load_fen, debug


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

board = load_fen("initial")
debug(queen_moves((4,3),board))