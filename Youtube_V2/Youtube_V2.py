import os.path

from moviepy.editor import AudioFileClip
from os import mkdir, listdir, path, remove, makedirs
from threading import Thread
from pytube import YouTube
from pathlib import Path
from time import sleep
from tqdm import tqdm
from re import search


lista_menu_principal = [' Adicionar link ', ' Downloads ', ' Abrir arquivo ', ' Sair ']
lista_menu_downloads = [' Música(MP3) ', ' Vídeo(MP4) ']


# ----------------------------------------------------------------------------------------------------------------------
"""#### Criando pastas """
path_home = Path.home()
path_arqu = str(Path(path_home, 'AppData', 'LocalLow', 'Youtube_V2'))
path_temp = str(Path(path_home, 'AppData', 'Local', 'Temp'))
path_down_mp3 = str(Path(path_home, 'Downloads', 'YouTube_V2', 'Músicas(MP3)'))
path_down_mp4 = str(Path(path_home, 'Downloads', 'YouTube_V2', 'Vídeos(MP4)'))

arq_youtube = str(path_arqu + '\\Link_Youtube_V2.txt')

# ----------------------------------------------------------------------------------------------------------------------
"""Declarando variaveis"""
linha = '----' * 24

# ----------------------------------------------------------------------------------------------------------------------
"""#### Função simples"""
def logo_tube(valor_entrada):
    linhas = '----' * 10
    print(f'{linhas}{valor_entrada}{linhas}')
# ----------------------------------------------------------------------------------------------------------------------


def leiaInt(valor_entrada):
    while True:
        try:
            valor_inteiro = int(input(valor_entrada))
            return valor_inteiro
        except:
            print(f'Você digitou um valor errado!')
# ----------------------------------------------------------------------------------------------------------------------


"""#### Funções threads"""
def thread_downloads():
    Thread(target=downloads).start()
# ----------------------------------------------------------------------------------------------------------------------

def thread_abrir_arq():
    pass
# ----------------------------------------------------------------------------------------------------------------------
def criando_pastas_midias():
    """
    Função responsável em criar os diretorios responsavel por receber os arquivos de downloads
    :return:
    """
    try:
        makedirs(path_down_mp3)
        makedirs(path_down_mp4)
    except FileExistsError:
        pass
    except FileNotFoundError:
        makedirs(path_down_mp3)
        makedirs(path_down_mp4)

# ----------------------------------------------------------------------------------------------------------------------

"""#### Funções simples"""
def criar_pasta_arq_link():
    """#### Função responsável em criar pasta por armazenas o arquivo que ficar os links"""
    try:
        mkdir(path_arqu)
    except FileExistsError:
        pass
    except FileNotFoundError:
        mkdir(path_arqu)
# ----------------------------------------------------------------------------------------------------------------------

def registrar_link(valor_entrada):

    """#### Verifica se a pasta foi criada"""
    criar_pasta_arq_link()

    """#### cria o obj para o titulo do video"""
    titulo_link = YouTube(valor_entrada).title

    """#### Grava os dados do link no arquivo de texto; a função acima é responsável em criar """
    try:
        gravando_link = open(arq_youtube, 'a')
        gravando_link.write(f'{valor_entrada}\n')
        print(f'Link adicionado com sucesso! \n{linha}\nTitulo: {titulo_link}')
        sleep(2)

    except FileNotFoundError:
        gravando_link = open(arq_youtube, 'w')
        gravando_link.write(f'{valor_entrada}\n')

    except FileExistsError:
        pass
# ----------------------------------------------------------------------------------------------------------------------

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

# ----------------------------------------------------------------------------------------------------------------------
def mp3_to_mp4():
    print('Função "mp3_to_mp4"')

    for valor_mp4 in listdir(path_temp):
        if search('mp4', valor_mp4):
            "#### Renomeia o arquivo"
            mp4_file = path.join(path_temp, valor_mp4)
            mp3_file = path.join(path_down_mp3, path.splitext(valor_mp4)[0] + '.mp3')

            """#### Processa o MP4 para MP3"""
            novo_mp3 = AudioFileClip(mp4_file)
            novo_mp3.write_audiofile(mp3_file)
            remove(mp4_file)

# ----------------------------------------------------------------------------------------------------------------------
def downloads():
    criando_pastas_midias()
    while True:
        logo_tube(' Downloads ')

        """#### abrindo arquivo de texto"""
        try:
            valor_links = open(arq_youtube, 'r')
            link_down_tube = valor_links.readlines()

            """# listando os link salvos"""
            for indice, valor_link in enumerate(link_down_tube):
                valor_titulo = YouTube(valor_link).title
                print(f'[{indice + 1}] {valor_titulo}: \n{valor_link}')

            """### Abre para o usuário escolher o link"""
            print(linha)
            opc_downloads = leiaInt('Escolha uma opção (voltar=999): ') - 1
            """#### """
            if opc_downloads == 998:
                print('Voltando ao menu principal')
                sleep(2)
                break
            else:
                """#### Com as informações de de entrada, escolhe-se o link para o downloads"""
                link_downloads = link_down_tube[opc_downloads]
                obj_youtube = YouTube(link_downloads)

                """#### Menu downloads: aqui voce vai escolher qual extensão ira baixar, o mp3 ou mp4"""
                print(linha)
                for indice, valor in enumerate(lista_menu_downloads):
                    print(f'[{indice + 1}] - {valor}')

                opc_menu_down = leiaInt('Escolha uma opção: ')

                # Processo de downloads em MP3
                if opc_menu_down == 1:
                    print()
                    print(linha)
                    logo_tube('Downloads em MP3')

                    print()
                    print(linha)
                    print(f'Downloads em andamento, aguarde!')

                    try:
                        """#### Realiza o downloads do vídeo apenas com o audio"""
                        obj_youtube.streams.filter(only_audio=True).first().download(path_temp)

                        """# Chama a função para tranformar o videm em MP3"""
                        mp3_to_mp4()
                        print(f'Downloads finalizado... Verifique na pasta {path_down_mp3}')
                        sleep(2)
                    except:
                        print('Erro ao realizar o downloads do MP3')

                # Processo de downloads de vídeo"""
                elif opc_menu_down == 2:
                    print()
                    print(linha)
                    logo_tube('Downloads em MP4')
                    try:
                        print('Downloads em andamento, aguarde!!')
                        obj_youtube.streams.filter(adaptive=True).first().download(path_down_mp4)

                        print()
                        print(linha)
                        print(f'Downloads finalizado! \nVejá na pasta {path_down_mp4}')
                        sleep(2)
                    except:
                        print('Não foi possível realizado o downloads')

        except FileNotFoundError:
            print('\nArquivo não existe!')
            sleep(5)
        except FileExistsError:
            pass

# ----------------------------------------------------------------------------------------------------------------------
def abrir_arq():
    logo_tube(' Excecute um arquivos ')
    lista_mp3 = []
    lista_mp4 = []

    for valor_midia in listdir(path_down_mp3):
        lista_mp3.append(valor_midia)
    for valor_midia in listdir(path_down_mp4):
        lista_mp4.append(valor_midia)

    for indice, menu in enumerate(lista_menu_downloads):
        print(f'[{indice}] - {menu}')

    opc_midia = leiaInt('Escolha uma opção: ') - 1

# ----------------------------------------------------------------------------------------------------------------------

def barra_progresso():
    for i in tqdm():
        sleep(1)
# ----------------------------------------------------------------------------------------------------------------------

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
