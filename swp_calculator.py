import tkinter as tk
from tkinter import messagebox

def calculate_swp():
    try:
        principal = float(entry_principal.get())
        withdraw = float(entry_withdraw.get())
        rate = float(entry_rate.get())
        years = int(entry_years.get())

        r = (rate / 100) / 12
        n = years * 12
        balance = principal
        total_withdrawn = 0

        for _ in range(n):
            balance += balance * r
            if balance >= withdraw:
                balance -= withdraw
                total_withdrawn += withdraw
            else:
                total_withdrawn += balance
                balance = 0
                break

        result = f"Total Withdrawn: ₹{total_withdrawn:.2f}\nRemaining Balance: ₹{balance:.2f}"
        messagebox.showinfo("SWP Result", result)

    except:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("SWP Calculator")
root.geometry("300x300")

tk.Label(root, text="Initial Investment (₹)").pack()
entry_principal = tk.Entry(root)
entry_principal.pack()

tk.Label(root, text="Monthly Withdrawal (₹)").pack()
entry_withdraw = tk.Entry(root)
entry_withdraw.pack()

tk.Label(root, text="Annual Interest Rate (%)").pack()
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Duration (Years)").pack()
entry_years = tk.Entry(root)
entry_years.pack()

tk.Button(root, text="Calculate SWP", command=calculate_swp).pack()

root.mainloop()
