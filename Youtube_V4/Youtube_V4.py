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

        """#### Frames Label's diversos"""
        self.frame_label_principal = Labelframe(self.janela_principal, text='YouTube V4')
        self.frame_label_principal.config(height=495, width=895)
        self.frame_label_principal.pack(fill=tk.BOTH, pady=5, padx=5)


        self.caixa_de_entrada_link = Entry(None)



        """#### Declarações de variaveis"""

        self.janela_principal.mainloop()


iniciando_obj = Youtube_v4()
