import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="aluno",
    password="1234",
    database="monitoramento"
)

print("Conectado com sucesso!")