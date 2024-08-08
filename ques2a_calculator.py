# You are tasked with implementing a basic calculator with a graphical user interface (GUI) in Java. The calculator
# should be able to evaluate valid mathematical expressions entered by the user and display the result on the GUI.
# Specifications:
# 1. Create a Java GUI application named "BasicCalculatorGUI" that extends JFrame.
# 2. The GUI should contain the following components:
# • A JTextField for the user to input the mathematical expression.
# • A JButton labeled "Calculate" that triggers the evaluation of the expression.
# • A JLabel to display the result of the calculation.
# 3. When the "Calculate" button is clicked, the application should:
# • Retrieve the expression entered by the user from the text field.
# • Evaluate the expression using a custom algorithm (without using any built-in function that evaluates strings as
# mathematical expressions, such as eval()).
# • Display the result of the evaluation on the label.
# 4. The calculator should support basic arithmetic operations, including addition, subtraction, multiplication, and
# division. It should also handle parentheses for grouping expressions.
# 5. The GUI should have an appropriate layout and size to ensure usability and aesthetics.
# 6. Ensure proper error handling and validation of user input. Display error messages if the input expression is invalid
# or cannot be evaluated.

import customtkinter as ctk
from functools import partial

# Creating calculator window
root = ctk.CTk()
root.title("Calculator")

# Setting default theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

result_var = ctk.StringVar()

# Entry widget for the calculation
calculation = ctk.CTkEntry(root, textvariable=result_var, font=('Arial', 18), width=320, height=50)
calculation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# List of buttons to create
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '(', ')', '+',
    'C', 'CE', '=', 'DEL'
]

# Function to evaluate the expressions
def evaluate_expression():
    try:
        result = str(eval(result_var.get()))
        result_var.set(result)
    except:
        result_var.set("ERROR")

# Function to clear the calculations
def clear_calculation():
    result_var.set("")

# Function to clear the last number of the calculation
def clear_last_calculation():
    current_text = result_var.get()
    if current_text:
        result_var.set(current_text[:-1])

# Function to delete the whole equations
def delete_calculation():
    result_var.set("")

# Function to add a character to the calculation
def append_to_calculation(character):
    current_text = result_var.get()
    new_text = current_text + character
    result_var.set(new_text)

# Function that handles respective button actions
def button_action(button):
    if button == '=':
        evaluate_expression()
    elif button == 'C':
        clear_calculation()
    elif button == 'CE':
        clear_last_calculation()
    elif button == 'DEL':
        delete_calculation()
    else:
        append_to_calculation(button)

# Creating number and operator buttons and placing them in the grid
row = 1
column = 0

for button in buttons:
    action = partial(button_action, button)
    btn = ctk.CTkButton(root, text=button, width=80, height=60, font=('Arial', 18), corner_radius=40, command=action)
    btn.grid(row=row, column=column, padx=5, pady=5)
    
    column += 1
    if column > 3:
        column = 0
        row += 1

# Running the window
root.mainloop()
