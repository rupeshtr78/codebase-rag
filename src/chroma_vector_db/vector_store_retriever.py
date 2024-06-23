from typing import List

from langchain_chroma import Chroma
from langchain_community.document_loaders.generic import Document
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_openai import OpenAIEmbeddings


class ChromaStoreRetriever:
    def __init__(self, openAiEmbeddings: OpenAIEmbeddings):
        self.openAiEmbeddings = openAiEmbeddings

    def get_retriever(self, documents: List[Document]) -> VectorStoreRetriever:
        db = Chroma.from_documents(documents, self.openAiEmbeddings)
        retriever = db.as_retriever(
            search_type="mmr",
            # search_kwargs={"k": 8},
            search_kwargs={'k': 6, 'lambda_mult': 0.25}  # Useful if your dataset has many similar documents
        )
        return retriever
