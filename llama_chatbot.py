from langchain_community.llms import Ollama
from langchain_core .prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = Ollama(model="llama3") 
prompt =ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries."),
    ("user", "Question: {question}")
])
import os
import streamlit as st
st.title('LangChain Demo With Ollama LLM')
input_text = st.text_input("Search the topic you want")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
if input_text:
    st.write(chain.invoke({"question": input_text}))