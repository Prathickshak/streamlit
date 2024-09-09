import streamlit as st

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Set page title and configure layout
st.set_page_config(page_title="Simple Calculator", layout="centered")

# Display calculator title
st.title("Simple Calculator")
st.balloons()

# Get user input
num1 = st.number_input("Enter the first number:")
operation = st.selectbox("Select an operation:", ("Addition", "Subtraction", "Multiplication", "Division"))
num2 = st.number_input("Enter the second number:")

# Perform calculation based on user-selected operation
result = 0
if operation == "Addition":
    result = add(num1, num2)
elif operation == "Subtraction":
    result = subtract(num1, num2)
elif operation == "Multiplication":
    result = multiply(num1, num2)
elif operation == "Division":
    result = divide(num1, num2)

# Display the result
st.write("Result:", result)