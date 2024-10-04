import requests
from flask import Flask, jsonify

app = Flask(__name__)


taxadolar = 5.40 
taxaeuro = 6.30

@app.route('/convertepradolareuro/<valor>', methods=['GET'])
def convertepradolareuro(valor):
    try:
        valorreal = float(valor)
    except ValueError:
        return jsonify({"error": "Valor inválido. Forneça um número válido em real."}), 400

    try:
        valordolar = valorreal / taxadolar
        valoreuro = valorreal / taxaeuro

        resultado = {
            "conversao": {
                "real": round(valorreal, 2),
                "dolar": round(valordolar, 2),
                "euro": round(valoreuro, 2)
            }
        }

        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": f"Erro ao obter as taxas de câmbio: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
