# ASBL Landmark Real Estate Chatbot 🏡

This Streamlit application implements a conversational chatbot specifically designed to answer questions about the ASBL Landmark real estate project in Kukatpally, Hyderabad, particularly focusing on the "Live To Customer Offer".

It utilizes a Retrieval-Augmented Generation (RAG) approach, leveraging a local knowledge base file, Ollama for running language and embedding models locally, ChromaDB for vector storage, and LangChain to orchestrate the process.

## Features ✨

* **Conversational Interface:** Uses Streamlit's chat components for a user-friendly interaction.
* **RAG Pipeline:** Answers questions based on information retrieved from a provided text knowledge base (`.txt` file).
* **Context-Aware:** Maintains conversation history within a session to understand follow-up questions.
* **Local LLM & Embeddings:** Uses Ollama to run the language model (`gemma3:4b-it-q8_0`) and embedding model (`mxbai-embed-large:latest`) locally, ensuring data privacy.
* **Vector Store:** Employs ChromaDB to store and efficiently query document embeddings.
* **Modular Design:** Encapsulates the core RAG logic within the `ASBLChatbot` class.
* **Error Handling & Logging:** Includes basic error handling and logging for easier debugging.
* **Caching:** Uses Streamlit's `@st.cache_resource` to load the chatbot model efficiently, avoiding re-initialization on every interaction.

## Technology Stack 🛠️

* **Language:** Python 3.9+
* **Web Framework:** Streamlit
* **LLM Orchestration:** LangChain (`langchain`, `langchain-community`, `langchain-core`, `langchain-ollama`)
* **LLM Serving:** Ollama
* **Vector Database:** ChromaDB (`chromadb`)
* **Embeddings & LLM:** Ollama models (e.g., `mxbai-embed-large`, `gemma3:4b-it-q8_0`)

## Prerequisites 📋

1.  **Python:** Ensure you have Python 3.9 or later installed.
2.  **Ollama:** Install and run Ollama on your local machine. Follow the instructions at [https://ollama.com/](https://ollama.com/).
3.  **Ollama Models:** Pull the required models using the Ollama CLI:
    ```bash
    ollama pull mxbai-embed-large:latest
    ollama pull gemma3:4b-it-q8_0
    ```
    *Note: You can modify the model names in the Python script (`ASBLChatbot` class initialization) if you prefer to use different Ollama models.*
4.  **Knowledge Base File:** You need a text file (`.txt`) containing the information the chatbot should use. The current code expects it at: `/Users/devbrattripathi/Desktop/chatapp2/ASBL Landmark Project Knowledge Base (RAG Optimized).txt`. You **must** update the `KNOWLEDGE_FILE` variable in the script if your file is located elsewhere or named differently.

## Setup & Installation ⚙️

1.  **Clone the Repository (or save the code):**
    ```bash
    # If it's in a git repo:
    # git clone <repository-url>
    # cd <repository-directory>

    # Otherwise, just save the Python code as a file (e.g., `app.py`)
    # in a new directory.
    # Not a git repo as of now, so continue.
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies:** Create a `requirements.txt` file with the following content:
    ```txt
    streamlit
    langchain
    langchain-community
    langchain-core
    langchain-ollama
    chromadb
    # Add any other specific dependencies if needed, like 'tiktoken' often required implicitly
    tiktoken
    ```
    Then, install them:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Verify Ollama:** Ensure the Ollama application or server process is running in the background.
    ```bash
    ollama list
    ```
    # Should list all your LLM models

5.  **Place Knowledge Base File:** Make sure the `.txt` knowledge base file exists at the path specified in the `KNOWLEDGE_FILE` variable within the script, or update the path in the script accordingly.

## Configuration 🔧

Modify these variables directly in the Python script (`app.py` or your filename) as needed:

* `KNOWLEDGE_FILE`: Path to your text knowledge base file.
* `PERSIST_DIR`: Directory where the ChromaDB vector store will be saved (defaults to `"chroma_store"` in the script's directory).
* `OllamaLLM(model=...)`: Change `"gemma3:4b-it-q8_0"` if using a different Ollama *language* model.
* `OllamaEmbeddings(model=...)`: Change `"mxbai-embed-large:latest"` if using a different Ollama *embedding* model.

## Running the Application ▶️

1.  Ensure your virtual environment is activated.
2.  Make sure the Ollama server is running.
3.  Navigate to the directory containing your Python script (`app.py` or your chosen name).
4.  Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
    *(Replace `app.py` with your actual script filename if different)*

5.  Streamlit will provide a local URL (usually `http://localhost:8501`) to open in your web browser.

*Note: The first time you run the application, it might take a bit longer as it needs to load the documents, create embeddings, and build the ChromaDB vector store in the specified `persist_directory`.*

## Code Structure Overview 🏗️

* **Imports:** Imports necessary libraries from Streamlit, LangChain, Ollama, standard Python libraries, etc.
* **`ASBLChatbot` Class:**
    * `__init__`: Initializes the chatbot by loading documents, splitting them, setting up Ollama embeddings and LLM, creating/loading the ChromaDB vector store, defining the prompt template, and building the `ConversationalRetrievalChain` wrapped with `RunnableWithMessageHistory`.
    * `_load_documents`: Loads text from the specified file path.
    * `_split_documents`: Splits loaded documents into smaller chunks.
    * `_setup_vectorstore`: Creates the ChromaDB vector store from chunks and embeddings.
    * `_setup_prompt_template`: Defines the system and human message prompts for the LLM.
    * `_setup_rag_chain`: Configures the LangChain `ConversationalRetrievalChain` and wraps it for history management.
    * `invoke`: The method called by the Streamlit UI to get a response from the RAG chain, handling session ID and input/output.
* **Streamlit UI Code:**
    * Sets page configuration (`st.set_page_config`).
    * Handles `asyncio` event loop policy for POSIX systems.
    * `@st.cache_resource`: Caches the `ASBLChatbot` instance creation for performance.
    * Initializes session state (`st.session_state`) for chat messages and a unique session ID.
    * Displays existing chat messages.
    * Handles user input using `st.chat_input`.
    * Calls the `chatbot.invoke` method upon receiving user input.
    * Displays user messages and assistant responses in the chat interface.

## Troubleshooting / Notes ⚠️

* **Ollama Not Running:** Ensure the Ollama application/server is active before starting the Streamlit app. Check the Ollama documentation for troubleshooting.
* **Model Not Found:** Verify that you have pulled the exact model names specified in the code using `ollama pull <model_name>`.
* **File Not Found:** Double-check the `KNOWLEDGE_FILE` path in the script. Ensure the file exists and the application has permission to read it.
* **Dependencies:** Make sure all libraries listed in `requirements.txt` are installed correctly in your virtual environment.
* **Performance:** The initial setup (embedding and vector store creation) can be slow, especially for large knowledge bases. Subsequent runs using the persisted vector store (`persist_directory`) should be faster. The performance of the LLM itself depends on your hardware and the chosen model.
