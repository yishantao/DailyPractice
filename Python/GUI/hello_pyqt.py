# -*-coding:utf-8-*-
""""""
import sys
from PyQt5 import QtCore, QtGui


class MyWindow(QtGui.QWindow):
    def __init__(self):
        QtGui.QWindow.__init__(self)
        self.setWindowTitle('PyQT')
        self.resize(300, 200)


app = QtGui.QGuiApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
