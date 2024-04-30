from threading import Thread
from time import sleep

lista_menu = ['Adicionar link', 'Baixar links', 'Ver links', 'Sair']

# ######################################################################################################################
"""#### Funções basicas"""
def leiaInt(valor_recebido):
    while True:
        try:
            valor_inteiro = int(input(valor_recebido))
            return valor_inteiro
        except ValueError:
            print('Você digitou um valor incorreto')


# ######################################################################################################################
"""#### Funções de threads"""
def thread_adicionar_link():
    print('thread_adicionar_link')
    pass


def thread_baixar_links():
    print('thread_baixar_links')
    pass


def thread_ver_links():
    print('thread_ver_links')
    pass

# ######################################################################################################################
"""#### Funções de processo"""
def adicionar_link():
    print('adicionar_link')
    pass


def baixar_links():
    print('baixar_links')
    pass


def ver_links():
    print('ver_links')
    pass

# ######################################################################################################################
"""#### Menu principal"""
def menu():
    for indice in range(len(lista_menu)):
        print(f'[{indice + 1}] - {lista_menu[indice]}')

    opc_menu_principal = leiaInt('Escolha uma opcão: ')

    if opc_menu_principal == 1:
        thread_adicionar_link()

    elif opc_menu_principal == 2:
        thread_baixar_links()

    elif opc_menu_principal == 3:
        thread_ver_links()

    elif opc_menu_principal == 4:
        print('Fechando...')
        sleep(2)


menu()
