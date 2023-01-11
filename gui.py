from sre_parse import State
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        def button_click(self):
            self.sender().setStyleSheet("background-color : #ffffff")

        self.setWindowTitle("Contributions Pixel Art")
        self.setGeometry(100, 60, 1429, 400)
 
        # widgets = [
        #     QComboBox,
        #     QDateEdit,
        #     QDateTimeEdit,
        #     QLabel,
        #     QPushButton,
        #     QTimeEdit,
        # ]
        i = 1
        j = 1
        day_count = 0
        for i in range(53):
            for j in range(7):
                day_count = day_count + 1
                num = str(day_count)
                newBtn = QPushButton(num, self)
                newBtn.resize(25, 25)
                newBtn.move(i*27, j*27)
                newBtn.show()
                newBtn.clicked.connect(lambda state, x=day_count: button_click(newBtn))
                if(day_count == 365):
                    break
            if(day_count == 365):
                    break

        # for w in widgets:
        #     layout.addWidget(w())


        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        #self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()