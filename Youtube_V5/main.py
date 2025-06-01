import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel

# app = QApplication([])
app = QApplication(sys.argv)  # contém os argumentos de linha de comando passados ao aplicativo

class JanelaPrincipalDownYT(QMainWindow):

    def __init__(self, link: str):
        super().__init__()
        self._link = link
        self.setWindowTitle('Download YouTube')
        self.setFixedSize(QSize(400, 400))  # QSize Bloqueia o tamanho da janela.

        self.btn_add_link = QPushButton('Adicionar')
        self.btn_add_link.setStyleSheet('font-size: 30px;')
        self.btn_add_link.clicked.connect(self.download_link)

        self.setCentralWidget(self.btn_add_link)

    def download_link(self):
        print(self._link)


obj_init_yt = JanelaPrincipalDownYT('link')
obj_init_yt.download_link()
obj_init_yt.show()

app.exec()
