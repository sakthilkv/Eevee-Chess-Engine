
"""
#Board Representation

White: Uppercase
Black: Lowercase

Empty: ""

"""

import copy
board = [
            ["r","n","b","q","k","b","n","r"],
            ["p","p","p","p","p","p","p","p"],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["","","","P","","","",""],
            ["","","","","","","",""],
            ["P","P","P","P","P","P","P","P"],
            ["R","N","B","Q","K","B","N","R"]
         ]
def load_fen(fen):
    return board

def debug(moves):
    state = copy.deepcopy(board)
    for move in moves:
        state[move[0]][move[1]] = "*"
    
    for square in state:
        for piece in square:
            if piece == "":
                print("   ", end="")
            else:
                print(f" {piece} ", end="")
        print()