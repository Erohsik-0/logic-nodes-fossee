from PyQt5.QtWidgets import QGraphicsItem, QGraphicsTextItem, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsRectItem
from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QPen, QBrush

class BaseNode(QGraphicsItem):
    def __init__(self, node_type, num_inputs=1, num_outputs=1):
        super().__init__()
        self.node_type = node_type
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.initUI()

    def initUI(self):
        # Set up the node's graphical representation
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        
        # Draw the node's background
        self.rect = QGraphicsRectItem(0, 0, 100, 100, self)
        self.rect.setBrush(QBrush(Qt.lightGray))
        self.rect.setPen(QPen(Qt.black))

        # Add node type label
        self.text_item = QGraphicsTextItem(self.node_type, self)
        self.text_item.setPos(10, 10)

        # Draw input sockets
        self.input_sockets = []
        for i in range(self.num_inputs):
            socket = QGraphicsEllipseItem(-10, 30 + i * 20, 10, 10, self)
            socket.setBrush(QBrush(Qt.red))
            self.input_sockets.append(socket)

        # Draw output sockets
        self.output_sockets = []
        for i in range(self.num_outputs):
            socket = QGraphicsEllipseItem(100, 30 + i * 20, 10, 10, self)
            socket.setBrush(QBrush(Qt.green))
            self.output_sockets.append(socket)

    def boundingRect(self):
        return QRectF(0, 0, 100, 100)

    def paint(self, painter, option, widget):
        pass