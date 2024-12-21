from PyQt5.QtWidgets import QGraphicsTextItem, QPushButton, QGraphicsProxyWidget
from .base_node import BaseNode

class OutputNode(BaseNode):
    def __init__(self):
        super().__init__('Output', num_inputs=1, num_outputs=0)
        self.initUI()

    def initUI(self):
        super().initUI()

        # Add a display field for showing the output value
        self.output_display = QGraphicsTextItem(self)
        self.output_display.setPos(10, 50)

        # Add a button to write output to a file
        self.save_button = QPushButton("Save")
        self.button_proxy = QGraphicsProxyWidget(self)
        self.button_proxy.setWidget(self.save_button)
        self.button_proxy.setPos(10, 70)
        self.save_button.clicked.connect(self.save_to_file)

    def save_to_file(self):
        # Logic to save output to a file
        with open("output.txt", "w") as file:
            file.write(self.output_display.toPlainText())