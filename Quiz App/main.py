import streamlit as st
import time

st.title("Quiz Application")

question_lists = [
    {
        "question": "What is the purpose of the `print()` function in Python?",
        "options": ["To store data", "To display output", "To read files", "To execute loops"],
        "answer": "To display output",
        "explanation": "The `print()` function is used to display text or data on the console."
    },
    {
        "question": "How does a dictionary store data in Python?",
        "options": ["Indexed format", "Key-Value pairs", "Sequential order", "Only integer values"],
        "answer": "Key-Value pairs",
        "explanation": "Dictionaries store data as key-value pairs, allowing fast lookups using keys."
    },
    {
        "question": "Which loop runs until the given condition becomes `False`?",
        "options": ["for loop", "do-while loop", "while loop", "foreach loop"],
        "answer": "while loop",
        "explanation": "The `while` loop continues executing as long as the condition evaluates to `True`."
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def",
        "explanation": "Functions in Python are defined using the `def` keyword, followed by the function name and parentheses."
    },
    {
        "question": "What is the correct syntax for an `if` statement in Python?",
        "options": ["if x = 5:", "if (x == 5)", "if x == 5:", "if x := 5"],
        "answer": "if x == 5:",
        "explanation": "Python uses `==` for comparison in conditional statements."
    },
    {
        "question": "Which of the following is **immutable** in Python?",
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "answer": "Tuple",
        "explanation": "A `tuple` is an immutable data structure, meaning its elements cannot be modified after creation."
    },
    {
        "question": "What mode is used to open a file for reading in Python?",
        "options": ["w", "r", "a", "x"],
        "answer": "r",
        "explanation": "The `r` mode is used to open a file in read mode, meaning the file’s contents can be accessed but not modified."
    },
    {
        "question": "What is **encapsulation** in Python?",
        "options": ["Hiding implementation details", "Reusing existing code", "Defining multiple functions", "Creating loops"],
        "answer": "Hiding implementation details",
        "explanation": "Encapsulation is a concept in object-oriented programming that restricts direct access to certain parts of an object to protect data integrity."
    },
    {
        "question": "Which function is used to create a button in Streamlit?",
        "options": ["st.button()", "st.create_button()", "st.add_button()", "st.new_button()"],
        "answer": "st.button()",
        "explanation": "The `st.button()` function in Streamlit creates an interactive button for users."
    },
    {
        "question": "Which Python library is commonly used for data analysis?",
        "options": ["NumPy", "Matplotlib", "Pandas", "Tkinter"],
        "answer": "Pandas",
        "explanation": "`Pandas` is a powerful library for data manipulation and analysis, especially for working with structured data."
    }
]

if "current_index" not in st.session_state:
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.quiz_finished = False

if st.session_state.current_index < len(question_lists):
    question_data = question_lists[st.session_state.current_index]

    st.subheader(f"Question {st.session_state.current_index + 1} / {len(question_lists)}")
    st.progress((st.session_state.current_index + 1) / len(question_lists))

    st.subheader(question_data["question"])

    select_answer = st.radio("Choose your answer", question_data["options"], key="answer")

    if st.button("Submit Answer"):
        if select_answer == question_data["answer"]:
            st.success("Correct! ✅")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect! ❌ The correct answer is: {question_data['answer']}")

        st.info(f"Explanation: {question_data['explanation']}")

        time.sleep(2)
        st.session_state.current_index += 1
        st.rerun()
else:
    st.session_state.quiz_finished = True

if st.session_state.quiz_finished:
    st.title("Quiz Completed! 🎉")
    st.subheader(f"Your Final Score: {st.session_state.score} / {len(question_lists)}")

    if st.button("Restart Quiz"):
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.quiz_finished = False
        st.rerun()
