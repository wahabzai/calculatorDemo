import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Create inputs for two numbers
num1 = st.number_input("Enter first number", value=0.0, step=0.1)
num2 = st.number_input("Enter second number", value=0.0, step=0.1)

# Select the operation
operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the calculation based on the operation selected
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

# Display the result
st.write("Result:", result)
