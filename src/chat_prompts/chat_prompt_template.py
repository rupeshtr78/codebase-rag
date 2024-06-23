from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.vectorstores import VectorStoreRetriever
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from .. import logger

class CodePromptTemplate:
    def __init__(self, model: str = "gpt-4"):
        self.prompt = None
        self.model = model

        # if self.model == "gpt-4":
        #     self.prompt = self.openai_prompt_template(VectorStoreRetriever("gpt-4"))

    # create a chat prompt template for the code generation model
    def openai_prompt_template(self, retriever: VectorStoreRetriever):
        llm = ChatOpenAI(model=self.model)
        if not llm:
            logger.error("Failed to load the LLM model")

        # First we need a prompt that we can pass into an LLM to generate this search query
        prompt = ChatPromptTemplate.from_messages(
            [
                ("placeholder", "{chat_history}"),
                ("user", "{input}"),
                (
                    "user",
                    "Given the above conversation, generate a search query to look up to get information relevant to the "
                    "conversation",
                ),
            ]
        )

        if not prompt:
            logger.error("Failed to create the prompt template")

        retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

        if not retriever_chain:
            logger.error("Failed to create the retriever chain")

        # Now we need a prompt that we can pass into an LLM to generate the answer
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "Answer the user's questions based on the below context:\n\n{context}",
                ),
                ("placeholder", "{chat_history}"),
                ("user", "{input}"),
            ]
        )

        if not prompt:
            logger.error("Failed to create the prompt template")

        document_chain = create_stuff_documents_chain(llm, prompt)

        if not document_chain:
            logger.error("Failed to create the document chain")

        qa = create_retrieval_chain(retriever_chain, document_chain)

        if not qa:
            logger.error("Failed to create the retrieval chain")
        return qa
