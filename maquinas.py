import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="aluno",
    password="1234",
    database="monitoramento"
)

cursor = conexao.cursor()

# cadastrar máquina
def cadastrar_maquina():
    nome = input("Nome da máquina: ")
    setor = input("Setor: ")

    cursor.execute(
        "INSERT INTO maquinas (nome, setor) VALUES (%s, %s)",
        (nome, setor)
    )
    conexao.commit()

    print("Máquina cadastrada!")

# listar máquinas
def listar_maquinas():
    cursor.execute("SELECT * FROM maquinas")

    for m in cursor.fetchall():
        print(m)

# menu 
def menu():
    while True:
        print("\n1 - Cadastrar máquina")
        print("2 - Listar máquinas")
        print("3 - Sair")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_maquina()
        elif op == "2":
            listar_maquinas()
        elif op == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


menu()