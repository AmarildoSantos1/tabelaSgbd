import sqlite3

def exibir_tabela():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM pessoas')
    registros = cursor.fetchall()

    print("ID\tNome\t\tIdade\tCidade")
    print("-" * 40)

    for registro in registros:
        print(f"{registro[0]}\t{registro[1]}\t\t{registro[2]}\t{registro[3]}")

    conn.close()

exibir_tabela()
