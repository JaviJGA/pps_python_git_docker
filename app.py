from flask import Flask
from bayeta import frotar
import jsonify

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello worl"

@app.route('/frotar/<n_frotar>', methods=['GET'])
def frotar_epicamente(n_frotar):
    response = frotar()
    return jsonify(response)



# no tocar xd
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

