from src.graphics.NodePainter import NodePainter

BLACK = (0, 0, 0)


class EdgePainter:

    def __init__(self, src: NodePainter, dest, weight, color=BLACK, text=''):
        self.src_x = src.x
        self.src_y = src.y
        self.dest_x = dest.x
        self.dest_y = dest.y
        self.color = color
        self.text = Text(node.get_x(), node.get_y(), str(self.node.get_key()))
        self.over = False
        self.scaler = Scale()
        self.new_x = None
        self.new_y = None