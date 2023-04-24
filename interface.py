import streamlit as st
import pandas as pd
import numpy as np
from AppTest import *

st.title('ViewIt Chatbot')

DATE_COLUMN = 'date/time'

# @st.cache_data
# def load_data():
#     data = pd.read_json(DATA_URL)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache_data)")

chat_hist = pd.DataFrame({
    
})

def answerMe(vector_index):
    v_index = GPTSimpleVectorIndex.load_from_disk(vector_index)
    while True:
        prompt = st.text_input(label='Ask a question', value="Properties in Marina Dubai")
        response = v_index.query(prompt, response_mode='compact')
        print(f'Response: {response} \n')


if st.checkbox('Show chat history'):
    st.subheader('Chat history')
    st.write(chat_hist)

