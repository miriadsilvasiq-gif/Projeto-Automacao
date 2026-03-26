import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="aluno",
    password="1234",
    database="monitoramento"
)

cursor = conexao.cursor()

def cadastrar_operador():
    nome = input("Nome do operador: ")
    turno = input("Turno: ")

    cursor.execute(
        "INSERT INTO operadores (nome, turno) VALUES (%s, %s)",
        (nome, turno)
    )
    conexao.commit()

    print("Operador cadastrado!")


cadastrar_operador()