# GenAI

## Large Language Model and Large Image Model using Gemini

### Environment Setup:

Virtual Environment Creation: Utilized Conda to create an optimized environment for project deployment.
Dependencies (requirements.txt):
Streamlit: Used for frontend development.
google-generativeai: Integrated to access the Gemini Pro API.
python-dotenv: Managed environment variables securely.

### Configuration:
Created a .env file to securely store environment variables.

### Model Initialization:
Initialized the model using GenerativeModel (gemini-1.5-flash).

### Application Development:
app.py: Built a simple LLM application using Streamlit, incorporating a user input field and a submission button to display the generated response.
vision.py: Implemented image response generation using a model based on gemini-pro-vision, including an image upload feature with PIL (Python Imaging Library).

### Commands to run the application:
streamlit run app.py
streamlit run vision.py

Demo for vision.py

![image](https://github.com/user-attachments/assets/5ef905ee-ea91-4d7b-ad0b-345e8049cffb)

![image](https://github.com/user-attachments/assets/aad0151a-a196-4a5f-9f40-750b65c5fa81)

Demo of App.py:

![image](https://github.com/user-attachments/assets/cf5ec03f-1254-42dd-8548-a07616c743e0)

![image](https://github.com/user-attachments/assets/70f63941-8e65-46c0-99a6-0156f8c8ccac)


## Chatbot Application Using Google Gemini Pro

### Description:

This project demonstrates a simple yet functional chatbot application developed using Streamlit and Google Gemini Pro API. The chatbot is designed to interact with users in a conversational manner, providing responses based on the questions asked.

### Features:

Environment Setup: Utilizes Conda for creating an optimized virtual environment. Dependencies include Streamlit for the frontend, google-generativeai for accessing the Gemini Pro API, and python-dotenv for secure management of environment variables.
Configuration: Environment variables are securely stored in a .env file, and the application is configured to use these variables for API access.
Model Initialization: Initializes the Gemini Pro model and maintains chat history using the Generative AI API.
Real-time Interaction: Streams responses from the model and displays them in real-time. User queries and responses are stored in the session state to maintain the chat history.
Streamlit Interface: Provides a user-friendly interface with a text input for questions and a button to submit them. Displays both the current response and the entire chat history.
Usage:

Ensure you have the required dependencies installed. You can set up the environment using conda and install the necessary packages listed in requirements.txt.
Create a .env file with your Google API key to enable API access.
Run the Streamlit app using streamlit run <script_name>.py.
Interact with the chatbot through the web interface and view responses along with the conversation history.
Setup Instructions:

Install dependencies: pip install -r requirements.txt
Configure API key in .env file.
Start the application with Streamlit: streamlit run <script_name>.py
This project showcases the integration of a modern conversational AI model with an interactive web interface, leveraging Streamlit's capabilities to deliver a seamless user experience.

![image](https://github.com/user-attachments/assets/6e4bcd4e-be66-4959-85f6-6e00edb0b2e6)




