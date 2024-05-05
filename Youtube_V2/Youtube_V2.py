from pytube import YouTube
from threading import Thread
from tqdm import tqdm
from time import sleep


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

"""#### Funções de processo"""
def adicionar_link():
    pass

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
