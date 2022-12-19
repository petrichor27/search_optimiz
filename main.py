# -*- coding: utf-8 -*-
# pyuic5 -x main_form.ui -o name.py
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib import rcParams
import numpy as np
import sys
from lab1_gradient import *
from lab2_simplix import *
from lab3_ga import *
from lab4_funcs import *
from lab5_pybee import *
from lab5_funcs import *
from lab6_immune_network import *
from lab7_bacteria import *
from lab8_immune_network import *
from lab8_bacteria import *

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
        self.label_2.setGeometry(QtCore.QRect(910, 90, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label_function = QtWidgets.QLabel(self.centralwidget)
        self.label_function.setGeometry(QtCore.QRect(910, 130, 270, 120))
        self.label_function.setText("")
        self.label_function.setObjectName("label_function")
        self.pushButton_create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create.setGeometry(QtCore.QRect(970, 320, 131, 71))
        self.pushButton_create.setObjectName("pushButton_create")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(920, 410, 141, 41))
        self.label_3.setObjectName("label_3")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(900, 470, 321, 371))
        self.label_result.setText("")
        self.label_result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_result.setObjectName("label_result")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(1130, 280, 81, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.hide()
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(910, 280, 210, 21))
        self.label_4.setObjectName("label_4")
        self.label_4.hide()
        self.comboBox_lab4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_lab4.setGeometry(QtCore.QRect(910, 130, 301, 41))
        self.comboBox_lab4.setObjectName("comboBox_lab4")
        self.comboBox_lab4.hide()
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(910, 200, 210, 21))
        self.label_5.setObjectName("label_5")
        self.label_5.hide()
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(1130, 200, 81, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.hide()
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(910, 280, 215, 71))
        self.label_6.setObjectName("label_6")
        self.label_6.hide()
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(1130, 300, 81, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.hide()
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(910, 350, 210, 71))
        self.label_7.setObjectName("label_7")
        self.label_7.hide()
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(1130, 370, 81, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_4.hide()
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(910, 420, 210, 71))
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setObjectName("label_8")
        self.label_8.hide()
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(1130, 440, 81, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_5.hide()
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_plot.setTitle(_translate("MainWindow", "GroupBox"))
        self.label.setText(_translate("MainWindow", "Метод:"))
        self.label_2.setText(_translate("MainWindow", "Функция:"))
        self.pushButton_create.setText(_translate("MainWindow", "Построить\nграфик"))
        self.label_3.setText(_translate("MainWindow", "Результаты:"))
        self.label_4.setText(_translate("MainWindow", "Количество поколений:"))
        self.textEdit.setText(_translate("MainWindow", "50"))



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.gridlayout = None
        self.base_parametrs_for_form()


    def base_parametrs_for_form(self):
        self.setupUi(self)
        rcParams['font.family'] = 'Segoe Print'
        rcParams['font.size'] = 12
        self.pushButton_create.clicked.connect(self.buttonCreate_clicked)
        self.fig = Figure(figsize=(5, 3))
        self.canvas = FigureCanvas(self.fig)
        llayout = QVBoxLayout(self.groupBox_plot)
        llayout.addWidget(self.canvas, 88)
        methods = ['Выбрать','Метод градиентного спуска','Симплекс-метод','Генетический алгоритм','Алгоритм роя частиц','Пчелиный алгоритм','Искусственная иммунная сеть','Бактериальный алгоритм','Гибридный алгоритм']
        self.comboBox.clear()
        self.comboBox.addItems(methods)
        self.comboBox.activated.connect(self.comboBox_activated)


    def comboBox_activated(self):
        index = self.comboBox.currentIndex()
        if index == 1:
            self.base_parametrs_for_form()
            self.comboBox.setCurrentIndex(index)
            self.label_function.setText(GradientMethod.fun_text())
        elif index == 2:
            self.base_parametrs_for_form()
            self.comboBox.setCurrentIndex(index)
            self.label_function.setText(SimplixMethod.fun_text())
        elif index == 3:
            self.base_parametrs_for_form()
            self.comboBox.setCurrentIndex(index)
            self.label_function.setText(GA.fun_text())
            self.textEdit.show()
            self.label_4.show()
        elif index == 4:
            self.base_parametrs_for_form()
            self.comboBox.setCurrentIndex(index)
            self.pushButton_create.setGeometry(QtCore.QRect(970, 500, 131, 71))
            self.label_3.setGeometry(QtCore.QRect(910, 590, 141, 41))
            self.label_result.setGeometry(QtCore.QRect(900, 630, 321, 221))
            self.textEdit.setGeometry(QtCore.QRect(1130, 240, 81, 31))
            self.label_4.setGeometry(QtCore.QRect(910, 240, 210, 21))
            self.comboBox_lab4.clear()
            self.comboBox_lab4.addItems(['Функция сферы','Функция Швефеля','Функция Растригина'])
            self.comboBox_lab4.show()
            self.label_5.setText("Количество частиц:")
            self.label_6.setText("Коэфф.текущей\nскорости:")
            self.label_7.setText("Коэфф.собственного\nлучшего значения:")
            self.label_8.setText("Коэфф.глобального\nлучшего значения:")
            self.label_4.show()
            self.label_5.show()
            self.label_6.show()
            self.label_7.show()
            self.label_8.show()
            self.textEdit_3.setText("0.1")
            self.textEdit_2.setText("50")
            self.textEdit_4.setText("1.0")
            self.textEdit_5.setText("5.0")
            self.textEdit.show()
            self.textEdit_2.show()
            self.textEdit_3.show()
            self.textEdit_4.show()
            self.textEdit_5.show()
        elif index == 5: 
            self.base_parametrs_for_form()
            self.comboBox.setCurrentIndex(index)
            self.pushButton_create.setGeometry(QtCore.QRect(970, 500, 131, 71))
            self.label_3.setGeometry(QtCore.QRect(910, 590, 141, 41))
            self.label_result.setGeometry(QtCore.QRect(900, 630, 321, 221))
            self.textEdit.setGeometry(QtCore.QRect(1130, 240, 81, 31))
            self.label_4.setGeometry(QtCore.QRect(910, 240, 210, 21))
            self.comboBox_lab4.clear()
            self.comboBox_lab4.addItems(['Функция Химмельблау','Функция Растригина','Функция Розенброка'])
            self.comboBox_lab4.show()
            self.label_4.setText("Количество итераций:")
            self.label_5.setText("Кол-во разведчиков:")
            self.label_6.setText("Количество пчел\nдля лучших участков:")
            self.label_7.setText("Количество пчел для\nост.выбр. участков:")
            self.label_4.show()
            self.label_5.show()
            self.label_6.show()
            self.label_7.show()
            self.textEdit_3.setText("5")
            self.textEdit_2.setText("50")
            self.textEdit_4.setText("15")
            self.textEdit.show()
            self.textEdit_2.show()
            self.textEdit_3.show()
            self.textEdit_4.show()
        
        elif index == 6:
            self.base_parametrs_for_form()
            self.comboBox.setCurrentIndex(index)
            self.pushButton_create.setGeometry(QtCore.QRect(970, 500, 131, 71))
            self.label_3.setGeometry(QtCore.QRect(910, 590, 141, 41))
            self.label_result.setGeometry(QtCore.QRect(900, 630, 321, 221))
            self.textEdit.setGeometry(QtCore.QRect(1130, 240, 81, 31))
            self.label_4.setGeometry(QtCore.QRect(910, 240, 210, 21))
            self.label_function.setGeometry(QtCore.QRect(910, 130, 301, 60))
            self.label_function.setText('F(x,y) = (1-x1)**2 +\n100*(x2-x1*x1)**2') #910, 130, 301, 41
            self.label_4.setText("Количество антител:")
            self.label_5.setText("Количество поколений:")
            self.label_6.setText("Количество антигенов:")
            self.label_7.setText("Пороговый коэфф\nгибели антител:")
            self.label_8.setText("Пороговый коэфф\nсжатия сети:")
            self.label_4.show()
            self.label_5.show()
            self.label_6.show()
            self.label_7.show()
            self.label_8.show()
            self.textEdit_3.setText("20")
            self.textEdit_2.setText("50")
            self.textEdit_4.setText("10")
            self.textEdit_5.setText("10")
            self.textEdit.show()
            self.textEdit_2.show()
            self.textEdit_3.show()
            self.textEdit_4.show()
            self.textEdit_5.show()

        elif index == 7:
            self.base_parametrs_for_form()
            self.comboBox.setCurrentIndex(index)
            self.pushButton_create.setGeometry(QtCore.QRect(970, 500, 131, 71))
            self.label_3.setGeometry(QtCore.QRect(910, 590, 141, 41))
            self.label_result.setGeometry(QtCore.QRect(900, 630, 321, 221))
            self.textEdit.setGeometry(QtCore.QRect(1130, 240, 81, 31))
            self.label_4.setGeometry(QtCore.QRect(910, 240, 210, 21))
            self.label_function.setGeometry(QtCore.QRect(910, 130, 301, 60))
            self.label_function.setText('F(x,y) = -(x1**2 + x2**2)') #910, 130, 301, 41
            self.label_4.setText("Количество бактерий:")
            self.label_5.setText("Количество поколений:")
            self.label_6.setText("Количество бактерий\nдля ликвидации:")
            self.label_7.setText("Вероятность\nликвидации бактерии:")
            self.label_8.setText("Количество поколений\nс ухудшением функции:")
            self.label_4.show()
            self.label_5.show()
            self.label_6.show()
            self.label_7.show()
            self.label_8.show()
            self.textEdit_3.setText("20")
            self.textEdit_2.setText("100")
            self.textEdit_4.setText("0.7")
            self.textEdit_5.setText("5")
            self.textEdit.show()
            self.textEdit_2.show()
            self.textEdit_3.show()
            self.textEdit_4.show()
            self.textEdit_5.show()

        elif index == 8:
            self.base_parametrs_for_form()
            self.comboBox.setCurrentIndex(index)
            self.pushButton_create.setGeometry(QtCore.QRect(970, 500, 131, 71))
            self.label_3.setGeometry(QtCore.QRect(910, 590, 141, 41))
            self.label_result.setGeometry(QtCore.QRect(900, 630, 321, 221))
            self.textEdit.setGeometry(QtCore.QRect(1130, 240, 81, 31))
            self.label_4.setGeometry(QtCore.QRect(910, 200, 210, 51))
            self.label_5.setGeometry(QtCore.QRect(910, 260, 210, 51))
            self.label_6.setGeometry(QtCore.QRect(910, 320, 215, 71))
            self.label_7.setGeometry(QtCore.QRect(910, 380, 210, 71))
            self.label_8.setGeometry(QtCore.QRect(910, 420, 210, 71))
            self.label_function.setGeometry(QtCore.QRect(910, 130, 301, 60))
            self.textEdit.setGeometry(QtCore.QRect(1130, 210, 81, 31))
            self.textEdit_2.setGeometry(QtCore.QRect(1130, 270, 81, 31))
            self.textEdit_3.setGeometry(QtCore.QRect(1130, 340, 81, 31))
            self.textEdit_4.setGeometry(QtCore.QRect(1130, 400, 81, 31))
            self.textEdit_5.setGeometry(QtCore.QRect(1130, 440, 81, 31))
            self.label_function.setText('(x1*x1 + x2 - 11)**2 +\n(x1 + x2*x2 - 7)**2')
            self.label_4.setText("Количество поколений\nдля иммунной сети:")
            self.label_5.setText("Количество поколений\nдля бакт.алгоритма:")
            self.label_6.setText("Количество лучших\nантител:")
            self.label_7.setText("Количество бактерий\nна 1 антитело:")
            self.label_8.setText("Количество антител:")
            self.label_4.show()
            self.label_5.show()
            self.label_6.show()
            self.label_7.show()
            self.label_8.show()
            self.textEdit.setText("50")
            self.textEdit_2.setText("50")
            self.textEdit_3.setText("5")
            self.textEdit_4.setText("4")
            self.textEdit_5.setText("30")
            self.textEdit.show()
            self.textEdit_2.show()
            self.textEdit_3.show()
            self.textEdit_4.show()
            self.textEdit_5.show()

    def plot_surface(self,X,Y,F,point):
        self.set_canvas_table_configuration(len(X[0]), (X[0], Y[0], F[0]))
        self._ax.plot_surface(X, Y, F, rstride=1, cstride=1, cmap="viridis", alpha=0.7, edgecolor="none")
        if point != []:
            self._ax.scatter(point[0], point[1], point[2], color="r", linewidth=2);
            self.canvas.draw()


    def ga_iter(self):
        if self.generation < self.steps:
            self.fig.clf()
            self.plot_surface(self.x,self.y,self.f,[])
            self.population = self.g.method(self.population)
            self.generation += 1 
            res = []
            best = self.population[0][0]
            for i in self.population:
                for j in i:
                    res.append(j)
                    if GA.fun(best[0],best[1]) > GA.fun(j[0],j[1]):
                        best = j

            result_text = 'Самая приспособленная особь:\nx = ' + str(round(best[0],3)) + '\ny = ' + str(round(best[1],3)) + '\nf(x,y) = ' + str(round(GA.fun(best[0],best[1]),3)) + '\n Поколение ' + str(self.generation)
            self.label_result.setText(result_text)
            self._ax.set_xlim(-2,2)
            self._ax.set_ylim(-2,4)
            self._ax.set_zlim(-1,3500)

            for point in res:
                self._ax.scatter(point[0], point[1], GA.fun(point[0],point[1]), color="r", linewidth=2)
            self.canvas.draw()

    def swarm_lab4_iter(self):
        if self.iterCount >= self.tempIter:
            self.fig.clf()
            self.plot_surface(self.x,self.y,self.f,[])
            self.label_result.setText('Итерация: ' + str(self.tempIter) + '\nЛучшая позиция:\nx1 = ' + str(round(self.g.globalBestPosition[0],3)) + '\nx2 = ' + str(round(self.g.globalBestPosition[1],3)) + '\nf = ' + str(round(self.g.globalBestFinalFunc,3)))
            res = self.g.swarmPositions
            for point in res:
                if self.func == 0:
                    self._ax.scatter(point[0], point[1], Swarm_X2.fun(point[0], point[1]), color="r", linewidth=2)
                elif self.func == 1:
                    self._ax.scatter(point[0], point[1], Swarm_Schwefel.fun(point[0], point[1]), color="r", linewidth=2)
                elif self.func == 2:
                    self._ax.scatter(point[0], point[1], Swarm_Rastrigin.fun(point[0], point[1]), color="r", linewidth=2)
            self.canvas.draw()
            self.g.nextIteration()
            self.tempIter += 1
    
    def bee_lab5_iter(self):
        if self.iterCount >= self.tempIter:
            self.fig.clf()
            self.plot_surface(self.x,self.y,self.f,[])
            self.currhive.nextstep()
            if self.currhive.bestfitness != self.best_func:
                self.best_func = self.currhive.bestfitness
                self.func_counter = 0

            else:
                self.func_counter += 1
                if self.func_counter == self.max_func_counter:
                    self.currhive.range = [self.currhive.range[m] * self.koeff[m] for m in range(len(self.currhive.range))]
                    self.func_counter = 0

            self.label_result.setText('Итерация: ' + str(self.tempIter) + '\nЛучшая позиция:\nx1 = ' + str(round(self.currhive.bestposition[0],3))+ '\nx2 = ' + str(round(self.currhive.bestposition[1],3)) + '\nf(x,y) = ' + str(round(-self.currhive.bestfitness,3)))

            res = self.currhive.positions()
            for point in res:
                if point[2] == self.currhive.bestfitness and point[0] == self.currhive.bestposition[0] and point[1] == self.currhive.bestposition[1]:
                    self._ax.scatter(point[0], point[1], -point[2], color="black", linewidth=3)
                else:
                    self._ax.scatter(point[0], point[1], -point[2], color="r", linewidth=2)

            self.canvas.draw()
            self.tempIter += 1

    def imm_lab6_iter(self):
        if self.iterCount >= self.tempIter:
            self.fig.clf()
            self.plot_surface(self.x,self.y,self.f,[])
            self.net.next_iteration()
            self.label_result.setText('Итерация: ' + str(self.tempIter) + '\nЛучшая позиция:\nx1 = ' + str(round(self.net.best_cell.position[0],3)) + '\nx2 = ' + str(round(self.net.best_cell.position[1],3)) + '\nf = ' + str(round(self.net.best_cell.fitness,3)))
            antibody = self.net.get_antibody_positions()
            antigen = self.net.get_antigen_positions()
            for point in antibody:
                if point[0] == self.net.best_cell.position[0] and point[1] == self.net.best_cell.position[1] and point[2] == self.net.best_cell.fitness:
                    self._ax.scatter(point[0], point[1], point[2], color="black", linewidth=4)
                else:
                    self._ax.scatter(point[0], point[1], point[2], color="red", linewidth=2)
            for point in antigen:
                self._ax.scatter(point[0], point[1], point[2], color="yellow", linewidth=2)

            self.canvas.draw()
            self.tempIter += 1

    def bact_lab7_iter(self):
        if self.iterCount >= self.tempIter:
            self.fig.clf()
            self.plot_surface(self.x,self.y,self.f,[])
            self.bact.next_iteration()
            self.label_result.setText('Итерация: ' + str(self.tempIter) + '\nЛучшая позиция:\nx1 = ' + str(round(self.bact.best_bacterium.position[0],3)) + '\nx2 = ' + str(round(self.bact.best_bacterium.position[1],3)) + '\nf = ' + str(round(self.bact.best_bacterium.fitness,3)))
            bacteria = self.bact.get_positions()

            for point in bacteria:
                if point[0] == self.bact.best_bacterium.position[0] and point[1] == self.bact.best_bacterium.position[1] and point[2] == self.bact.best_bacterium.fitness:
                    self._ax.scatter(point[0], point[1], point[2], color="black", linewidth=4)
                    # print(point)
                else:
                    self._ax.scatter(point[0], point[1], point[2], color="red", linewidth=2)


            self.canvas.draw()
            self.tempIter += 1

    def imm_lab8_iter(self):
        if self.iterCount_for_imm >= self.tempIter:
            self.fig.clf()
            self.plot_surface(self.x,self.y,self.f,[])
            self.population_of_antibodies = self.net.create_memory_cells(self.population_of_antibodies, self.population_of_antigens)
            self.label_result.setText('Этап искусственной иммунной\nсети\nИтерация: ' + str(self.tempIter))

            for point in self.population_of_antibodies.to_list():
                self._ax.scatter(point[0], point[1], HimmelblauBacterium.fun(point[0], point[1]), color="red", linewidth=2)
            for point in self.population_of_antigens.to_list():
                self._ax.scatter(point[0], point[1], HimmelblauBacterium.fun(point[0], point[1]), color="yellow", linewidth=2)
            self.canvas.draw()
            self.tempIter += 1

        elif self.tempIter2 == 0: 
            self.best_imm = self.find_n_best(HimmelblauBacterium.fun,self.population_of_antibodies.to_list(),self.count_of_best_imm)
            self.bact = BacteriaAlgoritm2(HimmelblauBacterium,self.best_imm,self.count_of_bact_for_one_imm,self.count_error,self.radius)
            self.tempIter2 += 1

        else:
            if self.iterCount_for_bact >= self.tempIter2:
                self.fig.clf()
                self.plot_surface(self.x,self.y,self.f,[])
                self.bact.next_iteration()
                self.label_result.setText('Этап бактериального алгоритма\nИтерация: ' + str(self.tempIter2) + '\nЛучшая позиция:\nx1 = ' + str(round(self.bact.best_bacterium.position[0],3)) + '\nx2 = ' + str(round(self.bact.best_bacterium.position[1],3)) + '\nf = ' + str(round(self.bact.best_bacterium.fitness,3)))
                bacteria = self.bact.get_positions()

                for point in self.best_imm:
                    self._ax.scatter(point[0], point[1], HimmelblauBacterium.fun(point[0], point[1]), color="green", linewidth=2)
                for point in bacteria:
                    if point[0] == self.bact.best_bacterium.position[0] and point[1] == self.bact.best_bacterium.position[1] and point[2] == self.bact.best_bacterium.fitness:
                        self._ax.scatter(point[0], point[1], point[2], color="black", linewidth=4)
                    else:
                        self._ax.scatter(point[0], point[1], point[2], color="red", linewidth=2)
                self.canvas.draw()
                self.tempIter2 += 1

            else: self.timer.stop()

    def find_n_best(self, f, population, n):
        population.sort(key=lambda x: f(x[0],x[1]), reverse=False)
        return population[:n]

    def buttonCreate_clicked(self):
        index = self.comboBox.currentIndex()
        if index == 1:
            g = GradientMethod()
            x,y,f = g.graph()
            point,result_text = g.method()
            self.label_result.setText(result_text)
            self.plot_surface(x,y,f,point)

        elif index == 2:
            g = SimplixMethod()
            x,y,f = g.graph()
            point,result_text = g.method()
            self.label_result.setText(result_text)
            self.plot_surface(x,y,f,point)

        elif index == 3:
            N = 20
            self.g = GA()
            self.x,self.y,self.f = self.g.graph()
            self.plot_surface(self.x,self.y,self.f,[])
            self.steps = int(self.textEdit.toPlainText())
            self.population = self.g.make_start_population(N)
            self.generation = 0
            self.timer = QtCore.QTimer()
            self.timer.setInterval(100)
            self.timer.timeout.connect(self.ga_iter)
            self.timer.start()

        elif index == 4:
            dimension = 2
            self.func = self.comboBox_lab4.currentIndex()

            obl = 100
            if self.func == 1:
                obl = 500
            elif self.func == 2:
                obl = 5

            self.minvalues = np.array ([-obl] * dimension)
            self.maxvalues = np.array ([obl] * dimension)
            self.iterCount = int(self.textEdit.toPlainText())
            self.swarmsize = int(self.textEdit_2.toPlainText())
            self.currentVelocityRatio = float(self.textEdit_3.toPlainText())
            self.localVelocityRatio = float(self.textEdit_4.toPlainText())
            self.globalVelocityRatio = float(self.textEdit_5.toPlainText())
            
            if self.func == 0:
                self.g = Swarm_X2(self.swarmsize, self.minvalues, self.maxvalues, 
                                self.currentVelocityRatio, self.localVelocityRatio, 
                                self.globalVelocityRatio)
            elif self.func == 1:
                self.g = Swarm_Schwefel(self.swarmsize, self.minvalues, self.maxvalues, 
                                self.currentVelocityRatio, self.localVelocityRatio, 
                                self.globalVelocityRatio)
            elif self.func == 2:
                self.g = Swarm_Rastrigin(self.swarmsize, self.minvalues, self.maxvalues, 
                                self.currentVelocityRatio, self.localVelocityRatio, 
                                self.globalVelocityRatio)
                
            self.x,self.y,self.f = self.g.graph()
            self.plot_surface(self.x,self.y,self.f,[])
            self.tempIter = 1
            self.timer = QtCore.QTimer()
            self.timer.setInterval(50)
            self.timer.timeout.connect(self.swarm_lab4_iter)
            self.timer.start()
                     
        elif index == 5:
            func = self.comboBox_lab4.currentIndex()

            if func == 0:
                bee = Himmelblaybee
            elif func == 1:
                bee = Rastriginbee
            elif func == 2:
                bee = Rosenbrockbee

            # Количество пчел-разведчиков
            scoutbeecount =  int(self.textEdit_2.toPlainText())
            
            # Количество пчел, отправляемых на выбранные, но не лучшие участки
            selectedbeecount = int(self.textEdit_4.toPlainText())
            
            # Количество пчел, отправляемые на лучшие участки
            bestbeecount =  int(self.textEdit_3.toPlainText())
            
            # Количество выбранных, но не лучших, участков
            selsitescount = 10
            
            # Количество лучших участков
            bestsitescount = 5
            
            # Максимальное количество итераций
            self.iterCount =  int(self.textEdit.toPlainText())
            
            # Через такое количество итераций без нахождения лучшего решения уменьшим область поиска
            self.max_func_counter = 10   
            
            # Во столько раз будем уменьшать область поиска
            self.koeff = bee.getrangekoeff()
            
            # Начальное значение целевой функции
            self.best_func = -1.0e9
                
            # Количество итераций без улучшения целевой функции
            self.func_counter = 0

            self.currhive = Hive(scoutbeecount, selectedbeecount, bestbeecount, selsitescount, bestsitescount, bee.getstartrange(), bee)
            self.x,self.y,self.f = bee.graph()
            self.plot_surface(self.x,self.y,self.f,[])

            self.tempIter = 1
            self.timer = QtCore.QTimer()
            self.timer.setInterval(100)
            self.timer.timeout.connect(self.bee_lab5_iter)
            self.timer.start()
        
        elif index == 6:
            g = ImmRosenbrock()
            self.x,self.y,self.f = g.graph()
            self.plot_surface(self.x,self.y,self.f,[])

            count_sb = int(self.textEdit.toPlainText())
            count_sg = int(self.textEdit_3.toPlainText())
            nb = int(count_sb*0.3)
            nc = 2
            bs = 0.5
            bb = int(self.textEdit_4.toPlainText())
            br = int(self.textEdit_5.toPlainText())
            bn = 0.1
            self.net = ImmuneNetwork(ImmRosenbrock,count_sb,count_sg,nb,nc,bs,bb,br,bn)

            self.iterCount = int(self.textEdit_2.toPlainText())
            self.tempIter = 1
            self.timer = QtCore.QTimer()
            self.timer.setInterval(300)
            self.timer.timeout.connect(self.imm_lab6_iter)
            self.timer.start()

        elif index == 7:
            g = HimmelblauBacterium2()
            self.x,self.y,self.f = g.graph()
            self.plot_surface(self.x,self.y,self.f,[])

            count = int(self.textEdit.toPlainText())
            count_e_d = int(self.textEdit_3.toPlainText())
            probability = float(self.textEdit_4.toPlainText())
            count_error = int(self.textEdit_5.toPlainText())
            self.bact = BacteriaAlgoritm(HimmelblauBacterium2,count,count_e_d,probability,count_error)

            self.iterCount = int(self.textEdit_2.toPlainText())
            self.tempIter = 1
            self.timer = QtCore.QTimer()
            self.timer.setInterval(300)
            self.timer.timeout.connect(self.bact_lab7_iter)
            self.timer.start()

        elif index == 8:
            self.iterCount_for_imm = int(self.textEdit.toPlainText())
            self.iterCount_for_bact = int(self.textEdit_2.toPlainText())
            self.count_of_best_imm = int(self.textEdit_3.toPlainText())
            self.count_of_bact_for_one_imm = int(self.textEdit_4.toPlainText())
            
            self.radius = 0.5
            self.count_error = 5
            
            count_sb = int(self.textEdit_5.toPlainText())
            count_sg = 10
            nb = 10
            nd = 5
            nc = 7
            bb = 0.4
            br = 0.4
            
            self.net = ImmuneNetworkAlgorithm(HimmelblauBacterium.fun,nb,nd,nc,bb,br)
            self.x,self.y,self.f = HimmelblauBacterium.graph()
            self.plot_surface(self.x,self.y,self.f,[])

            self.population_of_antibodies, self.population_of_antigens = self.net.immune_network_algorithm_init(-5,5,count_sb,count_sg)

            self.tempIter = 1
            self.tempIter2 = 0
            self.timer = QtCore.QTimer()
            self.timer.setInterval(300)
            self.timer.timeout.connect(self.imm_lab8_iter)
            self.timer.start()

        elif index == 0: 
            result_text = "Нужно выбрать метод!!!"
        
        self.show() 

    def set_canvas_table_configuration(self, row_count, data):
        self.fig.clf()
        self.fig.set_canvas(self.canvas)
        self._ax = self.canvas.figure.add_subplot(projection="3d")
        self._ax.set_xlabel("X")
        self._ax.set_ylabel("Y")
        self._ax.set_zlabel("F(x,y)")
        self._ax.view_init(elev=10., azim=70)
   

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
