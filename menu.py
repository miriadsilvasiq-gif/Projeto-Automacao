from maquinas import cadastrar_maquina, listar_maquinas
from sensores import cadastrar_sensor, listar_sensores
from operadores import cadastrar_operador
from leituras import registrar_leitura, listar_leituras

def menu():
    while True:
        print("\n--- SISTEMA INDUSTRIAL ---")
        print("1 - Cadastrar máquina")
        print("2 - Cadastrar sensor")
        print("3 - Cadastrar operador")
        print("4 - Registrar leitura")
        print("5 - Listar máquinas")
        print("6 - Listar sensores")
        print("7 - Listar leituras")
        print("8 - Sair")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_maquina()
        elif op == "2":
            cadastrar_sensor()
        elif op == "3":
            cadastrar_operador()
        elif op == "4":
            registrar_leitura()
        elif op == "5":
            listar_maquinas()
        elif op == "6":
            listar_sensores()
        elif op == "7":
            listar_leituras()
        elif op == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()