from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import os # <--- Importando a biblioteca de caminhos

app = Flask(__name__)
CORS(app) 

@app.route('/')
def home():
    return jsonify({'message': 'A API está online!'})

@app.route('/calcular', methods=['POST'])
def calcular():
    dados = request.get_json()
    
    if not dados.get('num1') or not dados.get('num2'):
        return jsonify({'erro': 'Preencha os dois números!'}), 400

    num1 = float(dados.get('num1'))
    num2 = float(dados.get('num2'))
    operacao = dados.get('operacao')

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

    # --- SALVANDO NO BANCO COM CAMINHO ABSOLUTO ---
    try:
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_banco = os.path.join(diretorio_atual, 'memoria.db')
        
        conexao = sqlite3.connect(caminho_banco)
        cursor = conexao.cursor()
        
        cursor.execute('''
            INSERT INTO calculos (numero_1, operacao, numero_2, resultado)
            VALUES (?, ?, ?, ?)
        ''', (num1, operacao, num2, resultado))
        
        conexao.commit()
    except Exception as erro:
        print(f"Erro ao salvar no banco: {erro}")
    finally:
        conexao.close()
    # ----------------------------------------------

    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)