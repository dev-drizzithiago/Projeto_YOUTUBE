from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
import mysql.connector as db


def janela_principal():
    class YouTube_v3:
        def __init__(self):
            # JANELA DE LOGIN
            self.janela_principal_YT = tk.Tk()
            self.janela_principal_YT.title('DownTube')
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
                                          command=self.banco_dados)
            self.botao_entrar.pack(anchor='center')

            self.sair_janela = tk.Button(self.janela_principal_YT, text='Sair', width=5, height=1,
                                         command=self.janela_principal_YT.quit)
            self.sair_janela.pack(anchor='se')

            tk.mainloop()

        def banco_dados(self):
            usuario = self.login_caixa_txt.get()
            senha = self.pass_caixa_txt.get()
            try:
                self.conexao_banco = db.connect(host='localhost',
                                                user=usuario,
                                                password=senha,
                                                database='drizzithiago_sql')
                messagebox.showinfo('AVISO!', 'Abrindo o programa \n'
                                              'Aperte "ok" para continuar!')
                self.janela_principal_YT.withdraw()
                self.janela_menu()
            except db.Error as erro:
                messagebox.showerror('AVISO', F' ==> {erro}')

        # JANELA DE MENU
        def janela_menu(self):
            self.janela_menu = tk.Tk()
            self.janela_menu.title('Menu')
            self.janela_menu.geometry('300x150')
            self.frame_menu_1 = tk.Frame(self.janela_menu, width=50, height=50, padx=5, pady=5)
            self.frame_menu_1.pack(fill=tk.Y)
            self.frame_menu_2 = tk.Frame(self.janela_menu, width=50, height=50, padx=5, pady=5)
            self.frame_menu_2.pack(fill=tk.Y)

            self.label_frame_1 = tk.LabelFrame(self.janela_menu)

            self.opcao_menu = tk.IntVar()
            self.opcao_menu.set(1)

            self.label_principal = tk.Label(self.frame_menu_1, text='Escolha uma opção', padx=2, pady=2)
            self.label_principal.pack(anchor='center')
            self.opcao_1 = tk.Radiobutton(self.frame_menu_1, text='Adicionar link do YouTube', padx=5, pady=5,
                                          variable=self.opcao_menu, value=1)
            self.opcao_1.pack(side='left')
            self.opcao_2 = tk.Radiobutton(self.frame_menu_1, text='Listar os links', padx=5, pady=5,
                                          variable=self.opcao_menu, value=2)
            self.opcao_2.pack(side='left')
            self.botao_enter_menu = tk.Button(self.frame_menu_2, text='Adicionar um link', width=20, height=1,
                                              padx=2, pady=2, command=self.valor_opcao_menu)
            self.botao_enter_menu.pack(anchor='center')
            self.botao_fechar = tk.Button(self.frame_menu_2, text='Sair do programa', width=20, height=1,
                                          padx=2, pady=2, command=self.janela_menu.quit)
            self.botao_fechar.pack(side='right')

        def valor_opcao_menu(self):
            opcao = self.opcao_menu.get()
            print(opcao)
            if opcao == 1:
                self.janela_menu.destroy()
                self.janela_add_lnk()
            elif opcao == 2:
                messagebox.askyesno('Janela Menu', 'Deseja sair?')
                if messagebox.askyesno() == 'yes':
                    self.janela_menu.destroy()
            else:
                messagebox.showerror('Mensagem!', 'Opção invalida')

        def janela_add_lnk(self):
            self.janela_add_link = tk.Tk()
            self.janela_add_link.geometry('400x200')
            self.janela_add_link.title('Adicionando um LINK')
            self.frame_1 = tk.Frame(self.janela_add_link, padx=5, pady=5)
            self.frame_1.pack(fill=tk.Y)

            self.frame_2 = tk.Frame(self.janela_add_link, padx=5, pady=5)
            self.frame_2.pack(fill=tk.Y)

            self.label_txt_1 = tk.Label(self.frame_1, text='Adicione o link', bd=3, padx=10, pady=10)
            self.label_txt_1.pack(side='top')
            self.caixa_txt_1 = tk.Entry(self.frame_1, bd=3, width=100)
            self.caixa_txt_1.pack(anchor='center')

            self.botao_add_link = tk.Button(self.frame_2, text='Adicionar', bd=4, width=10, height=1, padx=3, pady=3,
                                            relief='groove', command=self.add_link_db)
            self.botao_add_link.pack(anchor='center')

            self.botao_fechar = tk.Button(self.frame_2, text='Sair', bd=4, width=10, height=1, pady=3, padx=3,
                                          relief='groove', command=self.fechar_programa)
            self.botao_fechar.pack(side='right')

        def add_link_db(self):
            link_yt = [self.caixa_txt_1.get()]
            titulo_yt_lnk = str(YouTube(link_yt).title)
            cursor = self.conexao_banco.cursor()
            self.limpar()
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

        def limpar(self):
            self.caixa_txt_1.delete('0', 'end')

        def fechar_programa(self):
            self.janela_add_link.destroy()
            self.conexao_banco.close()

    iniciando = YouTube_v3()


janela_principal()
