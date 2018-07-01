# -*-coding:utf-8-*-
"""信号和插槽"""

import sys
from PyQt5 import QtWidgets, QtCore


# 通过继承QtWidgets.QWidget创建类
class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('PyQT')  # 设置窗口标题
        self.resize(300, 200)  # 设置窗口大小
        gridlayout = QtWidgets.QGridLayout()  # 创建布局组件
        self.button1 = QtWidgets.QPushButton('Button1')  # 生成Button1
        gridlayout.addWidget(self.button1, 1, 1, 1, 3)  # 添加Button1
        self.button2 = QtWidgets.QPushButton('Button2')  # 生成Button2
        gridlayout.addWidget(self.button2, 2, 2)
        self.setLayout(gridlayout)  # 向窗口中添加布局组件
        self.button1.clicked.connect(self.OnButton1)
        self.button2.clicked.connect(self.OnButton2)
        # self.connect(self.button1, QtCore.PYQT_SIGNAL('clicked()'), self.OnButton1)
        # self.connect(self.button2, QtCore.PYQT_SIGNAL('clicked()'), self.OnButton2)

    def OnButton1(self):
        self.button1.setText('clicked')

    def OnButton2(self):
        self.button2.setText('clicked')


app = QtWidgets.QApplication(sys.argv)  # 创建QApplication对象
my_window = MyWindow()
my_window.show()  # 显示窗口
sys.exit(app.exec_())
