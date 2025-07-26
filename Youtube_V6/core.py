"""
from pytubefix import Search

results = Search('Github Issue Best Practices')

for video in results.videos:
    print(f'Title: {video.title}')
    print(f'URL: {video.watch_url}')
    print(f'Duration: {video.length} sec')
    print('---')

Title: Good Practices with GitHub Issues
URL: https://youtube.com/watch?v=v1AeHaopAYE
Duration: 406 sec
---
Title: GitHub Issues Tips and Guidelines
URL: https://youtube.com/watch?v=kezinXSoV5A
Duration: 852 sec
---
Title: 13 Advanced (but useful) Git Techniques and Shortcuts
URL: https://youtube.com/watch?v=ecK3EnyGD8o
Duration: 486 sec
---
Title: Managing a GitHub Organization Tools, Tips, and Best Practices - Mark Matyas
URL: https://youtube.com/watch?v=1T4HAPBFbb0
Duration: 1525 sec
---
Title: Do you know the best way to manage GitHub Issues?
URL: https://youtube.com/watch?v=OccRyzAS4Vc
Duration: 534 sec
---

"""

from os import path, listdir, makedirs, remove, system

from pathlib import Path
from re import search
from time import sleep

from moviepy.editor import AudioFileClip
from pytubefix import YouTube

import sqlite3

class YouTubeDownload:

    path_home = Path.home()

    DB_YOUTUBE_ONE = Path(path_home, 'OneDrive', 'Documentos', 'YouTube_V6', 'dados_core.db')
    path_down_mp3_one = Path(path_home, 'OneDrive', 'Documentos', 'YouTube_V6', 'Músicas(MP3)')
    path_down_mp4_one = Path(path_home, 'OneDrive', 'Documentos', 'YouTube_V6', 'Vídeos(MP4)')

    DB_YOUTUBE = Path(path_home, 'Documentos', 'dados_core.db')
    path_down_mp3 = Path(path_home, 'Documentos', 'YouTube_V6', 'Músicas(MP3)')
    path_down_mp4 = Path(path_home, 'Documentos', 'YouTube_V6', 'Vídeos(MP4)')

    # Pasta vai receber o vídeo apenas com o som para ser modificado para audio
    path_temp = str(Path(path_home, 'AppData', 'Local', 'Temp'))

    # Variavel que vai receber o caminho do banco de dados

    pasta_com_onedrive = path.join(path_home, 'OneDrive', 'Documentos')

    def __init__(self):
        self.link = None
        self.conexao_banco = None
        self.cursor = None

    def registrando_link_base_dados(self, link):
        print('Registrando link na base de dados...')
        validacao_link = self.validar_link_youtube(link=link)
        obj_tube = YouTube(link)

        if validacao_link:
            ...
        else:
            return " Link não é valido."



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

    def validar_link_youtube(self, link):
        if link[:23] != 'https://www.youtube.com':
            print('Você não colocou um link YouTube!')
            return False
        else:
            return True

    def criando_pastas_destino_onedrive(self):
        try:
            makedirs(self.path_down_mp3_one)
            makedirs(self.path_down_mp4_one)
        except FileExistsError:
            ...

    def criando_pastas_destina_normal(self):
        try:
            makedirs(self.path_down_mp3)
            makedirs(self.path_down_mp4)
        except FileExistsError:
            ...

    def validando_sistema(self):

        try:
            listdir(self.pasta_com_onedrive)
            self.criando_pastas_destino_onedrive()
        except FileExistsError:
            self.criando_pastas_destina_normal()

    def criando_banco_dados(self):
        """
        Cria a tabela padrão para ser utilizado no banco.
        :return:
        """
        tabela = """
        CREATE TABLE IF NOT EXISTS INFO_TUBE(
            id int auto_increment not null, 
            autor_link varchar(255), 
            titulo_link varchar(255), 
            duracao varchar(255), 
            link_tube varchar(500), 
            miniatura varchar(500), 
            primary key(id) 
        );
        """
        try:
            # Valida se a tabela existe
            self.cursor.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='INFO_TUBE';")
            verif_exist_base_dados = self.cursor.fetchone()

            # Caso a tabela exista finaliza o metodo. Geralmente ela não exista no primeiro acesso.
            if verif_exist_base_dados:
                return
            else:
                self.cursor.execute(tabela)
                print('Tabela criada...')
        except Exception as error:
            print(f'Erro ao criar a tabela {error}')

    def conectando_base_dados(self):
        try:
            listdir(self.pasta_com_onedrive)
            self.conexao_banco = sqlite3.connect(self.DB_YOUTUBE_ONE)
            print('Base de dados conectado...')
            self.cursor = self.conexao_banco.cursor()
        except FileNotFoundError:
            self.conexao_banco = sqlite3.connect(self.DB_YOUTUBE)
            print('Base de dados conectado...')
            self.cursor = self.conexao_banco.cursor()
