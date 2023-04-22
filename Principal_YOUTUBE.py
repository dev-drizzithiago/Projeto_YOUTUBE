import mysql.connector
import tkinter as tk
from tkinter import messagebox
import mysql.connector as db
from time import sleep
from pytube import YouTube


def janela_principal():
    fonte_Times = ('Times new raman', 14)

    class YouTube_v3:
        def __init__(self):
            # self.janela_add_lnk_tk()
            # JANELA DE LOGIN
            self.janela_login = tk.Tk()
            self.janela_login.focus_displayof()
            self.janela_login.geometry('400x300')
            self.janela_login.title('DownTube')
            self.janela_login.configure(bg='#C0C0C0')
            self.frame_1 = tk.Frame(self.janela_login, width=20, height=20, pady=10, padx=10, bg='#C0C0C0')
            self.frame_1.pack(fill=tk.Y)
            self.frame_2 = tk.Frame(self.janela_login, width=20, height=20, pady=10, padx=10, bg='#C0C0C0')
            self.frame_2.pack(fill=tk.Y)
            self.frame_3 = tk.Frame(self.janela_login, width=20, height=20, pady=10, padx=10, bg='#C0C0C0')
            self.frame_3.pack(fill=tk.Y)
            self.frame_4 = tk.Frame(self.janela_login, width=20, height=20, pady=10, padx=10, bg='#C0C0C0')
            self.frame_4.pack(anchor='se')

            # VARIÁVEIS
            self.opcao_db = tk.IntVar()
            self.opcao_db.set(int)

            # BOTÃO RADIOS
            self.radio_bd_1 = tk.Radiobutton(self.frame_3, text='Banco de Dados externo (db4free.net)', bg='#C0C0C0',
                                             padx=5, pady=5, variable=self.opcao_db, value=1)
            self.radio_bd_1.pack(anchor='w')
            self.radio_bd_2 = tk.Radiobutton(self.frame_3, text='Banco de Dados Interno (localhost)', bg='#C0C0C0',
                                             padx=5, pady=5, variable=self.opcao_db, value=2)
            self.radio_bd_2.pack(anchor='w')

            #  Caixa de Texto
            self.lb_caixa_txt_login = tk.Label(self.frame_1, text='Login', bg='#C0C0C0')
            self.lb_caixa_txt_login.pack(side='top')
            self.login_caixa_txt = tk.Entry(self.frame_1, width=40, bd=4, bg='#C0C0C0')
            self.login_caixa_txt.pack(ancho='center')

            self.lb_caixa_txt_pass = tk.Label(self.frame_1, text='PassWord', bg='#C0C0C0')
            self.lb_caixa_txt_pass.pack(side='top')
            self.pass_caixa_txt = tk.Entry(self.frame_1, width=40, bd=4, show='"', bg='#C0C0C0')
            self.pass_caixa_txt.pack(anchor='center')

            self.botao_entrar = tk.Button(self.frame_2, text='Conectar', width=15, height=1, relief='ridge',
                                          bg='#DCDCDC',
                                          command=self.banco_dados_opcao)
            self.botao_entrar.pack(anchor='center')

            self.sair_janela = tk.Button(self.frame_4, text='Sair', width=5, height=1, relief='ridge', bg='#DCDCDC',
                                         pady=5, padx=5, command=self.janela_login.destroy)
            self.sair_janela.pack(side='right')

            tk.mainloop()

        def banco_dados_opcao(self):
            opcao_bd_enter = self.opcao_db.get()
            if opcao_bd_enter == 1:
                self.servidor_banco_dados = 'db4free.net'
            elif opcao_bd_enter == 2:
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
                self.janela_login.destroy()
                self.janela_principal_tk()
            except db.Error as erro:
                messagebox.showerror('AVISO', F' ==> {erro}')
                resp = messagebox.askyesno('ERRO!', 'Deseja continuar??')
                if not resp:
                    self.janela_login.destroy()

        def janela_add_lnk_tk(self):
            # JANELA ADD_LINK
            self.janela_add_link = tk.Tk()
            self.janela_add_link.geometry('700x200')
            self.janela_add_link.title('Adicione um LINK')
            self.janela_add_link.configure(bg='#A9A9A9')

            # FRAME
            self.frame_1_add_lnk = tk.Frame(self.janela_add_link, padx=5, pady=5, bg='#A9A9A9')
            self.frame_1_add_lnk.pack(fill=tk.Y)
            self.frame_2_add_lnk = tk.Frame(self.janela_add_link, padx=5, pady=5, bg='#A9A9A9')
            self.frame_2_add_lnk.pack(fill=tk.Y)
            self.frame_3_add_lnk = tk.Frame(self.janela_add_link, padx=5, pady=5, bg='#A9A9A9')
            self.frame_3_add_lnk.pack(fill=tk.Y)

            # LABEL_1
            self.label1 = tk.Label(self.frame_1_add_lnk, text='Adicione um link do Youtube', bd=3, padx=10, pady=10,
                                   height=2, bg='#A9A9A9')
            self.label1.pack(fill='both', expand='yes')

            # Caixa de entrada
            self.caixa_txt_1 = tk.Entry(self.frame_1_add_lnk, bd=2, width=100, bg='#A9A9A9')
            self.caixa_txt_1.pack(anchor='center')

            # BOTÕES
            self.botao_add_link = tk.Button(self.frame_3_add_lnk, text='Adicionar', bd=4, width=10, height=1, padx=3,
                                            pady=3,
                                            bg='#D3D3D3', relief='groove', command=self.add_link_db)
            self.botao_add_link.pack(anchor='center')

            self.botao_fechar = tk.Button(self.janela_add_link, text='Sair', bd=4, width=10, height=1, pady=3, padx=3,
                                          bg='#D3D3D3', relief='groove', command=self.janela_add_link.destroy)
            self.botao_fechar.pack(side='right')

            # Função responsável por adicionar o link no banco de dados.

        def add_link_db(self):
            link_yt = str([self.caixa_txt_1.get()])  # Pega o link na caixa de texto e coloca em numa variável.
            titulo_arq = YouTube(link_yt).title  # Prepara o link e apenas o titulo é adiciona na variável.
            cursor = self.conexao_banco.cursor()  # Busca a conexão com o DB e joga instruções numa variável.
            print(titulo_arq)
            try:
                # Comando em SQL para adicionar no DB
                comando_SQL = 'INSERT INTO youtube (' \
                              'link_youtube, titulo_yt) ' \
                              'VALUES (%s, %s)'
                valores_sql_lnk = (link_yt, titulo_arq)  # atribui os valores na variável
                cursor.execute(comando_SQL, valores_sql_lnk)  # Executa o comando e adicionar literalmente no db
                messagebox.showinfo('Aviso!', f'Vídeo adicionado com sucesso! \n{titulo_arq}')
                self.limpar_caixa_addlink()  # Limpa a caixa de texto para poder adicionar outro link
                sleep(0.5)
                self.listagem_arq_bd_view()
            except db.Error as falha:
                messagebox.showerror('AVISO', f'Ocorreu um erro ao adicionar o link \n'
                                              f'{falha}')

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

            self.barra_rolagem = tk.Scrollbar(self.frame_view_2, orient='vertical')
            self.barra_rolagem.pack(side='right', fill=tk.Y)

            self.lista_titulos = tk.Listbox(self.frame_view_2, bg='#FFDEAD', selectmode='extended', width=100,
                                            height=20, yscrollcommand=self.barra_rolagem.set)
            self.lista_titulos.pack(padx=10, pady=10, expand='YES', anchor='center')

            # BOTÕES RADIOS
            self.radio_addLink = tk.Radiobutton(self.frame_view_3, text='Adicionar mais um link', bg='#B0E0E6', bd=5,
                                                width=20, padx=5, pady=5, variable=self.var_opcao, value=1)
            self.radio_addLink.pack(side='left')
            #
            self.radio_princp = tk.Radiobutton(self.frame_view_3, text='Downloads', bg='#B0E0E6', bd=5, width=10,
                                               padx=5, pady=5, variable=self.var_opcao, value=2)
            self.radio_princp.pack(side='left')
            #
            self.radio_atualizar = tk.Radiobutton(self.frame_view_3, text='Atualizar', bg='#B0E0E6', bd=5, width=10,
                                                  padx=5, pady=5, variable=self.var_opcao, value=3)
            self.radio_atualizar.pack(side='left')
            #
            self.radio_limpar = tk.Radiobutton(self.frame_view_3, text='Limpar', bg='#B0E0E6', bd=5, width=10, padx=5,
                                               pady=5, variable=self.var_opcao, value=4)
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
                self.janela_downloads_tk()
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

        def barra_progresso(self):
            self.progresso_wd = tk.Tk()
            self.progresso_wd.geometry('10x10')

        def limpar_caixa_addlink(self):
            self.caixa_txt_1.delete('0', 'end')

        def limpar_caixa_lista_links(self):
            self.lista_titulos.delete('0', 'end')

        def janela_downloads_tk(self):
            self.janela_downloads = tk.Tk()
            self.janela_downloads.geometry('300x300')
            self.janela_downloads.configure(bd=3, pady=5, padx=5)
            self.frame_down_1 = tk.Frame(self.janela_downloads, width=50, height=10, padx=5, pady=5, bd=2, bg='#6495ED')
            self.frame_down_1.pack(anchor='n')
            self.frame_down_2 = tk.Frame(self.janela_downloads, width=50, height=10, padx=5, pady=5, bd=2, bg='#6495ED')
            self.frame_down_2.pack(anchor='center')
            self.frame_down_3 = tk.Frame(self.janela_downloads, width=50, height=10, padx=5, pady=5, bd=2, bg='#6495ED')
            self.frame_down_3.pack(anchor='s')
            self.var_down_opc_radio = tk.IntVar()
            self.var_down_opc_radio.set(int)
            self.label_down_opc = tk.Label(self.frame_down_1, text='Escolha uma opcao')
            self.radio_down_opc_video = tk.Radiobutton(self.frame_down_2, text='Vídeo', pady=5, padx=5, bd=2, bg='#6495ED')
            self.radio_down_opc_video.pack(side='left')

            links_lista_1 = []
            selecao_titulo = self.lista_titulos.curselection()

            for titulo_link in selecao_titulo:
                titulo_escolhido = self.lista_titulos.get(titulo_link)
                links_lista_1.append(titulo_escolhido)

            for dados_down in links_lista_1:
                titulo_down = str(dados_down)
                cursor_down = self.conexao_banco.cursor()
                try:
                    convertendo_down_sql = str("SELECT * FROM youtube "
                                               "WHERE titulo_yt LIKE " + '"' + titulo_down + '"')
                    comando_sql_down = convertendo_down_sql
                    cursor_down.execute(comando_sql_down)
                except mysql.connector.Error as falha:
                    messagebox.showerror('ERROR', f' Ocorreu um erro: \n{falha}')
                for id, link, titulo in cursor_down:
                    self.link_video = str(link)
                    self.titulo_inf = str(titulo)
                try:
                    downloads = YouTube(self.link_video)
                    downloads.streams.filter(adaptive=True).first().download('C:/Youtube/Videos')
                    messagebox.showinfo('Downloads...', f'Download do vídeo \n{self.titulo_inf} \nFoi concluído')
                except:
                    messagebox.showerror('AVISO!!', 'Ocorreu um erro no downloads do video!')

    iniciando = YouTube_v3()


janela_principal()
