import mysql.connector, json, os
from datetime import datetime

conexao = mysql.connector.connect(host="localhost", user="aluno", password="1234", database="monitoramento")
cursor = conexao.cursor()

def classificar(v): return "NORMAL" if v<=70 else "ALERTA" if v<=90 else "CRITICO"

def registrar_leitura():
    cursor.execute("SELECT id_sensor, tipo FROM sensores")
    sensores = cursor.fetchall()
    if not sensores: return print("Nenhum sensor!")
    for s in sensores: print(f"ID:{s[0]}, Tipo:{s[1]}")
    
    valor = float(input("Temperatura: "))
    id_sensor = int(input("ID sensor: "))
    
    cursor.execute("INSERT INTO leituras (valor,id_sensor,data_hora) VALUES (%s,%s,%s)", (valor,id_sensor,datetime.now()))
    conexao.commit()
    id_leitura = cursor.lastrowid
    
    nivel = classificar(valor)
    cursor.execute("INSERT INTO alertas (nivel,id_leitura) VALUES (%s,%s)", (nivel,id_leitura))
    conexao.commit()
    
    os.makedirs("../dados_json", exist_ok=True)
    with open("../dados_json/leituras.json","a") as f:
        json.dump({"sensor":id_sensor,"valor":valor,"nivel":nivel,"data_hora":datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, f)
        f.write("\n")
    
    print(f"Leitura registrada! Status: {nivel}")

def listar_leituras():
    cursor.execute(
        "SELECT l.id_leitura, l.valor, s.tipo, a.nivel, l.data_hora "
        "FROM leituras l "
        "JOIN sensores s ON l.id_sensor=s.id_sensor "
        "JOIN alertas a ON l.id_leitura=a.id_leitura "
        "ORDER BY l.data_hora DESC"
    )
    for l in cursor.fetchall():
        print(f"ID:{l[0]}, Valor:{l[1]}°C, Sensor:{l[2]}, Status:{l[3]}, Data:{l[4]}")
