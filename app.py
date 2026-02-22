# Importamos request de flask y la nueva función de bayeta
from flask import Flask, jsonify, request
from bayeta import frotar, insertar_frases

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, mundo"

@app.route('/frotar/<n_frotar>', methods=['GET'])
def frotar_epicamente(n_frotar):
    n_frotar = int(n_frotar)
    response = frotar(n_frotar)
    return jsonify(response)

# NUEVO ENDPOINT
@app.route('/frotar/add', methods=['POST'])
def add_frases():
    # Obtenemos el JSON de la petición
    datos = request.get_json()
    
    # Comprobamos que nos hayan enviado la clave "frases"
    if datos and "frases" in datos:
        insertar_frases(datos["frases"])
        return jsonify({"mensaje": "Frases añadidas correctamente"}), 200
    else:
        return jsonify({"error": "Formato incorrecto. Usa {'frases': ['frase1', 'frase2']}"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
