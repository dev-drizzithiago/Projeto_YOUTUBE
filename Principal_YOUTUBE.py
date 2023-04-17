from pytube import YouTube
import tkinter as tk
from tkinter import messagebox, Tk
from tkinter.ttk import *
import mysql.connector as db
import sqlite3


def janela_principal():
    fonte_Times = ('Times new raman', 14)

    class YouTube_v3:
        def __init__(self):
            # JANELA DE LOGIN
            self.largura = str(600)
            self.altura = str(250)
            self.janela_principal_YT = tk.Tk()
            self.janela_principal_YT.focus_displayof()
            self.janela_principal_YT.geometry('300x200')
            self.janela_principal_YT.title('DownTube')
            self.frame_1 = tk.Frame(self.janela_principal_YT, width=20, height=20, pady=10, padx=10)
            self.frame_1.pack(fill=tk.Y)
            self.frame_2 = tk.Frame(self.janela_principal_YT, width=20, height=20, pady=10, padx=10)
            self.frame_2.pack(fill=tk.Y)
            self.frame_3 = tk.Frame(self.janela_principal_YT, width=20, height=20, pady=10, padx=10)
            self.frame_3.pack(anchor='se')

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

            self.sair_janela = tk.Button(self.frame_3, text='Sair', width=5, height=1, relief='ridge',
                                         pady=5, padx=5, command=self.janela_principal_YT.destroy)
            self.sair_janela.pack(side='right')

            tk.mainloop()

        def banco_dados(self):
            usuario = self.login_caixa_txt.get()
            senha = self.pass_caixa_txt.get()
            try:
                self.conexao_banco = db.connect(host='localhost',
                                                user=usuario,
                                                password=senha,
                                                database='drizzithiago_sql')
                print('AVISO!', 'Abrindo o programa \n'
                                'Aperte "ok" para continuar!')
                self.janela_principal_YT.destroy()
                self.janela_menu_tk()
            except db.Error as erro:
                messagebox.showerror('AVISO', F' ==> {erro}')
                resp = messagebox.askyesno('ERRO!', 'Deseja continuar??')
                if not resp:
                    messagebox.showwarning('', 'Seu programa não vai funcionar \nsem um banco de dados conectado')
                    self.janela_principal_YT.destroy()

        # JANELA DE MENU
        def janela_menu_tk(self):
            self.janela_menu = tk.Tk()
            self.janela_menu.title('Menu')
            self.frame_menu_1 = tk.Frame(self.janela_menu, padx=5, pady=5)
            self.frame_menu_1.pack(fill=tk.Y)
            self.frame_menu_2 = tk.Frame(self.janela_menu, padx=5, pady=5)
            self.frame_menu_2.pack(fill=tk.Y, expand='yes')

            self.label_frame_1 = tk.LabelFrame(self.janela_menu)

            self.opcao_menu = tk.IntVar()
            self.opcao_menu.set(int)

            self.label_principal = tk.Label(self.frame_menu_1, text='Escolha uma opção', padx=2, pady=2)
            self.label_principal.pack(anchor='center')

            self.opcao_1 = tk.Radiobutton(self.frame_menu_1, text='Adicionar link do YouTube', padx=5, pady=5,
                                          variable=self.opcao_menu, value=1)
            self.opcao_1.pack(side='left')

            self.opcao_2 = tk.Radiobutton(self.frame_menu_1, text='Listar os links', padx=5, pady=5,
                                          variable=self.opcao_menu, value=2)
            self.opcao_2.pack(side='left')

            self.botao_enter_menu = tk.Button(self.frame_menu_2, text='Adicionar um link', width=30, height=2,
                                              padx=2, pady=2, command=self.opcao_menu_op)
            self.botao_enter_menu.pack(anchor='center')
            self.botao_fechar = tk.Button(self.frame_menu_2, text='Sair do programa', width=30, height=2,
                                          padx=2, pady=2, command=self.janela_menu.destroy)
            self.botao_fechar.pack(side='right')

        def janela_add_lnk_tk(self):

            # JANELA ADD_LINK
            self.janela_menu.destroy()
            self.janela_add_link = tk.Tk()
            self.janela_add_link.geometry(self.largura + 'x' + self.altura)
            self.janela_add_link.title('Adicionando um LINK')

            # FRAME
            self.frame_1 = tk.Frame(self.janela_add_link, padx=5, pady=5)
            self.frame_1.pack(fill=tk.Y)
            self.frame_2 = tk.Frame(self.janela_add_link, padx=5, pady=5)
            self.frame_2.pack(fill=tk.Y)

            # LABEL
            self.label_txt_1 = tk.Label(self.frame_1, text='Adicione o link', bd=3, padx=10, pady=10)
            self.label_txt_1.pack(side='top')
            self.caixa_txt_1 = tk.Entry(self.frame_1, bd=3, width=100)
            self.caixa_txt_1.pack(anchor='center')

            # StringVar
            self.titulo_inf = tk.StringVar()

            # LABEL
            self.label_frame_2 = tk.LabelFrame(self.janela_add_link, text='Titulo Adicionado')
            self.label_frame_2.pack(anchor='center')

            # bOTÕES
            self.label_add = tk.Label(self.janela_add_link, textvariable=self.titulo_inf, bd=2, anchor='center',
                                      justify='center', relief='groove', width=100, height=3, padx=3, pady=3)
            self.label_add.pack(anchor='s')
            self.botao_add_link = tk.Button(self.frame_2, text='Adicionar', bd=4, width=10, height=1, padx=3, pady=3,
                                            relief='groove', command=self.add_link_db)
            self.botao_add_link.pack(anchor='center')
            self.botao_voltar = tk.Button(self.frame_2, text='Voltar', bd=4, width=10, height=1, pady=3, padx=3,
                                          relief='groove', command=self.voltar_menu)
            self.botao_voltar.pack(anchor='w')
            self.botao_fechar = tk.Button(self.frame_2, text='Sair', bd=4, width=10, height=1, pady=3, padx=3,
                                          relief='groove', command=self.janela_add_link.destroy)
            self.botao_fechar.pack(anchor='se')

        def janela_view_lnks_tk(self):

            # JANELA PRINCIPAL
            self.janela_view_link = tk.Tk()
            self.janela_view_link.title('VIEW MENU')
            self.janela_view_link.geometry('900x600')
            self.janela_view_link.configure(padx=10, pady=10, bg='#B0E0E6')

            # FRAME_VIEW
            self.frame_view_1 = tk.Frame(self.janela_view_link, bd=5, bg='#7FFFD4',
                                         width=200, height=100, padx=5, pady=5)
            self.frame_view_1.pack(anchor='n')

            self.frame_view_2 = tk.Frame(self.janela_view_link, bd=5, bg='#F4A460',
                                         width=200, height=100, padx=5, pady=5)
            self.frame_view_2.pack(anchor='center')

            self.frame_view_3 = tk.Frame(self.janela_view_link, bd=5, bg='#F0E68C',
                                         width=200, height=100, padx=5, pady=5)
            self.frame_view_3.pack(anchor='s')

            self.frame_view_4 = tk.Frame(self.janela_view_link, bd=5, bg='#F0E68C',
                                         width=200, height=100, padx=5, pady=5)
            self.frame_view_4.pack(anchor='s')

            # StringVar
            # self.var_view = tk.StringVar(value=dir())
            self.var_lista = tk.StringVar()

            # LABEL
            self.label_view_1 = tk.Label(self.frame_view_1, text='Escolha um titulo', font=fonte_Times, padx=10,
                                         pady=10)
            self.label_view_1.pack(anchor='sw')

            self.label_mostrar_selecionado = tk.Label(self.frame_view_4, width=100, height=20)
            self.label_mostrar_selecionado.pack(anchor='s')

            # LISTBOX
            self.lista_titulos = tk.Listbox(self.frame_view_2, bg='#FFDEAD', selectmode='extended',
                                            width=100, height=20)
            self.lista_titulos.pack(padx=10, pady=10, expand='YES', anchor='center')
            # self.lista_titulos.bind('<<ListBoxSelect>')

            # BOTÕES
            self.botao_downloads = tk.Button(self.frame_view_3, text='Downloads', width=10, padx=5, pady=5,
                                             command=self.downloads_yt)
            self.botao_downloads.pack(side='right')
            self.botao_atualizar = tk.Button(self.frame_view_3, text='Atualizar', width=10, padx=5, pady=5,
                                             command=self.listagem_arq_bd_view)
            self.botao_atualizar.pack(side='right')
            self.botao_limpar = tk.Button(self.frame_view_3, text='Limpar', width=10, padx=5, pady=5,
                                          command=self.limpar_caixa_lista_links)
            self.botao_limpar.pack(side='right')
            self.listagem_arq_bd_view()

        def listagem_arq_bd_view(self):
            # BUSCANDO AS INFORMAÇÕES NO BANCO DE DADOS
            self.bd_view = self.conexao_banco.cursor()  # Conecta com o bando de dados.
            self.comando_sql = 'SELECT * FROM youtube'  # Comando para listar os arquivos no bd
            self.bd_view.execute(self.comando_sql)  # Executando o comando
            self.titulos = list()  # Cria uma lista para colocar os dados.
            for id_link, link_yt, titulos_yt in self.bd_view:
                self.titulos.append(titulos_yt)
            self.limpar_caixa_lista_links()
            # LISTANDO COM OBJETO 'tk.ListBox'
            for lista_titulos_bd in range(len(self.titulos)):
                self.lista_titulos.insert('end', self.titulos[lista_titulos_bd])
                self.lista_titulos.itemconfig(lista_titulos_bd, bg="#DEB887")

        # Função responsável por adicionar o link no banco de dados.
        def add_link_db(self):
            link_yt = str([self.caixa_txt_1.get()])  # Pega o link na caixa de texto e coloca em numa variável.
            titulo_yt_lnk = YouTube(link_yt).title  # Prepara o link e apenas o titulo é adiciona na variável.
            self.titulo_inf.set(f'Vídeo adicionado: \n{titulo_yt_lnk}')  # Notifica que o link foi adicionando.
            cursor = self.conexao_banco.cursor()  # Busca a conexão com o DB e joga instruções numa variável.
            self.limpar_caixa_addlink()  # Limpa a caixa de texto para poder adicionar outro link
            try:
                # Comando em SQL para adicionar no DB
                comando_SQL = "INSERT INTO youtube (" \
                              "link_youtube, titulo_yt) " \
                              "VALUES (%s, %s)"
                valores_sql_lnk = (link_yt, titulo_yt_lnk)  # atribui os valores na variável
                cursor.execute(comando_SQL, valores_sql_lnk)  # Executa o comando e adicionar literalmente no db
            except db.Error as falha:
                messagebox.showerror('AVISO', f'Ocorreu um erro ao adicionar o link \n'
                                              f'{falha}')

        def barra_progresso(self):
            self.progresso_wd = tk.Tk()
            self.progresso_wd.geometry('10x10')

        def opcao_menu_op(self):
            opcao = self.opcao_menu.get()
            if opcao == 1:
                self.janela_add_lnk_tk()
            elif opcao == 2:
                self.janela_menu.destroy()
                self.janela_view_lnks_tk()

        def limpar_caixa_addlink(self):
            self.caixa_txt_1.delete('0', 'end')

        def limpar_caixa_lista_links(self):
            self.lista_titulos.delete('0', 'end')

        def voltar_menu(self):
            self.janela_add_link.destroy()
            self.janela_menu_tk()

        def downloads_yt(self):
            links_lista_1 = []
            selecao_titulo = self.lista_titulos.curselection()
            for titulo_link in selecao_titulo:
                titulo_escolhido = self.lista_titulos.get(titulo_link)
                links_lista_1.append(titulo_escolhido)
            for dados_down in links_lista_1:
                titulo_down = str(dados_down)
                cursor_down = self.conexao_banco.cursor()
                comando_down_sql = str("SELECT * FROM youtube "
                                       "WHERE titulo_yt = " + "'" + titulo_down + "%'")
                cursor_down.execute(comando_down_sql)
                for id, link, titulo in cursor_down:
                    print(link)

    iniciando = YouTube_v3()


janela_principal()
