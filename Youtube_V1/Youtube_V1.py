from os import mkdir, listdir, path, remove
from moviepy.editor import AudioFileClip
from threading import Thread
from pytube import YouTube
from pathlib import Path
from time import sleep
from re import search
import ffmpeg
import subprocess


# ######################################################################################################################
""" Declaração de variaveis"""
lista_menu = ['Adicionar link', 'Baixar links', 'Sair']

""" declaração das pastas que serão usadas para realizar os processos."""
home_path = Path.home()
path_temp = str(Path(home_path, 'AppData', 'Local', 'Temp'))
path_link = str(Path(home_path, 'AppData', 'LocalLow', 'Youtube_V1'))
path_move = str(Path(home_path, 'Videos'))
path_audi = str(Path(home_path, 'Músicas'))
path_down = Path(home_path, 'Downloads')
file_links = 'links_youtube.txt'

""" Criando pasta que ficara o arquivo de link"""
try:
    mkdir(path_link)
except FileExistsError:
    pass
except FileNotFoundError:
    path_link = str(Path(home_path, 'AppData', 'LocalLow', 'Youtube_V1'))
    mkdir(path_link)

arquivo_txt_links = f'{path_link}\\{file_links}'

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

# ######################################################################################################################
"""#### Funções de processo"""


def adicionar_link():
    """

    :return:
    """
    while True:
        print()
        logo_menus('adicionar_link')
        while True:
            link_add = str(input('Link youtube aqui(voltar:999): '))
            if link_add == '999':
                break
            elif link_add[:23] != 'https://www.youtube.com':
                print('---' * 14)
                print(f'Link não é youtube!')
            else:
                break
        if link_add != '999':
            try:
                save_link = open(arquivo_txt_links, 'a')
                save_link.write(f'{link_add}\n')
                print('Link adicionado com sucesso!')
                print()
                sleep(2)
            except FileExistsError:
                pass
            except FileNotFoundError:
                print('---' * 14)
                print('Arquivo "links_youtube.txt" foi criado com sucesso!')
                print()
                save_link = open(arquivo_txt_links, 'w')
        else:
            print('---' * 14)
            print('Voltando ao menu principal!')
            print()
            sleep(2)
            break

def baixar_links():
    """

    :return:
    """
    import moviepy.editor as mp
    while True:
        print()
        logo_menus('baixar_links')
        try:
            valor_links = open(arquivo_txt_links, 'r')
            open_link = valor_links.readlines()

            """# Mostra as links disponiveis para downloads"""
            print()
            logo_menus('Links disponiveis')
            for indice, links in enumerate(open_link):
                """ Montando obj youtube"""
                obj_youtube_title = YouTube(links).title
                print(f'[{indice + 1}] -> {obj_youtube_title}')

            print('---' * 14)
            selecao_link = leiaInt('Escolha uma opção(Voltar:999): ') - 1
            if selecao_link != 999:
                link_download = str(open_link[selecao_link])

                obj_youtube_downloads = YouTube(link_download)
                obj_title_verificacao = str(YouTube(link_download).title)
                print(obj_title_verificacao)

                """ Processo de downloads do arquivo em MP4"""
                try:
                    print(f'Realizando donwload do link: [{obj_youtube_downloads.title}] aguarde!')
                    sleep(1)
                    obj_youtube_downloads.streams.filter(only_audio=True).first().download(path_temp)

                    """### Chama a função para converter o video em mp3"""
                    mp4_to_mp3()
                except:
                    print(f'Não foi possível realizar o downloads do link {link_download}')

            else:
                print('---' * 14)
                print('Voltando ao menu principal!')
                print()
                sleep(2)
        except FileNotFoundError:
            print(f'Não existe link salvos')
            break

def mp4_to_mp3():

    """# Modificando mp4 para mp3"""

    """#### Procura todos os arquivos MP4"""
    for file in listdir(path_temp):
        if search('mp4', file):
            "#### Renomeia o arquivo"
            mp4_file = path.join(path_temp, file)
            mp3_file = path.join(path_down, path.splitext(file)[0] + '.mp3')
            """#### Processa o MP4 para MP3"""
            novo_mp3 = AudioFileClip(mp4_file)
            novo_mp3.write_audiofile(mp3_file)
            """#### Remove o arquivo MP4 para liberar espaço"""
            remove(mp4_file)

    print(f'Download realizado Sucesso!')
    print()


# ######################################################################################################################
"""#### Menu principal"""
def menu():
    print()
    logo_menus('Menu Principal')
    for indice in range(len(lista_menu)):
        print(f'[{indice + 1}] - {lista_menu[indice]}')

    opc_menu_principal = leiaInt('Escolha uma opcão: ')

    if opc_menu_principal == 1:
        thread_adicionar_link()

    elif opc_menu_principal == 2:
        thread_baixar_links()

    elif opc_menu_principal == 3:
        print('Fechando...')
        sleep(2)
        return True


while True:
    fechar_programa = menu()
    if fechar_programa:
        break
    else:
        menu()
