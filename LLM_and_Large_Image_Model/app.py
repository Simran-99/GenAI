from dotenv import load_dotenv
# in order to load all the environments
load_dotenv()
import os
import google.generativeai as genai
import streamlit as st
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Funtion to load Gemini model and get responses
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

#Initializing Streamlit app.
#Three fields would be used:
#1. Page config
#2. Header
#3. Input where we can give our own input
#4. Also creating submit button

st.set_page_config(page_title="Q&A demo")
st.header("Gemini LLM Application")
input=st.text_input("Input: ", key="input")
submit=st.button("Ask the question")

#When submit is clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)
    