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
