from .base_node import BaseNode

class XorNode(BaseNode):
    def __init__(self):
        super().__init__('XOR' , num_inputs=2, num_outputs=1)
        self.initUI()
        
    def initUI(self):
        super().initUI()
        
    def perform_logic(self, ip1 , ip2):
        return ip1 ^ ip2