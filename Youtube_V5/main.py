import sys
from PySide6.QtWidgets import QApplication, QWidget
app = QApplication(sys.argv)

class JanelaPrincipalDownYT:

    def __init__(self):
        self._link = None

        self.janela_principal = QWidget()
        self.janela_principal.show()

    def download_link(self, link: str):
        self._link = link

obj_init_yt = JanelaPrincipalDownYT()
resultado = obj_init_yt.download_link('link')
print(resultado)
app.exec()
