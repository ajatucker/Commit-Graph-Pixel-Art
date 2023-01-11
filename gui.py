from sre_parse import State
from turtle import color
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys
from datetime import datetime
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
    QWidget
)

class CommitList():
   def __init__(self, c_list):
        self.c_list = []
   def add_to_list(self, num):
        self.c_list.append(num)

class CommitSolver():
    def solve_datetime(self, num):
        num.rjust(3 + len(num), '0')
        curr_year = "2023"
        res = datetime.strptime(curr_year + "-" + num, "%Y-%j").strftime("%Y-%m-%d")
        str_res = str(res) + " 20:00"
        return str_res

    #def make_commit(self):


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        def button_click(self):
            print(self.sender().styleSheet())
            style = self.sender().styleSheet()

            if (style == "background-color : #e6eef1") :
                self.sender().setStyleSheet("background-color : #9be9a8")
            elif (style == "background-color : #9be9a8"):
                self.sender().setStyleSheet("background-color : #40c463")
            elif (style == "background-color : #40c463"):
                self.sender().setStyleSheet("background-color : #30a14e")
            elif (style == "background-color : #30a14e"):
                self.sender().setStyleSheet("background-color : #216e39") 
            else:
                self.sender().setStyleSheet("background-color : #e6eef1")

        self.setStyleSheet("background-color : #333333")
        self.setWindowTitle("Contributions Pixel Art")
        self.setGeometry(100, 60, 1429, 400)

        solve = CommitSolver()

        i = 1
        j = 1
        day_count = 0
        for i in range(53):
            for j in range(7):
                day_count = day_count + 1
                newBtn = QPushButton("", self)
                newBtn.resize(25, 25)
                newBtn.move(i*27, j*27)
                newBtn.setStyleSheet("background-color : #e6eef1")
                newBtn.setToolTip(solve.solve_datetime(str(day_count)))
                newBtn.show()
                newBtn.clicked.connect(lambda state, x=day_count: button_click(newBtn))
                if(day_count == 365):
                    break
            if(day_count == 365):
                    break
        
        commitBtn = QPushButton("Commit!", self)
        commitBtn.setStyleSheet("background-color : #4183C4")
        commitBtn.resize(200, 100)
        commitBtn.move(475, 250)
        clearBtn = QPushButton("Clear", self)
        clearBtn.setStyleSheet("background-color : #BD2C00")
        clearBtn.resize(200, 100)
        clearBtn.move(750, 250)

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