import streamlit as st
from chat import generate_response

def chat_interface():
    st.title("Plato's Work")
    user_input = st.text_input("You: ", "")
    chat_log = st.text_area("Dialogue", "")

    if st.button("Send"):
        chat_log = generate_response(user_input, chat_log)
        st.text_area("Dialogue", value=chat_log, height=200, max_chars=None, key=None)
        user_input = ""

if __name__ == "__main__":
    st.set_page_config(page_title="Dialogue With Plato's Work", page_icon=":guardsman:", layout="wide")
    st.write("Welcome to Plato's work!")
    chat_interface()