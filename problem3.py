from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtGui import QIcon

class ImageButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(ImageButton, self).__init__(*args, **kwargs)
        self.setIcon(QIcon("image/Green.png"))
        self.setStyleSheet("QPushButton { background-color: black; color: white; }")
        #self.setIconSize(self.size())

    def enterEvent(self, event):
        self.setIcon(QIcon("image/Green_wer.png"))

    def leaveEvent(self, event):
        self.setIcon(QIcon("image/Green.png"))

app = QApplication([])
button = ImageButton()
button.show()
app.exec_()
