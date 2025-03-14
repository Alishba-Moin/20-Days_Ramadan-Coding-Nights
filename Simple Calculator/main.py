import streamlit as st

def main():
    # Set page layout
    st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

    # Custom Styling
    st.markdown("""
        <style>
        .big-font { font-size: 25px !important; font-weight: bold; }
        .result-box { background-color: #2ecc71; padding: 10px; border-radius: 10px; font-size: 22px; color: white; text-align: center; }
        .error-box { background-color: #e74c3c; padding: 10px; border-radius: 10px; font-size: 18px; color: white; text-align: center; }
        </style>
        """, unsafe_allow_html=True)

    # Title
    st.title('🔢 Simple Calculator')
    st.write("Enter two numbers and choose an operation.")

    # Input Fields in a grid format
    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Enter number one:", value=0.0, step=0.1, format="%.2f")
    
    with col2:
        num2 = st.number_input("Enter number two:", value=0.0, step=0.1, format="%.2f")
    
    # Dropdown for Operation Selection
    operation = st.selectbox("Select Operation:", [
        "Addition (+)", 
        "Subtraction (-)", 
        "Multiplication (x)", 
        "Division (÷)"
    ])

    # Calculate Button
    if st.button("🧮 Calculate",  use_container_width=True):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (x)":
                result = num1 * num2
                symbol = "×"
            else:
                if num2 == 0:
                    st.markdown('<p class="error-box">❌ Error: Division by zero is not allowed!</p>', unsafe_allow_html=True)
                    return
                result = num1 / num2
                symbol = "÷"

            # Display Result
            st.markdown(f'<p class="result-box">{num1} {symbol} {num2} = {result:.2f}</p>', unsafe_allow_html=True)

        except Exception as e:
            st.markdown(f'<p class="error-box">⚠️ An error occurred: {str(e)}</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
