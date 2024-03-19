import pandas as pd
import numpy
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# The addresses are based on the platform "PythonAnywhere"
# Database address:
# 'https://www.pythonanywhere.com/user/MaPrado/files/home/MaPrado/mysite/car_data_2023_test.xlsx'

# Testing whether the API is live
@app.route('/')
def homepage():
    return 'A API está no ar'

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

    #table = pd.read_excel('https://www.pythonanywhere.com/user/MaPrado/files/home/MaPrado/mysite/car_data_2023_test.xlsx')
    # Excel file that contains the car data. This file is being used as the
    # local data source for the API endpoints.
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