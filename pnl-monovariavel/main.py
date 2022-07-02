# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from tkinter import messagebox
from PyQt5 import QtCore, QtGui, QtWidgets
from sqlalchemy import false, true
import math
from re import X
from hamcrest import none
from sympy import *
import numpy as np

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, Qt, QObject
from PyQt5.QtGui import QIcon

def secao_aurea(f, a, b, eps):

    alfa = ((math.sqrt(5)-1)/2)
    beta = 1 - alfa

    mi = a + beta*(b-a)
    l = a + alfa*(b-a)

    i=0
    while (b-a) >= eps:
        i+=1
        if f(mi) > f(l):
            a = mi
            mi = l
            l = a + alfa*(b-a)
        else:
            b = l
            l = mi
            mi = a + beta*(b-a)
        
    return [(a+b)/2,i]

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def busca_fibonacci(f, a, b, eps):
    Fn = (b-a)/eps
    fibo = []
    fibo.append(1)
    fibo.append(1)

    n=1
   
    while true:
        n += 1
        fibo.append(fibonacci(n))
        
        if fibo[n] > Fn:
            break
    
    mi = a + (fibo[n-2]/fibo[n])*(b-a)
    l = a + (fibo[n-1]/fibo[n])*(b-a)
    k=0
    for k in range(n-2):
        if f(mi) > f(l):
            a = mi
            mi = l
            l = a + (fibo[n-k-1]/fibo[n-k])*(b-a)
        else:
            b = l
            l = mi
            mi = a + (fibo[n-k-2]/fibo[n-k])*(b-a)
    
    return [(a+b)/2,k]

def busca_dicotomica(f, a, b, delta, eps):
    i=1
    while (b-a) >= eps:
        x = ((a+b)/2) - delta
        z = ((a+b)/2) + delta
        if f(x) > f(z):
            a = x
        else:
            b = z
        i += 1

    return [(a+b)/2,i]

def busca_uniforme(f, a, b, delta):
    x0 = a
    k=1
    while true:
        x1 = x0 + delta
        if f(x1) < f(x0):
            break
    delta = delta/10
    while true:
        x1 = x0 + delta
        if f(x1) < f(x0):
            break
    return 

def bissecao(f, a, b, eps):  
    i = 1  
    fa = f(a)  
    while True:  
        #iteracao da bissecao  
        p = a + (b-a)/2  
        fp = f(p)  
        #condicao de parada  
        if ((fp == 0) or ((b-a)/2 < eps)):  
            return p  
        #bissecta o intervalo  
        i = i+1  
        if (fa * fp > 0):  
            a = p  
            fa = fp  
        else:  
            b = p  

# f = funcao,df = derivada da funcao, x0 = valor inicial, eps = delta, itmax = max de it
def newton(f,a,b,eps):
    x = Symbol('x')
    i=0
    iteracao=0
    while True:
        raiz=a
        if f.diff(x)(raiz) != 0: # se a derivada for zero sai    
            raiz=raiz-f(raiz)/f.diff(x)(raiz)
            erro=raiz-a
            a=raiz
            iteracao=i
        else:
            break
        if abs(erro) <= eps:
            break
        i+=1
    if iteracao > i:
        iteracao = 0.25
    elif iteracao == i:
        iteracao = 0.75
    return [raiz, erro, iteracao]

###############################################################################################################

class Ui_mainWindow(object):

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(585, 687)
        mainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.botao_calcular = QtWidgets.QPushButton(self.centralwidget)
        self.botao_calcular.setGeometry(QtCore.QRect(430, 430, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.botao_calcular.setFont(font)
        self.botao_calcular.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_calcular.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.botao_calcular.setAutoRepeat(True)
        self.botao_calcular.setAutoDefault(True)
        self.botao_calcular.setDefault(False)
        self.botao_calcular.setFlat(False)
        self.botao_calcular.setObjectName("botao_calcular")
        self.metodos = QtWidgets.QComboBox(self.centralwidget)
        self.metodos.setGeometry(QtCore.QRect(310, 210, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.metodos.setFont(font)
        self.metodos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.metodos.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.metodos.setObjectName("metodos")
        self.metodos.addItem("")
        self.metodos.addItem("")
        self.metodos.addItem("")
        self.metodos.addItem("")
        self.metodos.addItem("")
        self.metodos.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 390, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 220, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-20, -10, 621, 211))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 280, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 280, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 340, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.form_e = QtWidgets.QLineEdit(self.centralwidget)
        self.form_e.setGeometry(QtCore.QRect(170, 340, 121, 31))
        self.form_e.setObjectName("form_e")
        self.form_a = QtWidgets.QLineEdit(self.centralwidget)
        self.form_a.setGeometry(QtCore.QRect(120, 280, 61, 31))
        self.form_a.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.form_a.setObjectName("form_a")
        self.form_func = QtWidgets.QLineEdit(self.centralwidget)
        self.form_func.setGeometry(QtCore.QRect(70, 430, 331, 41))
        self.form_func.setObjectName("form_func")
        self.form_b = QtWidgets.QLineEdit(self.centralwidget)
        self.form_b.setGeometry(QtCore.QRect(280, 280, 61, 31))
        self.form_b.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.form_b.setObjectName("form_b")
        self.out_x = QtWidgets.QLineEdit(self.centralwidget)
        self.out_x.setGeometry(QtCore.QRect(130, 570, 331, 41))
        self.out_x.setObjectName("out_x")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 490, 591, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 580, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 630, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.out_i = QtWidgets.QLineEdit(self.centralwidget)
        self.out_i.setGeometry(QtCore.QRect(200, 620, 91, 41))
        self.out_i.setObjectName("out_i")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(310, 320, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.form_delta = QtWidgets.QLineEdit(self.centralwidget)
        self.form_delta.setGeometry(QtCore.QRect(430, 340, 121, 31))
        self.form_delta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.form_delta.setObjectName("form_delta")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(130, 510, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        #Janela c tamanho fixo
        mainWindow.setFixedSize(mainWindow.width(), mainWindow.height())

        #Desabilita area de output
        self.out_i.setEnabled(False)
        self.out_x.setEnabled(False)

       #Combo box atualiza os campos para parametros dos metodos
        #self.metodos.currentIndexChanged.connect(self.modificar_campos)
        #self.botao_calcular.clicked.connect(self.calcular)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        def modificar_campos(self):
            if self.metodos.currentText() == "Busca Uniforme":
                self.form_e.setEnabled(False)
            elif(self.metodos.currentText()) == "Busca Dicotômica":
                self.form_delta.setEnabled(True)
            elif(self.metodos.currentText()) == "Seção Áurea":
                self.form_delta.setEnabled(False)
            elif(self.metodos.currentText()) == "Busca de Fibonacci":
                self.form_delta.setEnabled(False)
            elif(self.metodos.currentText()) == "Bisseção":
                self.form_delta.setEnabled(False)
            elif(self.metodos.currentText()) == "Newton":
                self.form_delta.setEnabled(False)
        
        #Calcula pelo metodo escolhido no combo box
       
        def calcular(self):

            ops = self.metodos.currentText()
            
            if (ops == "Busca Uniforme"):
                try:
                    f = self.form_func.text()
                    a = float(self.form_a.text())
                    b = float(self.form_b.text())
                    delta = float(self.form_delta.text())

                    resp = busca_uniforme(f,a,b,delta)
                    self.out_x.setText(self.out_x.text()+resp)
                    self.out_i.setText(resp)

                except ValueError:
                    messagebox.showwarning('Erro ao calcular!')

            elif ops == 2:
                try:
                    f = self.form_func.text()
                    a = float(self.form_a.text())
                    b = float(self.form_b.text())
                    delta = float(self.form_delta.text())
                    eps = float(self.form_e.text())

                    resp = busca_dicotomica(f,a,b,delta,eps)
                    self.out_x.setText(resp[0])
                    self.out_i.setText(resp[1])
                except ValueError:
                    messagebox.showwarning('Erro ao calcular!')

            elif ops == 3:
                try:
                    f = self.form_func.text()
                    a = float(self.form_a.text())
                    b = float(self.form_b.text())
                    eps = float(self.form_e.text())

                    resp = secao_aurea(f,a,b,delta,eps)
                    self.out_x.setText(resp[0])
                    self.out_i.setText(resp[1])
                except ValueError:
                    messagebox.showwarning('Erro ao calcular!')

            elif ops == 4:
                try:
                    f = self.form_func.text()
                    a = float(self.form_a.text())
                    b = float(self.form_b.text())
                    delta = float(self.form_delta.text())
                
                    resp = busca_fibonacci(f,a,b,delta)
                    self.out_x.setText(resp[0])
                    self.out_i.setText(resp[1])
                except ValueError:
                    messagebox.showwarning('Erro ao calcular!')

            elif ops == 5:
                try:
                    f = self.form_func.text()
                    a = float(self.form_a.text())
                    b = float(self.form_b.text())
                    eps = float(self.form_e.text())

                    resp = busca_uniforme(f,a,b,eps)
                    self.out_x.setText(resp[0])
                    self.out_i.setText(resp[1])
                except ValueError:
                    messagebox.showwarning('Erro ao calcular!')

            elif ops == 6:
                try:
                    f = self.form_func.text()
                    a = float(self.form_a.text())
                    b = float(self.form_b.text())
                    eps = float(self.form_e.text())

                    resp = busca_uniforme(f,a,b,eps)
                    self.out_x.setText(resp[0])
                    self.out_i.setText(resp[1])
                except ValueError:
                    messagebox.showwarning('Erro ao calcular!')

        

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "PNL : MONOVARIÁVEL"))
        self.botao_calcular.setText(_translate("mainWindow", "Calcular"))
        self.metodos.setItemText(0, _translate("mainWindow", "Busca Uniforme"))
        self.metodos.setItemText(1, _translate("mainWindow", "Busca Dicotômica"))
        self.metodos.setItemText(2, _translate("mainWindow", "Seção Áurea"))
        self.metodos.setItemText(3, _translate("mainWindow", "Busca de Fibonacci"))
        self.metodos.setItemText(4, _translate("mainWindow", "Bisseção"))
        self.metodos.setItemText(5, _translate("mainWindow", "Newton"))
        self.label.setText(_translate("mainWindow", "<html><head/><body><p>Min f(x) = Exemplo: 3*x**2+2*x-4</p></body></html>"))
        self.label_2.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Selecione o método:</span></p></body></html>"))
        self.label_3.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">PO II - T1</span></p><p align=\"center\">PROGRAMAÇÃO NÃO LINEAR:</p><p align=\"center\">MONOVARIÁVEL</p></body></html>"))
        self.label_4.setText(_translate("mainWindow", "<html><head/><body><p>s.a:</p></body></html>"))
        self.label_5.setText(_translate("mainWindow", "<html><head/><body><p>&lt;= x &lt;=</p></body></html>"))
        self.label_6.setText(_translate("mainWindow", "<html><head/><body><p>Com  E =</p></body></html>"))
        self.form_e.setToolTip(_translate("mainWindow", "Tolerância"))
        self.form_a.setToolTip(_translate("mainWindow", "a"))
        self.form_func.setToolTip(_translate("mainWindow", "Função Objetivo"))
        self.form_b.setToolTip(_translate("mainWindow", "b"))
        self.out_x.setToolTip(_translate("mainWindow", "Ponto mínimo"))
        self.label_7.setText(_translate("mainWindow", "x* ="))
        self.label_8.setText(_translate("mainWindow", "Iterações  = "))
        self.out_i.setToolTip(_translate("mainWindow", "Número de Iterações"))
        self.label_9.setText(_translate("mainWindow", "<html><head/><body><p>Com <a name=\"firstHeading\"/><span style=\" font-family:\'Linux Libertine\',\'Georgia\',\'Times\',\'serif\'; font-size:xx-large; color:#000000; background-color:#ffffff;\">Δ</span> =</p></body></html>"))
        self.form_delta.setToolTip(_translate("mainWindow", "Caso necessário"))
        self.label_10.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Ponto minímo encontrado:</span></p></body></html>"))

import sys

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
