# -*-coding:utf-8-*-
"""创建按钮"""

import sys
from PyQt5 import QtWidgets, QtCore


# 通过继承QtWidgets.QWidget创建类
class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('PyQT')  # 设置窗口标题
        self.resize(300, 200)  # 设置窗口大小
        gridlayout = QtWidgets.QGridLayout()  # 创建布局组件
        button1 = QtWidgets.QPushButton('Button1')  # 生成Button1
        gridlayout.addWidget(button1, 1, 1, 1, 3)  # 添加Button1
        button2 = QtWidgets.QPushButton('Button2')  # 生成Button2
        button2.setFlat(True)
        gridlayout.addWidget(button2, 2, 2)
        self.setLayout(gridlayout)  # 向窗口中添加布局组件


app = QtWidgets.QApplication(sys.argv)  # 创建QApplication对象
my_window = MyWindow()
my_window.show()  # 显示窗口
# exec_进入消息循环，exit确保应用程序的退出
sys.exit(app.exec_())
