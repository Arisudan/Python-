
# Tkinter Examples 🚀

This repository contains various **Tkinter** examples to help you learn **GUI programming** in Python. Each example is structured with **code snippets** followed by their **expected outputs**.

---

## 📌 1. Basic Tkinter Window  
Creates a simple Tkinter window.

```python
import tkinter as tk

# Create the main window
top = tk.Tk()
top.title("Basic Tkinter Window")

# Run the application
top.mainloop()
```

**🖥️ Output:**  
A blank Tkinter window with the title **"Basic Tkinter Window"**.

---

## 📌 2. Creating a Tkinter Application Class  
Uses an object-oriented approach to create a Tkinter window.

```python
import tkinter as tk

class App(tk.Tk):
   def __init__(self):
      super().__init__()
      self.title("Tkinter Class Example")

# Create and run the application
app = App()
app.mainloop()
```

**🖥️ Output:**  
A blank Tkinter window with the title **"Tkinter Class Example"**.

---

## 📌 3. Adding a Label and Button  
Creates a **label** and a **Quit button**.

```python
import tkinter as tk

root = tk.Tk()
root.title("Label and Button Example")

label = tk.Label(root, text="Hello, World!")
label.pack()

button = tk.Button(root, text="Quit", command=root.destroy)
button.pack()

root.mainloop()
```

**🖥️ Output:**  
A window with "Hello, World!" text and a **Quit** button.

---

## 📌 4. Taking User Input with Entry Field  
Takes user input and prints a greeting in the console.

```python
import tkinter as tk

root = tk.Tk()
root.title("User Input Example")

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

def greet():
    name = entry.get()
    print("Hello, " + name + "!")

button = tk.Button(root, text="Greet", command=greet)
button.pack()

root.mainloop()
```

**🖥️ Output:**  
User enters a name, clicks **Greet**, and "Hello, [name]!" is printed in the console.

---

## 📌 5. Simple Button Example  
A button without functionality.

```python
import tkinter as tk

root = tk.Tk()
root.title("Button Example")

button = tk.Button(root, text="Click me!")
button.pack()

root.mainloop()
```

**🖥️ Output:**  
A window with a **Click me!** button.

---

## 📌 6. Button with Functionality  
A button that prints "Hello, World!" when clicked.

```python
import tkinter as tk

root = tk.Tk()
root.title("Button Click Example")

def say_hello():
    print("Hello, World!")

button = tk.Button(root, text="Click me!", command=say_hello)
button.pack()

root.mainloop()
```

**🖥️ Output:**  
Clicking the button prints "Hello, World!" in the console.

---

## 📌 7. Entry Field with Button  
User enters text, and it gets printed in the console.

```python
import tkinter as tk

root = tk.Tk()
root.title("Entry Field Example")

entry = tk.Entry(root)
entry.pack()

def print_text():
    text = entry.get()
    print(text)

button = tk.Button(root, text="Print text", command=print_text)
button.pack()

root.mainloop()
```

**🖥️ Output:**  
User enters text, clicks **Print text**, and the input is printed in the console.

---

## 📌 8. Checkbox Example  
Demonstrates **Checkbutton** usage.

```python
import tkinter as tk

root = tk.Tk()
root.title("Checkbox Example")

var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Select me!", variable=var)
checkbutton.pack()

def print_value():
    value = var.get()
    print(value)

button = tk.Button(root, text="Print value", command=print_value)
button.pack()

root.mainloop()
```

**🖥️ Output:**  
0 (Unchecked) or 1 (Checked) is printed when clicking **Print value**.

---

## 📌 9. Radio Button Example  
Demonstrates **Radio buttons** with different options.

```python
import tkinter as tk

root = tk.Tk()
root.title("Radio Button Example")

var = tk.IntVar()
radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=var, value=1)
radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=var, value=2)

radiobutton1.pack()
radiobutton2.pack()

def print_value():
    value = var.get()
    print(value)

button = tk.Button(root, text="Print value", command=print_value)
button.pack()

root.mainloop()
```

**🖥️ Output:**  
1 (Option 1 selected) or 2 (Option 2 selected) is printed when clicking **Print value**.

---

## 📌 10. Getting User Input with `askinteger`  
Uses a dialog box to get an **integer input**.

```python
from tkinter.simpledialog import askinteger
from tkinter import *

top = Tk()
top.title("Integer Input Example")
top.geometry("200x100")

def show():
   num = askinteger("Input", "Enter an Integer:")
   print(num)

B = Button(top, text="Click", command=show)
B.pack()

top.mainloop()
```

**🖥️ Output:**  
A pop-up appears asking for an integer. The entered number is printed in the console.

---

## 📌 Conclusion  
These **Tkinter** examples cover the **basics of GUI programming** in Python. You can **modify** and **expand** these examples to build your own applications. 🚀  
