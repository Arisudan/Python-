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
git clone https://github.com/Arisudan/EMI_Home_Loan_Calculator.git
cd EMI_Home_Loan_Calculator
```

### Step 2: Run the Python Script

```bash
python EMI_Home_Loan.py
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

## License

This project is open-source and licensed under the MIT License.

---

### Author: [ARISUDAN TH]
GitHub: [https://github.com/Arisudan]
