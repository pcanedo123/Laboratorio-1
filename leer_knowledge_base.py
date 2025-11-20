import json

def leer_knowledge_base(archivo):
    """Lee la base de conocimiento desde un archivo JSON"""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo {archivo} no tiene formato JSON válido")
        return None

# Usar la función
knowledge_base = leer_knowledge_base('knowledge1_base.json')

if knowledge_base:
    print("Base de conocimiento cargada exitosamente:")
    print(f"Número de reglas: {len(knowledge_base.get('reglas', []))}")
    print(f"Respuesta por defecto: {knowledge_base.get('default', 'No definida')}")
    
    # Mostrar las reglas
    for i, regla in enumerate(knowledge_base.get('reglas', []), 1):
        print(f"\nRegla {i}:")
        print(f"  Keywords: {regla.get('keywords', [])}")
        print(f"  Respuesta: {regla.get('respuesta', '')}")