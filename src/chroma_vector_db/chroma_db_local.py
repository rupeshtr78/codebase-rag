import sys
from typing import TYPE_CHECKING, Any, Coroutine
import chromadb
from chromadb.config import Settings
from langchain.vectorstores import Chroma
from chromadb.api import AsyncClientAPI
from chromadb.api.models.AsyncCollection import AsyncCollection
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_core.documents import Document
from .. import logger


class ChromaLocal:
    def __init__(self, host: str, port: int, collection_name: str, embedding_model: str):
        self.host = host
        self.port = port
        self.collection_name = collection_name
        self.database = "chromadb_local"
        self.embedding_model = embedding_model
        self.client = self.get_chroma_async_client()

    # Initialize Chroma client with the local host URL
    def get_chroma_async_client(self) -> Coroutine[Any, Any, AsyncClientAPI]:
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
            sys.exit(0)
        return client

    def get_embedding_function(self) -> HuggingFaceEmbeddings:
        try:
            model = self.embedding_model
            model_kwargs = {
                'device': 'cpu',
                'trust_remote_code': True
            }
            encode_kwargs = {'normalize_embeddings': True}
            hf = HuggingFaceEmbeddings(
                model_name=model,
                model_kwargs=model_kwargs,
                encode_kwargs=encode_kwargs,
                search_kwargs={'k': 5},
            )
            return hf
        except Exception as e:
            logger.error(f"An error occurred while creating the HuggingFaceEmbeddings instance: {e}")
            # Handle the exception appropriately or re-raise it
            raise

    def get_chromadb(self):
        try:
            # Initialize Langchain Chroma instance
            langchain_chroma = Chroma(
                client=self.get_chroma_async_client(),
                collection_name=self.collection_name,
                embedding_function=self.get_embedding_function(),
            )
            return langchain_chroma
        except Exception as e:
            logger.error(f"An error occurred while initializing ChromaDB: {e}")
            # Handle the exception appropriately or re-raise it
            raise

    def create_chroma_collection(self, client: AsyncClientAPI) -> Coroutine[Any, Any, AsyncCollection]:
        try:
            collection = client.get_or_create_collection(
                name=self.collection_name,
            )
            return collection
        except ValueError:
            sys.exit(0)

    def add_documents_to_local_vectordb(self, split_docs: list[Document]) -> None:
        if not split_docs:
            logger.error(f"No documents found to split")
            return
        try:
            langchain_chroma: Chroma = self.get_chromadb()
            langchain_chroma.aadd_documents(split_docs)
        except Exception as e:
            logger.error(f"An error occurred while adding documents to ChromaDB: {e}")
            # Handle the exception appropriately or re-raise it
            raise

    def retrieve_from_local_vectordb(self, db: Chroma) -> VectorStoreRetriever:
        try:
            retriever = db.as_retriever(
                search_type="mmr",  # "similarity_score_threshold", "mmr", "knn"
                # search_kwargs={"k": 8},
                search_kwargs={'k': 6, 'lambda_mult': 0.25},  # Useful if your dataset has many similar documents
            )
            return retriever
        except Exception as e:
            logger.error(f"An error occurred while retrieving documents from ChromaDB: {e}")
            # Handle the exception appropriately or re-raise it
            raise
