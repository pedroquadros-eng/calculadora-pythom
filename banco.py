import sqlite3
import os

# 1. Descobre a pasta exata do arquivo e cria uma âncora
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_banco = os.path.join(diretorio_atual, 'memoria.db')

# 2. Conecta usando o caminho absoluto
conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS calculos (
    id_calculo INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_1 REAL,
    operacao TEXT,
    numero_2 REAL,
    resultado REAL,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

conexao.commit()
conexao.close()

print(f"✅ Banco criado com sucesso no caminho exato:\n{caminho_banco}")