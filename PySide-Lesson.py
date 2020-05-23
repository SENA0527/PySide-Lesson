# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import shiboken2 as shiboken

# ↓Maya library
#from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

class Widget(QWidget):

    def __init__(self):
        super(Widget, self).__init__()

        # 縦割りのレイアウトを作成してウィジェットにセットする
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # リストウィジェットをウィジェットにセットする
        self.list = QListWidget()
        self.layout.addWidget(self.list)

        # ボタンウィジェットをウィジェットにセットする
        self.button = QPushButton("button")
        self.layout.addWidget(self.button)
        self.button.clicked[()].connect(lambda: self.setItem())

    def setItem(self):
        self.list.addItem("item")


# ↓Maya  MainWindow Class
#class Window(MayaQWidgetBaseMixin,QMainWindow):

# MainWindow
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.wid = Widget()
        self.setCentralWidget(self.wid)
# ↓Maya 
"""def main():
    app = QApplication.instance()
    ui = Window()
    ui.show()
    sys.exit()
    app.exec_()"""

# stand alone
def main():
    app = QApplication(sys.argv)
    gui = Window()
    gui.show()
    sys.exit(app.exec_())

# インポート時に自動実行を防ぐ
if __name__ == '__main__':
    main()
