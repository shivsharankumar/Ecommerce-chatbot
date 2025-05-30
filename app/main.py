import streamlit as st
from faq import ingest_faq_data, faq_chain
from sql import sql_chain
from smalltalk import talk
from pathlib import Path
from router import semantics_router
import torch
torch.classes.__path__ = []
# faqs_path = Path(__file__).parent / "resources/faq_data.csv"accordion_data
faqs_path = Path(__file__).parent / "resources/accordion_data.csv"
ingest_faq_data(faqs_path)


def ask(query):
    
    route = semantics_router(query).name
    if route == 'faq':
        return faq_chain(query)
    elif route == 'sql':
        return sql_chain(query)
    elif route == 'small-talk':
        return talk(query)
    else:
        return f"Route {route} not implemented yet"

st.title("Retimer Bot")

query = st.chat_input("Write your query")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if query:
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.messages.append({"role":"user", "content":query})

    response = ask(query)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})


