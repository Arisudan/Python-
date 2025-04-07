import tkinter as tk
from tkinter import messagebox

def calculate_sip():
    try:
        monthly = float(entry_monthly.get())
        rate = float(entry_rate.get())
        years = int(entry_years.get())

        r = (rate / 100) / 12   # Monthly rate
        n = years * 12          # Total months

        maturity = monthly * (((1 + r) ** n - 1) / r) * (1 + r)
        invested = monthly * n

        result = f"Total Invested: ₹{invested:.2f}\nMaturity Amount: ₹{maturity:.2f}"
        messagebox.showinfo("SIP Result", result)
    except:
        messagebox.showerror("Error", "Please enter valid numbers.")

# GUI Window
root = tk.Tk()
root.title("SIP Calculator")
root.geometry("300x300")

tk.Label(root, text="Monthly Investment (₹)").pack()
entry_monthly = tk.Entry(root)
entry_monthly.pack()

tk.Label(root, text="Annual Interest Rate (%)").pack()
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Duration (Years)").pack()
entry_years = tk.Entry(root)
entry_years.pack()

tk.Button(root, text="Calculate SIP", command=calculate_sip).pack()

root.mainloop()
