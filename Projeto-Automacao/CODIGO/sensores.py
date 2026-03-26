# sensores.py
import mysql.connector

conexao = mysql.connector.connect(host="localhost", user="aluno", password="1234", database="monitoramento")
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
    cursor.execute("SELECT id_sensor, tipo, id_maquina FROM sensores")
    sensores = cursor.fetchall()
    if not sensores:
        print("Nenhum sensor cadastrado!")
        return
    print("\n=== Sensores Cadastrados ===")
    for s in sensores:
        print(f"ID: {s[0]}, Tipo: {s[1]}, Máquina: {s[2]}")

# Teste 
if __name__ == "__main__":
    while True:
        print("\n1 - Cadastrar sensor")
        print("2 - Listar sensores")
        print("0 - Sair")
        opc = input("Escolha uma opção: ")
        if opc == "1": cadastrar_sensor()
        elif opc == "2": listar_sensores()
        elif opc == "0": break
        else: print("Opção inválida!")