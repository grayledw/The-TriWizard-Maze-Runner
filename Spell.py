class Spell():
    def __init__(self, dx, dy, x, y, spell_image, frame):
        self.dx = dx
        self.dy = dy
        self.x = x
        self.y = y
        self.radius = 5
        self.frame = frame
        self.rectangle = spell_image.get_rect()
        self.image = spell_image

    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy

    def draw(self):
        self.rectangle = self.frame.blit(self.image, (self.x, self.y))

