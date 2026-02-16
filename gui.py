import tkinter as tk
from tkinter import 

root = tk.Tk()
root.title("Tic Tac Toe")

board = [" " for _ in range(9)]
player = "X"
buttons = []

def check_winner(p):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == p:
            return True
    return False

def click(i):
    global player
    if board[i] == " ":
        board[i] = player
        buttons[i].config(text=player)

        if check_winner(player):
            messagebox.showinfo("Winner", f"Player {player} wins!")
            root.destroy()
        elif " " not in board:
            messagebox.showinfo("Draw", "It's a draw!")
            root.destroy()
        else:
            player = "O" if player == "X" else "X"

for i in range(9):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 24),
        width=5,
        height=2,
        command=lambda i=i: click(i)
    )
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()
