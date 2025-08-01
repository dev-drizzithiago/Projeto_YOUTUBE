import os
from os import system
from time import sleep
import core


class Menu:
    lista_menu_principal = [' Adicionar link ', ' Downloads ', ' Abrir arquivo ', ' Sair ']
    linha = '----' * 24

    def __init__(self):

        self.core_ = core.YouTubeDownload()

        print('Validando sistema de arquivos...!')
        self.core_.validando_sistema()

        print('Validando base de dados...')
        self.core_.conectando_base_dados()

        print('Validando tabelas de dados...!')
        self.core_.criando_tabela_dados()

    def menu_app(self):

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
            while True:
                print()
                print()
                print(self.linha)

                link_tube = str(input('Cole o link aqui(voltar=999): '))
                validacao_link = self.core_.validar_link_youtube(link_tube)
                if link_tube == '999':
                    print('Voltando ao menu principal...')
                    sleep(1)
                    break
                elif validacao_link:
                    print('Adicionando link, aguarde...')
                    resulta_processo = self.core_.registrando_link_base_dados(link_tube)
                    print(resulta_processo)
                else:
                    print(f'Link incorreto: {link_tube}')
                    print('Você precisa colocar um link valido...')
                    sleep(3)

        elif valor_opc == 2:
            print()
            print()
            lista_url = self.core_.listando_info_base_dados()
            for item in lista_url:
                print(item)
                sleep(2)

        elif valor_opc == 3:
            print()
            print()
            return 3

        elif valor_opc == 4:
            print()
            print()
            system('cls')
            print(self.linha)
            print('Saindo do programa!')
            sleep(1)
            return 4

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


if __name__ == "__main__":
    iniciando_obj_menu = Menu()

    while True:
        iniciando_obj_menu.menu_app()
