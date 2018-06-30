# -*-coding:utf-8-*-
"""使用空白项布置组件"""

import sys
from PyQt5 import QtWidgets, QtCore


# 通过继承QtWidgets.QMainWindow创建类
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle('PyQT')  # 设置窗口标题
        self.resize(300, 200)  # 设置窗口大小
        gridlayout = QtWidgets.QGridLayout()
        spacer1 = QtWidgets.QSpacerItem(300, 40)
        spacer2 = QtWidgets.QSpacerItem(300, 40)
        label = QtWidgets.QLabel('Label', self)
        label.setAlignment(QtCore.Qt.AlignCenter)
        gridlayout.addItem(spacer1, 0, 0)
        gridlayout.addWidget(label, 1, 0)
        gridlayout.addItem(spacer2, 2, 0)
        self.setLayout(gridlayout)


app = QtWidgets.QApplication(sys.argv)  # 创建QApplication对象
my_window = MyWindow()
my_window.show()  # 显示窗口
# exec_进入消息循环，exit确保应用程序的退出
sys.exit(app.exec_())
