import tkinter as tk
from tkinter import messagebox

# When a button is clicked, this function runs
def on_click(event):
    button = event.widget["text"]  # Get the button text

    # If equals button is clicked
    if button == "=":
        try:
            expression = entry.get()       # Get what's typed
            result = eval(expression)      # Evaluate the math
            entry.delete(0, tk.END)        # Clear the box
            entry.insert(tk.END, str(result))  # Show result
        except:
            messagebox.showerror("Error", "Invalid Expression")

    # If Clear button is clicked
    elif button == "C":
        entry.delete(0, tk.END)

    # For all other buttons (numbers/operators)
    else:
        entry.insert(tk.END, button)

# Create the calculator window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Create the text field to type/display expression
entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=8)

# Buttons to show on calculator
button_values = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

# Create the buttons row by row
for row in button_values:
    row_frame = tk.Frame(root)
    row_frame.pack(expand=True, fill="both")

    for value in row:
        btn = tk.Button(row_frame, text=value, font=("Arial", 18))
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        btn.bind("<Button-1>", on_click)

# Run the calculator app
root.mainloop()
