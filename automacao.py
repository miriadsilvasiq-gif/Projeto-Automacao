import sqlite3

conexao = sqlite3.connect('projeto.db')

print ('conexao realizada com sucesso')

cursor = conexao.cursor()