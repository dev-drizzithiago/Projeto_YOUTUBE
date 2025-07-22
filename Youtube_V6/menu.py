from os import system
from time import sleep
import core


class Menu:
    lista_menu_principal = [' Adicionar link ', ' Downloads ', ' Abrir arquivo ', ' Sair ']
    linha = '----' * 24

    def __init__(self):

        self.core_ = core.YouTubeDownload()
        self.core_.criando_banco_dados()

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
            print()
            print()

            print(self.linha)
            link_tube = str(input('Cole o link aqui(voltar=999): '))

            resulta_processo = self.core_.registrando_link_base_dados(link_tube)

        elif valor_opc == 2:
            print()
            print()
            return 2

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
    while True:
        iniciando_obj_menu = Menu()


