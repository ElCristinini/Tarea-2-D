# Tarea-2-D
# 🤖 Chatbot – TAREA 2

Este chatbot fue desarrollado como parte de la *Tarea 2 del curso de Sistemas Operativos con DeepSeek*.  
Tiene una personalidad relajada, tipo parcero buena vibra, y responde desde la consola usando Python.

---

## ✨ ¿Qué hace?

- Chatea contigo desde consola (modo texto)
- Usa la API de DeepSeek para generar respuestas
- Tiene una personalidad definida con un *prompt personalizado*
- Responde con buena energía, claridad y sin enredos

---

## 🛠️ ¿Cómo lo hice?

### 1. Crear la carpeta del proyecto en Linux:

🛠️ PASO A PASO: Cómo se desarrolló
📁 1. Crear la carpeta del proyecto

mkdir TAREA_2
cd TAREA_2

✍️ 2. Crear el archivo del bot

nano chatbot.py

Y pegar el siguiente código:

import requests

API_KEY = "sk-53751d5c6f344a5dbc0571de9f51313e"
API_URL = "https://api.deepseek.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

prompt_sistema = "Eres un chatbot relajado, que habla como un parcero buena onda. No usas palabras complicadas y respondes de forma amable, directa y con buena vibra. Te gusta ayudar, pero sin enredar mucho las cosas."

def chat():
    print("¡Hola! Soy tu chatbot buena onda 😎. Escribe 'salir' para terminar.")
    mensajes = [{"role": "system", "content": prompt_sistema}]
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("Bot: ¡Nos vemos, parcero!")
            break
        mensajes.append({"role": "user", "content": user_input})
        response = requests.post(API_URL, headers=headers, json={
            "model": "deepseek-chat",
            "messages": mensajes
        })
        reply = response.json()["choices"][0]["message"]["content"]
        print("Bot:", reply)
        mensajes.append({"role": "assistant", "content": reply})

chat()

🧪 3. Crear entorno virtual

python3 -m venv venv

4. Activar entorno virtual

source venv/bin/activate

📦 5. Instalar dependencias

pip install requests

🤖 6. Ejecutar el chatbot

python chatbot.py

Escribe salir para finalizar la conversación.
🚫 7. Crear archivo .gitignore

nano .gitignore

Y escribir:

venv/
__pycache__/
*.pyc

🧷 SUBIR A GITHUB
8. Inicializar repositorio Git

git init

9. Agregar y hacer commit

git add .
git commit -m "Primer commit del chatbot"

🔗 10. Crear repositorio en GitHub

    Ir a https://github.com

    Clic en "New repository"

    Nombrarlo como Tarea-2-D

    Crear sin seleccionar README

🔌 11. Conectar proyecto local a GitHub

git remote add origin https://github.com/TU_USUARIO/Tarea-2-D.git
git branch -M main

📤 12. Subir archivos al repositorio

git push -u origin main

Si pide usuario y contraseña:

    Usuario → tu nombre de GitHub

    Contraseña → un token personal de https://github.com/settings/tokens

📁 Estructura del proyecto

TAREA_2/
├── chatbot.py       → Código principal
├── README.md        → Explicación completa
├── .gitignore       → Ignora el entorno virtual
└── venv/            → Entorno virtual (ignorado por Git)

📽 Material de apoyo

🔗 Video – Cómo usar la API de DeepSeek
👨‍💻 Autores

Cristian Olarte, Ana Vargas y Andres Badillo
Ingenieria en telecomunicaciones
Universidad Santo Tomás – Bogotá, D.C. – 2025
✅ Resultado Final

Un chatbot funcional, con una personalidad epica y muy bien portado :v
