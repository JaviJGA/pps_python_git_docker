import os
from pymongo import MongoClient
from frases import datos as frases_texto

# Configuramos la URI apuntando al contenedor 'mi-mongo' (Paso 8)
MONGO_URI = 'mongodb://mi-mongo:27017/'

def instanciar():
    """Conexión con el motor, obtener la BBDD y la colección concreta"""
    cliente_mongo = MongoClient(MONGO_URI)
    bd = cliente_mongo['bayeta']
    coleccion = bd['frases_auspiciosas']
    return coleccion

def inicializar():
    """Inicialización: inserta datos si la colección está vacía"""
    coleccion = instanciar()
    
    if coleccion.count_documents({}) == 0:
        # Transformamos la lista de strings de frases.py al formato dict
        datos_para_insertar = [{"frase": f} for f in frases_texto]
        coleccion.insert_many(datos_para_insertar)
        print("Base de datos inicializada con éxito.")

def consultar(n_frases: int):
    """Consulta: obtiene frases aleatorias"""
    coleccion = instanciar()
    
    # Usamos la tubería de agregación del fichero original
    pipeline = [{'$sample': {'size': n_frases}}]
    frases_aleatorias = list(coleccion.aggregate(pipeline))
    
    # Extraemos solo el texto para devolver la lista de strings
    return [f['frase'] for f in frases_aleatorias]
