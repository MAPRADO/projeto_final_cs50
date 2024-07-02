import sqlite3

# Conectando com o banco de dados
connect = sqlite3.connect('my_database.db')

# Criando um cursor
cursor = connect.cursor()

""" # Criar uma tabela chamada 'name'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS name (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT NOT NULL,
        car_brand TEXT NOT NULL,
        model TEXT NOT NULL,
        motor FLOAT NOT NULL
    );
''')

# Inserir alguns dados na tabela name
cursor.execute('INSERT INTO name (user_name, car_brand, model, motor) VALUES (?, ?, ?, ?)', ('Marcio', 'VW', 'UP', 1.0))

# Criar uma tabela chamada 'advantage'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS advantage (
        id_advantage INTEGER PRIMARY KEY AUTOINCREMENT,
        alcohol_value FLOAT NOT NULL,
        gasoline_value FLOAT NOT NULL,
        advantage TEXT NOT NULL,
        id_name INTEGER,
        FOREIGN KEY(id_name) REFERENCES name(id)
    );
''')

# Inserir alguns dados na tabela advantage
cursor.execute('INSERT INTO advantage (alcohol_value, gasoline_value, advantage, id_name) VALUES (?, ?, ?, ?)', (9.3, 13.4, 'gasolina', 1)) """

""" # Loop para deletar as linhas com IDs de 1 a 32

for linhas in range(1, 33):

    # excluindo um registro da tabela
    cursor.execute('''
    DELETE FROM name
    WHERE id = ?
    ''', (linhas,))
    
    # excluindo um registro da tabela
    cursor.execute('''
    DELETE FROM advantage
    WHERE id_advantage = ?
    ''', (linhas,)) """
    
# Deletando os id's 45
cursor.execute('''
    DELETE FROM name
    WHERE id = 33
    ''',)

cursor.execute('''
    DELETE FROM advantage
    WHERE id_advantage = 33
    ''',)


connect.commit()

connect.close()