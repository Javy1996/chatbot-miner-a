# 🤖 Chatbot de Minería - UST Ingeniería Civil en Minas

Este proyecto es un chatbot inteligente diseñado para responder preguntas relacionadas con los contenidos de la asignatura de Minería, utilizando inteligencia artificial a través de la API de OpenAI y Streamlit.

## 🏫 Institución
**Universidad Santo Tomás**  
**Carrera: Ingeniería Civil en Minas**

## 🚀 ¿Qué hace este chatbot?

- 📚 Responde preguntas basadas en documentos cargados.
- 🧠 Usa el modelo `gpt-3.5-turbo` de OpenAI.
- 🖼️ Incluye historial de preguntas/respuestas.
- 🖼️ Muestra el logo oficial de la carrera.
- 🔄 Permite reiniciar la conversación.

## 📂 Estructura del repositorio

📁 docs_mineria/ ← Carpeta con archivos fuente (PDF, Word, etc.)
📄 app.py ← Archivo principal de Streamlit
🖼️ logo.jpg ← Logo oficial de la carrera
📁 .streamlit/
└── secrets.toml ← Clave API de OpenAI (NO compartir públicamente)

bash
Copiar
Editar

## 🔐 Configuración de la API Key

En `.streamlit/secrets.toml`, debes tener:

```toml
OPENAI_API_KEY = "sk-..."
