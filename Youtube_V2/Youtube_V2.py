from threading import Thread
from pytube import YouTube
from pathlib import Path
from time import sleep
from tqdm import tqdm
from os import mkdir

lista_menu_principal = ['Adicionar link', 'Downloads', 'View Links adicionados', 'Abrir arquivo', 'Sair']
lista_menu_downloads = ['Vídeo(MP4)', 'Música(MP3)']

"""#### Criando pastas """
path_home = Path.home()
path_arqu = Path(path_home, 'AppData', 'LocalLow', 'Youtube_V2')
path_temp = Path(path_home, 'AppData', 'Local', 'Temp')
path_move = Path(path_home, 'Vídeos')
path_musc = Path(path_home, 'Músicas')


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
    Thread(target=adicionar_link()).start()


def thread_downloads():
    pass


def thread_view_links_add():
    pass


def thread_abrir_arq():
    pass


def thread_barra_progresso():
    Thread(target=barra_progresso()).start()


"""#### Funções simples"""
def criar_pasta_arq_link():
    """#### Cria a pasta dentro do APPDATA"""
    try:
        mkdir(path_arqu)
    except FileExistsError:
        pass


def registrar_link(valor_entrada):
    try:
        gravando_link = open(path_arqu, 'a')
        gravando_link.write(f'{valor_entrada} \n')
        print('Link adicionado com sucesso!')
    except FileExistsError:
        pass
    except FileNotFoundError:
        gravando_link = open(path_arqu, 'w')
        gravando_link.write(f'{valor_entrada} \n')


"""#### Funções de processo"""
def adicionar_link():
    logo_tube('Adicionar link')
    while True:
        link_tube = str(input('Link aqui (voltar=999): ')).lower()
        if link_tube == '999':
            print('voltando ao menu principal')
            sleep(1)
            break
        elif link_tube[:23] != 'https://www.youtube.com/':
            print('Não é um link YouTube!')
        else:
            registrar_link(link_tube)


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
    while True:
        print('----' * 24)
        print('                                    github.com/dev-drizzithiago ')
        print('                                          @drizzithiago ')
        print('----' * 24)

        logo_tube('Menu Principal')
        for valor_menu in range(len(lista_menu_principal)):
            print(f'[ {valor_menu + 1} ] ==> {lista_menu_principal[valor_menu]}')

        valor_opc = leiaInt('Escolha uma opção: ')

        if valor_opc == 1:
            thread_adicionar_link()

        elif valor_opc == 2:
            pass

        elif valor_opc == 3:
            pass

        elif valor_opc == 4:
            print('Saindo do programa!')
            sleep(1)
            break


menu_principal()
