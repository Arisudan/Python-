import tkinter as tk
from tkinter import messagebox

def on_click(event):
    button = event.widget["text"]  

    if button == "=":
        try:
            expression = entry.get()       
            result = eval(expression)      
            entry.delete(0, tk.END)        
            entry.insert(tk.END, str(result))  
        except:
            messagebox.showerror("Error", "Invalid Expression")

    elif button == "C":
        entry.delete(0, tk.END)

    else:
        entry.insert(tk.END, button)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=8)


button_values = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for row in button_values:
    row_frame = tk.Frame(root)
    row_frame.pack(expand=True, fill="both")

    for value in row:
        btn = tk.Button(row_frame, text=value, font=("Arial", 18))
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        btn.bind("<Button-1>", on_click)

root.mainloop()
