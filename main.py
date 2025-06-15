import tkinter as tk
from tkinter import ttk, messagebox
from bson.objectid import ObjectId
from pymongo import MongoClient

class GerenciadorTarefasApp:
    def __init__(self, janela):
        self.janela = janela

        self.janela.title("Gerenciador de Tarefas")

        self.janela.geometry("950x700")

        self.janela.configure(bg="#19131d")

        self.cliente = MongoClient("mongodb://localhost:27017")

        self.bd = self.cliente["gerenciador_tarefas_db"]

        self.colecao = self.bd["tarefas"]

        estilo = ttk.Style()

        estilo.theme_use('default')

        estilo.configure("Treeview", background = "ffffff", foreground = "black", rowheight = 25, fielbackground = "ffffff", font = ("Arial", 11))

        estilo.configure("Treeview.Heading", font = ("Arial", 12, "bold"))

        estilo.map("Treeview", background = [("selected", "black")], foreground = [("selected", "white")])

        quadro_entrada = tk.Frame(self.janela, bg = "#A09DB1")

        quadro_entrada.pack(pady = 10, padx = 10, fill = "x")

        rotulo_titulo = tk.Label(quadro_entrada, text = "Titulo da Tarefa", font = ("Arial", 17), bg = "#f0f0f0")

        rotulo_titulo.grid(row = 0, column = 0, sticky = 'e', padx = 5, pady = 5)

        self.entrada_titulo = tk.Entry(quadro_entrada, width = 55, font = ("Arial", 15))

        self.entrada_titulo.grid(row = 0, column = 1, columnspan = 3, sticky = 'w', padx = 5, pady = 5)

        rotulo_descricao = tk.Label(quadro_entrada, text = "Descrição da Tarefa", font = ("Arial", 18), bg = "#f1f1f1") # o que está sendo escrito no quadro, texto

        rotulo_descricao.grid(row = 1, column = 0, sticky = 'ne', padx = 5, pady = 5)

        self.rotulo_texto_descricao = tk.Text(quadro_entrada, width = 55, height = 5, font = ("Arial", 12)) # style do campo do input

        self.rotulo_texto_descricao.grid(row = 1, column = 1, sticky = 'w', padx = 5, pady = 5) # adicionando o input na tela

        rotulo_status = tk.Label(quadro_entrada, text = "Status", font = ("Arial", 12), bg = "#f0f0f0")

        rotulo_status.grid(row = 2, column = 0, sticky = 'we', padx = 5, pady = 5)

        self.var_status = tk.StringVar()

        self.combo_status = ttk.Combobox(quadro_entrada, textvariable = self.var_status, values = ["Pendente", "Concluida"], state = "readonly", font = ('Arial', 11))

        self.combo_status.grid(row = 2, column = 1, padx = 5, pady = 5)

        self.combo_status.current(0)

        quadro_botoes = tk.Frame(self.janela, bg = "#f0f0f0")

        quadro_botoes.pack(pady = 10)

        botao_adicionar = tk.Button(quadro_botoes, text = "Adicionar Tarefa", command = self.adicionar_tarefa, bg = "#a5d6a7", font = ("Arial", 11, "bold"), width = 18)

        botao_adicionar.grid(row = 0, column = 0, padx = 10, pady = 5)

    def adicionar_tarefa(self):
        print("...")


janela_principal = tk.Tk()

app = GerenciadorTarefasApp(janela_principal)

janela_principal.mainloop()