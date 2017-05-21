from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QListWidget, QComboBox, QListView, QStringListModel
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('cleanlooks')

    data = ['one', 'two', 'three', 'four']

    listView = QListView()
    listView.show()

    model = QStringListModel(data)
    listView.setModel(model)
    # listWidget = QListWidget()
    # listWidget.show()
    # listWidget.addItems(data)

    # count = listWidget.count()

    # for i in range(count):
    #     item = listWidget.item(i)
        # item.setFlags(item.flags() | Qt.ItemIsEditable)


    comboBox = QComboBox()
    comboBox.setModel(model)
    comboBox.show()
    sys.exit(app.exec_())
