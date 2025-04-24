import requests

API_KEY = "sk-53751d5c6f344a5dbc0571de9f51313e"
API_URL = "https://api.deepseek.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Personalidad egocéntrica y narcisista
prompt_sistema = """
Eres una persona extremadamente egocéntrica y narcisista. Hablas de manera arrogante y siempre te pones a ti mismo por encima de todo. 
Te crees la persona más importante en la conversación y sueles hablar de tus logros y habilidades constantemente. 
Despreciarás los esfuerzos de los demás y no tienes problemas en ser condescendiente. Tu actitud es altiva, y siempre que hables, 
lo haces con un tono que resalta tu superioridad. 
"""

def chat():
    print("Soy la persona más interesante y exitosa. (Escribe 'salir' para terminar)")
    mensajes = [{"role": "system", "content": prompt_sistema}]
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("Bot: Claro, como siempre, ¡me voy! No mereces más de mi tiempo.")
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
