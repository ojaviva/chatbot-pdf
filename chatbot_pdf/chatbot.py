import fitz  # PyMuPDF para leer PDF
import gradio as gr
import openai
import os
from dotenv import load_dotenv

# Cargar clave de OpenAI
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Función para extraer texto del PDF
def extraer_texto(pdf_path):
    texto = ""
    with fitz.open(pdf_path) as doc:
        for pagina in doc:
            texto += pagina.get_text()
    return texto

# Función para responder preguntas
def chatbot(pdf, pregunta):
    if pdf is None:
        return "Por favor, sube un archivo PDF."
    
    texto = extraer_texto(pdf.name)
    prompt = f"Usa la siguiente información para responder la pregunta:\n\n{texto}\n\nPregunta: {pregunta}\nRespuesta:"
    
    respuesta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Eres un asistente útil."},
                  {"role": "user", "content": prompt}]
    )
    
    return respuesta["choices"][0]["message"]["content"]

# Interfaz con Gradio
interfaz = gr.Interface(
    fn=chatbot,
    inputs=[gr.File(label="Sube tu PDF"), gr.Textbox(label="Pregunta")],
    outputs="text",
    title="Chatbot con PDF",
    description="Sube un archivo PDF y haz preguntas sobre su contenido."
)

# Ejecutar app
if __name__ == "__main__":
    interfaz.launch()
