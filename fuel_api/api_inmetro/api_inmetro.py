import pandas as pd
import csv
import json
from flask import Flask, jsonify


app = Flask(__name__)

# Os endereços são baseados na plataforma "PythonAnywhere"
# Construir as funcionalidades e após os testes mudar para a base de dados real
@app.route('/')
def homepage():
    return 'A API está no ar'

@app.route('/teste')
def get_data():  # sourcery skip: for-append-to-extend, identity-comprehension, list-comprehension, simplify-generator
    reader = pd.read_csv('/home/MaPrado/mysite/Criando API no Python.csv')
    data = []
    for row in reader:
        data.append(row)
    return json.dumps(data)

@app.route('/pegar_vendas')
def pegar_vendas():
    tabela = pd.read_csv('/home/MaPrado/mysite/Criando API no Python.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)

#  Rodar a nossa API
if __name__ == "__main__":
    app.run()