# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saper.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 681, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_time = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_time.sizePolicy().hasHeightForWidth())
        self.label_time.setSizePolicy(sizePolicy)
        self.label_time.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_time.setObjectName("label_time")
        self.horizontalLayout.addWidget(self.label_time)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_mine_left = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_mine_left.sizePolicy().hasHeightForWidth())
        self.label_mine_left.setSizePolicy(sizePolicy)
        self.label_mine_left.setObjectName("label_mine_left")
        self.horizontalLayout.addWidget(self.label_mine_left)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 684, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.act_easy = QtWidgets.QAction(MainWindow)
        self.act_easy.setObjectName("act_easy")
        self.act_mid = QtWidgets.QAction(MainWindow)
        self.act_mid.setObjectName("act_mid")
        self.act_hard = QtWidgets.QAction(MainWindow)
        self.act_hard.setObjectName("act_hard")
        self.menu.addSeparator()
        self.menu.addAction(self.act_easy)
        self.menu.addAction(self.act_mid)
        self.menu.addAction(self.act_hard)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Сапёр"))
        self.label_time.setText(_translate("MainWindow", "Время"))
        self.pushButton.setText(_translate("MainWindow", "RESET"))
        self.label_mine_left.setText(_translate("MainWindow", "TextLabel"))
        self.menu.setTitle(_translate("MainWindow", "Сложность"))
        self.act_easy.setText(_translate("MainWindow", "Легкий"))
        self.act_mid.setText(_translate("MainWindow", "Средний"))
        self.act_hard.setText(_translate("MainWindow", "Сложный"))
