import pytest
from langchain_community.document_loaders.generic import Document
from langchain_community.document_loaders.parsers import LanguageParser
from logging import getLogger
from src.document_loaders import CodeBaseLoader

@pytest.fixture
def code_base_loader():
    return CodeBaseLoader(path="/path/to/codebase", model="model_name", language="python")

def test_doc_loader(code_base_loader):
    documents = code_base_loader.code_loader()
    
    assert isinstance(documents, list)
    assert all(isinstance(doc, Document) for doc in documents)
    assert len(documents) > 0

def test_doc_loader_empty_path():
    code_base_loader = CodeBaseLoader(path="", model="model_name", language="python")
    documents = code_base_loader.code_loader()
    
    assert isinstance(documents, list)
    assert len(documents) == 0

def test_doc_loader_invalid_language(code_base_loader):
    code_base_loader.language = "invalid_language"
    documents = code_base_loader.code_loader()
    
    assert isinstance(documents, list)
    assert len(documents) == 0