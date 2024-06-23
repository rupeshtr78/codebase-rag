# @TODO : Add the code to start the chroma db and add the documents to the chroma db
from typing import TYPE_CHECKING, Any
import chromadb
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings, GooglePalmEmbeddings
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Initialize Chroma client with the local host URL
persistent_client = chromadb.HttpClient(host="localhost", port=8080)
async_clinet = chromadb.AsyncHttpClient(host="localhost", port=8080)
collection = persistent_client.get_or_create_collection("your_collection_name")

# Define embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Initialize Langchain Chroma
langchain_chroma = Chroma(
    client=async_clinet,
    collection_name="your_collection_name",
    embedding_function=embedding_function
)




# Load documents
directory = '/path/to/your/documents'
loader = DirectoryLoader(directory)
documents = loader.load()

# Split documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
split_docs = text_splitter.split_documents(documents)

# Embed and add documents to Chroma
langchain_chroma.add_documents(split_docs)

# start docker-compose for chroma db
def start_chroma_db(self):
    pass
def get_chroma_client(self) -> ClientAPI:
    client = None
    try:
        client =chromadb.HttpClient(
                    host=self.host,
                    port=self.port,
                    settings=Settings(
                        chroma_client_auth_provider="chromadb.auth.basic_authn.BasicAuthClientProvider",
                        chroma_client_auth_credentials="admin:testDb@rupesh",
                    ),
                )
    except ValueError:
    # We don't expect to be able to connect to Chroma. We just want to make sure
    # there isn't an ImportError.
        sys.exit(0)
    return client

# async client for chroma db better for streamlit
def get_chroma_async_client(self) -> AsyncClientAPI:
    client = None
    try:
        client = chromadb.AsyncHttpClient(
                    host=self.host,
                    port=self.port,
                    settings=Settings(
                        chroma_client_auth_provider="chromadb.auth.basic_authn.BasicAuthClientProvider",
                        chroma_client_auth_credentials="admin:testDb@rupesh",
                    ),
                )
    except ValueError:
    # We don't expect to be able to connect to Chroma. We just want to make sure
    # there isn't an ImportError.
        sys.exit(0)
    return client
