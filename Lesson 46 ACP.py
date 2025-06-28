import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Label to show result
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=20)

# Function to play the game
def play(user_choice):
    comp_choice = random.choice(choices)
    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Scissors" and comp_choice == "Paper") or \
         (user_choice == "Paper" and comp_choice == "Rock"):
        result = f"You Win! Computer chose {comp_choice}."
    else:
        result = f"You Lose! Computer chose {comp_choice}."
    result_label.config(text=result)

# Buttons
tk.Button(root, text="Rock", command=lambda: play("Rock"), width=15).pack(pady=5)
tk.Button(root, text="Paper", command=lambda: play("Paper"), width=15).pack(pady=5)
tk.Button(root, text="Scissors", command=lambda: play("Scissors"), width=15).pack(pady=5)

# Start the GUI
root.mainloop()
