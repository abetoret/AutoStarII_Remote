# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\AutoSTAR_remote_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(315, 475)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_Help = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Help.setObjectName("pushButton_Help")
        self.gridLayout.addWidget(self.pushButton_Help, 9, 1, 1, 1)
        self.pushButton_Num5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Num5.setObjectName("pushButton_Num5")
        self.gridLayout.addWidget(self.pushButton_Num5, 6, 1, 1, 1)
        self.pushButton_Num9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Num9.setObjectName("pushButton_Num9")
        self.gridLayout.addWidget(self.pushButton_Num9, 7, 2, 1, 1)
        self.pushButton_Num4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Num4.setObjectName("pushButton_Num4")
        self.gridLayout.addWidget(self.pushButton_Num4, 6, 0, 1, 1)
        self.pushButton_Num8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Num8.setObjectName("pushButton_Num8")
        self.gridLayout.addWidget(self.pushButton_Num8, 7, 1, 1, 1)
        self.pushButton_ScrollDown = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ScrollDown.setObjectName("pushButton_ScrollDown")
        self.gridLayout.addWidget(self.pushButton_ScrollDown, 9, 2, 1, 1)
        self.pushButton_Num0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Num0.setObjectName("pushButton_Num0")
        self.gridLayout.addWidget(self.pushButton_Num0, 8, 1, 1, 1)
        self.pushButton_Num6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Num6.setObjectName("pushButton_Num6")
        self.gridLayout.addWidget(self.pushButton_Num6, 6, 2, 1, 1)
        self.pushButton_ScrollUp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ScrollUp.setObjectName("pushButton_ScrollUp")
        self.gridLayout.addWidget(self.pushButton_ScrollUp, 9, 0, 1, 1)
        self.pushButton_Num7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Num7.setObjectName("pushButton_Num7")
        self.gridLayout.addWidget(self.pushButton_Num7, 7, 0, 1, 1)
        self.plainTextEdit_LCD = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit_LCD.setFont(font)
        self.plainTextEdit_LCD.setReadOnly(True)
        self.plainTextEdit_LCD.setObjectName("plainTextEdit_LCD")
        self.gridLayout.addWidget(self.plainTextEdit_LCD, 0, 0, 1, 3)
        self.pushButton_Mode = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Mode.setObjectName("pushButton_Mode")
        self.gridLayout.addWidget(self.pushButton_Mode, 1, 1, 1, 1)
        self.pushButton_Goto = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Goto.setObjectName("pushButton_Goto")
        self.gridLayout.addWidget(self.pushButton_Goto, 1, 2, 1, 1)
        self.pushButton_East = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_East.setObjectName("pushButton_East")
        self.gridLayout.addWidget(self.pushButton_East, 3, 2, 1, 1)
        self.pushButton_South = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_South.setObjectName("pushButton_South")
        self.gridLayout.addWidget(self.pushButton_South, 4, 1, 1, 1)
        self.pushButton_Num1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Num1.setObjectName("pushButton_Num1")
        self.gridLayout.addWidget(self.pushButton_Num1, 5, 0, 1, 1)
        self.pushButton_Num2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Num2.setObjectName("pushButton_Num2")
        self.gridLayout.addWidget(self.pushButton_Num2, 5, 1, 1, 1)
        self.pushButton_Num3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Num3.setObjectName("pushButton_Num3")
        self.gridLayout.addWidget(self.pushButton_Num3, 5, 2, 1, 1)
        self.pushButton_Enter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Enter.setObjectName("pushButton_Enter")
        self.gridLayout.addWidget(self.pushButton_Enter, 1, 0, 1, 1)
        self.pushButton_West = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_West.setObjectName("pushButton_West")
        self.gridLayout.addWidget(self.pushButton_West, 3, 0, 1, 1)
        self.pushButton_North = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_North.setObjectName("pushButton_North")
        self.gridLayout.addWidget(self.pushButton_North, 2, 1, 1, 1)
        self.pushButton_Back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.gridLayout.addWidget(self.pushButton_Back, 8, 0, 1, 1)
        self.pushButton_Fwd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Fwd.setObjectName("pushButton_Fwd")
        self.gridLayout.addWidget(self.pushButton_Fwd, 8, 2, 1, 1)
        self.pushButton_FocIn = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_FocIn.setObjectName("pushButton_FocIn")
        self.gridLayout.addWidget(self.pushButton_FocIn, 10, 1, 1, 1)
        self.pushButton_FocOut = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_FocOut.setObjectName("pushButton_FocOut")
        self.gridLayout.addWidget(self.pushButton_FocOut, 10, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 315, 26))
        self.menubar.setObjectName("menubar")
        self.menuTelescope = QtWidgets.QMenu(self.menubar)
        self.menuTelescope.setEnabled(True)
        self.menuTelescope.setObjectName("menuTelescope")
        self.menuDisplay = QtWidgets.QMenu(self.menubar)
        self.menuDisplay.setObjectName("menuDisplay")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionselect = QtWidgets.QAction(MainWindow)
        self.actionselect.setObjectName("actionselect")
        self.actionconnect = QtWidgets.QAction(MainWindow)
        self.actionconnect.setEnabled(True)
        self.actionconnect.setObjectName("actionconnect")
        self.actiondisconnect = QtWidgets.QAction(MainWindow)
        self.actiondisconnect.setEnabled(False)
        self.actiondisconnect.setObjectName("actiondisconnect")
        self.actionpoll = QtWidgets.QAction(MainWindow)
        self.actionpoll.setCheckable(True)
        self.actionpoll.setChecked(True)
        self.actionpoll.setObjectName("actionpoll")
        self.actionupdate_now = QtWidgets.QAction(MainWindow)
        self.actionupdate_now.setEnabled(False)
        self.actionupdate_now.setObjectName("actionupdate_now")
        self.menuTelescope.addAction(self.actionconnect)
        self.menuTelescope.addAction(self.actiondisconnect)
        self.menuDisplay.addAction(self.actionpoll)
        self.menuDisplay.addAction(self.actionupdate_now)
        self.menubar.addAction(self.menuTelescope.menuAction())
        self.menubar.addAction(self.menuDisplay.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Help.setText(_translate("MainWindow", "?"))
        self.pushButton_Help.setShortcut(_translate("MainWindow", "?"))
        self.pushButton_Num5.setText(_translate("MainWindow", "5"))
        self.pushButton_Num5.setShortcut(_translate("MainWindow", "5"))
        self.pushButton_Num9.setText(_translate("MainWindow", "9"))
        self.pushButton_Num9.setShortcut(_translate("MainWindow", "9"))
        self.pushButton_Num4.setText(_translate("MainWindow", "4"))
        self.pushButton_Num4.setShortcut(_translate("MainWindow", "4"))
        self.pushButton_Num8.setText(_translate("MainWindow", "8"))
        self.pushButton_Num8.setShortcut(_translate("MainWindow", "8"))
        self.pushButton_ScrollDown.setText(_translate("MainWindow", "down"))
        self.pushButton_ScrollDown.setShortcut(_translate("MainWindow", "PgDown"))
        self.pushButton_Num0.setText(_translate("MainWindow", "0"))
        self.pushButton_Num0.setShortcut(_translate("MainWindow", "0"))
        self.pushButton_Num6.setText(_translate("MainWindow", "6"))
        self.pushButton_Num6.setShortcut(_translate("MainWindow", "6"))
        self.pushButton_ScrollUp.setText(_translate("MainWindow", "up"))
        self.pushButton_ScrollUp.setShortcut(_translate("MainWindow", "PgUp"))
        self.pushButton_Num7.setText(_translate("MainWindow", "7"))
        self.pushButton_Num7.setShortcut(_translate("MainWindow", "7"))
        self.pushButton_Mode.setText(_translate("MainWindow", "MODE"))
        self.pushButton_Mode.setShortcut(_translate("MainWindow", "Esc"))
        self.pushButton_Goto.setText(_translate("MainWindow", "GO TO"))
        self.pushButton_Goto.setShortcut(_translate("MainWindow", "Home"))
        self.pushButton_East.setText(_translate("MainWindow", ">"))
        self.pushButton_East.setShortcut(_translate("MainWindow", "Right"))
        self.pushButton_South.setText(_translate("MainWindow", "v"))
        self.pushButton_South.setShortcut(_translate("MainWindow", "Down"))
        self.pushButton_Num1.setText(_translate("MainWindow", "1"))
        self.pushButton_Num1.setShortcut(_translate("MainWindow", "1"))
        self.pushButton_Num2.setText(_translate("MainWindow", "2"))
        self.pushButton_Num2.setShortcut(_translate("MainWindow", "2"))
        self.pushButton_Num3.setText(_translate("MainWindow", "3"))
        self.pushButton_Num3.setShortcut(_translate("MainWindow", "3"))
        self.pushButton_Enter.setText(_translate("MainWindow", "ENTER"))
        self.pushButton_Enter.setShortcut(_translate("MainWindow", "Return"))
        self.pushButton_West.setText(_translate("MainWindow", "<"))
        self.pushButton_West.setShortcut(_translate("MainWindow", "Left"))
        self.pushButton_North.setText(_translate("MainWindow", "^"))
        self.pushButton_North.setShortcut(_translate("MainWindow", "Up"))
        self.pushButton_Back.setText(_translate("MainWindow", "BACK"))
        self.pushButton_Fwd.setText(_translate("MainWindow", "FWD"))
        self.pushButton_FocIn.setText(_translate("MainWindow", "Focus in"))
        self.pushButton_FocIn.setShortcut(_translate("MainWindow", "+"))
        self.pushButton_FocOut.setText(_translate("MainWindow", "Focus out"))
        self.pushButton_FocOut.setShortcut(_translate("MainWindow", "-"))
        self.menuTelescope.setTitle(_translate("MainWindow", "Telescope"))
        self.menuDisplay.setTitle(_translate("MainWindow", "LCD"))
        self.actionselect.setText(_translate("MainWindow", "select"))
        self.actionconnect.setText(_translate("MainWindow", "connect"))
        self.actiondisconnect.setText(_translate("MainWindow", "disconnect"))
        self.actionpoll.setText(_translate("MainWindow", "poll"))
        self.actionupdate_now.setText(_translate("MainWindow", "update now"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
