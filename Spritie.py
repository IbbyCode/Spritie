class Sprite():
    name = ''
    x = 0
    y = 0
    xmomentum = 0
    ymomentum = 0
    slot = 0
    attributes = {}
    def __init__(self, name):
        self.name = name
        print('Sprite ',name,' created')
    def up(self, l = 1):
        self.y += l
    def down(self, l = 1):
        self.y -= l
    def right(self, l = 1):
        self.x += l
    def left(self, l = 1):
        self.x -= l
    def kill(self):
        del self
