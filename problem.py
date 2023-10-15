from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем кнопку
        self.button = QPushButton('Выбрать папку', self)

        # Подключаем кнопку к событию нажатия
        self.button.clicked.connect(self.select_folder)

        # Устанавливаем кнопку в качестве центрального виджета главного окна
        self.setCentralWidget(self.button)

    def select_folder(self):
        # Открываем диалоговое окно выбора директории
        folder = QFileDialog.getExistingDirectory(self, 'Выберите папку', '')

        # Если пользователь выбрал директорию, сохраняем путь в переменную
        if folder:
            self.folder_path = folder
            print(folder)

app = QApplication([])
main = MainWindow()
main.show()
sys.exit(app.exec_())
