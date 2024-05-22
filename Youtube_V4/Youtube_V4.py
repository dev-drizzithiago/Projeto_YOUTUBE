"""Declarações dos modulos do youtobe"""
from os import makedirs, listdir, path, remove
from tkinter.messagebox import showwarning
from tkinter.messagebox import askquestion
from moviepy.editor import AudioFileClip
from threading import Thread
from pytube import YouTube
from tkinter.ttk import *
from pathlib import Path
from re import search
import tkinter as tk

"""Declaração dos modulos de cadastros"""
from mysql.connector import Connect

"""Criando pasta home"""
try:
    path_home_ = Path.home()
except:
    showwarning('AVISO!', 'Função para criara caminho da pasta home não foi criada')

"""Declarando as pastas de destino diversas"""
path_temp_yt = str(Path(path_home_, 'AppData', 'Local', 'Temp'))
path_arq_yt_ = str(Path(path_home_, 'AppData', 'LocalLow', 'Youtube_V4'))
path_musicas = str(Path(path_home_, 'Downloads', 'Youtube_V4', 'Músicas(MP3)'))
path_videos_ = str(Path(path_home_, 'Downloads', 'Youtube_V4', 'Vídeos(MP4)'))

"""Declarando criação de arquivo"""
registro_yt_txt = '\\Youtube_V4.txt'
caminho_arq_txt = f'{path_arq_yt_}{registro_yt_txt}'

try:
    makedirs(path_musicas)
    makedirs(path_videos_)
    makedirs(path_arq_yt_)
except FileExistsError:
    pass

"""#### Declaração de variaveis"""
linha = '---' * 20


class Youtube_v4:
    def __init__(self):

        """ Janela principal"""
        self.janela_principal = tk.Tk()
        self.janela_principal.geometry('900x500+250+100')
        self.janela_principal.title('Projeto_YouTube_V4')
        self.janela_principal.resizable(0, 0)

        # ##############################################################################################################
        """#### Frames Label's diversos"""
        self.frame_label_principal = Labelframe(self.janela_principal, text='YouTube V4')
        self.frame_label_principal.config(height=495, width=895)
        self.frame_label_principal.pack(fill=tk.BOTH, pady=5, padx=5)
        # --------------------------------------------------------------------------------------------------------------
        """#### Frame Lista cache"""
        self.frame_label_lista_cache = Labelframe(self.frame_label_principal)
        self.frame_label_lista_cache.config(text='Links Salvos - Selecione um título para baixar')
        self.frame_label_lista_cache.place(y=5, x=5)

        # ##############################################################################################################
        """#### Lista dos links que estão salvos no computador"""
        self.var_lista_cache_links_add = tk.StringVar()
        self.lista_cache_links_add = tk.Listbox(self.frame_label_lista_cache, selectmode=tk.SINGLE)
        self.lista_cache_links_add.config(height=10, width=142, justify=tk.LEFT)
        self.lista_cache_links_add.bind('<Button-1>', self.ativar_botao_downloads)
        self.lista_cache_links_add.pack(anchor='center', fill=tk.BOTH, pady=5, padx=5)
        # --------------------------------------------------------------------------------------------------------------
        """#### Barra de rolagem Vertical da lista de cache"""
        self.barra_rolagem_lista_cache_Y = Scrollbar(self.frame_label_principal, orient=tk.VERTICAL)
        self.barra_rolagem_lista_cache_Y.config(command=self.lista_cache_links_add.yview)
        self.lista_cache_links_add.config(yscrollcommand=self.barra_rolagem_lista_cache_Y.set)
        self.barra_rolagem_lista_cache_Y.place(in_=self.lista_cache_links_add)
        self.barra_rolagem_lista_cache_Y.place(relx=1, relheight=1, bordermode='outside')
        # ##############################################################################################################
        """#### Frame caixa de entrada """
        self.frame_label_caixa_entrada = Labelframe(self.janela_principal)
        self.frame_label_caixa_entrada.config(text='Caixa de entrada | Copie um link para adicionar no banco de dados:')
        self.frame_label_caixa_entrada.place(y=220, x=12)
        # --------------------------------------------------------------------------------------------------------------
        self.var_caixa_de_entrada = tk.StringVar()
        self.caixa_de_entrada_link = Entry(self.frame_label_caixa_entrada, textvariable=self.var_caixa_de_entrada)
        self.caixa_de_entrada_link.config(width=143, justify=tk.CENTER)
        self.caixa_de_entrada_link.bind('<KeyRelease>', self.ativar_botao_adicionar_link)
        self.caixa_de_entrada_link.pack(anchor='center', pady=5, padx=5)
        # ##############################################################################################################
        """ Frame Botões"""
        # --------------------------------------------------------------------------------------------------------------
        """#### Botão adicionar """
        self.frame_botao_adicionar = LabelFrame(self.frame_label_principal, text='Adicione o link')
        self.frame_botao_adicionar.place(y=250, x=5)

        self.botao_add_link = Button(self.frame_botao_adicionar, text='Aplicar')
        self.botao_add_link.config(width=15, state=tk.DISABLED)
        self.botao_add_link.pack(anchor='center')
        # --------------------------------------------------------------------------------------------------------------
        """#### Botão downloads """
        self.frame_botao_down = LabelFrame(self.frame_label_principal, text='Baixar o link')
        self.frame_botao_down.place(y=295, x=5)

        self.botao_down_link = Button(self.frame_botao_down, text='Aplicar')
        self.botao_down_link.config(width=50, state=tk.DISABLED)
        self.botao_down_link.config(command=self.thread_download_link)
        self.botao_down_link.pack(anchor='center')
        # --------------------------------------------------------------------------------------------------------------
        """#### Botão limpar tudo"""
        self.frame_lbl_botao_limpar = LabelFrame(self.frame_label_principal, text='Limpar')
        self.frame_lbl_botao_limpar.place(y=250, x=110)

        self.botao_limpar_lista = Button(self.frame_lbl_botao_limpar, text='Aplicar')
        self.botao_limpar_lista.config(width=15, command=self.limpar_lista_cache)
        self.botao_limpar_lista.pack(anchor='center')
        # --------------------------------------------------------------------------------------------------------------
        """#### Botão delete"""
        self.frame_lbl_delete = Labelframe(self.frame_label_principal, text='Deletar: ')
        self.frame_lbl_delete.place(y=250, x=215)

        self.botao_deletar = Button(self.frame_lbl_delete, text='Aplicar')
        self.botao_deletar.config(width=15, command=self.thread_deletar_links)
        self.botao_deletar.config(state=tk.DISABLED)
        self.botao_deletar.pack(anchor='center')
        # --------------------------------------------------------------------------------------------------------------
        """#### Botão radio mp3/mp4"""
        self.frame_lbl_botao_radio_opc_midia = LabelFrame(self.frame_label_principal, text='Escolha uma opção:')
        self.frame_lbl_botao_radio_opc_midia.config(height=44, width=270)
        self.frame_lbl_botao_radio_opc_midia.place(y=250, x=610)

        self.var_radio_ = tk.StringVar()
        self.radio_mp3_midia = Radiobutton(self.frame_lbl_botao_radio_opc_midia, text='Downloads (MP3)')
        self.radio_mp3_midia.config(variable=self.var_radio_, value='MP3')
        self.radio_mp3_midia.place(y=-2, x=5)

        self.radio_mp4_midia = Radiobutton(self.frame_lbl_botao_radio_opc_midia, text='Downloads (MP4)')
        self.radio_mp4_midia.config(variable=self.var_radio_, value='MP4')
        self.radio_mp4_midia.place(y=-2, x=140)
        # --------------------------------------------------------------------------------------------------------------
        """#### Informções de processo"""
        self.frame_lbl_info_link = Labelframe(self.frame_label_principal, text='Informações do processo: ')
        self.frame_lbl_info_link.config(height=65, width=875)
        self.frame_lbl_info_link.place(y=345, x=5)

        self.var_info_lbl_status_processos = tk.StringVar()
        self.lbl_status_processos = Label(self.frame_lbl_info_link, text=self.var_info_lbl_status_processos)
        self.lbl_status_processos.config(text='', justify='center')
        self.lbl_status_processos.place(y=15, x=50)

        # --------------------------------------------------------------------------------------------------------------
        """Barra de progresso"""
        self.frame_lbl_progresso = LabelFrame(self.frame_label_principal, text='Progresso!')
        self.frame_lbl_progresso.config(height=50, width=875)
        self.frame_lbl_progresso.place(y=410, x=5)

        self.barra_progresso_geral = Progressbar(self.frame_lbl_progresso)
        self.barra_progresso_geral.config(mode='determinate', length=868)
        self.barra_progresso_geral.place(y=1, x=1)
        # --------------------------------------------------------------------------------------------------------------

        """#### Declarações de variaveis"""
        self.ativar_ = False

        """#### Chamando a thread para listar os links adicionados"""
        self.thread_leitura_link()

        self.janela_principal.mainloop()

    """#### Eventos diversos """

    def ativar_botao_downloads(self, *args):
        self.botao_down_link.config(state=tk.NORMAL)
        self.botao_deletar.config(state=tk.NORMAL)

    def ativar_botao_adicionar_link(self, *args):
        link = self.var_caixa_de_entrada.get()
        validado_autor = YouTube(link).author
        validado_titulo = YouTube(link).title
        self.lbl_status_processos.config(text=f'Validação do link: [{validado_autor} - {validado_titulo}]')

        if self.quantidade_links == 20:
            showwarning('AVISO!', 'Possui 20 links salvos, delete algum link para adicioar outra. ')
            self.caixa_de_entrada_link.delete(0, 'end')
        else:
            if link[:24] == 'https://www.youtube.com/':
                self.botao_add_link.config(state=tk.NORMAL)
                self.botao_add_link.config(command=self.thread_add_link)
                print('Link validado com sucesso!')

    """#### Processo diversos"""
    """### Threads"""

    def thread_add_link(self):
        Thread(target=self.registrando_link_youtube).start()

    def thread_leitura_link(self):
        Thread(target=self.leitura_arq_links).start()

    def thread_download_link(self):
        Thread(target=self.downloads_link).start()

    def thread_deletar_links(self):
        Thread(target=self.deletar_links).start()

    """### Manipulação do arquivo de texto"""

    def registrando_link_youtube(self):
        """

        :return:
        """
        valor_link_entrada = self.var_caixa_de_entrada.get()
        try:
            registro_lnk_yt = open(caminho_arq_txt, 'a')
            registro_lnk_yt.write(f'{valor_link_entrada}\n')
            print('Arquivo registrado com sucesso!')
            self.botao_add_link.config(state=tk.DISABLED)
            self.caixa_de_entrada_link.delete(0, 'end')
            self.thread_leitura_link()
            registro_lnk_yt.close()

        except FileNotFoundError:
            registro_lnk_yt = open((caminho_arq_txt, 'w'))
            registro_lnk_yt.write(f'{valor_link_entrada}\n')
            print('Arquivo registrado com sucesso!')
            self.botao_add_link.config(state=tk.DISABLED)
            self.caixa_de_entrada_link.delete(0, 'end')
            self.thread_leitura_link()
            registro_lnk_yt.close()

        except FileExistsError:
            pass

    def leitura_arq_links(self):
        """#### A linha descrita abaixo, serve para quando clicar em atualizar, limpa a lista de reponhe os dados"""
        self.lista_cache_links_add.delete(0, 'end')
        try:
            valor_arq_txt_link = open(caminho_arq_txt, 'r')
            self.lendo_arq_txt_lnk = valor_arq_txt_link.readlines()
            valor_arq_txt_link.close()
            self.lbl_status_processos.config(text='Carregando lista de links, aguarde!')
            self.barra_progresso_geral.start()

        except FileNotFoundError:
            self.barra_progresso_geral.stop()
            print('Arquivo não foi encontrado')
            self.lbl_status_processos.config(text='Arquivo que contem os links não foi encontrado. \n'
                                                  'Tente adicionar um link para criar!')

        """#### Variavel server para guardar a quantidade de links que possui guardadas. """
        try:
            self.quantidade_links = len(self.lendo_arq_txt_lnk)
        except:
            print('self.quantidade_links - error')

        try:
            for indice, valor_link in enumerate(self.lendo_arq_txt_lnk):
                autor_link = YouTube(valor_link).author
                titulo_link = YouTube(valor_link).title
                self.lista_cache_links_add.insert('end', f'{indice + 1} - {autor_link} ---- {titulo_link}')
            self.barra_progresso_geral.stop()
            self.lbl_status_processos.config(text='Lista carregada!')
        except:
            print('for indice, valor_link in enumerate(self.lendo_arq_txt_lnk): - error')

        self.frame_lbl_botao_limpar.config(text='Limpar')
        self.botao_limpar_lista.config(command=self.limpar_lista_cache)

    """# Funções básicas"""

    def limpar_lista_cache(self):

        """#### Limpando as variaveis"""
        self.botao_down_link.config(state=tk.DISABLED)
        self.lista_cache_links_add.delete(0, 'end')
        self.caixa_de_entrada_link.delete(0, 'end')
        self.var_radio_.set(0)

        """#### Declarando o botão para atualizar a lista com os novos dados"""
        self.frame_lbl_botao_limpar.config(text='Atualizar')
        self.botao_limpar_lista.config(command=self.thread_leitura_link)

    def deletar_links(self):
        item_selecionado = self.lista_cache_links_add.curselection()
        try:
            abrindo_arq_link = open(caminho_arq_txt, 'r')
            lista_links = abrindo_arq_link.readlines()

            for indice in item_selecionado:
                pass

            resp_del = askquestion('Aviso!', 'Deseja deseja deletar esse link?')

            if resp_del:
                lista_links.pop(indice)
                print('Arquivo deletado com sucesso!')

            atualizado_registro_link_salvos = open(caminho_arq_txt, 'w')

            for valor_lista_atualizado_link in lista_links:
                atualizado_registro_link_salvos = open(caminho_arq_txt, 'a')
                try:
                    atualizado_registro_link_salvos.write(f'{valor_lista_atualizado_link}')
                    atualizado_registro_link_salvos.close()
                except:
                    showwarning('AVISO!', 'Não foi possível atualizar o arquivo')

        except FileNotFoundError:
            showwarning('AVISO!', 'Não existe nenhum arquivo')

        self.thread_leitura_link()

    def MP3_TO_MP4(self):
        for valor_arq_mp4 in listdir(path_temp_yt):
            if search('mp4', valor_arq_mp4):
                mp4_file = path.join(path_temp_yt, valor_arq_mp4)
                mp3_file = path.join(path_musicas, path.splitext(valor_arq_mp4)[0] + '.mp3')
                print(mp3_file)

                """#### transformando o arquivo mp4 em mp3"""
                novo_mp3 = AudioFileClip(mp4_file)
                novo_mp3.write_audiofile(mp3_file)

                """#### Remove o vestigio do arquivo mp4"""
                remove(mp4_file)

    """#### Downloads dos links"""

    def downloads_link(self):
        valor_radio = self.var_radio_.get()
        if len(valor_radio) > 0:

            if valor_radio == 'MP3':
                print()
                print(linha)
                print('Baixando em MP3')
                try:
                    for valor_cursor in self.lista_cache_links_add.curselection():
                        dados_selecionados = self.lendo_arq_txt_lnk[valor_cursor]

                    """#### Criando objeto do youtube"""
                    obj_youtube = YouTube(dados_selecionados)

                    """ Informando na label do programa"""
                    self.lbl_status_processos.config(text=f'Downloads {obj_youtube.author} - {obj_youtube.title} '
                                                          f'em andamento... Aguarde!')
                    """#### Processo de downloads do Audio """
                    """### Inicia a barra de progresso"""
                    self.barra_progresso_geral.start()

                    """#### Processo do downloads"""
                    try:
                        obj_youtube.streams.filter(only_audio=True).first().download(path_temp_yt)
                        """Abre a função para tranformar o arquivo MP4 em MP3"""
                        self.MP3_TO_MP4()

                        """ Finaliza o processo da barra de progresso. """
                        self.barra_progresso_geral.stop()
                        self.barra_progresso_geral.config(value=100)
                        self.lbl_status_processos.config(text=f'Downloads realizado com sucesso!')

                    except:
                        print('Erro ao fazer o downloads!')

                except:
                    showwarning('AVISO!', 'Não existem links para downloads')

            elif valor_radio == 'MP4':
                print()
                print(linha)
                print('Baixando em MP4')
                try:
                    for valor_cursor in self.lista_cache_links_add.curselection():
                        dados_selecionados = self.lendo_arq_txt_lnk[valor_cursor]

                        """#### Processo de downloads de videos """
                        """### Inicia a barra de progresso"""
                        self.barra_progresso_geral.start()

                        """#### Processo do downloads"""
                        try:
                            download = YouTube(dados_selecionados).streams.get_highest_resolution()
                            download.download(path_videos_)
                        except:
                            print('Erro ao fazer o downloads!')

                        """#### Desativa a barra de progresso e deixa com o valor de 100%"""
                        self.barra_progresso_geral.stop()
                        self.barra_progresso_geral.config(value=100)
                        print('Downloads realizado com sucesso!')

                except:
                    showwarning('AVISO!', 'Não existem links para downloads')
        else:
            showwarning('AVISO', 'Selecione uma extensão!')


def __AVISO__():
    local_registro = Path('C:', 'ProgramData', 'Youtube_V4')
    arquivo_de_log = 'log_YT_V4.log'
    arq_info_aviso = f'{local_registro}\\{arquivo_de_log}'

    """#### Criando pasta que vai receber o arquivo de log"""
    try:
        makedirs(local_registro)
    except FileExistsError:
        pass

    """#### Criando arquivo de log"""
    try:
        criando_arquivo_info = open(local_registro, 'a')
        criando_arquivo_info.write(f'{''}')

    except FileExistsError:
        pass
    criando_arquivo_info.close()


def __cadastro__():
    """
    Responsável em coletar informações do usuário. Serve apenas para experiência;
    Vou utilizar uma conexão para bando de dados.
    :return:
    """

    class CadastroRegistro:
        def __init__(self):
            """#### Janela principal"""
            self.janela_registro = tk.Tk()
            self.janela_registro.geometry('500x400+700+300')
            self.janela_registro.title('Registro')
            self.janela_registro.resizable(0, 0)
            # ----------------------------------------------------------------------------------------------------------
            """#### Frame label principal"""
            self.frame_lbl_principal_reg = Labelframe(self.janela_registro, text='Registro:')
            self.frame_lbl_principal_reg.config(height=380, width=480)
            self.frame_lbl_principal_reg.place(y=10, x=10)
            # ##########################################################################################################
            """#### Frame label para Caixa de de nome"""
            self.frame_lbl_box_nome = Labelframe(self.frame_lbl_principal_reg, text='Nome completo')
            self.frame_lbl_box_nome.config(height=60, width=455)
            self.frame_lbl_box_nome.place(y=10, x=10)
            # ----------------------------------------------------------------------------------------------------------
            """#### Caixa de entrada do codigo de ativação"""
            self.var_caixa_enter_nome = tk.StringVar()
            self.caixa_enter_nome = Entry(self.frame_lbl_box_nome, textvariable=self.var_caixa_enter_nome)
            self.caixa_enter_nome.config(width=72)
            self.caixa_enter_nome.place(y=5, x=5)
            # ##########################################################################################################
            """#### Frame Label para caixa de e-mail"""
            self.frame_lbl_box_entrada_mail = Labelframe(self.frame_lbl_principal_reg, text='Insira o seu e-mail aqui')
            self.frame_lbl_box_entrada_mail.config(height=60, width=455)
            self.frame_lbl_box_entrada_mail.place(y=70, x=10)
            # ----------------------------------------------------------------------------------------------------------
            """#### Caixa de entrada de e-mail"""
            self.var_caixa_email = tk.StringVar()
            self.caixa_enter_email = Entry(self.frame_lbl_box_entrada_mail, textvariable=self.var_caixa_email)
            self.caixa_enter_email.config(width=72)
            self.caixa_enter_email.place(y=5, x=5)
            # ##########################################################################################################
            """#### Frame label para Caixa de entrada para o codigo de ativação"""
            self.frame_lbl_box_ativacao = Labelframe(self.frame_lbl_principal_reg, text='Insira o codigo')
            self.frame_lbl_box_ativacao.config(height=60, width=455)
            self.frame_lbl_box_ativacao.place(y=130, x=10)
            # ----------------------------------------------------------------------------------------------------------
            """#### Caixa de entrada do codigo de ativação"""
            self.var_caixa_ativacao = tk.StringVar()
            self.caixa_codigo_ativacao = Entry(self.frame_lbl_box_ativacao, textvariable=self.var_caixa_ativacao)
            self.caixa_codigo_ativacao.config(width=72)
            self.caixa_codigo_ativacao.place(y=5, x=5)
            # ##########################################################################################################
            """#### Frame label para Caixa região"""
            self.frame_lbl_box_ativacao = Labelframe(self.frame_lbl_principal_reg, text='Insira o codigo')
            self.frame_lbl_box_ativacao.config(height=60, width=455)
            self.frame_lbl_box_ativacao.place(y=200, x=10)
            # ----------------------------------------------------------------------------------------------------------
            """#### Caixa de entrada Caixa região"""
            self.var_caixa_regiao = tk.StringVar()
            self.caixa_regiao = Entry(self.frame_lbl_box_ativacao, textvariable=self.var_caixa_regiao)
            self.caixa_regiao.config(width=72)
            self.caixa_regiao.place(y=5, x=5)
            # ##########################################################################################################
            """#### Frame label para os botões"""
            self.frame_lbl_botoes = Labelframe(self.frame_lbl_principal_reg, text='Escolha uma opção: ')
            self.frame_lbl_botoes.config(height=80, width=455)
            self.frame_lbl_botoes.place(y=265, x=10)
            # ----------------------------------------------------------------------------------------------------------
            """#### Botão para registrar"""
            self.botao_adicionar_registro = Button(self.frame_lbl_botoes, text='Registrar')
            self.botao_adicionar_registro.config(width=20, padding=1)
            self.botao_adicionar_registro.place(y=15, x=11)
            # ----------------------------------------------------------------------------------------------------------
            """#### Botão para limpar as caixas"""
            self.botao_limpar_caixa = Button(self.frame_lbl_botoes, text='Limpar')
            self.botao_limpar_caixa.config(width=20, padding=1)
            self.botao_limpar_caixa.place(y=15, x=161)
            # ----------------------------------------------------------------------------------------------------------
            """#### Botão para fechar o programa"""
            self.botao_fechar = Button(self.frame_lbl_botoes, text='Fechar')
            self.botao_fechar.config(width=20, padding=1)
            self.botao_fechar.place(y=15, x=310)

            self.registro_dados()

            """#########"""
            self.janela_registro.mainloop()

        def registro_dados(self):
            """#### Conectando ao bando de dados """
            open_senha = open('C:\\Users\\Thiago\\OneDrive\\Documentos\\Senha_youtube_v4\\senha.txt', 'r')
            senha = open_senha.readline()
            try:
                self.conexao_db = Connect(host='db4free.net',
                                          user='drizzithiago',
                                          password=senha,
                                          database='drizzithiago_sql')
                print('Conexão realizado com sucesso!')
            except:
                print('Não foi possível conectar ao banco de dados')
            nome_teste = 'Thiago'
            email_teste = '@hotmail.com'
            teste_regiao = 'São Paulo'
            self.comando_sql = "INSERT INTO registro_yt_4 (nome_completo, email_cadastro, regiao) " \
                               'VALUES (%s, %s, %s) '
            self.valor_sql = (nome_teste, email_teste, teste_regiao)
            curso_db = self.conexao_db.cursor()
            curso_db.execute(self.comando_sql, self.valor_sql)

    obj_inicio_registro = CadastroRegistro()


# __cadastro__()

iniciando_obj = Youtube_v4()
