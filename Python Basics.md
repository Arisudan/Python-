# Python Basics 🚀

This document contains fundamental **Python examples** covering **variables, data types, and functions**. Each example is structured with **code snippets** followed by their **expected outputs**.

---

## 📌 1. Printing a Variable  

```python
my_variable = "Hello, world!"
print(my_variable)
```

**🖥️ Output:**  
```
Hello, world!
```

---

## 📌 2. Unpacking a List  

```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)
```

**🖥️ Output:**  
```
apple
banana
cherry
```

---

## 📌 3. Simple String Assignment  

```python
x = "Python is awesome"
print(x)
```

**🖥️ Output:**  
```
Python is awesome
```

---

## 📌 4. Printing Multiple Variables  

```python
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
```

**🖥️ Output:**  
```
Python is awesome
```

---

## 📌 5. Addition of Two Numbers  

```python
x = 5
y = 10
print(x + y)
```

**🖥️ Output:**  
```
15
```

---

## 📌 6. Printing Different Data Types Together  

```python
x = 7
y = "Dhoni"
print(x, y)
```

**🖥️ Output:**  
```
7 Dhoni
```

---

## 📌 7. Concatenation Error  

```python
x = 7
y = "Dhoni"
print(x + y)  # This will cause an error
```

**🖥️ Output:**  
```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

---

## 📌 8. Using a Global Variable Inside a Function  

```python
x = "awesome"

def myfunc():
    print("The Python is " + x)

myfunc()
```

**🖥️ Output:**  
```
The Python is awesome
```

---

## 📌 9. Local and Global Scope  

```python
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)
```

**🖥️ Output:**  
```
Python is fantastic
Python is awesome
```

---

## 📌 10. Using `global` Keyword to Modify Global Variable  

```python
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)
```

**🖥️ Output:**  
```
Python is fantastic
```

---

## 📌 11. Modifying an Existing Global Variable  

```python
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)
```

**🖥️ Output:**  
```
Python is fantastic
```

---

## 📌 12. Checking Data Types  

```python
x = 5
print(type(x))

x = "Hello World"
print(x)
print(type(x))
```

**🖥️ Output:**  
```
<class 'int'>
Hello World
<class 'str'>
```

---

## 📌 13. Various Data Types in Python  

```python
x = ["apple", "banana", "cherry"]
print(type(x))

x = "Hello World"
print(type(x))

x = 20
print(type(x))

x = 20.5
print(type(x))

x = 1j
print(type(x))

x = ("apple", "banana", "cherry")
print(type(x))

x = range(6)
print(type(x))

x = {"name": "John", "age": 36}
print(type(x))

x = {"apple", "banana", "cherry"}
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(type(x))

x = True
print(type(x))

x = b"Hello"
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))

x = None
print(type(x))
```

**🖥️ Output:**  
```
<class 'list'>
<class 'str'>
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'tuple'>
<class 'range'>
<class 'dict'>
<class 'set'>
<class 'frozenset'>
<class 'bool'>
<class 'bytes'>
<class 'bytearray'>
<class 'memoryview'>
<class 'NoneType'>
```

---

## 📌 Conclusion  

This document provides an **overview of Python fundamentals** including:
- Variable assignment  
- List unpacking  
- String and numeric operations  
- Function scope (local and global variables)  
- Data types  

These examples help **beginners** understand **Python's core concepts** in a structured way. 🚀🔥  

Happy Coding! 🎉  
```
