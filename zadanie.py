from PyQt6 import QtWidgets, QtGui, QtCore
import sys

class AppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # window settings
        self.setWindowTitle("Path finding with bolid")
        self.setFixedSize(1400, 750)



def main():
    app = QtWidgets.QApplication(sys.argv)
    view = AppWindow()
    view.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
