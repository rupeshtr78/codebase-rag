from langchain_openai import OpenAIEmbeddings
from ..document_loaders.generic_loader import CodeBaseLoader
from ..document_splitters.recursive_character_text_splitter import LanguageTextSplitter
from ..chroma_vector_db.vector_store_retriever import ChromaStoreRetriever
from ..chat_prompts.chat_prompt_template import CodePromptTemplate


class ChatHelper:
    def __init__(self, path, language, openAiEmbeddings: OpenAIEmbeddings, model: str):
        self.loader = CodeBaseLoader(path, language)
        self.splitter = LanguageTextSplitter(language)
        self.retriever = ChromaStoreRetriever(openAiEmbeddings)
        self.prompt = CodePromptTemplate(model)

    def chat(self, question: str) -> str:
        documents = self.loader.doc_loader()
        chunks = self.splitter.document_chunks(documents)
        retriever = self.retriever.get_retriever(chunks)
        qa = self.prompt.openai_prompt_template(retriever)
        result = qa.invoke({"input": question})
        return result["answer"]
