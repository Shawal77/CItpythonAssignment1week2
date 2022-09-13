#advanced

from PyQt5.QtWidgets import *


def window():
    app = QApplication([])

    wig = QWidget()

    wig.setWindowTitle('Pyqt5 demo')



    wig.show()
    app.exec()

if __name__=='__main__':
    window()
