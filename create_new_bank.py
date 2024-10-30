import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv


# Criar uma função que conecta ao banco PostgreSQL no Supabase
def get_supabase_newBank():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    return conn


""" # Criar uma função que conecta ao banco de dados PostgreSQL local
def get_newBank():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME_LOCAL"), 
        user=os.getenv("DB_USER_LOCAL"), 
        password=os.getenv("DB_PASSWORD_LOCAL"), 
        host=os.getenv("DB_HOST_LOCAL"), 
        port=os.getenv("DB_PORT_LOCAL")
    )
    return conn

conn = get_newBank()  # Obtém a conexão com o banco de dados
cursor = conn.cursor()

# Criar uma tabela chamada 'name'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS name (
        id SERIAL PRIMARY KEY,
        user_name VARCHAR(255) NOT NULL,
        car_brand VARCHAR(255) NOT NULL,
        model VARCHAR(255) NOT NULL,
        motor REAL NOT NULL
    );
''')

# Criar uma tabela chamada 'advantage'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS advantage (
        id_advantage SERIAL PRIMARY KEY,
        alcohol_value REAL NOT NULL,
        gasoline_value REAL NOT NULL,
        advantage VARCHAR(255) NOT NULL,
        id_name SERIAL,
        FOREIGN KEY(id_name) REFERENCES name(id)
    );
''')

# Commit para salvar as mudanças
conn.commit()

# Fechar cursor e conexão
cursor.close()
conn.close() """