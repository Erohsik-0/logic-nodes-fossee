from .base_node import BaseNode

class NotNode(BaseNode):
    def __init__(self):
        super().__init__('NOT' , num_inputs=1, num_outputs=1)
        self.initUI()
        
    def initUI(self):
        super().initUI()
        
    def perform_logic(self, ip):
        return not ip