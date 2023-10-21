from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QFileDialog, QWidget, QVBoxLayout, QLabel, QMenu
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QObject, pyqtSignal
import os



class MainWindow(QMainWindow):
    my_signal = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.setMinimumSize(1600, 900)

        # menu = self.menuBar()
        # menu.setStyleSheet("font-size: 30px; background-color: yellow;")
        #
        # menu.setFixedHeight(50)
        # file = menu.addMenu("File")
        # # file.setStyleblue)
        # self.action = file.addAction("Open")
        # self.action.triggered.connect(self.open_file)

        menuBar = self.menuBar()
        menu = menuBar.addMenu("File")
        menuBar.setStyleSheet("font-size: 30px;")
        menuBar.setFixedHeight(50)

        action = QAction("Open", self)
        menu.addAction(action)
        action.triggered.connect(self.open_file)

        self.setStyleSheet("""
                    QMenuBar::item {
                        color: black;
                    }
                    QMenuBar::item:selected {
                        color: red;
                    }
                """)


        # menu2= self.menuBar()
        # file2 = menu2.addMenu("File")
        # menu2.setStyleSheet("font-size: 30px; background-color: blue")



        # self.action = self.menuBar().addMenu("File").addAction("Open")
        # self.action.triggered.connect(self.open_file)

    def open_file(self):
        print("open repository")
        folder = QFileDialog.getExistingDirectory(self, 'Выберите папку', '')

            # Если пользователь выбрал директорию, сохраняем путь в переменную
        if os.path.isdir(folder):
            self.folder_path = folder
            self.index_document = folder + "/index.html"

        # Создаем QWebEngineView
        self.webEngineView = QWebEngineView()
        self.webEngineView.setMinimumSize(1600, 900)
        # Загружаем страницу
        self.webEngineView.load(QUrl(self.index_document))

        # Устанавливаем QWebEngineView в качестве центрального виджета главного окна
        self.setCentralWidget(self.webEngineView)




app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
