# GenAI

##Large Language Model and Large Image Model using Gemini

###Environment Setup:

Virtual Environment Creation: Utilized Conda to create an optimized environment for project deployment.
Dependencies (requirements.txt):
Streamlit: Used for frontend development.
google-generativeai: Integrated to access the Gemini Pro API.
python-dotenv: Managed environment variables securely.

###Configuration:
Created a .env file to securely store environment variables.

###Model Initialization:
Initialized the model using GenerativeModel (gemini-1.5-flash).

###Application Development:
app.py: Built a simple LLM application using Streamlit, incorporating a user input field and a submission button to display the generated response.
vision.py: Implemented image response generation using a model based on gemini-pro-vision, including an image upload feature with PIL (Python Imaging Library).

###Commands to run the application:
streamlit run app.py
streamlit run vision.py

Demo for vision.py

![image](https://github.com/user-attachments/assets/5ef905ee-ea91-4d7b-ad0b-345e8049cffb)

![image](https://github.com/user-attachments/assets/aad0151a-a196-4a5f-9f40-750b65c5fa81)

Demo of App.py:

![image](https://github.com/user-attachments/assets/cf5ec03f-1254-42dd-8548-a07616c743e0)

![image](https://github.com/user-attachments/assets/70f63941-8e65-46c0-99a6-0156f8c8ccac)



