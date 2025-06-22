
import streamlit as st
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.llms import OpenAI
import os
api_key = st.secrets["OPENAI_API_KEY"]

# Configuración de la app
st.set_page_config(page_title="Chatbot Minería", layout="centered")

# Mostrar logo e información
st.image("logo.jpg", width=150)
st.title("🤖 Chatbot de Minería")
st.caption("Universidad Santo Tomás - Ingeniería Civil en Minas")

# Inicializar el historial si no existe
if "historial" not in st.session_state:
    st.session_state.historial = []

# Botón para reiniciar conversación
if st.button("🔄 Nueva conversación"):
    st.session_state.historial = []
    st.experimental_rerun()

# Caja de entrada de pregunta
pregunta = st.text_input("Escribe tu pregunta aquí 👇", key="input")

if pregunta:
    with st.spinner("Pensando..."):
        docs = SimpleDirectoryReader("docs_mineria").load_data()
        service_context = ServiceContext.from_defaults(
            llm=OpenAI(model="gpt-3.5-turbo", api_key=api_key)
        )
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        query_engine = index.as_query_engine()
        respuesta = query_engine.query(pregunta)

        st.session_state.historial.append((pregunta, respuesta))
        st.session_state.input = ""

# Mostrar historial
if st.session_state.historial:
    st.subheader("🗂 Historial de conversación:")
    for i, (q, r) in enumerate(reversed(st.session_state.historial), 1):
        st.markdown(f"**🟠 Pregunta {i}:** {q}")
        st.markdown(f"**🔵 Respuesta:** {r}")
        st.markdown("---")
else:
    st.info("Haz una pregunta para comenzar.")
