import sqlite3
import requests
import json
from flask import Flask, jsonify, redirect, render_template, request
from main_application import fplus

# Connection with the database
#connect = sqlite3.connect('db/my_database.db')

# Configure the application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Dicionário para armazenar os dados(fora da função)
shared_parameters = {}

# Route to the home page: index
@app.route("/", methods=["GET", "POST"])
def index():
    
    return render_template('index.html')

# Request and submission the data: requisition
@app.route("/requisition", methods=["POST"])
def requisition():
        
    # Getting user input from HTML
    name = request.form["name"]
    alcohol = request.form["alcohol"]
    gasoline = request.form["gasoline"]
    selectBrand = request.form["selectBrand"]
    selectModel = request.form["selectModel"]
    selectMotor = request.form["selectMotor"]
    #advantage = request. form["advantage"]
    
    # Construir a consulta a API
    value1 = selectBrand
    value2 = selectModel
    value3 = selectMotor

    url = 'https://maprado.pythonanywhere.com/api/filter'
    parametros_consulta = {
        "col1_name": "Marca",
        "value1": value1, 
        "col2_name": "Modelo",
        "value2": value2,
        "col3_name": "Motor",
        "value3": value3
    }

    # Fazer a requisição a API
    resposta_api = requests.get(url, params=parametros_consulta)
    
    # Verificar o resultado e fazer tratamento de erro
    if resposta_api.status_code == 200:
        # Processar os dados da resposta
        print("Consulta à API bem-sucedida!")
        
        resposta_api = resposta_api.json()
        shared_parameters['resposta_api'] = resposta_api
        shared_parameters['user_name']  = name
        shared_parameters['alcohol']  = alcohol
        shared_parameters['gasoline']  = gasoline
        
        # Testes das sáidas da api e dicionário
        print(resposta_api)
        print(shared_parameters)
        
        # Redirecione para a rota de entrega
        return redirect('/delivery')
        
    else:
        # Houve um erro na requisição
        print(f"Erro na consulta à API: {resposta_api.status_code}")
        
        # Retornar mensagem de erro (opcional)
        return jsonify({"error": "Falha na consulta à API"})

    
# Delivers results in table: delivery
@app.route("/delivery", methods=["GET", "POST"])
def delivery():
    try:
        connect = sqlite3.connect('C:/Users/prado/final_project_cs50/public/db/my_database.db')
        cursor = connect.cursor()
        
        # Extrair a chave dinamicamente
        chave_dinamica = list(shared_parameters['resposta_api'].keys())[0]
        
        name = shared_parameters['user_name']
        selectBrand = shared_parameters['resposta_api'][chave_dinamica]['Marca']
        selectModel = shared_parameters['resposta_api'][chave_dinamica]['Modelo']
        selectMotor = shared_parameters['resposta_api'][chave_dinamica]['Motor']
        alcohol = shared_parameters['alcohol']
        gasoline = shared_parameters['gasoline']
        
        # Valor a ser calculado pela função do main_application.py
        shared_parameters['advantage'] = 'vantagem'
        
        # Inserindo os dados no banco
        valores_name = (name, selectBrand, selectModel, selectMotor,)
        cursor.execute("INSERT INTO name (user_name, car_brand, model, motor) VALUES (?, ?, ?, ?)", valores_name)
        name_id = cursor.lastrowid  # Obtendo o último id inserido
        
        valores_advantage = (alcohol, gasoline, 'vantagem', name_id)
        cursor.execute("INSERT INTO advantage (alcohol_value, gasoline_value, advantage, id_name) VALUES (?, ?, ?, ?)", valores_advantage)
        
        connect.commit()
        
        # Selecionar dados das tabelas name e advantage e carregar na página
        cursor.execute("""
        SELECT name.user_name, name.car_brand, name.model, name.motor, 
        advantage.alcohol_value, advantage.gasoline_value, advantage.advantage 
        FROM name
        INNER JOIN advantage ON name.id = advantage.id_name
        """)
        
        linhas = cursor.fetchall()
        
    except sqlite3.Error as e:
        # Log de erro para depuração
        app.logger.error(f"Erro ao acessar o banco de dados: {e}")
        return "Erro ao acessar o banco de dados", 500

    finally:
        connect.close()

    return render_template('delivery.html', linhas=linhas)
    
#  Run our page
if __name__ == "__main__":
    app.run(debug=True)