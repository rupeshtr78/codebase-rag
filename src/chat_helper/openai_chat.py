from typing import Any

from langchain_openai import OpenAIEmbeddings
from ..document_loaders.generic_loader import CodeBaseLoader
from ..document_splitters.recursive_character_text_splitter import LanguageTextSplitter
from ..chroma_vector_db.vector_store_retriever import ChromaStoreRetriever
from ..chat_prompts.chat_prompt_template import CodePromptTemplate

from .. import logger


class OpenAiChatHelper:
    def __init__(self, path, language, openAiEmbeddings: OpenAIEmbeddings, model: str):
        self.loader = CodeBaseLoader(path, language)
        self.splitter = LanguageTextSplitter(language)
        self.retriever = ChromaStoreRetriever(openAiEmbeddings)
        self.prompt = CodePromptTemplate(model)
        self.language = language
        self.path = path
        self.openAiEmbeddings = openAiEmbeddings
        self.model = model

    def chat(self, question: str) -> Any | None:
        documents = self.loader.code_loader()
        if not documents:
            logger.error("No documents found.")
        chunks = self.splitter.document_chunks(documents) if documents else None
        if not chunks:
            logger.error("No chunks found.")
        retriever = self.retriever.get_retriever(chunks) if chunks else None
        if not retriever:
            logger.error("No retriever found.")
        qa = self.prompt.openai_prompt_template(retriever) if retriever else None

        if qa:
            result = qa.invoke({"input": question})
            if result and "answer" in result:
                return result["answer"]
            else:
                logger.error("No result found or 'answer' key missing in result.")
                return None
        else:
            logger.error("'qa' object is None.")
            return None
