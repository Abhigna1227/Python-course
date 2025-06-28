import tkinter as tk
from datetime import datetime, date

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        birth_date = date(year, month, day)
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# GUI window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x250")

# Labels and Entry boxes
tk.Label(root, text="Enter your Date of Birth").pack(pady=10)

tk.Label(root, text="Day:").pack()
day_entry = tk.Entry(root)
day_entry.pack()

tk.Label(root, text="Month:").pack()
month_entry = tk.Entry(root)
month_entry.pack()

tk.Label(root, text="Year:").pack()
year_entry = tk.Entry(root)
year_entry.pack()

# Button
tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI loop
root.mainloop()
