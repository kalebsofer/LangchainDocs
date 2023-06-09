# Leveraging Your Own Documents in a Langchain Pipeline
This project highlights how to leverage a ChromaDB vectorstore in a Langchain pipeline to create a GPT PDF Interpreter. You can load in a pdf based document and use it alongside an LLM without the need for fine tuning.

# Startup 🚀
1. Create a virtual environment `python -m venv env`
2. Activate it: 
   - Mac: `source env/bin/activate`
3. Clone this repo
4. Go into the directory
5. Install the required dependencies `pip install -r requirements.txt`
6. Add your OpenAI APIKey to line 15 of `app.py`, or create a config file and add it there.
7. Start the app `streamlit run app.py`  

# Other References 🔗
<p>The main LG Agent used:<a href="https://python.langchain.com/en/latest/modules/agents/toolkits/examples/vectorstore.html">Langchain VectorStore Agents
</a></p>

# Credit 
Nicholas Renotte:

https://github.com/nicknochnack 