from gpt_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI
import sys, os

#viewit api key
os.environ["OPENAI_API_KEY"] = "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"

def create_vector_index(path):
    max_input = 4096
    tokens = 256
    chunk_size = 600
    max_chunk_overlap = 20

    prompt_helper = PromptHelper(max_input, tokens, max_chunk_overlap, chunk_size_limit=chunk_size)

    #define LLM
    llm_predictor = LLMPredictor(OpenAI(
        temperature=0,
        model_name='text-ada-001',
        max_tokens=tokens
    ))

    #load data
    docs = SimpleDirectoryReader(path).load_data()
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    #create vector index
    vector_index = GPTSimpleVectorIndex.from_documents(docs, service_context=service_context)
    vector_index.save_to_disk('vectorIndex.json')
    return vector_index

def answerMe(vector_index):
    v_index = GPTSimpleVectorIndex.load_from_disk(vector_index)
    while True:
        prompt = input('Ask a question: ')
        response = v_index.query(prompt, response_mode='compact')
        print(f'Response: {response} \n')



# vector_index = create_vector_index('Knowledge')


answerMe('vectorIndex.json')

