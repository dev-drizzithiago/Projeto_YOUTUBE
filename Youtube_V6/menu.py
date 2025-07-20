
class Menu:
    lista_menu_principal = [' Adicionar link ', ' Downloads ', ' Abrir arquivo ', ' Sair ']
    def __init__(self):
        ...

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
                # self.adicionar_link()

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

