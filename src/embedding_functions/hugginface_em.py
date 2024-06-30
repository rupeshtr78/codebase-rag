from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings
from .. import logger


class VectorEmbeddingModel:
    def __init__(self, model_name, device):
        self.model_name = model_name

    def get_hf_embedding_function(self) -> HuggingFaceEmbeddings:
        try:
            model = self.model_name
            model_kwargs = {
                'device': 'cpu',
                'trust_remote_code': True
            }
            encode_kwargs = {'normalize_embeddings': True}
            hf = HuggingFaceEmbeddings(
                model_name=model,
                model_kwargs=model_kwargs,
                encode_kwargs=encode_kwargs,
                search_kwargs={'k': 5},
            )
            return hf
        except Exception as e:
            logger.error(f"An error occurred while creating the HuggingFaceEmbeddings instance: {e}")
            # Handle the exception appropriately or re-raise it
            raise

    def get_openai_embedding(self) -> OpenAIEmbeddings:
        try:
            openai_embeddings = OpenAIEmbeddings(model=self.model_name)
            return openai_embeddings
        except Exception as e:
            logger.error(f"An error occurred while creating the OpenAIEmbeddings instance: {e}")
            # Handle the exception appropriately or re-raise it
            raise
