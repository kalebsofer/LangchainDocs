import os
import config
from langchain.llms import OpenAI
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo,
)

# Set APIkey for OpenAI Service
# Can sub this out for other LLM providers
os.environ["OPENAI_API_KEY"] = config.OPENAI_API_KEY

# Create instance of OpenAI LLM
llm = OpenAI(temperature=0.1, verbose=True)

# Create and load PDF Loader, split pdf pages,
# and Load documents into vector database aka ChromaDB
loader = PyPDFLoader("annualreport.pdf")
pages = loader.load_and_split()
store = Chroma.from_documents(pages, collection_name="annualreport")

# Create vectorstore info object - metadata repo?
vectorstore_info = VectorStoreInfo(
    name="annual_report",
    description="a financial report as a pdf",
    vectorstore=store,
)
# Convert the document store into a langchain toolkit
toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

# Add the toolkit to an end-to-end LC
agent_executor = create_vectorstore_agent(llm=llm, toolkit=toolkit, verbose=True)
st.title("🦜🔗 GPT PDF Interpreter")
# Create a text input box for the user
prompt = st.text_input("Input your prompt here")

# If the user hits enter
if prompt:
    # Then pass the prompt to the LLM
    response = agent_executor.run(prompt)
    # ...and write it out to the screen
    st.write(response)

    # With a streamlit expander
    with st.expander("Document Similarity Search"):
        # Find the relevant pages
        search = store.similarity_search_with_score(prompt)
        # Write out the first
        st.write(search[0][0].page_content)
