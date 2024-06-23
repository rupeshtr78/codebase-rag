import pytest
from langchain_community.document_loaders.generic import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from document_splitters import TextSplitter

@pytest.fixture
def text_splitter():
    return TextSplitter(language="english")

def test_document_chunks(text_splitter):
    documents = [Document(content="This is document 1."), Document(content="This is document 2.")]
    expected_texts = ["This is document 1.", "This is document 2."]
    
    texts = text_splitter.document_chunks(documents)
    
    assert texts == expected_texts

def test_document_chunks_empty(text_splitter):
    documents = []
    expected_texts = []
    
    texts = text_splitter.document_chunks(documents)
    
    assert texts == expected_texts

def test_document_chunks_large_documents(text_splitter):
    documents = [Document(content="a" * 1000), Document(content="b" * 1000)]
    expected_texts = ["a" * 1000, "b" * 1000]
    
    texts = text_splitter.document_chunks(documents)
    
    assert texts == expected_texts