import streamlit as st  # Import Streamlit for the web interface.
import math             # Import math module for advanced operations.

# Set page configuration 
st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
)
def main():
    # Setting the page title .
    st.title("🧮 Simple Calculator")  
    st.write("✨ Enter two numbers and choose an operation ✨")  

    # Creating two columns for a side-by-side layout for inputs.
    col1, col2 = st.columns(2)  # Divides the page into two columns.

    # Input fields for numbers using the columns.
    with col1:  # First column for the first number.
        num1 = st.number_input("🔢 Enter first number", value=0.0)  # Input field to accept the first number.
    with col2:  # Second column for the second number.
        num2 = st.number_input("🔢 Enter second number (optional)", value=0.0)  # Input field to accept the second number.

    # Dropdown menu for selecting a mathematical operation 
    operation = st.selectbox(
        "📋 Choose operation",  # Label for the dropdown.
        [
            "➕ Addition (+)", 
            "➖ Subtraction (-)", 
            "✖ Multiplication (×)", 
            "➗ Division (÷)", 
            "➗ Modulus (%)", 
            "⬆️ Exponentiation (^)", 
            "📐 Square Root (√)", 
        ],
    )

    # Button to trigger the calculation when clicked .
    if st.button("🔍 Calculate"):
        try:
            if operation == "➕ Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "➖ Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "✖ Multiplication (×)":
                result = num1 * num2
                symbol = "×"
            elif operation == "➗ Division (÷)":
                if num2 == 0:
                    st.error("⚠️ Error: Division by zero!")
                    return
                result = num1 / num2
                symbol = "÷"
            elif operation == "➗ Modulus (%)":
                if num2 == 0:
                    st.error("⚠️ Error: Division by zero!")
                    return
                result = num1 % num2
                symbol = "%"
            elif operation == "⬆️ Exponentiation (^)":
                result = num1 ** num2
                symbol = "^"
            elif operation == "📐 Square Root (√)":
                if num1 < 0:
                    st.error("⚠️ Error: Cannot calculate the square root of a negative number!")
                    return
                result = math.sqrt(num1)
                symbol = "√"
                st.success(f"📐 √{num1} = {result}")  # Special case: only one input.
                return

            # Display result with styling and emojis.
            if operation not in ["📐 Square Root (√)"]:  # Exclude special case.
                st.success(f"🔴 {num1} {symbol} {num2} = {result}")

        except Exception as e:  # Catch any other exceptions that may occur.
            st.error(f"🚨 An error occurred: {str(e)}")  # Display a generic error message.

    # For displaying the Author's name
    st.write("✨ Built by [Talha Mehtab](https://github.com/Muhammad-Talhas) ✨")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()  
