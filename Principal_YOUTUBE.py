import mysql.connector
from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import mysql.connector as db


def janela_principal():
    fonte_Times = ('Times new raman', 14)

    class YouTube_v3:
        def __init__(self):
            # JANELA DE LOGIN
            self.largura = str(600)
            self.altura = str(250)
            self.janela_login = tk.Tk()
            self.janela_login.focus_displayof()
            self.janela_login.geometry('400x300')
            self.janela_login.title('DownTube')
            self.janela_login.configure(bg='#B0E0E6')
            self.frame_1 = tk.Frame(self.janela_login, width=20, height=20, pady=10, padx=10,  bg='#B0E0E6')
            self.frame_1.pack(fill=tk.Y)
            self.frame_2 = tk.Frame(self.janela_login, width=20, height=20, pady=10, padx=10,  bg='#B0E0E6')
            self.frame_2.pack(fill=tk.Y)
            self.frame_3 = tk.Frame(self.janela_login, width=20, height=20, pady=10, padx=10,  bg='#B0E0E6')
            self.frame_3.pack(fill=tk.Y)
            self.frame_4 = tk.Frame(self.janela_login, width=20, height=20, pady=10, padx=10,  bg='#B0E0E6')
            self.frame_4.pack(anchor='se')

            # VARIÁVEIS
            self.opcao_db = tk.IntVar()
            self.opcao_db.set(int)

            # BOTÃO RADIOS
            self.radio_bd_1 = tk.Radiobutton(self.frame_3, text='Banco de Dados externo (db4free.net)', bg='#B0E0E6',
                                             padx=5, pady=5, variable=self.opcao_db, value=1)
            self.radio_bd_1.pack(anchor='w')
            self.radio_bd_2 = tk.Radiobutton(self.frame_3, text='Banco de Dados Interno (localhost)', bg='#B0E0E6',
                                             padx=5, pady=5, variable=self.opcao_db, value=2)
            self.radio_bd_2.pack(anchor='w')

            #  Caixa de Texto
            self.lb_caixa_txt_login = tk.Label(self.frame_1, text='Login',  bg='#B0E0E6')
            self.lb_caixa_txt_login.pack(side='top')
            self.login_caixa_txt = tk.Entry(self.frame_1, width=40, bd=4,  bg='#B0E0E6')
            self.login_caixa_txt.pack(ancho='center')

            self.lb_caixa_txt_pass = tk.Label(self.frame_1, text='PassWord',  bg='#B0E0E6')
            self.lb_caixa_txt_pass.pack(side='top')
            self.pass_caixa_txt = tk.Entry(self.frame_1, width=40, bd=4, show='"',  bg='#B0E0E6')
            self.pass_caixa_txt.pack(anchor='center')

            self.botao_entrar = tk.Button(self.frame_2, text='Conectar', width=15, height=1, relief='ridge',
                                          command=self.banco_dados_opcao)
            self.botao_entrar.pack(anchor='center')

            self.sair_janela = tk.Button(self.frame_4, text='Sair', width=5, height=1, relief='ridge', bg='#B0E0E6',
                                         pady=5, padx=5, command=self.janela_login.destroy)
            self.sair_janela.pack(side='right')

            tk.mainloop()

        def banco_dados_opcao(self):
            opcao_bd_enter = self.opcao_db.get()
            if opcao_bd_enter == 1:
                self.servidor_banco_dados = 'db4free.net'
            elif opcao_bd_enter == 2:
                self.servidor_banco_dados = 'localhost'
            elif opcao_bd_enter == 3:
                # print('''Vou fazer o usuario escolher a pasta que ficara o arquivo na extensão de texto''')
                messagebox.showinfo('AVISO!',
                                    'Opção em desenvolvimento \nVocê esta sendo encaminhado para o servidor local!')
                self.servidor_banco_dados = 'localhost'
            else:
                messagebox.showwarning('ERRO', 'Ocorreu um ERRO na seleção da opção')
            usuario = self.login_caixa_txt.get()
            senha = self.pass_caixa_txt.get()
            try:
                self.conexao_banco = db.connect(host=self.servidor_banco_dados,
                                                user=usuario,
                                                password=senha,
                                                database='drizzithiago_sql')
                print('AVISO!', 'Abrindo o programa')
                self.janela_login.destroy()
                self.janela_principal_tk()
            except db.Error as erro:
                messagebox.showerror('AVISO', F' ==> {erro}')
                resp = messagebox.askyesno('ERRO!', 'Deseja continuar??')
                if not resp:
                    self.janela_login.destroy()

        # JANELA DE MENU

        def janela_add_lnk_tk(self):
            # JANELA ADD_LINK
            self.janela_add_link = tk.Tk()
            self.janela_add_link.geometry(self.largura + 'x' + self.altura)
            self.janela_add_link.title('Adicionando um LINK')
            self.janela_add_link.configure(bg='#B0E0E6')

            # FRAME
            self.frame_1 = tk.Frame(self.janela_add_link, padx=5, pady=5, bg='#B0E0E6')
            self.frame_1.pack(fill=tk.Y)
            self.frame_2 = tk.Frame(self.janela_add_link, padx=5, pady=5, bg='#B0E0E6')
            self.frame_2.pack(fill=tk.Y)

            # LABEL
            self.label_txt_1 = tk.Label(self.frame_1, text='Adicione o link', bd=3, padx=10, pady=10, bg='#B0E0E6')
            self.label_txt_1.pack(side='top')
            self.caixa_txt_1 = tk.Entry(self.frame_1, bd=3, width=100, bg='#B0E0E6')
            self.caixa_txt_1.pack(anchor='center')

            # StringVar
            self.titulo_inf = tk.StringVar()  # Responsavel por informar na label o que foi adicionado.

            # LABEL
            self.label_frame_2 = tk.LabelFrame(self.janela_add_link, text='Titulo Adicionado', bg='#B0E0E6')
            self.label_frame_2.pack(anchor='center')

            # bOTÕES
            self.label_add = tk.Label(self.janela_add_link, textvariable=self.titulo_inf, bd=2, anchor='center', bg='#B0E0E6',
                                      justify='center', relief='groove', width=100, height=3, padx=3, pady=3)
            self.label_add.pack(anchor='s')
            self.botao_add_link = tk.Button(self.frame_2, text='Adicionar', bd=4, width=10, height=1, padx=3, pady=3,
                                            bg='#B0E0E6', relief='groove', command=self.add_link_db)
            self.botao_add_link.pack(anchor='center')
            self.botao_fechar = tk.Button(self.frame_2, text='Sair', bd=4, width=10, height=1, pady=3, padx=3,
                                          bg='#B0E0E6', relief='groove', command=self.janela_add_link.destroy)
            self.botao_fechar.pack(anchor='se')

        def janela_principal_tk(self):

            # JANELA PRINCIPAL
            self.janela_view_link = tk.Tk()
            self.janela_view_link.title('VIEW MENU')
            self.janela_view_link.geometry('900x600')
            self.janela_view_link.configure(padx=10, pady=10, bg='#B0E0E6')

            # FRAME_VIEW
            self.frame_view_1 = tk.Frame(self.janela_view_link, bd=5, bg='#B0E0E6', width=200, height=100, padx=5,
                                         pady=5)
            self.frame_view_1.pack(anchor='center')
            self.frame_view_2 = tk.Frame(self.janela_view_link, bd=5, bg='#B0E0E6', width=200, height=100, padx=5,
                                         pady=5)
            self.frame_view_2.pack(anchor='center')
            self.frame_view_3 = tk.Frame(self.janela_view_link, bd=5, bg='#B0E0E6', width=200, height=100, padx=5,
                                         pady=5)
            self.frame_view_3.pack(anchor='center')
            self.frame_view_4 = tk.Frame(self.janela_view_link, bd=5, bg='#B0E0E6', width=200, height=100, padx=5,
                                         pady=5)
            self.frame_view_4.pack(side='bottom')

            # StringVar
            self.var_opcao = tk.IntVar()
            self.var_opcao.set(int)

            # LABEL
            self.label_view_1 = tk.Label(self.frame_view_1, text='Escolha um titulo e selecione uma opção abaixo',
                                         font=fonte_Times, padx=10, pady=10)
            self.label_view_1.pack(side='top')

            # LISTBOX
            self.lista_titulos = tk.Listbox(self.frame_view_2, bg='#FFDEAD', selectmode='extended', width=100,
                                            height=20)
            self.lista_titulos.pack(padx=10, pady=10, expand='YES', anchor='center')

            # BOTÕES RADIOS
            self.radio_addLink = tk.Radiobutton(self.frame_view_3, text='Adicionar mais um link', bg='#B0E0E6', bd=5,
                                                width=20, padx=5, pady=5, variable=self.var_opcao, value=1)
            self.radio_addLink.pack(side='left')

            self.radio_downloads = tk.Radiobutton(self.frame_view_3, text='Downloads', bg='#B0E0E6', bd=5, width=10, padx=5,
                                                  pady=5, variable=self.var_opcao, value=2)
            self.radio_downloads.pack(side='left')

            self.radio_atualizar = tk.Radiobutton(self.frame_view_3, text='Atualizar', bg='#B0E0E6', bd=5,  width=10, padx=5,
                                                  pady=5, variable=self.var_opcao, value=3)
            self.radio_atualizar.pack(side='left')
            self.radio_limpar = tk.Radiobutton(self.frame_view_3, text='Limpar', bg='#B0E0E6', bd=5, width=10, padx=5, pady=5,
                                               variable=self.var_opcao, value=4)
            self.radio_limpar.pack(side='left')

            # Bottão Entrar
            self.botao_enter = tk.Button(self.frame_view_4, text='Entrar', bg='#B0E0E6', bd=5, width=10, pady=5, padx=5,
                                         command=self.opcao_radio)
            self.botao_enter.pack(anchor='center')

            # lISTA OS DADOS QUANDO ABRE A JANELA
            self.listagem_arq_bd_view()

        def opcao_radio(self):
            opcao = self.var_opcao.get()
            if opcao == 1:  # Abrir janela para adicionar links.
                self.janela_add_lnk_tk()
            elif opcao == 2:  # Abre janela de opção para downloads
                self.downloads_yt()
            elif opcao == 3:  # atualiza a caixa do 'ListBox'
                self.listagem_arq_bd_view()
            elif opcao == 4:  # Limpa a caixa do 'ListBox'
                self.limpar_caixa_lista_links()

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
            try:
                self.titulo_yt_lnk = YouTube(link_yt).title  # Prepara o link e apenas o titulo é adiciona na variável.
                self.titulo_inf.set(f'Vídeo adicionado: \n{self.titulo_yt_lnk}')  # Notifica que o link foi adicionando.
            except:
                messagebox.showerror('ERROR', 'Ocorreu um erro ao adicionar um TITULO!')
            cursor = self.conexao_banco.cursor()  # Busca a conexão com o DB e joga instruções numa variável.
            self.limpar_caixa_addlink()  # Limpa a caixa de texto para poder adicionar outro link
            try:
                # Comando em SQL para adicionar no DB
                comando_SQL = 'INSERT INTO youtube (' \
                              'link_youtube, titulo_yt) ' \
                              'VALUES (%s, %s)'
                valores_sql_lnk = (link_yt, self.titulo_yt_lnk)  # atribui os valores na variável
                cursor.execute(comando_SQL, valores_sql_lnk)  # Executa o comando e adicionar literalmente no db
            except db.Error as falha:
                messagebox.showerror('AVISO', f'Ocorreu um erro ao adicionar o link \n'
                                              f'{falha}')

        def barra_progresso(self):
            self.progresso_wd = tk.Tk()
            self.progresso_wd.geometry('10x10')

        def limpar_caixa_addlink(self):
            self.caixa_txt_1.delete('0', 'end')

        def limpar_caixa_lista_links(self):
            self.lista_titulos.delete('0', 'end')

        def downloads_yt(self):
            links_lista_1 = []
            selecao_titulo = self.lista_titulos.curselection()
            for titulo_link in selecao_titulo:
                titulo_escolhido = self.lista_titulos.get(titulo_link)
                links_lista_1.append(titulo_escolhido)
            for dados_down in links_lista_1:
                titulo_down = str(dados_down)
                print(titulo_down)
                cursor_down = self.conexao_banco.cursor()
                try:
                    convertendo_down_sql = str("SELECT * FROM youtube "
                                               "WHERE titulo_yt LIKE " + '"' + titulo_down + '"')
                    comando_sql_down = convertendo_down_sql
                    cursor_down.execute(comando_sql_down)
                except mysql.connector.Error as falha:
                    messagebox.showerror('ERROR', f' Ocorreu um erro: \n{falha}')
                for id, link, titulo in cursor_down:
                    print(link)

    iniciando = YouTube_v3()


janela_principal()
