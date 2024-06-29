import tkinter as tk
from tkinter import messagebox
import mathimport tkinter as tk
from tkinter import messagebox
import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def exponentiate(x, y):
    return x ** y


def square_root(x):
    if x < 0:
        return "Error! Square root of negative number."
    return math.sqrt(x)


def perform_operation():
    global result
    num1 = float(entry1.get())
    operation = operation_var.get()

    if operation != "sqrt":
        num2 = float(entry2.get())

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    elif operation == 'exponentiate':
        result = exponentiate(num1, num2)
    elif operation == 'sqrt':
        result = square_root(num1)

    result_label.config(text=f"Result: {result}")


# Creating the main window
window = tk.Tk()
window.title("Python Calculator")

# Input fields
tk.Label(window, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

tk.Label(window, text="Enter second number (if needed):").grid(row=1, column=0)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

# Operation selection
operation_var = tk.StringVar(window)
operation_var.set("add")  # Default value

operations = {
    "Add": "add",
    "Subtract": "subtract",
    "Multiply": "multiply",
    "Divide": "divide",
    "Exponentiate": "exponentiate",
    "Square Root": "sqrt"
}

tk.Label(window, text="Select operation:").grid(row=2, column=0)
operation_menu = tk.OptionMenu(window, operation_var, *operations.keys())
operation_menu.grid(row=2, column=1)

# Perform operation button
perform_button = tk.Button(window, text="Calculate", command=perform_operation)
perform_button.grid(row=3, column=0, columnspan=2)

# Result label
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

# Running the main loop
window.mainloop()



def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def exponentiate(x, y):
    return x ** y


def square_root(x):
    if x < 0:
        return "Error! Square root of negative number."
    return math.sqrt(x)


def perform_operation():
    global result
    num1 = float(entry1.get())
    operation = operation_var.get()

    if operation != "sqrt":
        num2 = float(entry2.get())

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    elif operation == 'exponentiate':
        result = exponentiate(num1, num2)
    elif operation == 'sqrt':
        result = square_root(num1)

    result_label.config(text=f"Result: {result}")


# Creating the main window
window = tk.Tk()
window.title("Python Calculator")

# Input fields
tk.Label(window, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

tk.Label(window, text="Enter second number (if needed):").grid(row=1, column=0)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

# Operation selection
operation_var = tk.StringVar(window)
operation_var.set("add")  # Default value

operations = {
    "Add": "add",
    "Subtract": "subtract",
    "Multiply": "multiply",
    "Divide": "divide",
    "Exponentiate": "exponentiate",
    "Square Root": "sqrt"
}

tk.Label(window, text="Select operation:").grid(row=2, column=0)
operation_menu = tk.OptionMenu(window, operation_var, *operations.keys())
operation_menu.grid(row=2, column=1)

# Perform operation button
perform_button = tk.Button(window, text="Calculate", command=perform_operation)
perform_button.grid(row=3, column=0, columnspan=2)

# Result label
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

# Running the main loop
window.mainloop()
