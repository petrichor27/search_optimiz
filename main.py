# -*- coding: utf-8 -*-
# pyuic5 -x main_form.ui -o name.py


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
import numpy as np
import sys
from lab1_gradient import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1235, 860)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_plot = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_plot.setEnabled(True)
        self.groupBox_plot.setGeometry(QtCore.QRect(20, 10, 861, 831))
        self.groupBox_plot.setObjectName("groupBox_plot")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(910, 50, 301, 41))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(910, 20, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(910, 130, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label_function = QtWidgets.QLabel(self.centralwidget)
        self.label_function.setGeometry(QtCore.QRect(910, 170, 241, 50))
        self.label_function.setText("")
        self.label_function.setObjectName("label_function")
        self.pushButton_create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create.setGeometry(QtCore.QRect(970, 250, 131, 71))
        self.pushButton_create.setObjectName("pushButton_create")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(920, 410, 141, 41))
        self.label_3.setObjectName("label_3")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(900, 470, 321, 371))
        self.label_result.setText("")
        self.label_result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_result.setObjectName("label_result")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Методы поисковой оптимизации"))
        self.groupBox_plot.setTitle(_translate("MainWindow", "График"))
        self.label.setText(_translate("MainWindow", "Метод:"))
        self.label_2.setText(_translate("MainWindow", "Функция:"))
        self.pushButton_create.setText(_translate("MainWindow", "Построить\n"
"график"))
        self.label_3.setText(_translate("MainWindow", "Результаты:"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.gridlayout = None
        self.setupUi(self)
        self.pushButton_create.clicked.connect(self.buttonCreate_clicked)
        self.fig = Figure(figsize=(5, 3))
        self.canvas = FigureCanvas(self.fig)
        llayout = QVBoxLayout(self.groupBox_plot)
        llayout.addWidget(self.canvas, 88)
        methods = ['Выбрать','Метод градиентного спуска','Какой-то еще метод']
        self.comboBox.clear()
        self.comboBox.addItems(methods)
        self.comboBox.activated.connect(self.comboBox_activated)

    def comboBox_activated(self):
        index = self.comboBox.currentIndex()
        if index == 1:
            self.label_function.setText(GradientMethod.fun_text())

    def plot_surface(self,X,Y,Z,tochka):
        self.set_canvas_table_configuration(len(X[0]), (X[0], Y[0], Z[0]))
        self._ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap="viridis", edgecolor="none")
        self._ax.scatter(tochka[0], tochka[1], tochka[2], color="r", linewidth=2);
        self.canvas.draw()

    def buttonCreate_clicked(self):
        index = self.comboBox.currentIndex()
        x,y,z = [],[],[]
        tochka = []
        if index == 1:
            g = GradientMethod()
            x,y,z = g.graph()
            tochka,result_text = g.method()
            self.label_result.setText(result_text)

        self.plot_surface(x,y,z,tochka)
        self._ax.view_init(30, 30)
        self.show() 

    def set_canvas_table_configuration(self, row_count, data):
        self.fig.set_canvas(self.canvas)
        self._ax = self.canvas.figure.add_subplot(projection="3d")
        self._ax.set_xlabel("X")
        self._ax.set_ylabel("Y")
        self._ax.set_zlabel("Z")
   

class Canvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=1, height=1, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(Canvas, self).__init__(fig)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
