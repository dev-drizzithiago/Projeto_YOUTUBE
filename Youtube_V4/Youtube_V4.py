import tkinter as tk
from tkinter.ttk import *
from threading import Thread


class Youtube_v4:
    def __init__(self):

        """ Janela principal"""
        self.janela_principal = tk.Tk()
        self.janela_principal.geometry('900x500+250+100')
        self.janela_principal.title('Projeto_YouTube_V4')
        self.janela_principal.resizable(0,0)



        """#### Declarações de variaveis"""

        self.janela_principal.mainloop()


iniciando_obj = Youtube_v4()
