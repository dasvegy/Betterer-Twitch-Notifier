import sys
from PySide6 import QtCore, QtWidgets, QtGui


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


        self.button = QtWidgets.QPushButton("Click me!")
        self.button.setGeometry(20, 20, 20, 20)

        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)


        self.button.clicked.connect(self.magic)



    @QtCore.Slot()
    def magic(self):
        print(f"Sigma")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
