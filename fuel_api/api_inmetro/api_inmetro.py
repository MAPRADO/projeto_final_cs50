import pandas as pd
import numpy
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Os endereços são baseados na plataforma "PythonAnywhere"
# Endereço da base de dados:
# 'https://www.pythonanywhere.com/user/MaPrado/files/home/MaPrado/mysite/car_data_2023_test.xlsx'

# Testando se a API está no ar
@app.route('/')
def homepage():
    return 'A API está no ar'


# Seleciona todos os nomes das tabelas da base (Testes OK)
@app.route('/teste')
def get_data():
    #reader = pd.read_excel('https://www.pythonanywhere.com/user/MaPrado/files/home/MaPrado/mysite/car_data_2023_test.xlsx')
    reader = pd.read_excel('car_data_2023_test.xlsx')
    data = []
    for row in reader:
        data.append(row)
    return json.dumps(data)


# Mostra toda base como um dicionário em sequencia (Testes OK)
@app.route('/teste_dois')
def dados():
    reader = pd.read_excel('https://www.pythonanywhere.com/user/MaPrado/files/home/MaPrado/mysite/car_data_2023_test.xlsx')
    dados = reader.to_dict(orient='records')
    return json.dumps(dados)

# Este código está correto para a coluna do motor, filtra as 5 primeiras linhas (Testes OK)
@app.route('/motor')
def motor():
    #tabela = pd.read_excel('https://www.pythonanywhere.com/user/MaPrado/files/home/MaPrado/mysite/car_data_2023_test.xlsx')
    tabela = pd.read_excel('car_data_2023_test.xlsx')
    data = []
    for row in tabela['Motor'].head():
        data.append(row)
    return json.dumps(data)


# Este codigo está correto para filtro de uma coluna com uma linha, com parametros variáveis (Testes OK)
@app.route('/get_row', methods=['GET'])
def get_row():
    try:
        # Obter parâmetros da consulta
        column_name = request.args.get('column_name')
        value = request.args.get('value')

        # Verificar se os parâmetros foram fornecidos
        if not column_name or not value:
            return jsonify({'error': 'Forneça parâmetros válidos: column_name e value'})

        #df = pd.read_excel('https://www.pythonanywhere.com/user/MaPrado/files/home/MaPrado/mysite/car_data_2023_test.xlsx')
        df = pd.read_excel('car_data_2023_test.xlsx')

        # Verificar se a coluna existe no DataFrame
        if column_name not in df.columns:
            return jsonify({'error': f'A coluna {column_name} não existe no DataFrame'})

        # Selecionar a linha com base no valor da coluna
        row = df[df[column_name] == value].iloc[0].to_dict()
        return json.dumps(row)
    except IndexError:
        return jsonify({'error': 'Nenhuma linha encontrada'})


# Main code for creating the API and return filters (OK)
@app.route('/api/filter', methods=['GET'])
def filter_data():

    # Get query parameters
    col1_name = request.args.get('col1_name')
    value1 = request.args.get('value1')
    col2_name = request.args.get('col2_name')
    value2 = request.args.get('value2')
    col3_name = request.args.get('col3_name')
    value3 = request.args.get('value3')

    #tabela = pd.read_excel('https://www.pythonanywhere.com/user/MaPrado/files/home/MaPrado/mysite/car_data_2023_test.xlsx')
    # Excel file that contains the car data. This file is being used as the
    # data source for the API endpoints.
    table = pd.read_excel('car_data_2023_test.xlsx')
    
    # Apply the filter based on the provided column names and their respective values
    filter = table.loc[(table[col1_name] == value1) & (table[col2_name] == value2) & (table[col3_name] == float(value3))]
    
    filter = filter.sort_values('Etanol - cidade', ascending=False).head(1)
    
    # This block filters the data correctly, but I'm going to use the other with just one line
    """ table = table.loc[(table[col3_name] == float(value3))]
    table = table.loc[(table[col2_name] == value2)]
    table = table.loc[(table[col1_name] == value1)] """
    
    # Debugging test: Print the number of rows and columns found
    print(f"Filtered rows and columns: {(filter).shape}")
    print(f"Filtered value: {col3_name , value3}")
    
    # Convert filtered rows to JSON
    data = {}
    for row in filter.itertuples():
        # Use 'Index' or confirm the correct attribute for accessing the DataFrame index
        data[row.Index] = {
            "Combustivel": row[5],
            "Etanol - cidade": row[6],
            "Etanol - estrada": row[7],
            "Gasolina - cidade": row[8],
            "Gasolina - estrada": row[9],
            "Marca": row[1],
            "Modelo": row[2],
            "Motor": row[4],
            "Versao": row[3],

        }
        
    # Return the result
    return jsonify(data)

#  Run our API
if __name__ == "__main__":
    app.run(debug=True)