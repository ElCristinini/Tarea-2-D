# 🌸 UwU Chatbot Kawaii – TAREA 2

Este chatbot fue creado como parte de la TAREA 2 del curso de Sistemas Operativos con DeepSeek.  
Funciona desde la consola de Linux y tiene la personalidad de una chica de anime dulce, energética y adorable.  
Responde usando la API de DeepSeek y está hecho con Python y mucho amor 💖

---

## 🛠️ PASO A PASO: Cómo se desarrolló

---

### 📁 1. Crear la carpeta del proyecto

```bash
mkdir TAREA_2_ANIME
cd TAREA_2_ANIME
✍️ 2. Crear el archivo del bot
bash
Copiar
Editar
nano chatbot.py
Y pegar el siguiente código:

python
Copiar
Editar
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
🧪 3. Crear entorno virtual
bash
Copiar
Editar
python3 -m venv venv
▶️ 4. Activar entorno virtual
bash
Copiar
Editar
source venv/bin/activate
📦 5. Instalar dependencias
bash
Copiar
Editar
pip install requests
🤖 6. Ejecutar el chatbot
bash
Copiar
Editar
python chatbot.py
Escribe salir para finalizar la conversación.

🚫 7. Crear archivo .gitignore
bash
Copiar
Editar
nano .gitignore
Y escribir:

markdown
Copiar
Editar
venv/
_pycache_/
*.pyc
🧷 SUBIR A GITHUB
8. Inicializar repositorio Git
bash
Copiar
Editar
git init
9. Agregar y hacer commit
bash
Copiar
Editar
git add .
git commit -m "Primer commit del chatbot kawaii 🌸"
🔗 10. Crear repositorio en GitHub
Ir a https://github.com

Clic en “New repository”

Nombrarlo como Tarea-2-D

Crear sin seleccionar README

🔌 11. Conectar proyecto local a GitHub
bash
Copiar
Editar
git remote add origin https://github.com/TU_USUARIO/Tarea-2-D.git
git branch -M main
(Reemplaza TU_USUARIO por tu nombre de usuario en GitHub)

📤 12. Subir archivos al repositorio
bash
Copiar
Editar
git push -u origin main
Si pide usuario y contraseña:

Usuario → tu nombre de usuario de GitHub

Contraseña → un token personal

📁 Estructura del proyecto
plaintext
Copiar
Editar
TAREA_2_ANIME/
├── chatbot.py       → Código principal
├── README.md        → Explicación completa del proyecto
├── .gitignore       → Para ignorar el entorno virtual
└── venv/            → Entorno virtual (ignorado por Git)
📽 Material de apoyo
🔗 Video – Cómo usar la API de DeepSeek

👩‍💻 Autores
Cristian Olarte, Ana Vargas y Andres Badillo
Estudiantes de ingenieria de telecomunicaciones
Universidad Santo Tomás – Bogotá, D.C. – 2025
💖 "Programando con estilo, desu~ uwu~"


![Banner del chatbot kawaii](https://github.com/ElCristinini/Tarea-2-D/raw/main/portada.png)

