from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# Libera a comunicação de segurança com o Live Server
CORS(app) 

@app.route('/')
def home():
    return jsonify({'message': 'A API está online!'})

@app.route('/calcular', methods=['POST'])
def calcular():
    dados = request.get_json()
    
    # Prevenção caso os campos venham vazios
    if not dados.get('num1') or not dados.get('num2'):
        return jsonify({'erro': 'Preencha os dois números!'}), 400

    # Puxa os dados e transforma em números com casas decimais (float)
    num1 = float(dados.get('num1'))
    num2 = float(dados.get('num2'))
    operacao = dados.get('operacao')

    # A lógica matemática
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 == 0:
            return jsonify({'erro': 'Não é possível dividir por zero!'}), 400
        resultado = num1 / num2
    else:
        return jsonify({'erro': 'Operação inválida!'}), 400

    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True) 