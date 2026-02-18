import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar el cliente
client = genai.Client(api_key=API_KEY)

configuration = types.GenerateContentConfig(
    max_output_tokens=2048,
    system_instruction="""Eres un asistente de estudio especializado en Inteligencia Artificial.
Tus respuestas deben ser concisas y educativas teniendo presente que el usuario es un estudiante de Ingeniería de sistemas.
Si te hacen una pregunta que no está relacionada con la Inteligencia Artificial, responde:
'Lo siento, solo puedo responder preguntas relacionadas con temas de Inteligencia Artificial.'"""
)

# Inicialización del chat
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=configuration
)

print("--- Chat de Estudio IA ---")
print("(Escribe 'salir' para terminar)\n")

while True:
    user_input = input("Estudiante: ")

    if user_input.lower() in ["salir", "exit", "quit"]:
        print("Asistente: ¡Hasta pronto! Sigue practicando.")
        break

    try:
        response = chat.send_message(user_input)
        print(f"\nAsistente: {response.text}\n")

    except Exception as e:
        print(f"Error al procesar la solicitud: {e}")