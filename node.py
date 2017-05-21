from PyQt4.QtCore import QAbstractItemModel, QModelIndex


class Node(object):

    def __init__(self, name, parent=None):

        self.name = name
        self.children = []
        self.parent = parent

        if parent is not None:
            parent.addChild(self)

    def addChild(self, child):
        self.children.append(child)

    def name(self):
        return self.name

    def child(self, row):
        return self.children[row]

    def childCount(self):
        return len(self.children)

    def parent(self):
        return self.parent

    def row(self):
        if self.parent is not None:
            return self.parent.children.index(self)

    def __repr__(self):
        return self.log()

    def log(self, tabLevel=-1):
        output = ''
        tabLevel += 1

        for i in range(tabLevel):
            output += '\t'

        output += '|------' + self.name + '\n'

        for child in self.children:
            output += child.log(tabLevel)
        tabLevel -= 1
        output += '\n'
        return output


class SceneGraphModel(QAbstractItemModel):

    def __init__(self, root, parent=None):
        super().__init__(parent)
        self.rootNode = root

    def rowCount(self, parent):
        pass

    def columnCount(self, parent):
        pass

    def data(self, index, role):
        pass

    def headerData(self, section, orientation, role):
        pass

    def flags(self, index):
        pass

    def parent(self, index):

        node = index.internalPointer()
        parentNode = node.parent()

        if parentNode == self.rootNode:
            return QModelIndex()

        return self.createIndex(parentNode.row(), 0, parentNode)

    def index(self, row, column, parent):

        if not parent.isValid():
            parentNode = self.rootNode
        else:
            parentNode = parent.internalPointer()

        childItem = parentNode.child(row)

        if childItem:
            self.createIndex(row, column, childItem)
        else:
            QModelIndex()

if __name__ == '__main__':

    root = Node('Hips')
    childNode0 = Node('LeftPirateLeg', root)
    childNode1 = Node('RightLeg', root)
    childNode2 = Node('RightFoot', childNode1)
