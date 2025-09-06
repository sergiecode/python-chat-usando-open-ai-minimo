import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env
load_dotenv()

# Intentar obtener la API key desde variable de entorno
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print("No se encontró la variable de entorno OPENAI_API_KEY")
    print("O ve a https://platform.openai.com/api-keys para crear una API key")

# Configure the OpenAI client with your API key
client = OpenAI(api_key=api_key)

# Create a chat completion using the correct API method
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Using a valid model
    messages=[
        {"role": "user", "content": "¿Cómo puedo ser el mejor programador de Python?"}
    ]
)

print(response.choices[0].message.content)
