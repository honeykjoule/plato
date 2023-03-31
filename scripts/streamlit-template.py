import streamlit as st
from streamlit_chat import message

from langchain.chains import ConversationChain
from langchain.llms import OpenAI

def load_chain():
    llm = OpenAI(temperature=0)
    chain = ConversationChain(llm=llm)
    return chain

chain = load_chain()

st.set_page_config(page_title="Page Title", page_icon=":robot:")
st.header("Header")

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] =[]

if st.button("Clear Chat"):
    st.session_state["generated"] = []
    st.session_state["past"] = []

def get_text():
    if "input" not in st.session_state:
        st.session_state["input"] = ""

    input_text = st.text_input("You: ", st.session_state["input"], key="input")
    st.session_state["input"] = input_text

    if st.button("Send"):
        st.session_state.pop("input")
        return input_text

    return input_text
    # if "input" not in st.session_state:
    #     st.session_state["input"] = ""

    # input_text = st.text_input("You: ", st.session_state["input"], key="input")
    # st.session_state["input"] = input_text

    # if st.button("Send"):
    #     st.session_state.pop("input")
    #     return input_text

    # return input_text

    # input_text = st.text_input("You: ", "", key="input", on_change=True, on_submit=lambda: st.session_state.pop("input", None))
    # st.session_state["input"] = input_text
    # return input_text
    # input_text = st.text_input("You: ", "", key="input")
    # return input_text

user_input = get_text()

if user_input:

    output = chain.run(input=user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state["generated"]:

    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")