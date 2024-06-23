import streamlit as st
from langchain_openai import OpenAIEmbeddings
from ..chat_helper.openai_chat import ChatHelper as LangChainHelper


def chat_ui():
    # Streamlit UI
    st.title("LangChain Chat Interface")

    path = st.text_input("Enter the path to your documents:", value="")
    model = st.text_input("Enter the model you want to use:", value="gpt-4")
    language = st.text_input("Enter the programming language of your documents:", value="go")
    openAiEmbeddings = OpenAIEmbeddings(model="text-embedding-3-small", disallowed_special=())

    if 'helper' not in st.session_state or path != st.session_state.get('path', '') or model != st.session_state.get(
            'model', '') or language != st.session_state.get('language', ''):
        st.session_state.helper = LangChainHelper(path, language, openAiEmbeddings, model)
        st.session_state.path = path
        st.session_state.model = model
        st.session_state.language = language

    # question = st.text_input("Enter your question:")
    question = st.text_area("Enter your question:")

    # if st.button("Ask"):
    #     if question:
    #         answer = st.session_state.helper.chat(question)
    #         st.write(answer)
    #     else:
    #         st.write("Please enter a question.")
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if st.button("Ask"):
        if question:
            answer = st.session_state.helper.chat(question)
            st.session_state['history'].append((question, answer))
            for q, a in st.session_state['history']:
                st.markdown(f"**Question:** {q}\n\n**Answer:** {a}\n\n---")
        else:
            st.write("Please enter a question.")
