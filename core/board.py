
"""
#Board Representation

White: Uppercase
Black: Lowercase

Empty: ""

"""
board = [
            ["r","n","b","q","k","b","n","r"],
            ["p","p","p","p","p","p","p","p"],
            ["p","","","","","","",""],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["P","P","P","P","P","P","P","P"],
            ["R","N","B","Q","K","B","N","R"]
         ]
def load_fen(fen):
    return board

def debug(moves):
    
    for move in moves:
        board[move[0]][move[1]] = "*"
    
    for square in board:
        for piece in square:
            if piece == "":
                print("   ", end="")
            else:
                print(f" {piece} ", end="")
        print()