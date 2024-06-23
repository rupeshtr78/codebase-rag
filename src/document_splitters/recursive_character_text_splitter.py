from langchain_text_splitters import Language, RecursiveCharacterTextSplitter
from typing import TYPE_CHECKING, List
from langchain_community.document_loaders.generic import Document
from .. import logger

class LanguageTextSplitter:
    def __init__(self, language: str):
        self.language = language

    def document_chunks(self, documents: List[Document]) -> List[Document]:
        # Split the content of all documents.
        doc_splitter = RecursiveCharacterTextSplitter.from_language(
            language=Language(self.language), chunk_size=1024, chunk_overlap=200
        )

        if not doc_splitter:
            logger.error(f"Could not create a RecursiveCharacterTextSplitter for language {self.language}")
            return []

        texts = doc_splitter.split_documents(documents)
        if not texts:
            logger.error(f"Could not split documents for language {self.language}")
            return []

        return texts
