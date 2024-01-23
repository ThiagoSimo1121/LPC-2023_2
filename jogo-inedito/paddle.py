
class Paddle:
    def __init__(self, dest_x, dest_y, color, width, height):
        self.dest_x = dest_x
        self.dest_y = dest_y
        self.color = color
        self.width = width
        self.height = height

    def set_positiony(self,dest_y):
        self.dest_y = dest_y
