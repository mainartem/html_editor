from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QPushButton
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создайте виджет-панель
        self.dock = QDockWidget("Dock", self)

        # Создайте кнопку
        self.button = QPushButton("Hello, World!", self)

        # Установите виджет в виджет-панель
        self.dock.setWidget(self.button)
        self.dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        self.dock.setMaximumSize(50, 100000)
        # https://youtu.be/Y6_vNgSyQtU?si=PpfXj1P5r3eQ-SG-

        # Удалите кнопку закрытия и сворачивания
        self.dock.setFeatures(QDockWidget.DockWidgetMovable)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
