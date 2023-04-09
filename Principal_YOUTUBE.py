from pytube import YouTube
import tkinter as tk
from tkinter import filedialog, Menu


class YouTube_v3:

    def __init__(self):
        # MENU
        self.janela_principal_YT = tk.Tk()
       
        tk.mainloop()

    def nada_fazer(self):
        print('teste')

    def abrir(self):
        print(filedialog.askopenfilename(initialdir='C:/', title='Abrir Arquivo', filetypes=('Todos arquivos', '*.py')))

    def add_link(self):
        janela_add_link = tk.Tk()
        frame_1 = tk.Frame(janela_add_link)
        frame_1.pack(fill=tk.Y)
        frame_2 = tk.Frame(janela_add_link)
        frame_2.pack(fill=tk.Y)
        label_txt_1 = tk.Label(frame_1, text='Adicione o link ao lado... ==>', bd=1, padx=5, pady=5)
        label_txt_1.pack(side='left')
        caixa_txt_1 = tk.Entry(frame_1, textvariable='Caixa de texto', bd=1)
        caixa_txt_1.pack(anchor='center')
        botao_add_link = tk.Button(frame_2, bd=4, width=10, height=1, padx=3, pady=3, relief='groove', cursor='watch')
        botao_add_link.pack(anchor='center')
        tk.mainloop()


iniciando = YouTube_v3()
