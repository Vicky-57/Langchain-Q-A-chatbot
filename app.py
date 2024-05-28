## Q&A Chatbot
from langchain import OpenAI  # Updated import for OpenAI
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import openai  # Import the OpenAI library

# Set the OpenAI API key globally
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

# Function to load OpenAI model and get response
def get_openai_response(question):
    # Create an instance of the OpenAI model
    llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.5)
    response = llm(question)
    return response

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input_text = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

# If ask button is clicked
if submit and input_text:
    try:
        response = get_openai_response(input_text)
        st.subheader("The Response is:")
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
