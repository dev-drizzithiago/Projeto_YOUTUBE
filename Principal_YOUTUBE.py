from pytube import YouTube
import tkinter as tk
from tkinter import filedialog, Menu


class YouTube_v3:

    def __init__(self):
        # MENU
        self.janela_principal_YT = tk.Tk()
        self.barra_menu = Menu(self.janela_principal_YT)
        self.arq_menu = Menu(self.barra_menu, tearoff=0, relief='groove')
        self.arq_menu.add_command(label='Novo', command=self.add_link)
        self.arq_menu.add_command(label='Abrir', command=self.abrir)
        self.arq_menu.add_command(label='Salvar', command=self.nada_fazer)
        self.arq_menu.add_command(label='Salvar como', command=self.nada_fazer)
        self.arq_menu.add_command(label='Fechar', command=self.nada_fazer)

        self.arq_menu.add_separator()
        self.arq_menu.add_command(label='Sair', command=self.janela_principal_YT.quit)
        self.barra_menu.add_cascade(label='Arquivo', menu=self.arq_menu)

        self.edit_menu = Menu(self.barra_menu, tearoff=0)
        self.edit_menu.add_command(label='Desfazer')
        self.edit_menu.add_command(label='Cortar', command=self.nada_fazer)
        self.edit_menu.add_command(label='Copiar', command=self.nada_fazer)
        self.edit_menu.add_command(label='Colar', command=self.nada_fazer)
        self.edit_menu.add_command(label='Delete', command=self.nada_fazer)
        self.edit_menu.add_command(label='Selecionar tudo', command=self.nada_fazer)
        self.barra_menu.add_cascade(label='Editar', menu=self.edit_menu)

        self.ajuda_menu = Menu(self.barra_menu, tearoff=0)
        self.ajuda_menu.add_command(label='Indice de Ajuda', command=self.nada_fazer)
        self.ajuda_menu.add_command(label='Sobre...', command=self.nada_fazer)
        self.barra_menu.add_cascade(label='Ajuda', menu=self.ajuda_menu)

        self.janela_principal_YT.config(menu=self.barra_menu)
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
