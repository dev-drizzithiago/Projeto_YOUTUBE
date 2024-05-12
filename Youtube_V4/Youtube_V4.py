import tkinter as tk
from tkinter.ttk import *
from threading import Thread


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
        self.lista_cache_links_add.insert(0, 'teste')
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
        # self.caixa_de_entrada_link.config('<KeyRelease>', self.ativar_botao_adicionar_link)
        self.caixa_de_entrada_link.config(width=143, justify=tk.CENTER)
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

        """#### Declarações de variaveis"""
        self.ativar_ = False

        self.janela_principal.mainloop()

    def ativar_botao_downloads(self, *args):
        self.botao_down_link.config(state=tk.NORMAL)

    def ativar_botao_adicionar_link(self, *args):
        valor_texto = self.var_caixa_de_entrada.get()
        self.botao_add_link.config(state=tk.NORMAL)

iniciando_obj = Youtube_v4()

