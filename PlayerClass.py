import pygame
import math
from Rotater import *

pygame.init()

class Player():
    def __init__(self, image, frame, x, y):
        self.image = image
        self.angle = 0
        self.x = x
        self.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.offset = pygame.math.Vector2(0, 0)
        self.position = (self.x, self.y)
        self.rotater = Rotater()
        self.frame = frame
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.health = 3

    def draw(self):
        rotated_image, self.rect = self.rotater.rotate(self.image, self.angle, (self.x, self.y), self.offset)
        self.frame.blit(rotated_image, self.rect)
        #pygame.draw.rect(self.frame, pygame.Color("green"), self.rect, 5)

    def turn_left(self):
        self.angle += -3.3

    def turn_right(self):
        self.angle += 3.3

    def forwards(self, wall_rects):
        rad = (self.angle % 360) * math.pi / 180
        dx = 3.5 * math.sin(rad)
        dy = 3.5 * math.cos(rad)
        will_move = True
        for wall_rect in wall_rects:
            if wall_rect.collidepoint(self.x + dx, self.y - dy):
                will_move = False
        if will_move:
            self.x += dx
            self.y -= dy
            self.rect[0] = self.x
            self.rect[1] = self.y

        self.no_out_of_bonds()

    def backwards(self, wall_rects):
        rad = (self.angle % 360) * math.pi / 180
        dx = 3.5 * math.sin(rad)
        dy = 3.5 * math.cos(rad)
        will_move = True
        for wall_rect in wall_rects:
            if wall_rect.collidepoint(self.x - dx, self.y + dy):
                will_move = False
        if will_move:
            self.x -= dx
            self.y += dy
            self.rect[0] = self.x
            self.rect[1] = self.y

        self.no_out_of_bonds()

    def get_x_and_y_movement_increments(self):
        rad = (self.angle % 360) * math.pi / 180
        dx = int(3.5 * math.sin(rad))
        dy = -int(3.5 * math.cos(rad))
        return dx, dy

    def collides(self, rect):
        return self.rect.colliderect(rect)

    def change_health(self):
        self.health -= 1

    def no_out_of_bonds(self):
        if self.x >= self.frame.get_width():
            self.x = 1
        if self.y >= self.frame.get_height():
            self.y = 1
        if self.x <= 0:
            self.x = self.frame.get_width() - 1
        if self.y <= 0:
            self.y = self.frame.get_height() - 1
