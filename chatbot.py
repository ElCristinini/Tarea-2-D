import requests

# Clave API de DeepSeek (ya viene en la presentación)
API_KEY = "sk-53751d5c6f344a5dbc0571de9f51313e"
API_URL = "https://api.deepseek.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# PERSONALIDAD RELAJADA
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
