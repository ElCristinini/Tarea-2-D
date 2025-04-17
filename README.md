# 🌸 UwU Chatbot Kawaii – TAREA 2

Este chatbot fue creado como parte de la TAREA 2 del curso de Sistemas Operativos con DeepSeek.  
Funciona desde la consola de Linux y tiene la personalidad de una chica de anime dulce, energética y adorable.  
Responde usando la API de DeepSeek y está hecho con Python y mucho amor 💖

---

## 🛠️ PASO A PASO: Cómo se desarrolló

---
## 📁 1. Crear la carpeta del proyecto
mkdir Tarea-2-D.

cd Tarea-2-D.

---
## ✍️ 2. Crear el archivo del bot
nano chatbot.py

Ahora se crea el codigo, que quedaria de la siguiente manera:

import requests

API_KEY = "sk-53751d5c6f344a5dbc0571de9f51313e"
API_URL = "https://api.deepseek.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

prompt_sistema = "Eres una chica de anime dulce y energética. Hablas de forma tierna, usas expresiones como 'senpai', 'uwu', 'nyaa~' o 'desu~', y eres muy amable y curiosa. Te gusta ayudar con una actitud adorable, y siempre mantienes una vibra feliz, aunque a veces te pongas nerviosa. ¡Eres un bot kawaii y encantador!"

def chat():
    print("Konnichiwa~ Soy tu chatbot kawaii desu~! 🥺✨ (Escribe 'salir' para terminar)")
    mensajes = [{"role": "system", "content": prompt_sistema}]
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("Bot: ¡Bye bye senpai~! UwU 💖")
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
---
## 🧪 3. Crear entorno virtual

python3 -m venv venv

---
## ▶️ 4. Activar entorno virtual

source venv/bin/activate

---
## 📦 5. Instalar dependencias

pip install requests

---
## 🤖 6. Ejecutar el chatbot

python chatbot.py

---
## 🚫 7. Crear archivo .gitignore

nano .gitignore

Y ahora se pega:

venv/
__pycache__/
*.pyc


---
## 🧷 SUBIR A GITHUB
8. Inicializar repositorio Git

git init


---
## 9. Agregar y hacer commit

git add .
git commit -m "Primer commit del chatbot kawaii 🌸"

---
## 🔗 10. Crear repositorio en GitHub

Ir a https://github.com

Clic en “New repository”

Nombrarlo como Tarea-2-D

Crear sin seleccionar README

---
## 🔌 11. Conectar proyecto local a GitHub

git remote add origin https://github.com/TU_USUARIO/Tarea-2-D.git
git branch -M main

---
## 📤 12. Subir archivos al repositorio

git push -u origin main

Si tu usuario pide contraseña: 

Usuario → tu nombre de usuario en GitHub

Contraseña → un token personal de https://github.com/settings/tokens

---
## 📁 Estructura del proyecto


TAREA-2-D/

├── chatbot.py       → Código principal

├── README.md        → Explicación completa del proyecto

├── .gitignore       → Para ignorar el entorno virtual

└── venv/            → Entorno virtual (ignorado por Git)

---
## 📽 Material de apoyo

🔗 Video – Cómo usar la API de DeepSeek

---
## 👩‍💻 Autores

Cristian Olarte, Ana Vargas y Andres Badillo :D

Universidad Santo Tomas

Ingenieria de telecomunicaciones


💖 "Programando con ternura, desu~"


https://github.com/ElCristinini/Tarea-2-D/blob/main/chatbot%20funcionamiento.jpg


