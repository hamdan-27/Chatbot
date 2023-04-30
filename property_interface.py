# need to create new vector index with a knowldge json without index
# and try the app with that model


from gpt_index import GPTSimpleVectorIndex
from creds import api_key
from streamlit_chat import message
import streamlit as st
import os

# viewit api key
os.environ["OPENAI_API_KEY"] = api_key

# Load vector index for context
def load_vector_index(v_index):
    vector_index = GPTSimpleVectorIndex.load_from_disk(v_index)
    return vector_index

def gen_response(prompt):
    """
    Returns the AI response based on the context vector index
    """
    response = v_index.query(prompt, response_mode='compact')
    return response


def get_text():
    input_text = st.text_input("Ask a question: ", key='input', value="Hi",
                               placeholder='Any 2 bedroom apartments available in Dubai Marina?')
    return input_text


# App Title
st.title('ViewIt Chatbot')

# App Sidebar
with st.sidebar:
    st.markdown("""
                # About
                This Chatbot Assistant will help you look for your desired properties.

                # How does it work
                Simply enter your query in the text field and the assistant will help you out.
                """)

# storing chat history
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# Load Vector Index For Context (you can choose between ada and curie models)
v_index = load_vector_index('VectorIndices/vectorIndex-curie-001.json')

user_input = get_text()

# Generate a response if input exists
if user_input:
    output = str(gen_response(user_input))[2:]

    # store chat
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i)+'_user')
        message(st.session_state['generated'][i], key=str(i))
