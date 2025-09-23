import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QPushButton,
)

app = QApplication([])

# La ventana principal será directamente un QWidget
window = QWidget()
window.setWindowTitle("QHBoxLayout simple")

# Layout horizontal
layout = QHBoxLayout()
layout.addWidget(QPushButton("Left"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Right"))

# Asignar el layout al QWidget
window.setLayout(layout)

window.show()
sys.exit(app.exec())
