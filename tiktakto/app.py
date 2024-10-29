import tkinter as tk
from tkinter import messagebox

# Initialize the game window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Set player turn and board state
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = []

# Function to check for a winner
def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "" or board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

# Function to check for a tie
def is_tie():
    return all(all(cell != "" for cell in row) for row in board)

# Function to handle button click
def button_click(row, col):
    global current_player
    if board[row][col] == "":
        # Update board and button text
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled")

        # Check for win or tie
        if check_winner():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_board()
        elif is_tie():
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            reset_board()
        else:
            # Switch player
            current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showwarning("Tic-Tac-Toe", "Cell already taken!")

# Function to reset the board
def reset_board():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in buttons:
        for button in row:
            button.config(text="", state="normal")

# Create buttons for the board
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(window, text="", font=("Arial", 24), width=5, height=2,
                           command=lambda i=i, j=j: button_click(i, j))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

# Start the GUI event loop
window.mainloop()
