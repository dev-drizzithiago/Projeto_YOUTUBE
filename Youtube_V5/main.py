import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

# app = QApplication([])
app = QApplication(sys.argv)  # contém os argumentos de linha de comando passados ao aplicativo

class JanelaPrincipalDownYT(QMainWindow):

    def __init__(self):
        super().__init__()
        self._link = None
        self.setWindowTitle('Download YouTube')
        self.setFixedSize(QSize(400, 400))  # QSize Bloqueia o tamanho da janela.

        self.btn_add_link = QPushButton('Adicionar')
        self.btn_add_link.setStyleSheet('font-size: 30px;')
        self.btn_add_link.move(10, 50)

        self.setCentralWidget(self.btn_add_link)

        self.lbl_titulo = QLabel('teste')

    def download_link(self, link: str):
        self._link = link
        print(self._link)


obj_init_yt = JanelaPrincipalDownYT()
obj_init_yt.download_link('link')
obj_init_yt.show()

app.exec()
