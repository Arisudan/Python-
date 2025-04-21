# Python Threading Demo

This repository demonstrates how to run tasks in **single-threaded** and **multi-threaded** modes using Python. It's a simple but clear illustration of how multi-threading can reduce execution time when running independent tasks.

---

##  Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Single-threaded Execution](#single-threaded-execution)
- [Multi-threaded Execution](#multi-threaded-execution)
- [Conclusion](#conclusion)

---

##  Overview

This project simulates 3 tasks, each with a sleep delay to mimic work. We'll compare how long the tasks take to run:

- Sequentially (single-threaded)
- Concurrently (multi-threaded)

---

##  Requirements

- Python 3.x
- No external libraries are needed

You can run the code directly in your terminal or any Python IDE (like VS Code).

---

##  Single-threaded Execution

This version runs each task **one after the other**.

###  Code: `single_threaded.py`

```python
import time

start_time = time.time()

def task1():
    print("Task 1 is starting...")
    time.sleep(2)
    print("Task 1 is done.")

def task2():
    print("Task 2 is starting...")
    time.sleep(3)
    print("Task 2 is done.")

def task3():
    print("Task 3 is starting...")
    time.sleep(1)
    print("Task 3 is done.")

# Run the tasks sequentially
task1()
task2()
task3()

end_time = time.time()
print(f"All tasks completed in {round(end_time - start_time, 2)} seconds.")
```

###  Output

```
Task 1 is starting...
Task 1 is done.
Task 2 is starting...
Task 2 is done.
Task 3 is starting...
Task 3 is done.
All tasks completed in 6.0 seconds.
```

---

##  Multi-threaded Execution

This version runs all 3 tasks **at the same time** using Python’s `threading` module.

### Code: `multi_threaded.py`

```python
import time
import threading

start_time = time.time()

def task1():
    print("Task 1 is starting...")
    time.sleep(2)
    print("Task 1 is done.")

def task2():
    print("Task 2 is starting...")
    time.sleep(3)
    print("Task 2 is done.")

def task3():
    print("Task 3 is starting...")
    time.sleep(1)
    print("Task 3 is done.")

# Create threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for threads to complete
t1.join()
t2.join()
t3.join()

end_time = time.time()
print(f"All tasks completed in {round(end_time - start_time, 2)} seconds.")
```

###  Output

```
Task 1 is starting...
Task 2 is starting...
Task 3 is starting...
Task 3 is done.
Task 1 is done.
Task 2 is done.
All tasks completed in 3.0 seconds.
```

---

##  Conclusion

| Mode             | Total Time (Approx) |
|------------------|---------------------|
| Single-threaded  | 6 seconds           |
| Multi-threaded   | 3 seconds           |

Multi-threading is highly beneficial when your tasks are **independent and time-consuming**, like waiting for a response, I/O, or delays.

---
