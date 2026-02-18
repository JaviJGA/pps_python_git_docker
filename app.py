from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, mundo"

@app.route('/frotar/<n_frotar>', methods=['GET'])
def frotar_epicamente(n_frotar):
    n_frotar = int(n_frotar)
    response = frotar(n_frotar)
    return jsonify(response)


# no tocar xd
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
