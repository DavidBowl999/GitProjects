Files = "abcdefgh"
Ranks = "1,2,3,4,5,6,7,8"

def chessboard():
    back = [" rook ", "knight","bishop", "queen ", " king ", "bishop", "knight", " rook "]

    board = [[i for i in back],
             [" pawn "] * 8,
             ["      "] * 8,
             ["      "] * 8,
             ["      "] * 8,
             ["      "] * 8,
             [" pawn ".upper()] * 8,
             [i.upper() for i in back],
             ]
    return board

def generateBoard(board):
    print("\n    " + "        ".join(Files))
    print("  +" + "--------+" * 8)

    for rowIndex, row in enumerate(board):
        rank = 8 - rowIndex
        print(f"{rank} | " + " | ".join(row) + f" | {rank}")
        print("  +" + "--------+" * 8)

    print("    " + "        ".join(Files) + "\n")

if __name__ == "__main__":
    b = chessboard()
    generateBoard(b)
