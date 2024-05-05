from pytube import YouTube

lista_menu_principal = []
lista_menu_downloads = []




def leiaInt(valor_entrada):
    while True:
        try:
            valor_inteiro = int(input(valor_entrada))
            return valor_inteiro
        except TypeError:
            print(f'Você digitou um valor errado!')


"""#### Menu principal"""
def menu_principal():
    print('----' * 24)
    print('                                    github.com/dev-drizzithiago ')
    print('                                          @drizzithiago ')
    print('----' * 24)

