import sqlite3
banco = sqlite3.connect("database.db")
banco.execute("PRAGMA foreign_keys=on")
cursor = banco.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Pessoa(cpf INTEGER PRIMARY KEY,
              nome TEXT NOT NULL,
               nascimento DATE NOT NULL,
                oculos BOOLEAN NOT NULL);
''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Marca(
               id INTEGER NOT NULL,
               nome TEXT NOT NULL,
               sigla CHARACTER(2) NOT NULL,
               PRIMARY KEY(id)
               );''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Veiculo(
               placa CHARACTER(7) NOT NULL,
               ano INTEGER NOT NULL,
               cor TEXT NOT NULL,
               proprietario INTEGER NOT NULL,
               marca INTEGER NOT NULL,
               PRIMARY KEY(placa),
               FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
               FOREIGN KEY(marca) REFERENCES Marca(id)
               );
''')
#cursor.execute('''ALTER TABLE Veiculo ADD motor REAL;''')
#insersão de dados - query dinâmicas
comando = '''INSERT INTO Pessoa(cpf,nome, nascimento, oculos) VALUES (?,?,?,?)'''
#delimitador "?"