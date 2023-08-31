import csv
import sqlite3

# CSV
def adicionar_registros():
    novos_registros = [
        {"Nome": "João", "Idade": 30, "Cidade": "São Paulo"},
        {"Nome": "Ana", "Idade": 25, "Cidade": "Rio de Janeiro"},
        {"Nome": "Pedro", "Idade": 35, "Cidade": "Salvador"},
        {"Nome": "Mariana", "Idade": 28, "Cidade": "Belo Horizonte"},
        {"Nome": "Lucas", "Idade": 27, "Cidade": "Brasília"},
        {"Nome": "Laura", "Idade": 24, "Cidade": "Porto Alegre"}
    ]

    with open('data.csv', 'a', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=["Nome", "Idade", "Cidade"])
        
        for registro in novos_registros:
            csv_writer.writerow(registro)

# atualizar o registro de Maria no CSV
def atualizar_registro():
    with open('data.csv', 'r') as csv_file:
        registros = list(csv.DictReader(csv_file))
    
    for registro in registros:
        if registro["Nome"] == "Maria":
            registro["Nome"] = "Maria Antônio"
    
    with open('data.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=["Nome", "Idade", "Cidade"])
        csv_writer.writeheader()
        csv_writer.writerows(registros)

# excluir o registro de Miguel no CSV
def excluir_registro():
    with open('data.csv', 'r') as csv_file:
        registros = list(csv.DictReader(csv_file))
    
    registros = [registro for registro in registros if registro["Nome"] != "Miguel"]
    
    with open('data.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=["Nome", "Idade", "Cidade"])
        csv_writer.writeheader()
        csv_writer.writerows(registros)

# conectar ao banco de dados SQLite e adicionar registros
def conectar_banco_de_dados():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        cidade TEXT
    )
    ''')

    novos_registros = [
        ("João", 30, "São Paulo"),
        ("Ana", 25, "Rio de Janeiro"),
        ("Pedro", 35, "Salvador"),
        ("Mariana", 28, "Belo Horizonte"),
        ("Lucas", 27, "Brasília"),
        ("Laura", 24, "Porto Alegre")
    ]

    cursor.executemany('INSERT INTO pessoas (nome, idade, cidade) VALUES (?, ?, ?)', novos_registros)

    conn.commit()
    conn.close()

adicionar_registros()
atualizar_registro()
excluir_registro()
conectar_banco_de_dados()
