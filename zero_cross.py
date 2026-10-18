
import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x500")
root.resizable(False, False)

# Game variables
current_player = "X"
buttons = []
game_over = False


# Check winner
def check_winner():
    global game_over

    combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in combinations:
        a, b, c = combo

        if (
            buttons[a]["text"]== buttons[b]["text"]== buttons[c]["text"]
            != ""
        ):
            buttons[a].config(bg="lightgreen")
            buttons[b].config(bg="lightgreen")
            buttons[c].config(bg="lightgreen")

            game_over = True

            messagebox.showinfo(
                "Game Over",
                f"Player {current_player} wins!"
            )
            return True

    # Check draw
    if all(button["text"] != "" for button in buttons):
        game_over = True
        messagebox.showinfo("Game Over", "It's a Draw!")
        return True

    return False


# Button click function
def button_click(index):
    global current_player

    if game_over or buttons[index]["text"] != "":
        return

    buttons[index].config(text=current_player)

    if check_winner():
        return

    # Switch player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    turn_label.config(text=f"Player {current_player}'s Turn")


# Restart game
def restart_game():
    global current_player, game_over

    current_player = "X"
    game_over = False

    for button in buttons:
        button.config(text="", bg="SystemButtonFace")

    turn_label.config(text="Player X's Turn")


# Heading
title_label = tk.Label(
    root,
    text="Tic-Tac-Toe",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=10)

# Player turn label
turn_label = tk.Label(
    root,
    text="Player X's Turn",
    font=("Arial", 13)
)
turn_label.pack(pady=5)

# Game board
board = tk.Frame(root)
board.pack(pady=10)

for i in range(9):
    button = tk.Button(
        board,
        text="",
        font=("Arial", 22, "bold"),
        width=4,
        height=2,
        command=lambda i=i: button_click(i)
    )

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=3,
        pady=3
    )

    buttons.append(button)

# Restart button
restart_button = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 12),
    command=restart_game
)
restart_button.pack(pady=10)

# Run application
root.mainloop()
