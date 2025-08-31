"""
from pytubefix import Search

results = Search('GitHub Issue Best Practices')

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
from pytubefix.cli import on_progress
from pytubefix import Playlist

import sqlite3
import re


def on_progress_(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    porcentagem = (bytes_download / total_size) * 100
    print(f'Download: {porcentagem:.2f} concluido...')

def validacao_nome_arquivo(filename):
    """
    Corrige o nome, remove os caracteres especiais, evita os erros na criação
    :param filename: recebe o nome do arquivo, caso tenha erro, arquivo será corrigido.
    :return:
    """
    return re.sub(r'[\/:*?"<>|]', '-', filename)

class YouTubeDownload:
    linha = '----' * 24

    path_home = Path.home()

    DB_YOUTUBE_ONE = Path(path_home, 'OneDrive', 'Documentos', 'YouTube_V6', 'dados_core.db')
    path_down_mp3_one = Path(path_home, 'OneDrive', 'Documentos', 'YouTube_V6', 'Músicas(MP3)')
    path_down_mp4_one = Path(path_home, 'OneDrive', 'Documentos', 'YouTube_V6', 'Vídeos(MP4)')

    DB_YOUTUBE = Path(path_home, 'Documentos', 'dados_core.db')
    path_down_mp3 = Path(path_home, 'Documentos', 'YouTube_V6', 'Músicas(MP3)')
    path_down_mp4 = Path(path_home, 'Documentos', 'YouTube_V6', 'Vídeos(MP4)')

    # Pasta vai receber o vídeo apenas com o som para ser modificado para audio
    path_temp = str(Path(path_home, 'AppData', 'Local', 'Temp'))

    # Faz uma checagem na pasta
    pasta_com_onedrive = path.join(path_home, 'OneDrive', 'Documentos')

    def __init__(self):
        self.link = None
        self.conexao_banco = None
        self.cursor = None

    # Registra o link na base de dados.
    def registrando_link_base_dados(self, link):
        """
        Metodo responsável em registrar o link na base de dados.
        :param link: Recebe o link do youtube, validado pelo metodo 'validar_link_youtube'.
        1º O metodo pytubefix.YouTube processo o link e é estraido as informações do link como:
        Author, title, length(duração em segundos), thumbnail_url(miniatura) e watch_url(Link do vídeo)
        2º query_sqlite: cria o comanado para adicionar os valores na tabela.
        3º valores_query: Recebe as variáveis com os valores do link.
        4º self.cursor.execute(query_sqlite, valores_query): Executa o comando para adicionar os dados na tabela.
        :return: A confirmação que os dados foram salvos na tabela.
        """
        try:
            dados_tube = YouTube(link)  # Criando objeto

            try:
                # Adicionando url dentro da base de dados
                # Estou usando um placeholders para garantir que nenhum comando entre.
                query_sqlite = (
                    f"INSERT INTO INFO_TUBE (autor_link, titulo_link, duracao, miniatura, link_tube) "
                    f"VALUES (?, ?, ?, ?, ?); "
                )
                valores_query = (
                    dados_tube.author,
                    dados_tube.title,
                    str(dados_tube.length),
                    dados_tube.thumbnail_url,
                    dados_tube.watch_url,
                )
                self.cursor.execute(query_sqlite, valores_query)
                self.conexao_banco.commit()
                print(f'{dados_tube.author} - {dados_tube.title}')
                return 'Link salvo na base de dados.'

            except Exception as error:
                # Desfaz das operações em caso de erro.
                self.conexao_banco.rollback()
                return f'ERROR: Não foi possível salvar a URL na base de dados (registrando_link_base_dados): [{error}]'

        except Exception as error:
            print(f'ERROR: ocorreu um erro inexperado: [{error}]')

    def removendo_link_base_dados(self, link_remove: int):
        """
        Metódo responsável por remover o link da base de dados.
        :param link_remove: Recebe o valor do número do id do link.
        :return: Retorna a confirmação que o link foi deletado.
        """

        # Cria a query para o banco de dados.
        cmd_sql = f"DELETE FROM INFO_TUBE WHERE id={link_remove}"
        try:
            # Executa o comando do sql
            self.cursor.execute(cmd_sql)

            # Atualiza o banco de dados.
            self.conexao_banco.commit()

            # Retorna a confirmação da remoção.
            return f'Link deletado...'
        except Exception as error:
            print(f'Erro: {error}')

    # Listando Tabela INFO_TUBE
    def listando_info_base_dados(self):
        """
        Metodo responsável por lista as urls dentro da base de dados.
        :return: Sempre vai retornar um tubla. O "fronte" vai ser responsável em mostrar os dados.
        """
        # Consulta SQL. Busca todos os dados dentro da tabela  INFO_TUBE
        query_sqlite = "SELECT * FROM INFO_TUBE"

        # fetchall() extrai todos os resultados e retorna uma lista de tuplas.
        lista_urls = self.cursor.execute(query_sqlite).fetchall()
        lista_dict = list()

        # List comprehension gera uma lista com os nomes das colunas.
        # Itera os valores dentro da tabela e pega nos nomes da coluna.
        # Cada item em description é uma tupla, onde o primeiro elemento (desc[0]) é o nome da coluna.
        colunas = [desc[0] for desc in self.cursor.description]

        # itera as linhas que estão dentro da tabela
        for linha in lista_urls:

            # Junta a coluna com a linha e transforma em dicionário
            registro = dict(zip(colunas, linha))

            # Adiciona o dicionário na lista
            lista_dict.append(registro)

        return lista_dict

    # Faz download do arquivo em MP3.
    def download_music(self, dados_youtube):
        """
        1º O arquivo M4A é baixado para pasta "temp".
        2º O metodo mp4_to_mp3 é chamado e transforma o arquivo em MP3.
        :param dados_youtube: Entra o link do youtube.
        :return: Retorna a confirmação do processo em forma de string.
        """
        print()
        print(self.linha)
        download_yt = YouTube(dados_youtube, on_progress_callback=on_progress_)
        verificacao_sistema_pastas = self.validando_sistema()
        print(f'Realizando downloado do arquivo: {download_yt.author}-{download_yt.title}')
        print()
        stream = download_yt.streams.get_audio_only()
        stream.download(self.path_temp)

        # Chama o app para transformar o arquivo m4a(audio) em mp3(audio)
        self.mp4_to_mp3(autor_midia=download_yt.author)

    # Faz o download do arquivo em MP4
    def download_movie(self, link_down):
        """
        O download é simples, como não preciso converter nenhum arquivo. O vídeo é transferido direto para pasta
        padrão do app.
        :return: Retorna a confirmação do processo em forma de string.
        """

        download_yt = YouTube(link_down, on_progress_callback=on_progress_)
        verificacao_sistema_pastas_one_drive = self.validando_sistema()

        stream = download_yt.streams.get_highest_resolution()

        if verificacao_sistema_pastas_one_drive:
            stream.download(self.path_down_mp4_one)
        else:
            stream.download(self.path_down_mp4)

        print(self.linha)
        print('Download concluído!')

        # Arruma uma forma de voltar para a lista de urls
        print()
        print()

        sleep(2)
        self.limpeza_cmd()

    # Processo para transformar o arquivo de mp4 em mp3
    # Esse problema não tem nenhum não pode ser chamado pelo usuário, apenas para uso internet do app
    def mp4_to_mp3(self, autor_midia):

        """
       - Aqui, é realizado uma listage na pasta Temp, aonde fica alocado o arquivo mp4;
       - após localizar o arquivo mp4, é realizado a junção do local, para ser processado;
       - O mesmo procedimento é realizado para o arquivo mp3, mas nessa opção é dado o mesmo nome, mas muda apenas
       a extensão;
       - Logo depois é precessado o arquivo para transformar em mp3;
       - Depois que finaliza o processo, o arquivo mp4 é removido da pasta temp
       :param autor_midia: Geralmente os vídeos não acompanham o nome do autor, então eu acrescento no final do mp3,
       mas os nomes podem vir com caracteres especiais, então para evitar problemas, chama-se uma função interna para
       remove os caracteres especiais e evitar erros.
       """

        for arquivo_m4a in listdir(self.path_temp):
            if search('m4a', arquivo_m4a):
                m4a_file_abs = path.join(self.path_temp, arquivo_m4a)

                # valida os nomes do arquivo, removendo os caracteres especiais, caso tenham.
                nome_arquivo_m4a_validado = validacao_nome_arquivo(arquivo_m4a)
                autor_validado = validacao_nome_arquivo(autor_midia)

                if self.validando_sistema():
                    mp3_file = path.join(
                        self.path_down_mp3_one, f"{autor_validado}_{arquivo_m4a.replace('m4a', 'mp3')}"
                    )
                else:
                    mp3_file = path.join(
                        self.path_down_mp3, f"{autor_validado}_{arquivo_m4a.replace('m4a', 'mp3')}"
                    )

                print(mp3_file)

                """#### Processa o MP4 para MP3"""
                novo_mp3 = AudioFileClip(m4a_file_abs)
                novo_mp3.write_audiofile(mp3_file)
                remove(m4a_file_abs)

    # Valida se o link é valido.
    def validar_link_youtube(self, link):

        if 'https://' not in link[:9]:
            link = f'https://{link}'

        if 'www.' not in link[:13]:
            link = f'{link[:8]}www.{link[8:]}'

        if link[:23] != 'https://www.youtube.com':
            return False
        else:
            return True

    def criando_tabela_dados(self):
        """
        Cria a tabela padrão para ser utilizado no banco.
        :return:
        """
        tabela = """
        CREATE TABLE IF NOT EXISTS INFO_TUBE(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            autor_link VARCHAR(255), 
            titulo_link VARCHAR(255), 
            duracao VARCHAR(255), 
            miniatura VARCHAR(500), 
            link_tube VARCHAR(500) 
        );
        """
        try:
            # Valida se a tabela existe
            self.cursor.execute(
                "SELECT * FROM sqlite_master WHERE type='table' AND name='INFO_TUBE';"
            )
            verif_exist_base_dados = self.cursor.fetchone()

            # Caso a tabela exista finaliza o metodo. Geralmente ela não exista no primeiro acesso.
            if verif_exist_base_dados:
                print('Tabela de dados validado.')
                return
            else:
                self.cursor.execute(tabela)
                print('Tabela criada...')
        except Exception as error:
            print(f'Erro ao criar a tabela {error}')

    # Sempre que o programa é iniciado, é conectado a base de dados.
    def conectando_base_dados(self):
        try:
            listdir(self.pasta_com_onedrive)
            self.conexao_banco = sqlite3.connect(self.DB_YOUTUBE_ONE)
            print('Base de dados conectado.')
            self.cursor = self.conexao_banco.cursor()
            return self.conexao_banco
        except FileNotFoundError:
            self.conexao_banco = sqlite3.connect(self.DB_YOUTUBE)
            print('Base de dados conectado...')
            self.cursor = self.conexao_banco.cursor()
            return self.conexao_banco

    # Cria as pastas para caso o windows tenha o onedrive instalado
    def criando_pastas_destino_onedrive(self):
        try:
            makedirs(self.path_down_mp3_one)
            makedirs(self.path_down_mp4_one)
        except FileExistsError:
            ...

    # Cria as pastas sem o onedrive instalado
    def criando_pastas_destina_normal(self):
        try:
            makedirs(self.path_down_mp3)
            makedirs(self.path_down_mp4)
        except FileExistsError:
            return

    def validando_sistema(self):
        try:
            listdir(self.pasta_com_onedrive)
            self.criando_pastas_destino_onedrive()
            return True
        except FileExistsError:
            self.criando_pastas_destina_normal()
            return False

    def limpeza_cmd(self):
        system('cls')
