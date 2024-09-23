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
        self.lnome = tk.Label(self.janela, text="Nome:")
        self.lnome.pack()
        self.entrynome = tk.Entry(self.janela)
        self.entrynome.pack()
        self.lpreco = tk.Label(self.janela, text="Preço:")
        self.lpreco.pack()
        self.entrypreco = tk.Entry(self.janela)
        self.entrypreco.pack()


janela = tk.Tk() #criação da janela principal
product_app = PrincipalBD(janela)
#cria uma instancia da classe PrincipalBD, passa como argumento a janela principal
janela.title("Bem Vindo a Aplicação de Banco de Dados")
janela.geometry("900x700")
janela.mainloop()
