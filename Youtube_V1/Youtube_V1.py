from threading import Thread

lista_menu = ['Adicionar link', 'Baixar links', 'Ver links', 'Sair']

# ######################################################################################################################
"""#### Funções basicas"""
def LeiaInt(valor_recebido):
    pass


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

menu()
