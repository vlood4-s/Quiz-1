board = [" " for _ in range(9)]

def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(player):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def play_game():
    player = "X"
    for turn in range(9):
        print_board()
        try:
            move = int(input(f"Player {player}, choose a position (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid position! Choose 1-9.")
                continue
            if board[move] != " ":
                print("That spot is already taken. Try again.")
                continue
        except:
            print("Invalid input! Enter a number 1-9.")
            continue

        board[move] = player

        if check_winner(player):
            print_board()
            print(f"Player {player} wins!")
            return

      
        player = "O" if player == "X" else "X"

    print_board()
    print("It's a draw!")


play_game()
