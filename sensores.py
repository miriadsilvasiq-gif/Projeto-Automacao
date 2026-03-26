import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="aluno",
    password="1234",
    database="monitoramento"
)

cursor = conexao.cursor()

def cadastrar_sensor():
    tipo = input("Tipo do sensor: ")
    id_maquina = input("ID da máquina: ")

    cursor.execute(
        "INSERT INTO sensores (tipo, id_maquina) VALUES (%s, %s)",
        (tipo, id_maquina)
    )
    conexao.commit()

    print("Sensor cadastrado!")


def listar_sensores():
    cursor.execute("SELECT * FROM sensores")
    for s in cursor.fetchall():
        print(s)


cadastrar_sensor()