import sqlite3
import os

# 1. Usa a mesma âncora para ler
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_banco = os.path.join(diretorio_atual, 'memoria.db')

# 2. Abre a porta do banco no caminho absoluto
conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

cursor.execute("SELECT * FROM calculos")
linhas = cursor.fetchall()

print("\n--- 🗄️ HISTÓRICO DE CÁLCULOS DA SUA TABELA FATO ---")
print(f"{'ID':<5} | {'NÚMERO 1':<10} | {'OPERADOR':<10} | {'NÚMERO 2':<10} | {'RESULTADO':<10} | {'DATA E HORA'}")
print("-" * 80)

for linha in linhas:
    print(f"{linha[0]:<5} | {linha[1]:<10} | {linha[2]:<10} | {linha[3]:<10} | {linha[4]:<10} | {linha[5]}")

conexao.close()
print("\n")