from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *
from mysql.connector import errorcode
import mysql.connector as db


def janela_principal():
    class YouTube_v3:
        def __init__(self):
            # MENU
            self.janela_principal_YT = tk.Tk()
            self.frame_1 = tk.Frame(self.janela_principal_YT, width=20, height=20, pady=10, padx=10)
            self.frame_1.pack(fill=tk.Y)
            self.frame_2 = tk.Frame(self.janela_principal_YT, width=20, height=20, pady=10, padx=10)
            self.frame_2.pack(fill=tk.Y)

            self.lb_caixa_txt_login = tk.Label(self.frame_1, text='Login')
            self.lb_caixa_txt_login.pack(side='top')
            self.login_caixa_txt = tk.Entry(self.frame_1, width=40, bd=4)
            self.login_caixa_txt.pack(ancho='center')

            self.lb_caixa_txt_pass = tk.Label(self.frame_1, text='PassWord')
            self.lb_caixa_txt_pass.pack(side='top')
            self.pass_caixa_txt = tk.Entry(self.frame_1, width=40, bd=4)
            self.pass_caixa_txt.pack(anchor='center')

            self.botao_entrar = tk.Button(self.frame_2, text='Entrar', width=15, height=1, relief='ridge',
                                          command=self.add_link)
            self.botao_entrar.pack(anchor='center')

            self.sair_janela = tk.Button(self.janela_principal_YT, text='Sair', width=5, height=1, command=self.janela_principal_YT.quit)
            self.sair_janela.pack(anchor='se')

            tk.mainloop()

        def add_link(self):
            usuario = self.login_caixa_txt.get()
            senha = self.pass_caixa_txt.get()
            try:
                self.conexao_banco = db.connect(host='db4free.net',
                                           user=usuario,
                                           password=senha,
                                           database='drizzithiago_sql')
                messagebox.showinfo('AVISO!', 'Abrindo o programa \n'
                                              'Aperte "ok" para continuar!')
                self.janela_principal_YT.destroy()

                janela_add_link = tk.Tk()
                frame_1 = tk.Frame(janela_add_link, width=20, height=20, padx=5, pady=5)
                frame_1.pack(fill=tk.Y)
                frame_2 = tk.Frame(janela_add_link, width=20, height=20, padx=5, pady=5)
                frame_2.pack(fill=tk.Y)

                label_txt_1 = tk.Label(frame_1, text='Adicione o link', bd=3, padx=10, pady=10)
                label_txt_1.pack(side='top')
                caixa_txt_1 = tk.Entry(frame_1, textvariable='Caixa de texto', bd=1)
                caixa_txt_1.pack(anchor='center')

                botao_add_link = tk.Button(frame_2, text='Adicionar', bd=4, width=10, height=1, padx=3, pady=3, relief='groove')
                botao_add_link.pack(anchor='center')
                tk.mainloop()
            except db.Error as erro:
                messagebox.showerror('AVISO', F' ==> {erro}')

        def add_link_(self):
            self.conexao_banco.cursor()
            comando_SQL = "INSERTO INTO youtube (id_link, link_youtube) values " \
                          "default, " 

    iniciando = YouTube_v3()


janela_principal()
