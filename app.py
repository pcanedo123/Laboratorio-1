import json
from flask import Flask, request, jsonify
from flask_cors import CORS

# Inicializar la aplicación de Flask
app = Flask(__name__)

CORS(app)

try:    
    with open('knowledge1_data.json', 'r', encoding='utf-8') as f:
        knowledge1_base = json.load(f)
        print("Base de conocimiento 1 cargada correctamente")
except FileNotFoundError:
    print("Error: Archivo 'knowledge1_data.json' no encontrado.")
    knowledge1_base = {
        "reglas": [
            {
                "keywords": ["Hola", "buenos días", "buenas noches", "buenas tardes"],
                "respuesta": "Hola soy el bot de Casa ROK, ¿En que puedo ayudarte  hoy?"
            },
            {
                "keywords": ["adios", "hasta luego", "chao", "nos vemos", "bye"],
                "respuesta": "Hasta luego, es un place haber charlado contigo"
            },
            {
                "keywords": ["¿como estas?", "me puedes ayudar", "que tal"],
                "respuesta": "Estoy bien, gracias por preguntar, ¿en que puedo ayudarte hoy?"
            }
        ],
        "default": "Lo siento,no entendi esa pregunta. Quieres reformularla o prefieres que te contacte con un agente de servicio al cliente?"
    }

# Iniciar el servidor
if __name__ == '__main__':
    print("Servidor iniciado")
    app.run(debug=True, port=5000)
    











