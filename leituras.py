import mysql.connector
import json
from datetime import datetime
import os

conexao = mysql.connector.connect(
    host="localhost",
    user="aluno",
    password="1234",
    database="monitoramento"
)

cursor = conexao.cursor()

def classificar(valor):
    if valor <= 70:
        return "NORMAL"
    elif valor <= 90:
        return "ALERTA"
    else:
        return "CRITICO"


def registrar_leitura():
    cursor.execute("SELECT * FROM sensores")
    print("\nSensores disponíveis:")
    for s in cursor.fetchall():
        print(s)

    valor = float(input("Temperatura: "))
    id_sensor = input("ID do sensor: ")

    cursor.execute(
        "INSERT INTO leituras (valor, id_sensor) VALUES (%s, %s)",
        (valor, id_sensor)
    )
    conexao.commit()

    id_leitura = cursor.lastrowid
    nivel = classificar(valor)

    cursor.execute(
        "INSERT INTO alertas (nivel, id_leitura) VALUES (%s, %s)",
        (nivel, id_leitura)
    )
    conexao.commit()

    os.makedirs("../dados_json", exist_ok=True)

    dados = {
        "sensor": id_sensor,
        "valor": valor,
        "nivel": nivel,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open("../dados_json/leituras.json", "a") as f:
        json.dump(dados, f)
        f.write("\n")

    print(f"Leitura registrada! Status: {nivel}")


registrar_leitura()