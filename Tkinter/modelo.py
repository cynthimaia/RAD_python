import sqlite3
class AppBD():
    def __init__(self):
        self.create_table() #quando a classe é instanciada, cria a tabela no banco de dados
    def abrirConexao(self):
        try:
            self.connection = sqlite3.connect('database.db')
            #abre conexão
        except sqlite3.Error as error:
            print("Falha ao se conectar ao banco de dados", error)
    def create_table(self):
        self.abrirConexao()
        create_table_query = """CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_query)
        except sqlite3.Error as error:
            print("Falha ao criar tabela", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conesão com o sqlite foi fechada!")
    def inserirDados(self, name, price):
        self.abrirConexao()
        insert_query = """INSERT INTO products(name,price) VALUES (?,?)"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_query,(name,price))
            self.connection.commit()
            print("Produto inserido com sucesso!")
        except sqlite3.Error as error:
            print('Falha ao inserir dados', error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o slite foi fechada!")
    def select_all_products(self):
        self.abrirConexao()
        select_query = "SELECT * FROM products"
        products = []
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_query)
            products = cursor.fetchall() #recupera os registros no banco
        except sqlite3.Error as error:
            print("Falha ao retornar produtos", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o sqlite foi fechada!")
        return products #retorna a lista de produtos
    
    def update_product(self, product_id,name, price):
        self.abrirConexao()
        update_query = """UPDATE products
        SET name =?, price = ? WHERE id = ?  """
        try:
            cursor = self.connection.cursor()
            cursor.execute(update_query, (name, price,product_id ))
            self.connection.commit()
            print("Produto atualizado com sucesso")
        except sqlite3.Error as error:
            print("Falha ao atualizar o produto", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o sqlite foi fechada.")
    def delete_product(self, product_id):
        self.abrirConexao()
        delete_query = "DELETE FROM products WHERE id = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(delete_query, (product_id,))
            self.connection.commit()
            print('Produto deletado com sucesso')
        except sqlite3.Error as error:
            print('Falha ao deletar produto', error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o sqlite foi fechada!")





