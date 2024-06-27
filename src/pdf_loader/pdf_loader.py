from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders.generic import  Document

class PdfLoaderReader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_and_split(self) -> list[Document]:
        loader = PyPDFLoader(self.file_path)
        pages = loader.load_and_split()
        return pages
    
    
    def pdf_faiss_index(self, page: list[Document]) -> list[Document]:
        pages = self.load_and_split()
        faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())
        docs = faiss_index.similarity_search("What is LayoutParser?", k=2)
        # for doc in docs:
        #     print(str(doc.metadata["page"]) + ":", doc.page_content[:300])
        return docs
    


