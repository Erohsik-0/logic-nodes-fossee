from .base_node import BaseNode

class XnorNode(BaseNode):
    def __init__(self):
        super().__init__('XNOR' , num_inputs=2, num_outputs=1)
        self.initUI()
        
    def initUI(self):
        super().initUI()
        
    def perform_logic(self, ip1 , ip2):
        return not ( ip1 ^ ip2 )