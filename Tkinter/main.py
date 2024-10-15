import tkinter as tk
from tkinter import ttk #Treeview
import modelo 
class PrincipalBD():
    def __init__(self, win):
        self.objBD = modelo.AppBD()
        #instancia da classe APPBD para manipular o banco de dados do modelo
        self.janela = win
        #atribui a janela principal ao atributo self.janela
        self.treeProdutos = ttk.Treeview(self.janela, columns=("Código do produto", "nome", "preço"), show="headings")
        #define os titulos das colunas
        self.treeProdutos.heading("Código do produto", text="Código do produto:")
        self.treeProdutos.heading("nome", text="Nome:")
        self.treeProdutos.heading("preço",text= "Preço:")
        self.treeProdutos.pack()

        self.ExibirTela()

        self.lnome = tk.Label(self.janela, text="Nome:")
        self.lnome.pack()
        self.entrynome = tk.Entry(self.janela)
        self.entrynome.pack()
        self.lpreco = tk.Label(self.janela, text="Preço:")
        self.lpreco.pack()
        self.entrypreco = tk.Entry(self.janela)
        self.entrypreco.pack()

        self.btnCadastrar = tk.Button(self.janela, text="Adicionar Produtos", command=self.CadastrarProduto)
        self.btnCadastrar.pack()

        self.btnAtualizar = tk.Button(self.janela, text="Atualizar", command=self.AtualizarProduto)
        self.btnAtualizar.pack()

        self.btnExcluir = tk.Button(self.janela, text="Excluir", command=self.ExcluirProduto)
        self.btnExcluir.pack()

    def ExibirTela(self):
        try:
            self.treeProdutos.delete(*self.treeProdutos.get_children()) 
            products = self.objBD.select_all_products()
            #print(products)
            for product in products:
                print(product)
                self.treeProdutos.insert("", tk.END, values=product)
        except:
            print("Não foi possivel exibir os campos.")

    def CadastrarProduto(self):
        try:
            name = self.entrynome.get()
            price = float(self.entrypreco.get())
            self.objBD.inserirDados(name, price)
            print(f'Produto cadastrado: nome - {name}, preço - {price}')
            #limpar entradas após o cadastro
            self.entrynome.delete(0, tk.END)
            self.entrypreco.delete(0, tk.END)
            self.ExibirTela()
            print('Produto cadastrado com sucesso')
        except:
            print("Não foi possivel fazer o cadastro!")
    def AtualizarProduto(self):
        try:
            select_item = self.treeProdutos.selection()
            print("Select item",select_item )
            if not select_item:
                return
            item = self.treeProdutos.item(select_item)
            print("Item", item)
            product = item['values']
            print(product)
            product_id = product[0]
            nome = self.entrynome.get()
            preco = float(self.entrypreco.get())
            self.objBD.update_product(product_id, nome, preco)
            self.ExibirTela()

            self.entrynome.delete(0, tk.END)
            self.entrypreco.delete(0, tk.END)
        except:
            print('Não foi possivel fazer a atualização')
    def ExcluirProduto(self):
        try:
            selected_item = self.treeProdutos.selection()
            if not selected_item:
                return
            item = self.treeProdutos.item(selected_item)
            print(item)
            product = item['values']
            print(product)
            product_id = product[0]
            self.objBD.delete_product(product_id)
            self.ExibirTela()
            print("Produto excluido com sucesso!")
        except:
            print("Não foi possivel excluir")
    




janela = tk.Tk() #criação da janela principal
product_app = PrincipalBD(janela)
#cria uma instancia da classe PrincipalBD, passa como argumento a janela principal
janela.title("Bem Vindo a Aplicação de Banco de Dados")
janela.geometry("900x700")
janela.mainloop()
