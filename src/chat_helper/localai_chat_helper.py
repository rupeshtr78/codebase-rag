from langchain_openai import OpenAIEmbeddings
from ..document_loaders.generic_loader import CodeBaseLoader
from ..document_splitters.recursive_character_text_splitter import LanguageTextSplitter
from ..chroma_vector_db.vector_store_retriever import ChromaStoreRetriever
from ..chroma_vector_db.chroma_db_local import ChromaLocal
from ..chat_prompts.chat_prompt_template import CodePromptTemplate

from .. import logger


class LocalAiChatHelper:
    def __init__(self, path, language, openAiEmbeddings: OpenAIEmbeddings, ai_model: str):
        self.loader = CodeBaseLoader(path, language)
        self.splitter = LanguageTextSplitter(language)
        self.retriever = ChromaLocal(host="0.0.0.0", port=8080, collection_name="chromadb_local",
                                     embedding_model="sentence-transformers/all-mpnet-base-v2")
        self.prompt = CodePromptTemplate(ai_model)

    def chat(self, question: str) -> str:
        documents = self.loader.code_loader()
        if not documents:
            logger.error("No documents found.")

        chunks = self.splitter.document_chunks(documents) if documents else None
        if not chunks:
            logger.error("No chunks found.")

        db = self.retriever.get_chromadb() if chunks else None
        if not db:
            logger.error("No db found.")

        retriever = self.retriever.retrieve_from_local_vectordb(db) if db else None
        if not retriever:
            logger.error("No retriever found.")

        qa = self.prompt.openai_prompt_template(retriever) if retriever else None
        if not qa:
            logger.error("No QA found.")

        result = qa.invoke({"input": question}) if qa else None
        if not result:
            logger.error("No result found.")

        return result["answer"]
