from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QScrollArea, QWidget, QVBoxLayout, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtCore import QUrl


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем QWebEngineView
        self.webEngineView = QWebEngineView()

        # Загружаем страницу
        self.webEngineView.load(QUrl("https://www.google.com"))

        # Устанавливаем QWebEngineView в качестве центрального виджета главного окна
        self.setCentralWidget(self.webEngineView)

      

        # Создаем панель меню
        menubar = self.menuBar()

        # Создаем пункты меню
        file_menu = menubar.addMenu('&Файл')
        edit_menu = menubar.addMenu('&Редактирование')

        # Создаем действия для пункта "Файл"
        new_action = QAction('Новый', self)
        open_action = QAction('Открыть', self)
        save_action = QAction('Сохранить', self)

        # Добавляем действия в пункт "Файл"
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        # Создаем действия для пункта "Редактирование"
        cut_action = QAction('Вырезать', self)
        copy_action = QAction('Копировать', self)
        paste_action = QAction('Вставить', self)

        # Добавляем действия в пункт "Редактирование"
        edit_menu.addAction(cut_action)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)


app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
