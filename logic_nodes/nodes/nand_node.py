from .base_node import BaseNode

class NandNode(BaseNode):
    def __init__(self):
        super().__init__('NAND' , num_inputs=2, num_outputs=1)
        self.initUI()
        
    def initUI(self):
        super().initUI()
        
    def perform_logic(self, ip1 , ip2):
        return not (ip1 and ip2)