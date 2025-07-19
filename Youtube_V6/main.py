
from os import path, listdir,makedirs, remove, system
from pathlib import Path
from re import search

from moviepy.editor import AudioFileClip
from pytubefix import YouTube

import sqlite3

class YouTubeDownload:
    lista_menu_principal = [' Adicionar link ', ' Downloads ', ' Abrir arquivo ', ' Sair ']

    def __init__(self, link):
        self.link = None

    def download_music(self):
        ...

    def download_movie(self):
        ...

    def mp4_to_mp3(self):
        """
       - Aqui, é realizado uma listage na pasta Temp, aonde fica alocado o arquivo mp4;
       - após localizar o arquivo mp4, é realizado a junção do local, para ser processado;
       - O mesmo procedimento é realizado para o arquivo mp3, mas nessa opção é dado o mesmo nome, mas muda apenas
       a extensão;
       - Logo depois é precessado o arquivo para transformar em mp3;
       - Depois que finaliza o processo, o arquivo mp4 é removido da pasta temp
       """

        for valor_mp4 in listdir():
            if search('m4a', valor_mp4):
                "#### Renomeia o arquivo"
                mp4_file = path.join()
                mp3_file = path.join()

                """#### Processa o MP4 para MP3"""
                novo_mp3 = AudioFileClip(mp4_file)
                novo_mp3.write_audiofile(mp3_file)
                remove(mp4_file)

    def manipulando_pastas(self):
        """#### Criando pastas """

        path_home = Path.home()
        path_temp = str(Path(path_home, 'AppData', 'Local', 'Temp'))
        try:
            self.path_down_mp3 = str(Path(path_home, 'Documentos', 'YouTube_V6', 'Músicas(MP3)'))
            self.path_down_mp4 = str(Path(path_home, 'Documentos', 'YouTube_V6', 'Vídeos(MP4)'))
        except FileNotFoundError:
            makedirs(self.path_down_mp3)
            makedirs(self.path_down_mp4)

        self.DB_YOUTUBE = str(Path(path_home, 'Documentos', 'YouTube_V6'))

    def banco_dados(self):
        conexao_banco = sqlite3.connect(self.DB_YOUTUBE)

    def menu_app(self):

        while True:
            print()
            print('----' * 24)
            print('                                    github.com/dev-drizzithiago ')
            print('                                          @drizzithiago ')
            print('----' * 24)

            self.logo_tube(' Menu Principal ')
            for valor_menu in range(len(self.lista_menu_principal)):
                print(f'[ {valor_menu + 1} ] ==> {self.lista_menu_principal[valor_menu]}')

            print()
            print(self.linha)
            valor_opc = self.leiaInt('Escolha uma opção: ')

            if valor_opc == 1:
                print()
                print()
                self.adicionar_link()

            elif valor_opc == 2:
                print()
                print()
                self.downloads()

            elif valor_opc == 3:
                print()
                print()
                self.abrir_arq()

            elif valor_opc == 4:
                print()
                print()
                system('cls')
                print(self.linha)
                print('Saindo do programa!')
                sleep(1)
                break

            else:
                print('Opção incorreta!!')
                sleep(5)

    def leiaInt(self, valor_entrada):
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

    def logo_tube(self, valor_entrada):
        """
        :param valor_entrada: Recebe o valor com o nome de cada função;
        :return:
        """
        linhas = '----' * 10
        print(f'{linhas}{valor_entrada}{linhas}')

if __name__ == '__main__':
    obj_youtube_download = YouTubeDownload()