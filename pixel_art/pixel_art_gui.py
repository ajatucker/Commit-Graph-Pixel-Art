from sre_parse import State
from turtle import color
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys
from pixel_art_logic import *
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


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        def button_commit(self, b_list, sol):
            for b in b_list:
                style = b.styleSheet()
                loop_num = 0

                if (style == "background-color : #9be9a8") :
                    print("commit once")
                elif (style == "background-color : #40c463"):
                    loop_num = 4
                elif (style == "background-color : #30a14e"):
                    loop_num = 9
                elif (style == "background-color : #216e39"):
                    loop_num = 14
                
                commits = CommitList()
                commits.build_list(loop_num, b)

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

        def button_clear(self, b_list):
            print("Cleared")
            for b in b_list:
                b.setStyleSheet("background-color : #e6eef1")


        self.setStyleSheet("background-color : #333333")
        self.setWindowTitle("Contributions Pixel Art")
        self.setGeometry(100, 60, 1429, 400)


        solve = CommitSolver()

        button_list = []
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
                button_list.append(newBtn)
                if(day_count == 365):
                    break
            if(day_count == 365):
                    break
        
        commitBtn = QPushButton("Commit!", self)
        commitBtn.clicked.connect(lambda state, x=button_list: button_commit(commitBtn, button_list, solve))
        commitBtn.setStyleSheet("background-color : #4183C4")
        commitBtn.resize(200, 100)
        commitBtn.move(475, 250)
        clearBtn = QPushButton("Clear", self)
        clearBtn.clicked.connect(lambda state, x=button_list: button_clear(clearBtn, button_list))
        clearBtn.setStyleSheet("background-color : #BD2C00")
        clearBtn.resize(200, 100)
        clearBtn.move(750, 250)

        # for w in widgets:
        #     layout.addWidget(w())


        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        #self.setCentralWidget(widget)
