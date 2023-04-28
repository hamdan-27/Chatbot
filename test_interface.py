'''
This chatbot has no knowledge of ViewIt properties. Test App only.
'''

from streamlit_chat import message
import streamlit as st
import pandas as pd
import numpy as np
import openai

openai.api_key = st.secrets["api_secret"]

def generate_response(prompt):
    completions = openai.Completion.create(
        engine = 'text-curie-001',
        prompt = prompt,
        max_tokens = 512,
        n = 1,
        stop = None,
        temperature = .5
    )
    message = completions.choices[0].text
    return message

st.title('ViewIt Chatbot')

with st.sidebar:
    st.markdown("""
                # About
                This Chatbot Assistant will help you look for your desired properties

                # How does it work
                Simply enter your query in the text field and the assistant will help you out.
                """)

# storing chat history
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("Ask a question: ", key='input', value="Hi, how are you?",
                               placeholder='Any 2 bedroom apartments available in Dubai Marina?')
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    
    #store chat
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i)+'_user')
        message(st.session_state['generated'][i], key=str(i))
