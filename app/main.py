import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model="gpt-5", temperature=0, stream_usage=True)

# messages = [
#     (
#         "system",
#         "You are travel assistant. Help the user informing about travel questions."
#     ),
#     ("human",
#      "I don't know how to organize my bag. Can you haelp me?")
# ]

st.set_page_config(page_title ="Chat", layout="centered")
st.title("")


if "messages" not in st.session_state:
    st.session_state["messages"] = []

messages = st.session_state["messages"]

for type, content in messages:
    chat = st.chat_message(type)
    chat.markdown(content)


print(messages)

in_message = st.chat_input("Send your question:")

if in_message:
    messages.append(("human", in_message))
    chat = st.chat_message("human")
    chat.markdown(in_message)

    response = llm.invoke(in_message)
    
    messages.append(("ai", response.content))
    chat = st.chat_message("ai")
    chat.markdown(response.content)


# if in_message:
#     chat = st.chat_message("human")
#     chat.markdown(in_message)
#     response = llm.invoke(in_message)
#     chat = st.chat_message("ai")
#     chat.markdown(response.content)






# print(llm.invoke(messages).content)