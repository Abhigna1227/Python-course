import tkinter as tk
from tkinter import messagebox

# Function to check password strength
def check_strength():
    password = entry.get()
    length = len(password)
    
    if length == 0:
        result = "Please enter a password!"
    elif length < 6:
        result = "Password Strength: Weak "
    elif length < 10:
        result = "Password Strength: Medium"
    else:
        result = "Password Strength: Strong "
    
    messagebox.showinfo("Result", result)

# Set up the main window
root = tk.Tk()
root.title("Password Strength Checker ")
root.geometry("300x150")

# Add a label
label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

# Entry widget for password
entry = tk.Entry(root, show="*", width=25)
entry.pack()

# Button to check strength
check_button = tk.Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=10)

# Run the app
root.mainloop()

