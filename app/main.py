import streamlit as st
from openai import OpenAI
from langchain_openai import ChatOpenAI
import os

openai_key = os.environ.get("OPENAI_API_KEY")

print(openai_key)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

llm = ChatOpenAI(
    model="gpt-5",
    temperature=0,
    stream_usage=True
)


messages = [
    (
        "system",
        "You are travel assistant. Help the user informing about travel questions."
    ),
    ("human",
     "I don't know how organize my bag. Can you haelp me?")
]

print(llm.invoke(messages))