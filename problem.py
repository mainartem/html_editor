import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.layout  = QVBoxLayout()
        self.layout.addWidget(MyBar(self))
        self.layout.addStretch(-1)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addStretch(-1)
        self.setFixedSize(800,400)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.label = QLabel(self)
        self.pixmap = QPixmap('image/logo.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(
            self.pixmap.width(),
            self.pixmap.height()
        )


class ImageButtonRed(QPushButton):
    def __init__(self, *args, **kwargs):
        super(ImageButtonRed, self).__init__(*args, **kwargs)
        #self.setIconSize(self.size())
        self.setIcon(QIcon("image/Red.png"))
        self.setStyleSheet("QPushButton { background-color: black; color: white; }")

    def enterEvent(self, event):
        self.setIcon(QIcon("image/Red_wer.png"))

    def leaveEvent(self, event):
        self.setIcon(QIcon("image/Red.png"))


class ImageButtonYellow(QPushButton):
    def __init__(self, *args, **kwargs):
        super(ImageButtonYellow, self).__init__(*args, **kwargs)

        #self.setIconSize(self.size())
        self.setIcon(QIcon("image/Yellow.png"))
        self.setStyleSheet("QPushButton { background-color: black; color: white; }")

    def enterEvent(self, event):
        self.setIcon(QIcon("image/Yellow_wer.png"))

    def leaveEvent(self, event):
        self.setIcon(QIcon("image/Yellow.png"))


class ImageButtonGreen(QPushButton):
    def __init__(self, *args, **kwargs):
        super(ImageButtonGreen, self).__init__(*args, **kwargs)
        #self.setIconSize(self.size())
        self.setIcon(QIcon("image/Green.png"))
        self.setStyleSheet("QPushButton { background-color: black; color: white; }")

    def enterEvent(self, event):
        self.setIcon(QIcon("image/Green_wer.png"))

    def leaveEvent(self, event):
        self.setIcon(QIcon("image/Green.png"))


class MyBar(QWidget):
    def __init__(self, parent):
        super(MyBar, self).__init__()
        self.setWindowIcon(QIcon("image/logo.png"))

        self.parent = parent
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.title = QLabel("My Own Bar")
        self.title.setFixedHeight(35)
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)

        self.title.setStyleSheet("""
            background-color: black;
            color: white;
        """)

        # Добавляем кнопки закрытия, сворачивания и развертывания
        self.close_button = ImageButtonRed()
        self.close_button.clicked.connect(self.parent.close)
        self.layout.addWidget(self.close_button)

        self.minimize_button = ImageButtonYellow()
        self.minimize_button.clicked.connect(self.parent.showMinimized)
        self.layout.addWidget(self.minimize_button)

        def showMaximizedClick():
            if self.parent.windowState():
                self.parent.showNormal()
            else:
                self.parent.showMaximized()

        self.maximize_button = ImageButtonGreen()#.setIcon(QIcon("image/Green.png"))
        self.maximize_button.clicked.connect(showMaximizedClick)
        self.layout.addWidget(self.maximize_button)

        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.pressing = False

    def resizeEvent(self, QResizeEvent):
        super(MyBar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.move(self.mapToGlobal(self.movement))
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
