import sqlite3
banco = sqlite3.connect("database.db")
cursor = banco.cursor()
# para escrever em sql.
#cursor.execute("CREATE TABLE cliente(nome text, idade integer, sext text)")
#inserir dados
cursor.execute("INSERT INTO cliente VALUES('Cynhtia', 29, 'f'), ('pedro', 20,'m')")
banco.commit() #confirmar alterações no banco de dados
cursor.execute("Select * from cliente")
print(cursor.fetchall()) #retonar todos os registros
cursor.close()
banco.close()