# 🤖 Chat con OpenAI - Aplicación Educativa

Una aplicación simple en Python que demuestra cómo integrar y usar la API de OpenAI para crear un chat básico. Este proyecto tiene fines educativos y es perfecto para aprender los fundamentos de la integración con APIs de inteligencia artificial.

## 📋 ¿Qué hace esta aplicación?

Esta aplicación Python realiza lo siguiente:
- Se conecta a la API de OpenAI usando la biblioteca oficial `openai`
- Carga la API key de forma segura usando variables de entorno
- Envía una consulta predefinida al modelo GPT-3.5-turbo
- Muestra la respuesta generada por la IA en la consola

Es un ejemplo mínimo y funcional que puedes usar como base para proyectos más complejos con IA.

## 🛠️ Requisitos previos

- Python 3.7 o superior
- Una cuenta en OpenAI con acceso a la API
- Una API key válida de OpenAI

## 📦 Configuración del ambiente Python

### Paso 1: Instalar Python

1. Ve a [python.org](https://www.python.org/downloads/)
2. Descarga la versión más reciente de Python para tu sistema operativo
3. Durante la instalación, asegúrate de marcar "Add Python to PATH"
4. Verifica la instalación abriendo una terminal y ejecutando:
   ```bash
   python --version
   ```

### Paso 2: Crear un entorno virtual (recomendado)

Es una buena práctica crear un entorno virtual para cada proyecto:

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### Paso 3: Instalar las dependencias

```bash
pip install openai python-dotenv
```

## 🔑 Configuración de la API Key

### Paso 1: Obtener tu API Key

1. Ve a [OpenAI Platform](https://platform.openai.com/api-keys)
2. Inicia sesión o crea una cuenta
3. Haz clic en "Create new secret key"
4. Copia la API key generada (guárdala en un lugar seguro)

### Paso 2: Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```bash
# Crear el archivo .env
touch .env  # En macOS/Linux
# En Windows puedes crear el archivo directamente desde el explorador
```

Agrega tu API key al archivo `.env`:

```env
OPENAI_API_KEY=tu_api_key_aqui
```

**⚠️ IMPORTANTE**: Nunca subas tu archivo `.env` al repositorio. Asegúrate de que esté en tu `.gitignore`.

## 🚀 Cómo ejecutar la aplicación

1. Clona o descarga este repositorio
2. Navega al directorio del proyecto
3. Activa tu entorno virtual (si lo creaste)
4. Instala las dependencias
5. Configura tu archivo `.env` con tu API key
6. Ejecuta la aplicación:

```bash
python open-ai-chat-test.py
```

## 📝 Estructura del código

```python
import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener API key
api_key = os.getenv('OPENAI_API_KEY')

# Crear cliente de OpenAI
client = OpenAI(api_key=api_key)

# Realizar consulta
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "¿Cómo puedo ser el mejor programador de Python?"}
    ]
)

# Mostrar respuesta
print(response.choices[0].message.content)
```

## 🔧 Personalización

Puedes modificar la consulta cambiando el contenido en:

```python
{"role": "user", "content": "Tu pregunta aquí"}
```

También puedes experimentar con diferentes modelos:
- `gpt-3.5-turbo` (más económico)
- `gpt-4` (más potente, pero más costoso)

## 💡 Ideas para expandir este proyecto

- Crear un chat interactivo en bucle
- Agregar diferentes roles (system, assistant, user)
- Implementar un historial de conversación
- Crear una interfaz gráfica con tkinter o web con Flask
- Agregar manejo de errores más robusto

## 🐛 Solución de problemas

### Error de API Key
```
No se encontró la variable de entorno OPENAI_API_KEY
```
**Solución**: Verifica que tu archivo `.env` esté en la raíz del proyecto y contenga tu API key.

### Error de conexión
```
Connection error
```
**Solución**: Verifica tu conexión a internet y que tu API key sea válida.

### Error de cuota
```
Quota exceeded
```
**Solución**: Verifica tu saldo en OpenAI o considera usar un modelo más económico.

## 📚 Recursos adicionales

- [Documentación oficial de OpenAI](https://platform.openai.com/docs)
- [Guía de mejores prácticas de OpenAI](https://platform.openai.com/docs/guides/production-best-practices)
- [Pricing de OpenAI](https://openai.com/pricing)

## 👨‍💻 Sobre el autor

**Sergie Code** - Software Engineer y Educator

¡Sígueme en mis redes sociales para más contenido de programación!

- 📽️ **YouTube**: https://www.youtube.com/@SergieCode
- 🧑🏼‍💼 **LinkedIn**: https://www.linkedin.com/in/sergiecode/
- 🐙 **GitHub**: https://github.com/sergiecode  
- 📸 **Instagram**: https://www.instagram.com/sergiecode
- 🕊️ **Twitter**: https://twitter.com/sergiecode
- 🧵 **Threads**: https://www.threads.net/@sergiecode
- 🎞️ **TikTok**: https://www.tiktok.com/@sergiecode
- 👤 **Facebook**: https://www.facebook.com/sergiecodeok

⭐ **¡Si este proyecto te fue útil, no olvides darle una estrella!** ⭐
