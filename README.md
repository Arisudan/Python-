# GUI Calculator Projects Using Python and Tkinter

This repository contains beginner-friendly projects that demonstrate how to create basic graphical user interfaces using Python and the Tkinter library. The primary focus is on building a functional calculator that allows users to perform arithmetic operations using button inputs.

---

## Installation Guide

### 1. Installing Python on Windows

To get started, make sure Python is installed on your system.

1. Visit the official Python website: https://www.python.org/downloads/
2. Download the latest version suitable for your Windows system.
3. Run the installer and ensure you check the box labeled "Add Python to PATH".
4. Click "Install Now" and follow the installation steps.

To confirm installation, open Command Prompt and type:

```bash
python --version
```

If installed correctly, the installed version number will be displayed.

---

## Project Overview

The project demonstrates how to:

- Create buttons dynamically using Tkinter
- Capture button click events
- Perform expression evaluation
- Display the result or clear the screen as needed

This is a great starting point for anyone new to Python GUI development.

---

## Running the Project

### 1. Clone the Repository

To download the project files, use the following commands in your terminal:

```bash
git clone https://github.com/Arisudan/python-.git
cd python-
```

### 2. Run the Calculator Application

Make sure you're in the project directory, then run:

```bash
Basic_Calculator.py
```

This will open a basic calculator window where you can perform operations using the on-screen buttons.

---

## File Description

- `Basic_Calculator.py`  
  This file contains the Python code for the calculator interface. It uses Tkinter to render the window, buttons, and display logic for evaluating basic arithmetic expressions.

---

## Features

- Graphical interface built with Tkinter
- Clickable buttons for numbers and operations
- Input field to show the current expression
- Evaluation of expressions using Python’s built-in `eval()` function
- Error handling for invalid expressions
- Option to clear the input using a "C" button

---

## How It Works

1. Each button is mapped to a character (number or operator).
2. Button clicks are handled using a common event function.
3. On pressing "=", the current expression is evaluated.
4. If the expression is invalid, an error popup appears.
5. "C" clears the current input.

---

## Customization Tips

- To add new operations (e.g., square root, exponentiation), you can extend the button list and handle custom logic in the event handler.
- You can modify the button layout or style using Tkinter options such as font, color, padding, etc.

---

## Conclusion
This Basic Calculator project demonstrates how Python and Tkinter can be used to build simple yet functional GUI applications. By integrating button-driven input with real-time expression evaluation, the project serves as an excellent starting point for beginners to understand event handling, GUI layouts, and basic arithmetic logic in Python. It lays a solid foundation for developing more advanced tools such as scientific calculators or financial applications with expanded capabilities.

---

# EMI Home Loan Calculator – Python GUI Application

This project is a simple graphical user interface application developed in Python using Tkinter. It estimates an approximate monthly EMI (Equated Monthly Installment) for a home loan based on user input for total loan amount and loan duration. This tool is primarily designed for demonstration and learning purposes.

---

## Features

- Clean and interactive GUI using Tkinter
- User input for:
  - Number of years for the loan
  - Total loan amount
- EMI calculated using a simplified formula
- Displays a financial note: **"AVOID EMI"**
- Easy-to-understand and minimal design

---

## How to Run the Application

### Step 1: Clone the Repository

```bash
git clone https://github.com/Arisudan/Python-.git
cd Python-
```

### Step 2: Run the Python Script

```bash
python EMI_Home _Loan.py
```

This will open a window with a button labeled **"EMI for home loan"**.

---

## How to Use

1. Click on **"EMI for home loan"** in the GUI.
2. Enter the **loan duration** in years when prompted.
3. Enter the **total loan amount** when prompted.
4. The program prints an approximate EMI value in the terminal along with the message: **"AVOID EMI"**.

---

## EMI Formula Used

```text
EMI = (Loan Amount / (Years * 12)) + 0.85 * (Loan Amount / (Years * 12))
```

Note: This is a simplified calculation and does not account for real-world interest rates.

---

## File Description

- `EMI_Home_Loan.py`  
  Main Python script containing the logic and interface code using Tkinter.

---

## Source Code: EMI_Home_Loan.py

```python
from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("200x200")

def show():
   num = askinteger("Input", "Enter no. of years")
   amt = askinteger("Input", "Enter total amount")
   print((amt / (num * 12)) + 0.85 * (amt / (num * 12)))
   print("AVOID EMI")

B = Button(top, text="EMI for home loan", command=show)
B.place(x=50, y=50)

top.mainloop()
```

---

## Notes

- Results are printed in the terminal. For better user experience, output can be redirected to the GUI using message boxes or text labels.
- The EMI formula used is intended for educational purposes only and does not reflect actual bank EMI calculations.

---

## Conclusion

The EMI Home Loan Calculator provides a simple and interactive way to estimate monthly loan installments using Python's Tkinter library. While the EMI formula used here is a basic approximation, this project effectively demonstrates the use of GUI components, user input handling, and arithmetic operations in a beginner-friendly environment. It serves as a foundational project for those looking to explore financial applications or build more advanced calculators with real-world formulas and GUI enhancements

---
Sure! Here's a clean, professional, and easy-to-understand **README** file content for your **SIP Calculator GUI project**:

---

# SIP Calculator GUI – Python Tkinter

This project is a **Simple SIP (Systematic Investment Plan) Calculator** built using **Python's Tkinter** library. It helps users calculate their **total invested amount** and **maturity value** based on monthly investments, interest rate, and investment duration.

---

## 📌 Features

- User-friendly graphical interface using Tkinter  
- Calculates total invested amount and maturity value  
- Displays results in a popup message box  
- Input validation with error messages for invalid entries  

---

## 🧰 Requirements

- Python 3.x  
- `tkinter` (comes pre-installed with standard Python)

---

## 📥 Installation on Windows


1. **Verify Installation**  
   Open Command Prompt and type:
   ```
   python --version
   ```

2. **Run the Script**  
   - Save the Python file as `sip_calculator.py`
   - Open a terminal or command prompt in that folder
   - Run:
     ```
     python sip_calculator.py
     ```

---

## How the Calculator Works

The calculator uses the standard **SIP maturity formula**:

```
Maturity Value = P × ((1 + r)^n – 1) / r) × (1 + r)
```

Where:
- `P` = Monthly investment amount  
- `r` = Monthly interest rate = Annual Rate / 12 / 100  
- `n` = Total number of months = Years × 12  

The total invested amount is calculated by:

```
Invested Amount = P × n
```

---

## 🧾 Code Overview

```python
import tkinter as tk
from tkinter import messagebox

def calculate_sip():
    try:
        monthly = float(entry_monthly.get())
        rate = float(entry_rate.get())
        years = int(entry_years.get())

        r = (rate / 100) / 12
        n = years * 12

        maturity = monthly * (((1 + r) ** n - 1) / r) * (1 + r)
        invested = monthly * n

        result = f"Total Invested: ₹{invested:.2f}\nMaturity Amount: ₹{maturity:.2f}"
        messagebox.showinfo("SIP Result", result)
    except:
        messagebox.showerror("Error", "Please enter valid numbers.")

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
```

---

## Output Example

If you input:

- Monthly Investment: ₹2000  
- Annual Interest Rate: 12  
- Duration: 5 years  

The output will be something like:
```
Total Invested: ₹120000.00
Maturity Amount: ₹162938.27
```

---

## Conclusion
This SIP Calculator offers a simple and effective way for users to estimate the returns on their monthly investments using a graphical interface. By combining the power of Python and Tkinter, the project helps users understand how systematic investments grow over time with compounding interest. It serves as a practical tool for beginners learning about GUI development and financial planning concepts. This project can also be extended with features like charts, export options, or comparison between different interest rates to enhance usability and learning experience.

---

## License

This project is open-source and licensed under the MIT License.

---

### Author: ARISUDAN TH
GitHub: https://github.com/Arisudan
