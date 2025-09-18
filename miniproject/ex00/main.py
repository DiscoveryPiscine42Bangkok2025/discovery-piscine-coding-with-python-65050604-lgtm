from checkmate import checkmate,print_board

def main():
    board = """\
...K
..K.
...P
....\
"""
    print_board(board)
    checkmate(board)

if __name__ == "__main__":
    main()