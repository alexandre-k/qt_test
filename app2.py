import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QPushButton

class mainClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tableWidget = tableManager()
        self.returnedTableWidget = self.tableWidget.makeTable(self)

        btnMaker = buttonManager()
        btnMaker.makeTestBtn(self)

        self.setGeometry(100, 100, 700, 600)
        self.show()


class buttonManager(QWidget):
    def __init__(self):
        super().__init__()

    def makeTestBtn(self, parent):
        testBtn01 = QPushButton("2 X 4", parent)
        testBtn02 = QPushButton("4 X 8", parent)
        testBtn03 = QPushButton("8 X 16", parent)
        testBtn04 = QPushButton("16 X 32", parent)

        testBtn01.move(50, 450)
        testBtn02.move(200, 450)
        testBtn03.move(350, 450)
        testBtn04.move(500, 450)


class tableManager(QWidget):
    def __init__(self):
        super().__init__()

    def makeTable(self, parent):
        self.tableMaker = QTableWidget(parent)
        self.tableMaker.setGeometry(50, 50, 600, 400)

        return self.tableMaker


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = mainClass()
    sys.exit(app.exec_())
