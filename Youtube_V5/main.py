import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
app = QApplication(sys.argv)

class JanelaPrincipalDownYT:

    def __init__(self):
        self._link = None

        self.janela_principal = QWidget()
        self.janela_principal.show()

        self.lbl_titulo_link = QLabel(self.janela_principal)
        self.lbl_titulo_link.show()

    def download_link(self, link: str):
        self._link = link
        self.lbl_titulo_link(self._link)


obj_init_yt = JanelaPrincipalDownYT()
resultado = obj_init_yt.download_link('link')
print(resultado)
app.exec()
