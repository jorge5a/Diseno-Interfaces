import sys

from PySide6 import QtWidgets
from red import Red

app = QtWidgets.QApplication(sys.argv)

window = Red()
window.show()

app.exec()