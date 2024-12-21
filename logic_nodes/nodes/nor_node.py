from .base_node import BaseNode

class NorNode(BaseNode):
    def __init__(self):
        super().__init__('NOR' , num_inputs=2, num_outputs=1)
        self.initUI()
        
    def initUI(self):
        super().initUI()
        
    def perform_logic(self, ip1 , ip2):
        return not ( ip1 or ip2 )