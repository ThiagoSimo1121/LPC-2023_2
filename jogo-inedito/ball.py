class Ball:

    def __init__(self, status, dest_x, dest_y, color, width, height, speedx, speedy):
        self.status = status
        self.dest_x = dest_x
        self.dest_y = dest_y
        self.color = color
        self.width = width
        self.height = height
        self.speedx = speedx
        self.speedy = speedy

    def set_positionx(self, dest_x):
        self.dest_x = dest_x

    def set_positiony(self, dest_y):
        self.dest_y = dest_y

    def get_positionx(self):
        return self.dest_x

    def get_positiony(self):
        return self.dest_y

    def set_speedx(self, speedx):
        self.speedx = speedx

    def set_speedy(self, speedy):
        self.speedy = speedy
