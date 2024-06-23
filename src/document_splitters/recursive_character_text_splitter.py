from langchain_text_splitters import Language, RecursiveCharacterTextSplitter
from typing import TYPE_CHECKING, List
from langchain_community.document_loaders.generic import Document


class LanguageTextSplitter:
    def __init__(self, language: str):
        self.language = language

    def document_chunks(self, documents: List[Document]) -> List[Document]:
        # Split the content of all documents.
        doc_splitter = RecursiveCharacterTextSplitter.from_language(
            language= Language(self.language), chunk_size=1024, chunk_overlap=200
        )
        texts = doc_splitter.split_documents(documents)
        return texts
