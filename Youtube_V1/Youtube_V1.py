from threading import Thread
from pytube import YouTube
from pathlib import Path
from time import sleep
from os import mkdir, listdir
from re import search

# ######################################################################################################################
""" Declaração de variaveis"""
lista_menu = ['Adicionar link', 'Baixar links', 'Ver links', 'Sair']

""" declaração das pastas que serão usadas para realizar os processos."""
home_path = Path.home()
path_temp = str(Path(home_path, 'AppData', 'Local', 'Temp'))
path_link = str(Path(home_path, 'AppData', 'LocalLow'))
path_move = str(Path(home_path, 'Videos'))
file_links = 'links_youtube.txt'

""" Criando pasta que ficara o arquivo de link"""
try:
    mkdir(path_link)
except FileExistsError:
    pass
except FileNotFoundError:
    path_link = str(Path(home_path, 'AppData', 'LocalLow'))
    mkdir(path_link + 'Youtube_V1')
print(path_link)
arquivo_txt_links = f'{path_link}\\{file_links}'
print(f'Arquivos de texto: {arquivo_txt_links}')

# ######################################################################################################################
"""#### Funções basicas"""


def leiaInt(valor_recebido):
    while True:
        try:
            valor_inteiro = int(input(valor_recebido))
            return valor_inteiro
        except ValueError:
            print('Você digitou um valor incorreto')


# ----------------------------------------------------------------------------------------------------------------------
def logo_menus(valor_recebido):
    linha = '----' * 10
    print(f'{linha}{valor_recebido}{linha}')


# ######################################################################################################################
"""#### Funções de threads"""


def thread_adicionar_link():
    print('thread_adicionar_link')
    Thread(target=adicionar_link()).start()


def thread_baixar_links():
    print('thread_baixar_links')
    Thread(target=baixar_links()).start()


def thread_ver_links():
    print('thread_ver_links')
    Thread(target=ver_links()).start()


# ######################################################################################################################
"""#### Funções de processo"""


def adicionar_link():
    """

    :return:
    """
    logo_menus('adicionar_link')
    while True:
        link_add = str(input('Link youtube aqui: '))
        if link_add[:23] != 'https://www.youtube.com':
            print(f'Link não é youtube!')
        else:
            break
    try:
        save_link = open(arquivo_txt_links, 'a')
        save_link.write(f'{link_add}\n')
        print('Link adicionado com sucesso!')
        print()
        sleep(2)
    except FileExistsError:
        pass
    except FileNotFoundError:
        print('Arquivo "links_youtube.txt" foi criado com sucesso!')
        save_link = open(arquivo_txt_links, 'w')


def baixar_links():
    """

    :return:
    """

    logo_menus('baixar_links')
    try:
        valor_links = open(arquivo_txt_links, 'r')
        open_link = valor_links.readlines()

        """# Mostra as links disponiveis para downloads"""
        print()
        for indice, links in enumerate(open_link):
            """ Mantando obj youtube"""
            obj_youtube_title = YouTube(links).title
            print(f'[{indice + 1}] -> {obj_youtube_title}')

        selecao_link = leiaInt('Escolha uma opção: ') - 1
        link_download = str(open_link[selecao_link])

        obj_youtube_downloads = YouTube(link_download)
        obj_title_verificacao = str(YouTube(link_download).title)
        print(obj_title_verificacao)

        """ Processo de downloads do arquivo em MP4"""
        try:
            print(f'Realizando donwload do link: [{obj_youtube_downloads.title}] aguarde!')
            sleep(1)
            obj_youtube_downloads.streams.filter(adaptive=True).first().download(path_temp)
            print(f'Download realizado ucesso!')
            print()
        except:
            print(f'Não foi possível realizar o downloads do link {link_download}')

    except FileNotFoundError:
        print(f'Não existe link salvos')


def ver_links():
    """

    :return:
    """
    logo_menus('Opção desativada!')
    pass


# ######################################################################################################################
"""#### Menu principal"""


def menu():
    for indice in range(len(lista_menu)):
        print(f'[{indice + 1}] - {lista_menu[indice]}')

    opc_menu_principal = leiaInt('Escolha uma opcão: ')

    if opc_menu_principal == 1:
        thread_adicionar_link()

    elif opc_menu_principal == 2:
        thread_baixar_links()

    elif opc_menu_principal == 3:
        thread_ver_links()

    elif opc_menu_principal == 4:
        print('Fechando...')
        sleep(2)
        return False


while True:
    fechar_programa = menu()
    if fechar_programa:
        break
    else:
        menu()
