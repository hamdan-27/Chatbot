# need to create new vector index with a better model than ada (curie or davinci)
# and try the app with that model

# should i integrate all the code in one file?
# or should i keep components separate?
# like: > creating vector index
#       > streamlit interface

# try both


from gpt_index import GPTSimpleVectorIndex
from streamlit_chat import message
import streamlit as st
import os

# viewit api key
os.environ["OPENAI_API_KEY"] = "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"

v_index = GPTSimpleVectorIndex.load_from_disk('vectorIndex.json')


def gen_response(prompt):
    response = v_index.query(prompt, response_mode='compact')
    return response

# App Title
st.title('ViewIt Chatbot')

# App Sidebar
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
    input_text = st.text_input("Ask a question: ", key='input', value="Hi",
                               placeholder='Any 2 bedroom apartments available in Dubai Marina?')
    return input_text


user_input = get_text()

if user_input:
    output = str(gen_response(user_input))[2:]

    # store chat
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i)+'_user')
        message(st.session_state['generated'][i], key=str(i))
