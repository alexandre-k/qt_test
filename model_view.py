from PyQt4 import uic
from PyQt4.QtCore import QAbstractListModel, Qt, QModelIndex, QAbstractTableModel
from PyQt4.QtGui import (QListView, QTreeView,
                         QComboBox, QTableView,
                         QApplication, QColor,
                         QWidget, QPixmap,
                         QIcon)
import sys
import numpy


class PaletteListModel(QAbstractListModel):

    def __init__(self, colors=[], parent=None):
        super().__init__()
        self._colors = colors

    def headerData(self, section, orientation, role):

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return 'Palette'
            else:
                return 'Color {}'.format(section)

    def data(self, index, role):

        if role == Qt.EditRole:
            return self._colors[index.row()].name()

        elif role == Qt.ToolTipRole:
            return 'Hex code: ' + self._colors[index.row()].name()

        elif role == Qt.DecorationRole:

            row = index.row()
            value = self._colors[row]

            pixmap = QPixmap(26, 26)
            pixmap.fill(value)
            icon = QIcon(pixmap)
            return icon

        elif role == Qt.DisplayRole:
            row = index.row()
            value = self._colors[row]
            return value.name()

    def rowCount(self, parent):
        return len(self._colors)

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def setData(self, index, value, role=Qt.EditRole):

        if role == Qt.EditRole:
            row = index.row()
            color = QColor(value)

            if color.isValid():
                self._colors[row] = color
                self.dataChanged.emit(index, index)
                return True
            return False

    def insertRows(self, position, rows, parent=QModelIndex):

        self.beginInsertRows(parent, position, position + rows - 1)

        for i in range(rows):
            self._colors.insert(position, QColor('#000000'))

        self.endInsertRows()

        return True

    def removeRows(self, position, rows, parent=QModelIndex):

        self.beginRemoveRows(parent, position, position + rows - 1)

        for i in range(rows):
            value = self._colors[position]
            self._colors.remove(value)

        self.endRemoveRows()

        return True


class PaletteTableModel(QAbstractTableModel):

    def __init__(self, colors=[[]], headers=[], parent=None):
        super().__init__()
        self._colors = colors
        self._headers = headers

    def headerData(self, section, orientation, role):

        if role == Qt.DisplayRole:

            if orientation == Qt.Horizontal:

                if section < len(self._headers):
                    return self._headers[section]
                else:
                    return 'TEMP'
            else:
                return 'Color {}'.format(section)

    def insertRows(self, position, rows, parent=QModelIndex()):
        self.beginInsertRows(parent, position, position + rows - 1)

        for i in range(rows):
            defaultValues = [QColor('#000000') for i in range(self.columnCount(None))]
            self._colors.insert(position, defaultValues)

        self.endInsertRows()
        return True

    def insertColumns(self, position, columns, parent=QModelIndex()):
        self.beginInsertColumns(parent, position, position + columns - 1)

        rowCount = len(self._colors)

        for i in range(columns):
            for j in range(rowCount):
                self._colors[j].insert(position, QColor('#000000'))

        self.endInsertColumns()
        return True

    def rowCount(self, parent):
        return len(self._colors)

    def columnCount(self, parent):
        return len(self._colors[0])

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def data(self, index, role):

        if role == Qt.EditRole:
            row = index.row()
            column = index.column()
            return self._colors[row][column]

        if role == Qt.ToolTipRole:
            row = index.row()
            column = index.column()
            return 'Hex code: ' + self._colors[row][column]

        if role == Qt.DecorationRole:
            row = index.row()
            column = index.column()
            value = self._colors[row][column]

            pixmap = QPixmap(26, 26)
            pixmap.fill(value)
            icon = QIcon(pixmap)
            return icon

        if role == Qt.DisplayRole:
            row = index.row()
            column = index.column()
            return self._colors[row][column]
        
    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:

            row = index.row()
            column = index.column()
            color = QColor(value)

            if color.isValid():
                self._colors[row][column] = color
                self.dataChanged.emit(index, index)
                return True
        return False




# base, form = uic.loadUiType('test.ui')

# class WindowTest(base, form):

#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setupUi(self)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle('plastique')
    with open('test.ui', 'r') as stylesheet:
        app.setStyleSheet(stylesheet.read())

    red = QColor(255, 0, 0)
    green = QColor(0, 255, 0)
    blue = QColor(0, 0, 255)

    rowCount = 4
    columnCount = 6

    headers = ['Palette0', 'Colors', 'Brushes', 'Omg', 'Technical', 'Artist']
    table_data = [[QColor('#FFFF00') for i in range(columnCount)] for j in range(rowCount)]

    # w = QWidget()
    # w.show()

    # listView = QListView()
    # model = PaletteListModel([red, green, blue])

    # listView.setModel(model)
    # listView.show()

    # treeView = QTreeView()
    # treeView.show()

    # comboBox = QComboBox()
    # comboBox.show()

    tableView = QTableView()
    table_model = PaletteTableModel(table_data, headers)
    table_model.insertRows(0, 5)
    table_model.insertColumns(6, 3)
    tableView.setModel(table_model)
    tableView.show()

    # window = WindowTest()
    # window.show()


    # comboBox.setModel(model)

    # model.insertRows(2, 5, QModelIndex())
    # model.removeRows(1, 6, QModelIndex())

    sys.exit(app.exec_())
