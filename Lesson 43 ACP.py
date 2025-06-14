import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        p = float(principal_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())

        si = (p * r * t) / 100
        ci = p * ((1 + r / 100) ** t) - p

        result_label.config(
            text=f"Simple Interest: ₹{si:.2f}\nCompound Interest: ₹{ci:.2f}"
        )
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers!")

root = tk.Tk()
root.title("Interest Calculator")

tk.Label(root, text="Principal (₹):").grid(row=0, column=0)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1)

tk.Label(root, text="Rate (%):").grid(row=1, column=0)
rate_entry = tk.Entry(root)
rate_entry.grid(row=1, column=1)

tk.Label(root, text="Time (years):").grid(row=2, column=0)
time_entry = tk.Entry(root)
time_entry.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate_interest).grid(row=3, column=0, columnspan=2)
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
