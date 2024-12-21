from PyQt5.QtWidgets import QGraphicsTextItem, QLineEdit, QGraphicsProxyWidget
from .base_node import BaseNode

class InputNode(BaseNode):
    def __init__(self):
        super().__init__('Input', num_inputs=0, num_outputs=1)
        self.initUI()

    def initUI(self):
        super().initUI()
        
        # Add an input field for entering values
        self.input_field = QLineEdit()
        self.input_proxy = QGraphicsProxyWidget(self)
        self.input_proxy.setWidget(self.input_field)
        self.input_proxy.setPos(10, 50)
        
        
        