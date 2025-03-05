# 🤖 Chatbot con PDF usando OpenAI y Gradio 🤖

Este proyecto **.py** es una aplicación de chatbot que permite a los usuarios **subir un archivo PDF** y hacer preguntas sobre su contenido.  
Utiliza **Gradio** para la interfaz, **PyMuPDF** para extraer texto del PDF y la API de **OpenAI** para generar respuestas.

## 🚀 Características
✅ Subir un archivo **PDF**  
✅ Hacer preguntas sobre su contenido  
✅ Respuestas generadas con **GPT-4**  
✅ Interfaz fácil de usar con **Gradio**  

## 📌 Requisitos
Antes de ejecutar el proyecto, instala las dependencias necesarias con:

```bash
pip install -r requirements.txt
```

Además, necesitas una clave de API de **OpenAI**.  
Regístrate en [OpenAI](https://openai.com/) y genera tu clave, luego crea un archivo **.env** en la raíz del proyecto con:

```bash
OPENAI_API_KEY="tu_clave_aquí"
```

## 🛠 Cómo ejecutar la aplicación

```bash
git clone https://github.com/ojaviva/chatbot-pdf.git
cd chatbot-pdf
python app.py
```

## 📜 Archivo de Dependencias (`requirements.txt`)

```txt
pymupdf
gradio
openai
python-dotenv
```

Para instalar, usa:

```bash
pip install -r requirements.txt
```

## 🔒 Licencia
Este proyecto está bajo la licencia **MIT**.
