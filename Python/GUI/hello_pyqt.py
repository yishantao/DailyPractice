# -*-coding:utf-8-*-
"""创建窗口"""

import sys
from PyQt5 import QtWidgets


# 通过继承QtWidgets.QMainWindow创建类
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle('PyQT')  # 设置窗口标题
        self.resize(300, 200)  # 设置窗口大小


app = QtWidgets.QApplication(sys.argv)  # 创建QApplication对象
my_window = MyWindow()
my_window.show()  # 显示窗口
# exec_进入消息循环，exit确保应用程序的退出
sys.exit(app.exec_())
