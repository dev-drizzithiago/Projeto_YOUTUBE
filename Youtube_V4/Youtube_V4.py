from tkinter.messagebox import showwarning
from threading import Thread
from pytube import YouTube
from tkinter.ttk import *
from pathlib import Path
from os import makedirs
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
        self.frame_label_caixa_entrada = Labelframe(self.janela_principal, text='Caixa de entrada:')
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
        self.frame_botao_down.place(y=250, x=120)

        self.botao_down_link = Button(self.frame_botao_down, text='Aplicar')
        self.botao_down_link.config(width=15, state=tk.DISABLED)
        self.botao_down_link.pack(anchor='center')
        # --------------------------------------------------------------------------------------------------------------
        """#### Botão limpar tudo"""
        frame_lbl_botao_limpar = LabelFrame(self.frame_label_principal, text='Limpar')
        frame_lbl_botao_limpar.place(y=250, x=779)

        self.botao_limpar_lista = Button(frame_lbl_botao_limpar, text='Aplicar')
        self.botao_limpar_lista.config(width=15)
        self.botao_limpar_lista.config(command=self.limpar_lista_cache)
        self.botao_limpar_lista.pack(anchor='center')
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
        valor_arq_txt_link = open(caminho_arq_txt, 'r')
        self.lendo_arq_txt_lnk = valor_arq_txt_link.readlines()

        for indice, valor_link in enumerate(self.lendo_arq_txt_lnk):
            valor_link = YouTube(valor_link).title
            self.lista_cache_links_add.insert('end', f'{indice + 1} - {valor_link}')

    """# Funções básicas"""
    def limpar_lista_cache(self):
        self.lista_cache_links_add.delete(0, 'end')
        self.botao_down_link.config(state=tk.DISABLED)
        self.caixa_de_entrada_link.delete(0, 'end')

    def downloads_link(self):
        try:
            for valor_cursor in self.lista_cache_links_add.curselection():
                dados_selecionados = self.lendo_arq_txt_lnk[valor_cursor]
                print(dados_selecionados)
        except:
            showwarning('AVISO!', 'Não existem links para downloads')




iniciando_obj = Youtube_v4()

