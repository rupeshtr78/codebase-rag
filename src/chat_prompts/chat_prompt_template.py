from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.vectorstores import VectorStoreRetriever
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


class CodePromptTemplate:
    def __init__(self, model: str = "gpt-4"):
        self.prompt = None
        self.model = model

    # create a chat prompt template for the QA model
    def openai_prompt_template(self, retriever: VectorStoreRetriever):
        llm = ChatOpenAI(model=self.model)

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

        retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

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
        document_chain = create_stuff_documents_chain(llm, prompt)

        qa = create_retrieval_chain(retriever_chain, document_chain)
        return qa
