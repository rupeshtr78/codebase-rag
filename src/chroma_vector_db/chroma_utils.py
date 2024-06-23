import os
import subprocess

from langchain_community.document_loaders import DirectoryLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from .. import logger


def documents_loader_recursive(dir_path: str) -> list[Document]:
    if os.path.isdir(dir_path):
        logger.error(f"Directory path does not exist: {dir_path}")
        return []
    try:
        loader = DirectoryLoader(path=dir_path, recursive=True)
        documents = loader.load()
        return documents
    except Exception as e:
        logger.error(f"An error occurred while adding documents to ChromaDB: {e}")
        # Handle the exception appropriately or re-raise it
        raise


def documents_splitter(dir_path: str) -> list[Document]:
    documents = documents_loader_recursive(dir_path)
    if not documents:
        logger.error(f"No documents found to split")
        return []
    try:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        split_docs = text_splitter.split_documents(documents)
        return split_docs
    except Exception as e:
        logger.error(f"An error occurred while adding documents to ChromaDB: {e}")
        # Handle the exception appropriately or re-raise it
        raise


def start_chroma_db(self):
    try:
        # Specify the path to your docker-compose.yml file
        docker_compose_file_path = "/path/to/your/docker-compose.yml"
        command = f"docker-compose -f {docker_compose_file_path} up -d"
        subprocess.check_call(command, shell=True)
        logger.info("ChromaDB service started successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"An error occurred while starting the ChromaDB service: {e}")
        # Handle the exception appropriately or re-raise it
        raise
