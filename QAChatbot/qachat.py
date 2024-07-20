from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load Gemini Pro Model and get response

model=genai.GenerativeModel("gemini-pro")
##History would store all the history
chat=model.start_chat(history=[])

def get_gemini_response(question):
    #As LLM model is going to give the output we would stream it and display it

    response=chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="Q&A demo")
st.header("Chatbot Application")

#Streamlit ptovides you session states for chathistory if it does not exist

#Starting a char session with an empty history list
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
#Providing your input and submitting
input=st.text_input("input",key="input")
submit=st.button("Ask the question")
#If input present abd submit is clicked
if input and submit:
    response=get_gemini_response(input)
    #Add user query and response to session chat history
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The response is ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
st.subheader("The chat history is")
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")