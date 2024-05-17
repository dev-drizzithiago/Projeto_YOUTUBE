from tkinter.messagebox import showwarning
from moviepy.editor import AudioFileClip
from os import makedirs, listdir, path
from threading import Thread
from pytube import YouTube
from tkinter.ttk import *
from pathlib import Path
from re import search
import tkinter as tk








"""Criando pasta home"""
try:
    path_home_ = Path.home()
except:
    showwarning('AVISO!', 'Função para criara caminho da pasta home não foi criada')

"""Declarando as pastas de destino diversas"""
path_musicas = str(Path(path_home_, 'Downloads', 'Youtube_V4', 'Músicas(MP3)'))
path_videos_ = str(Path(path_home_, 'Downloads', 'Youtube_V4', 'Vídeos(MP4)'))
path_arq_yt_ = str(Path(path_home_, 'AppData', 'LocalLow', 'Youtube_V4'))
path_temp_yt = str(Path(path_home_, 'AppData', 'Local', 'Temp'))

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
        self.frame_label_lista_cache = Labelframe(self.frame_label_principal, text='Links Salvos - '
                                                                                   'Selecione um título para baixar')
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
        self.frame_botao_down.place(y=250, x=330)

        self.botao_down_link = Button(self.frame_botao_down, text='Aplicar')
        self.botao_down_link.config(width=30, state=tk.DISABLED)
        self.botao_down_link.pack(anchor='center')
        # --------------------------------------------------------------------------------------------------------------
        """#### Botão limpar tudo"""
        self.frame_lbl_botao_limpar = LabelFrame(self.frame_label_principal, text='Limpar')
        self.frame_lbl_botao_limpar.place(y=250, x=120)

        self.botao_limpar_lista = Button(self.frame_lbl_botao_limpar, text='Aplicar')
        self.botao_limpar_lista.config(width=15)
        self.botao_limpar_lista.config(command=self.limpar_lista_cache)
        self.botao_limpar_lista.pack(anchor='center')
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
        """Barra de progresso"""
        self.frame_lbl_progresso = LabelFrame(self.frame_label_principal, text='Progresso!')
        self.frame_lbl_progresso.config(height=50, width=875)
        self.frame_lbl_progresso.place(y=300, x=5)

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
        self.botao_down_link.config(command=self.thread_download_link)

    def ativar_botao_adicionar_link(self, evento):
        link = self.var_caixa_de_entrada.get()
        if link[:24] == 'https://www.youtube.com/':
            print(f'Validação do link: \n{link}')
            self.botao_add_link.config(state=tk.NORMAL)
            self.botao_add_link.config(command=self.thread_add_link)

    """#### Processo diversos"""
    """### Threads"""
    def thread_add_link(self):
        Thread(target=self.registrando_link_youtube).start()

    def thread_leitura_link(self):
        Thread(target=self.leitura_arq_links).start()

    def thread_download_link(self):
        Thread(target=self.downloads_link).start()

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
        valor_arq_txt_link = open(caminho_arq_txt, 'r')
        self.lendo_arq_txt_lnk = valor_arq_txt_link.readlines()

        for indice, valor_link in enumerate(self.lendo_arq_txt_lnk):
            valor_link = YouTube(valor_link).title
            self.lista_cache_links_add.insert('end', f'{indice + 1} - {valor_link}')

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

    def info_midias(self):
        pass

    def MP3_TO_MP4(self):
        for valor_arq_mp4 in listdir(path_temp_yt):
            if search('mp4', valor_arq_mp4):
                mp4_file = path.join(path_temp_yt, valor_arq_mp4)
                mp3_file = path.join(path_musicas, path.splitext(mp4_file)[0] + '.mp3')

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
                    """#### Processo de downloads do Audio """
                    """### Inicia a barra de progresso"""
                    self.barra_progresso_geral.start()

                    """#### Processo do downloads"""
                    try:
                        downloads = YouTube(dados_selecionados).streams.get_audio_only()
                        downloads.download(path_temp_yt)
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

iniciando_obj = Youtube_v4()

