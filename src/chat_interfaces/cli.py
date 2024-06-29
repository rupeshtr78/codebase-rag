import click
from langchain_openai import OpenAIEmbeddings
from ..chat_helper.openai_chat import OpenAiChatHelper
from ..chat_helper.localai_chat_helper import LocalAiChatHelper

@click.command()
@click.option('--path', prompt='Enter the path to your documents', help='The path to your documents.')
@click.option('--model', prompt='Enter the model you want to use', default='gpt-4', help='The model to use for QA.')
@click.option('--language', prompt='Enter the programming language of your documents', default='go',
              help='The programming language of the documents.')
def chat_cli(path, model, language):
    openAiEmbeddings = OpenAIEmbeddings(model="text-embedding-3-small", disallowed_special=())
    helper = OpenAiChatHelper(path, language, openAiEmbeddings, model)
    embedding_model = "sentence-transformers/all-mpnet-base-v2"
    local_helper = LocalAiChatHelper(path, language, embedding_model, model)
    while True:
        question = input("Enter your question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        # answer = helper.chat(question)
        answer = local_helper.chat(question)
        click.echo(answer)



if __name__ == '__main__':
    chat_cli()
