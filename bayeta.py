from mongo_service import consultar, inicializar

# Intentamos inicializar la DB al arrancar el módulo
try:
    inicializar()
except Exception as e:
    print(f"Aviso: No se pudo conectar a Mongo al inicializar (ignorar si es entorno de build): {e}")

def frotar(n_frases: int = 1):
    # Sustituimos el bucle anterior por la consulta a Mongo
    lista = consultar(n_frases)
    return lista
