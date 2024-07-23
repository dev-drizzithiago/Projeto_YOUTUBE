from os import mkdir, listdir, path, remove, makedirs, startfile, system
from moviepy.editor import AudioFileClip
from threading import Thread
from pytube import YouTube
from pathlib import Path
from time import sleep
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
    """
    Deixa a aparencia de casa função melhor
    :param valor_entrada: Recebe o valor com o nome de casa função;
    :return:
    """
    linhas = '----' * 10
    print(f'{linhas}{valor_entrada}{linhas}')


# ----------------------------------------------------------------------------------------------------------------------
def leiaInt(valor_entrada):
    """
    Reponsável em analisar se o valor que entrar, é um número inteiro;
    :param valor_entrada:  Recebe o valor em número de cada opção que o usuário escolheu;
    :return: Se estiver correto, retorna o valor para função de destino;
    """
    while True:
        try:
            valor_inteiro = int(input(valor_entrada))
            return valor_inteiro
        except:
            print(f'Você digitou um valor incorreto!')


# ----------------------------------------------------------------------------------------------------------------------
"""#### Funções threads"""


def thread_downloads():
    Thread(target=downloads).start()


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
    """#### Função responsável em criar pasta para armazenar o arquivo que fica salvo os links"""
    try:
        mkdir(path_arqu)
    except FileExistsError:
        pass
    except FileNotFoundError:
        mkdir(path_arqu)


# ----------------------------------------------------------------------------------------------------------------------
def registrar_link(valor_entrada):
    """
    :param valor_entrada: Recebe o valor do link
    1) Verifica se o arquivo de texto que vai receber o link está criada, caso não esteja, a funçção já está
    preparada para criar um;
    2) Com o link do YouTube, é colocando o título do link na variavel "titulo_link";
    3) Se tudo estiver correto, é aberto o arquivo de texto, logo depois é registrado o link e fechado o arquivo;
    :return:
    """
    criar_pasta_arq_link()

    """#### cria o obj para o titulo do video"""
    titulo_link = YouTube(valor_entrada).title

    """#### Grava os dados do link no arquivo de texto; a função acima é responsável em criar """
    try:
        gravando_link = open(arq_youtube, 'a')
        gravando_link.write(f'{valor_entrada}\n')
        gravando_link.close()
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
    """
    - Função responsável em receber o link, para que posteriormente ser registrado
    1) solicita ao usuário o link do YouTube;
    2) verifica se o link realmente é do YouTube, caso seja, a função "registro_link" é registrado
    no arquivo responsãvel;
    :return:
    """
    logo_tube('Adicionar link')

    while True:

        print(linha)
        link_tube = str(input('Cole o link aqui(voltar=999): '))

        if link_tube == '999':
            print('Voltando ao menu principal')
            sleep(1)
            system('cls')
            break

        elif link_tube[:23] != 'https://www.youtube.com':
            print('Você não colocou um link YouTube!')

        else:
            print('Registrando...!')
            sleep(1)
            registrar_link(link_tube)


# ----------------------------------------------------------------------------------------------------------------------
def mp3_to_mp4():
    """
    - Aqui, é realizado uma listage na pasta Temp, aonde fica alocado o arquivo mp4;
    - após localizar o arquivo mp4, é realizado a junção do local, para ser processado;
    - O mesmo procedimento é realizado para o arquivo mp3, mas nessa opção é dado o mesmo nome, mas muda apenas
    a extensão;
    - Logo depois é precessado o arquivo para transformar em mp3;
    - Depois que finaliza o processo, o arquivo mp4 é removido da pasta temp
    """

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
                valor_autor = YouTube(valor_link).author
                print(f'[{indice + 1}] {valor_autor} - {valor_titulo}: \n{valor_link}')

            """### Abre para o usuário escolher o link"""
            print(linha)
            opc_downloads = leiaInt('Escolha uma opção (voltar=999): ') - 1
            """#### """
            if opc_downloads == 998:
                print('Voltando ao menu principal')
                sleep(2)
                system('cls')
                break
            else:
                """#### Com as informações de de entrada, escolhe-se o link para o downloads"""
                link_downloads = link_down_tube[opc_downloads]
                obj_youtube = YouTube(link_downloads)

                """#### Menu downloads: aqui voce vai escolher qual extensão ira baixar, o mp3 ou mp4"""
                print()
                logo_tube('MP3/MP4')
                print(linha)
                for indice, valor in enumerate(lista_menu_downloads):
                    print(f'[{indice + 1}] - {valor}')

                print(linha)
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
                        print(f'Download finalizado... \nVerifique o MP3 na pasta [{path_down_mp3}]')
                        sleep(2)
                    except:
                        print('Não foi possível realizar o download')

                # Processo de downloads de vídeo"""
                elif opc_menu_down == 2:
                    print()
                    print(linha)
                    logo_tube('Downloads em MP4')
                    try:
                        print('Download em andamento, aguarde!!')
                        (obj_youtube.streams.get_highest_resolution().download(path_down_mp4))

                        print()
                        print(linha)
                        print(f'Download finalizado! \nVerifique o MP4 na pasta  [{path_down_mp4}]')
                        sleep(2)
                    except:
                        print('Não foi possível realizado o downloads')

        except FileNotFoundError:
            print('\nO arquivo que contém os links não existe! \nAdicione um link para criar')
            sleep(5)
            system('cls')
            break
        except FileExistsError:
            pass


# ----------------------------------------------------------------------------------------------------------------------
"""#### Funçao responsável em excultar as mídias do usuário."""
def abrir_arq():
    """
    Essa função utiliza as configurações padrão do windows.
    1) Criado duas listas para receber as mídias que forem encontradas nas pastas padrão do aplicativo;
    2) é realizado a listagem nas pastas, encontrando as mídias, os valores vão inseridos nas suas listas;
    3) mostra o menu de mídias para o usuário escolher, entre músicas e videos;
    4) escolhendo uma opção é apresentado a lista de mídias da categoria selecionada;
    5) o usuário escolhendo a mídia, existe uma função que vai buscar a mídia selecionada e deixar preparada para que a
    função "startfile" receba os valores corretos; eu usei o modulo "os.startfile" para abrir a mídia, usando ao
    player padrão do windows.
    6) Após selecionar a mídia, vai carregar o audio/video; eu usei um threading para que o programa não trave quando
    for aberto o player.
    :return:
    """
    while True:
        logo_tube(' Excecute um arquivos ')
        lista_mp3 = []
        lista_mp4 = []

        for valor_midia in listdir(path_down_mp3):
            lista_mp3.append(str(valor_midia))

        for valor_midia in listdir(path_down_mp4):
            lista_mp4.append(str(valor_midia))

        print()
        print(linha)
        for indice, menu in enumerate(lista_menu_downloads):
            print(f'[{indice + 1}] - {menu}')

        print()
        print(linha)
        opc_midia = leiaInt('Escolha uma opção(Voltar=999): ')

        if opc_midia == 999:
            print('Voltando ao menu principal!')
            sleep(2)
            system('cls')
            break

        # Opção de músicas
        elif opc_midia == 1:
            while True:
                print()
                print('Músicas')
                print(linha)

                if len(lista_mp3) == 0:
                    print('Não existe nenhuma música na pasta')
                    sleep(2)
                    break
                else:
                    for indice, valor_mp3 in enumerate(lista_mp3):
                        print(f'{indice + 1} - {valor_mp3}')

                print()
                print(linha)
                opc_mp3 = leiaInt('Escolha uma Música(voltar=999): ') - 1
                """Função que volta o menu"""
                if opc_mp3 == 998:
                    print('Voltando ao menu!')
                    break

                """#### Realiza a junção do caminha e arquivo para que seja lido pela Thread"""
                caminho_mp3 = str(path_down_mp3 + '\\' + lista_mp3[opc_mp3])

                print()
                print(linha)
                print(f'Iniciando: {caminho_mp3}')
                sleep(2)

                """#### Inicia a música no play padrão do windows"""
                Thread(target=startfile(caminho_mp3)).start()

        # Opão de vídeos
        elif opc_midia == 2:
            while True:
                print()
                print('Vídeos')
                print(linha)

                if len(lista_mp4) == 0:
                    print('Não existe nenhuma música na pasta')
                    sleep(2)
                    break
                else:
                    for indice, valor_mp4 in enumerate(lista_mp4):
                        print(f'{indice + 1} - {valor_mp4}')

                print()
                print(linha)
                opc_mp4 = leiaInt('Escolha uma opção(voltar=999): ') - 1
                """Função que volta o menu"""
                if opc_mp4 == 998:
                    print('Voltando ao menu!')
                    break

                """#### Realiza a junção do caminha e arquivo para que seja lido pela Thread"""
                caminho_mp4 = str(path_down_mp4 + '\\' + lista_mp4[opc_mp4])

                print()
                print(linha)
                print(f'Iniciando: {caminho_mp4}')
                sleep(2)

                """### Iniciando o vídeo no play padrão do windows"""
                Thread(target=startfile(caminho_mp4)).start()

        else:
            print('Opção invalida!')
            sleep(5)


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
            abrir_arq()

        elif valor_opc == 4:
            system('cls')
            print(linha)
            print('Saindo do programa!')
            sleep(1)
            break

        else:
            print('Opção incorreta!!')
            sleep(5)


menu_principal()
