from threading import Thread
from pytube import YouTube
from pathlib import Path
from time import sleep
from tqdm import tqdm
from os import mkdir


lista_menu_principal = ['Adicionar link', 'Downloads', 'View Links adicionados', 'Abrir arquivo', 'Sair']
lista_menu_downloads = []


"""#### Função simples"""
def logo_tube(valor_entrada):
    linhas = '---' * 10
    print(f'{linhas}{valor_entrada}{linhas}')

def leiaInt(valor_entrada):
    while True:
        try:
            valor_inteiro = int(input(valor_entrada))
            return valor_inteiro
        except TypeError:
            print(f'Você digitou um valor errado!')

"""#### Funções threads"""
def thread_adicionar_link():
    pass

def thread_downloads():
    pass

def thread_view_links_add():
    pass

def thread_abrir_arq():
    pass

def thread_barra_progresso():
    Thread(target=barra_progresso()).start()

"""#### Funções simples"""
def criar_arq_links():
    pass

def criar_pasta_arq_link():
    """#### Criando pasta HOME"""
    path_home = Path.home()
    path_arqu = Path(path_home, 'AppData', 'LocalLow', 'Youtube_V2')
    path_temp = Path(path_home, 'AppData', 'Local', 'Temp')
    path_move = Path(path_home, 'Vídeos')
    path_mosi = Path(path_home, 'Músicas')

"""#### Funções de processo"""
def adicionar_link():
    logo_tube('Adicionar link')
    link_tube = str(input('Link aqui: ')).lower()


def downloads():
    pass

def view_links_add():
    pass

def abrir_arq():
    pass

def barra_progresso():
    for i in tqdm(range(10)):
        sleep(1)

"""#### Menu principal"""
def menu_principal():
    print('----' * 24)
    print('                                    github.com/dev-drizzithiago ')
    print('                                          @drizzithiago ')
    print('----' * 24)

    logo_tube('Menu Principal')
    for valor_menu in range(len(lista_menu_principal)):
        print(f'{valor_menu + 1} ==> {lista_menu_principal[valor_menu]}')

    valor_opc = leiaInt('Escolha uma opção: ')



thread_barra_progresso()
