# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generateReportsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 493)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnSalesinLast7DaysGraph = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalesinLast7DaysGraph.setGeometry(QtCore.QRect(180, 140, 120, 23))
        self.btnSalesinLast7DaysGraph.setMinimumSize(QtCore.QSize(120, 23))
        self.btnSalesinLast7DaysGraph.setStyleSheet("#btnSalesinLast7DaysGraph{\n"
"    border:3px solid #48ACAC; \n"
"    color: rgb(72, 172, 172);\n"
"}\n"
"#btnSalesinLast7DaysGraph:hover{\n"
"    background-color: rgb(72, 172, 172);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.btnSalesinLast7DaysGraph.setObjectName("btnSalesinLast7DaysGraph")
        self.btnAllEmployeeGraph = QtWidgets.QPushButton(self.centralwidget)
        self.btnAllEmployeeGraph.setGeometry(QtCore.QRect(180, 190, 120, 23))
        self.btnAllEmployeeGraph.setMinimumSize(QtCore.QSize(120, 23))
        self.btnAllEmployeeGraph.setStyleSheet("#btnAllEmployeeGraph{\n"
"    border:3px solid #48ACAC; \n"
"    color: rgb(72, 172, 172);\n"
"}\n"
"#btnAllEmployeeGraph:hover{\n"
"    background-color: rgb(72, 172, 172);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.btnAllEmployeeGraph.setObjectName("btnAllEmployeeGraph")
        self.btnSalesinLast7DaysTabular = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalesinLast7DaysTabular.setGeometry(QtCore.QRect(320, 140, 120, 23))
        self.btnSalesinLast7DaysTabular.setMinimumSize(QtCore.QSize(120, 23))
        self.btnSalesinLast7DaysTabular.setStyleSheet("#btnSalesinLast7DaysTabular{\n"
"    border:3px solid #48ACAC; \n"
"    color: rgb(72, 172, 172);\n"
"}\n"
"#btnSalesinLast7DaysTabular:hover{\n"
"    background-color: rgb(72, 172, 172);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.btnSalesinLast7DaysTabular.setObjectName("btnSalesinLast7DaysTabular")
        self.label_88 = QtWidgets.QLabel(self.centralwidget)
        self.label_88.setGeometry(QtCore.QRect(10, 140, 151, 20))
        self.label_88.setMaximumSize(QtCore.QSize(777977, 9888989))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_88.setFont(font)
        self.label_88.setStyleSheet("color:#48ACAC")
        self.label_88.setObjectName("label_88")
        self.btnAllEmployeeTabular = QtWidgets.QPushButton(self.centralwidget)
        self.btnAllEmployeeTabular.setGeometry(QtCore.QRect(320, 190, 120, 23))
        self.btnAllEmployeeTabular.setMinimumSize(QtCore.QSize(120, 23))
        self.btnAllEmployeeTabular.setStyleSheet("#btnAllEmployeeTabular{\n"
"    border:3px solid #48ACAC; \n"
"    color: rgb(72, 172, 172);\n"
"}\n"
"#btnAllEmployeeTabular:hover{\n"
"    background-color: rgb(72, 172, 172);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.btnAllEmployeeTabular.setObjectName("btnAllEmployeeTabular")
        self.label_89 = QtWidgets.QLabel(self.centralwidget)
        self.label_89.setGeometry(QtCore.QRect(10, 190, 151, 20))
        self.label_89.setMaximumSize(QtCore.QSize(777977, 9888989))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_89.setFont(font)
        self.label_89.setStyleSheet("color:#48ACAC")
        self.label_89.setObjectName("label_89")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnSalesinLast7DaysGraph.setText(_translate("MainWindow", "Graph"))
        self.btnAllEmployeeGraph.setText(_translate("MainWindow", "Graph"))
        self.btnSalesinLast7DaysTabular.setText(_translate("MainWindow", "Tabular"))
        self.label_88.setText(_translate("MainWindow", "Sales in Last 7 Days"))
        self.btnAllEmployeeTabular.setText(_translate("MainWindow", "Tabular"))
        self.label_89.setText(_translate("MainWindow", "All Employees"))
