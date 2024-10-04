import requests
from flask import Flask, jsonify

app = Flask(name)

taxadolar = 5.40 
taxaeuro = 6.30

@app.route('/convertepradolareuro/<valor>', methods=['GET'])
def convertepradolareuro(valor):
    try:
        valorreal = float(valor)
    except ValueError:
        return jsonify({"error": "Valor inválido. Forneça um número válido em real."}), 400

    try:
        valordolar = valor_real / taxa_dolar
        valor_euro = valor_real / taxa_euro

        resultado = {
            "conversao": {
                "real": round(valor_real, 2),
                "dolar": round(valor_dolar, 2),
                "euro": round(valor_euro, 2)
            }
        }

        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": "Erro ao obter as taxas de câmbio"}), 500

if __name == '__main':
    app.run(host='0.0.0.0', port=5000, debug=True)