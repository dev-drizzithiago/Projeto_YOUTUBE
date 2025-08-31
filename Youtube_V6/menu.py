import os
from os import system
from time import sleep
import core


class Menu:
    lista_menu_principal = [' Adicionar link ', ' Downloads ', ' Abrir arquivo ', ' Excluir link ']
    lista_menu_downloads = [' Música(MP3) ', ' Vídeo(MP4) ']
    linha = '----' * 24

    def __init__(self):
        self.logo_inicial()

        self.core_ = core.YouTubeDownload()

        print('Validando sistema de arquivos...!')
        resultado = self.core_.validando_sistema()
        print(resultado)

        print('Validando base de dados...')
        self.core_.conectando_base_dados()

        print('Validando tabelas de dados...!')
        self.core_.criando_tabela_dados()

    def menu_app(self):

        self.logo_tube(' Menu Principal ')
        for valor_menu in range(len(self.lista_menu_principal)):
            print(f'[ {valor_menu + 1} ] ==> {self.lista_menu_principal[valor_menu]}')
        print("[ 0 ] ==>  Sair ")

        print()
        print(self.linha)
        valor_opc = self.leiaInt('Escolha uma opção: ')

        # opcao para salvar o link
        if valor_opc == 1:
            while True:
                print()
                print(self.linha)

                link_tube = str(input('Cole o link aqui(voltar=999): '))
                validacao_link = self.core_.validar_link_youtube(link_tube)
                if link_tube == '999':
                    print()
                    print(self.linha)
                    print('Voltando ao menu principal...')
                    sleep(1)
                    break
                elif validacao_link:
                    print()
                    print(self.linha)
                    print('Adicionando link, aguarde...')
                    resulta_processo = self.core_.registrando_link_base_dados(link_tube)
                    print(resulta_processo)
                else:
                    print(f'Link incorreto: {link_tube}')
                    print('Você precisa colocar um link valido...')
                    sleep(3)

        # opção para fazer download, mais complexo.
        elif valor_opc == 2:
            self.limpeza_cmd()
            print()
            lista_url = self.core_.listando_info_base_dados()

            while True:
                self.logo_tube(' Lista do conteúdo ')
                for index, item in enumerate(lista_url):
                    print(f'[ {index+1} ] => {item['autor_link']}-{item['titulo_link']}')

                print()
                print(self.linha)
                opcao = self.leiaInt('Escolha uma opção(voltar=999): ')

                if opcao == 999:
                    print()
                    print(self.linha)
                    print('Voltando ao menu principal...')
                    sleep(1)
                    self.limpeza_cmd()
                    break

                link_para_download = lista_url[opcao-1]['link_tube']

                while True:
                    self.logo_tube(' Opção de download ')
                    for indice, item in enumerate(self.lista_menu_downloads):
                        print(f' [ {indice+1} ] => {item}')

                    print()
                    print(self.linha)
                    opcao_down = self.leiaInt('Escolha uma opção (voltar=999): ')
                    if opcao_down == 999:
                        print()
                        print(self.linha)
                        print('Voltando um menu...')
                        sleep(1)
                        self.limpeza_cmd()
                        break
                    elif opcao_down == 1:
                        print()
                        print(self.linha)
                        print('Download música')
                        self.core_.download_music(link_para_download)
                        break
                    elif opcao_down == 2:
                        print('Download Vídeo')
                        self.core_.download_movie(link_para_download)
                        break

        # opção para reproduzir as mídias
        elif valor_opc == 3:
            while True:

                # Lista o menu de mídia. Escolhe entre mp3 ou mp4
                for indice, item in enumerate(self.lista_menu_downloads):
                    print(f'{indice+1} - {item}')

                print()
                print(self.linha)
                opcao_midia = self.leiaInt('Escolha uma opção(999): ')

                if opcao_midia == 999:
                    print('Voltando ao menu principal.')
                    sleep(1)
                    break

                # Condição para obter as midias corretas, conforme a escolha do usuário.
                elif opcao_midia == 1:
                    listando_midia = os.listdir(self.core_.path_down_mp3_one)
                    caminho_abs_midia = self.core_.path_down_mp3_one
                elif opcao_midia == 2:
                    listando_midia = os.listdir(self.core_.path_down_mp4_one)
                    caminho_abs_midia = self.core_.path_down_mp4_one
                else:
                    print('Opção inválida')

                print()
                print(self.linha)
                # Lista as mídias que já foram baixadas para o computador.
                for indice, item in enumerate(listando_midia):
                    print(f'{indice + 1} ==> {item}')

                print()
                print(self.linha)
                opcao_open = self.leiaInt('Estolha uma mídia: ')

                # Abre a mídia com o reprodutor padrão.
                os.startfile(os.path.join(caminho_abs_midia, listando_midia[opcao_open-1]))

        # Remove link na base de dados.
        elif valor_opc == 4:
            print()
            print(self.linha)
            while True:
                lista_url = self.core_.listando_info_base_dados()
                for index, item in enumerate(lista_url):
                    print(f"{index+1} - {item['autor_link']} - {item['titulo_link']}")

                print()
                print(self.linha)
                opcao = self.leiaInt('Escolha uma opção para deletar(voltar=999): ')

                if opcao == 999:
                    print('Voltando ao menu...')
                    break

                print()
                print(self.linha)
                try:
                    retorno_resultado = self.core_.removendo_link_base_dados(lista_url[opcao-1]['id'])
                    print()
                    print(retorno_resultado)
                except IndexError:
                    print('Opção inválida...')

                print()
                print(self.linha)

        elif valor_opc == 0:
            print()
            self.limpeza_cmd()
            print(self.linha)
            print('Saindo do programa!')
            sleep(1)
            return True

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

    def logo_inicial(self):
        print()
        print('----' * 24)
        print('                                    github.com/dev-drizzithiago ')
        print('                                          @drizzithiago ')
        print('----' * 24)

    def limpeza_cmd(self):
        system('cls')

if __name__ == "__main__":
    iniciando_obj_menu = Menu()

    while True:
        finish_app = iniciando_obj_menu.menu_app()

        if finish_app:
            break
