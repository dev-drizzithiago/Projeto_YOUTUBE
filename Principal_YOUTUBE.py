from pytube import YouTube
import tkinter as tk
from tkinter import *


class YouTube_v3:
    def __init__(self):
        print('BEM VINDO AO NOVO PROGRAMA!')
        print('Teste o novo programa!')
        self.janela_principal_YT = tk.Tk()

        self.frama_1 = tk.Frame(self.janela_principal_YT)
        self.frama_1.pack()

        self.frama_2 = tk.Frame(self.janela_principal_YT)
        self.frama_2.pack()

        arq_menu = Menu(self.janela_principal_YT)


        tk.mainloop()

iniciando = YouTube_v3()
