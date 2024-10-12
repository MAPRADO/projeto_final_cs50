import psycopg2
from psycopg2 import sql

# Criar uma função que conecta ao banco de dados PostgreSQL local
def get_newBank():
    conn = psycopg2.connect(
        dbname="postgres", 
        user="postgres", 
        password="cs50_project", 
        host="localhost", 
        port="5432"
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
conn.close()


# Criar uma função que conecta ao banco PostgreSQL no Supabase
def get_supabase_newBank():
    conn = psycopg2.connect(
        dbname="postgres", 
        user="postgres.hsvhwqwzamqqrujzfyey", 
        password="Shanta%cs50Map", 
        host="aws-0-us-west-1.pooler.supabase.com", 
        port="6543"
    )
    return conn