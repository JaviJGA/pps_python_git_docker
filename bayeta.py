# Actualizamos el import para traer también 'insertar'
from mongo_service import consultar, inicializar, insertar

try:
    inicializar()
except Exception as e:
    print(f"Aviso: No se pudo conectar a Mongo al inicializar: {e}")

def frotar(n_frases: int = 1):
    lista = consultar(n_frases)
    return lista

# Nueva función
def insertar_frases(frases: list):
    insertar(frases)
