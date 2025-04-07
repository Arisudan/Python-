import tkinter as tk
from tkinter import messagebox

def on_click(event):
    btn_text = event.widget["text"]

    if btn_text == "=":
        try:
            # Evaluate the expression and show result
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            messagebox.showerror("Error", "Invalid Expression")
    elif btn_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, btn_text)


root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)


entry = tk.Entry(root, font=("Arial", 20), bd=10, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=8, pady=10)


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["%", "0", "C", "+"],
    ["="]
]

for row in buttons:
    row_frame = tk.Frame(root)
    row_frame.pack(expand=True, fill="both")
    for text in row:
        btn = tk.Button(row_frame, text=text, font=("Arial", 18), relief="groove")
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        btn.bind("<Button-1>", on_click)

root.mainloop()
