from pytube import YouTube
import tkinter as tk
from tkinter import *


class YouTube_v3:
    def __init__(self):
        self.janela_principal_YT = tk.Tk()

        self.barra_menu = Menu(self.janela_principal_YT)
        self.arq_menu = Menu(self.barra_menu, tearoff=0)
        self.arq_menu.add_command(label='Novo', command=self.nada_fazer)
        self.arq_menu.add_command(label='Abrir', command=self.nada_fazer)
        self.arq_menu.add_command(label='Salvar', command=self.nada_fazer)
        self.arq_menu.add_command(label='Salvar como', command=self.nada_fazer)
        self.arq_menu.add_command(label='Sair', command=self.nada_fazer)

        self.janela_principal_YT.config(menu=self.barra_menu)
        tk.mainloop()

    def nada_fazer(self):
        novo_arq = Toplevel(self.janela_principal_YT)
        botao_menu = Button(novo_arq, text="Botão fazer nada")
        botao_menu.pack()


iniciando = YouTube_v3()
