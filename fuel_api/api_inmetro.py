import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Construir as funcionalidades
@app.route('/')
def homepage():
    return 'A API está no ar'

@app.route('/pegar_vendas')
def pegar_vendas():
    tabela = pd.read_csv('Criando API no Python.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)

#  Rodar a nossa API
# app.run()

if __name__ == "__main__":
	app.run(debug=True)