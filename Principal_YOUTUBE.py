from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
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
                                          command=self.janela_menu)
            self.botao_entrar.pack(anchor='center')

            self.sair_janela = tk.Button(self.janela_principal_YT, text='Sair', width=5, height=1,
                                         command=self.janela_principal_YT.quit)
            self.sair_janela.pack(anchor='se')

            tk.mainloop()

        def janela_menu(self):
            self.janela_menu = tk.Tk()
            self.frame_menu_1 = tk.Frame(self.janela_menu)
            self.frame_menu_1.pack(fill=tk.Y)
            self.frame_menu_2 = tk.Frame(self.janela_menu)
            self.frame_menu_2.pack(fill=tk.Y)
            self.label_principal = tk.Label(self.frame_menu_1, text='Escolha uma opção')
            self.label_principal.pack(anchor='center')


        def janela_add_lnk(self):
            self.janela_add_link = tk.Tk()
            self.frame_1 = tk.Frame(self.janela_add_link, width=20, height=20, padx=5, pady=5)
            self.frame_1.pack(fill=tk.Y)
            self.frame_2 = tk.Frame(self.janela_add_link, width=20, height=20, padx=5, pady=5)
            self.frame_2.pack(fill=tk.Y)

            self.label_txt_1 = tk.Label(self.frame_1, text='Adicione o link', bd=3, padx=10, pady=10)
            self.label_txt_1.pack(side='top')
            self.caixa_txt_1 = tk.Entry(self.frame_1, textvariable='Caixa de texto', bd=3, width=100)
            self.caixa_txt_1.pack(anchor='center')

            botao_add_link = tk.Button(self.frame_2, text='Adicionar', bd=4, width=10, height=1, padx=3, pady=3,
                                       relief='groove', command=self.add_link_db)
            botao_add_link.pack(anchor='center')
            self.botao_sair = tk.Button(self.frame_2, text='Voltar ao Menu Principal', width=6, height=2, pady=2,
                                        padx=2,
                                        command=self.janela_add_link.destroy)
            self.botao_sair_programa = Button(self.frame_2, text='Sair do Programa')
            self.botao_sair_programa.pack(anchor='SE')


        def add_link(self):
            usuario = self.login_caixa_txt.get()
            senha = self.pass_caixa_txt.get()
            try:
                self.conexao_banco = db.connect(host='localhost',
                                                user=usuario,
                                                password=senha,
                                                database='mercadinho_pinheiro')
                messagebox.showinfo('AVISO!', 'Abrindo o programa \n'
                                              'Aperte "ok" para continuar!')
                self.janela_principal_YT.destroy()
            except db.Error as erro:
                messagebox.showerror('AVISO', F' ==> {erro}')

        def add_link_db(self):
            link_yt = str([self.caixa_txt_1.get()])
            cursor = self.conexao_banco.cursor()
            titulo_yt_lnk = YouTube(link_yt).title
            print(titulo_yt_lnk)
            try:
                comando_SQL = "INSERT INTO youtube (" \
                              "link_youtube, titulo_yt) " \
                              "VALUES (%s, %s) "
                valores_sql_lnk = (link_yt, titulo_yt_lnk)
                cursor.execute(comando_SQL, valores_sql_lnk)
                messagebox.showinfo('AVISO!', f'Foi adicionado o vídeo {titulo_yt_lnk}')
            except db.Error as falha:
                messagebox.showerror('AVISO', f'Ocorreu um erro ao adicionar o link \n'
                                              f'{falha}')

    iniciando = YouTube_v3()


janela_principal()
