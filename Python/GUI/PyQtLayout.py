# -*-coding:utf-8-*-
"""使用布局组件布置多个标签"""

import sys
from PyQt5 import QtWidgets, QtCore


# 通过继承QtWidgets.QMainWindow创建类
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle('PyQT')  # 设置窗口标题
        self.resize(300, 200)  # 设置窗口大小
        grid_layout = QtWidgets.QGridLayout()
        hbox_layout1 = QtWidgets.QHBoxLayout()
        hbox_layout2 = QtWidgets.QHBoxLayout()
        vbox_layout1 = QtWidgets.QVBoxLayout()
        vbox_layout2 = QtWidgets.QVBoxLayout()
        label1 = QtWidgets.QLabel('Label1', self)
        label1.setAlignment(QtCore.Qt.AlignCenter)
        label2 = QtWidgets.QLabel('Label2')
        label3 = QtWidgets.QLabel('Label3')
        label4 = QtWidgets.QLabel('Label4')
        label5 = QtWidgets.QLabel('Label5')
        hbox_layout1.addWidget(label1)
        vbox_layout1.addWidget(label2)
        vbox_layout1.addWidget(label3)
        vbox_layout2.addWidget(label4)
        vbox_layout2.addWidget(label5)
        hbox_layout2.addLayout(vbox_layout1)
        hbox_layout2.addLayout(vbox_layout2)
        grid_layout.addLayout(hbox_layout1, 0, 0)
        grid_layout.addLayout(hbox_layout2, 1, 0)
        grid_layout.setRowMinimumHeight(1, 180)
        self.setLayout(grid_layout)


app = QtWidgets.QApplication(sys.argv)  # 创建QApplication对象
my_window = MyWindow()
my_window.show()  # 显示窗口
# exec_进入消息循环，exit确保应用程序的退出
sys.exit(app.exec_())
