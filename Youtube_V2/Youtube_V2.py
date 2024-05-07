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
path_arqu = str(Path(path_home, 'AppData', 'LocalLow', 'Youtube_V2'))
path_temp = str(Path(path_home, 'AppData', 'Local', 'Temp'))
path_move = str(Path(path_home, 'Vídeos'))
path_musc = str(Path(path_home, 'Músicas'))
arq_youtube = str(path_arqu + '\\Link_Youtube_V2.txt')

"""Declarando variaveis"""
linha = '----' * 24

"""#### Função simples"""
def logo_tube(valor_entrada):
    linhas = '----' * 10
    print(f'{linhas}{valor_entrada}{linhas}')


def leiaInt(valor_entrada):
    while True:
        try:
            valor_inteiro = int(input(valor_entrada))
            return valor_inteiro
        except TypeError:
            print(f'Você digitou um valor errado!')


"""#### Funções threads"""
def thread_downloads():
    Thread(target=downloads).start()


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
    except FileNotFoundError:
        mkdir(path_arqu)


def registrar_link(valor_entrada):
    criar_pasta_arq_link()
    try:
        gravando_link = open(arq_youtube, 'a')
        gravando_link.write(f'{valor_entrada}\n')
        print('Link adicionado com sucesso!')

    except FileNotFoundError:
        gravando_link = open(arq_youtube, 'w')
        gravando_link.write(f'{valor_entrada}\n')

    except FileExistsError:
        pass


"""#### Funções de processo"""
def adicionar_link():
    logo_tube('Adicionar link')

    while True:
        print(linha)
        link_tube = str(input('Link aqui (voltar=999): '))

        if link_tube == '999':
            print('voltando ao menu principal')
            sleep(1)
            break

        elif link_tube[:23] != 'https://www.youtube.com':
            print('Não é um link YouTube!')

        else:
            print('Registrando...!')
            sleep(1)
            registrar_link(link_tube)


def downloads():
    while True:
        logo_tube(' Downloads ')

        """#### Menu downloads: aqui voce vai escolher qual extensão ira baixar, o mp3 ou mp4"""
        for indice, valor in enumerate(lista_menu_downloads):
            print(f'{indice + 1} - {valor}')

        """#### abrindo arquivo de texto"""
        try:
            valor_links = open(arq_youtube, 'r')
            link_down_tube = valor_links.readlines()
            for indice, valor_link in enumerate(link_down_tube):
                valor_titulo = YouTube(valor_link).title
                print(f'{indice + 1} {valor_titulo} - {valor_link}')

        except FileNotFoundError:
            print('\nArquivo não existe!')
            sleep(5)
        except FileExistsError:
            pass
        input()


def view_links_add():
    print()
    logo_tube(' Links salvos ')
    try:
        valor_arq_tube = open(arq_youtube, 'r')
        abrindo_arq_tube = valor_arq_tube.readlines()

        for valor_link in abrindo_arq_tube:
            obj_tube_titulo = YouTube(valor_link).title
            print(f'[{obj_tube_titulo}]')

    except FileNotFoundError:
        print(linha)
        print(' Arquivos com os links não exite! ')
        sleep(5)


def abrir_arq():
    logo_tube(' Excecute um arquivos ')


def barra_progresso():
    for i in tqdm(range(10)):
        sleep(1)


"""#### Menu principal"""
def menu_principal():
    while True:
        print()
        print('----' * 24)
        print('                                    github.com/dev-drizzithiago ')
        print('                                          @drizzithiago ')
        print('----' * 24)

        logo_tube(' Menu Principal ')
        for valor_menu in range(len(lista_menu_principal)):
            print(f'[ {valor_menu + 1} ] ==> {lista_menu_principal[valor_menu]}')

        print()
        print(linha)
        valor_opc = leiaInt('Escolha uma opção: ')

        if valor_opc == 1:
            adicionar_link()

        elif valor_opc == 2:
            downloads()

        elif valor_opc == 3:
            thread_abrir_arq()

        elif valor_opc == 4:
            print(linha)
            print('Saindo do programa!')
            sleep(1)
            break


menu_principal()
