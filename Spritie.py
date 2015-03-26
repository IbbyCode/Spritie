def sprite():
    class Sprite():
        x = 0
        y = 0
        xmomentum = 0
        ymomentum = 0
        slot = 0
        def up(self, l = 1):
            self.y += l
        def down(self, l = 1):
            self.y -= 1
        def right(self, l = 1):
            self.x += l
        def left(self, l = 1):
            self.x -= 1
    return Sprite()
