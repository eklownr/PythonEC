import pygame


class MyRect:
    def __init__(self, x, y, width, height, thickness):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.thickness = thickness

    def draw(self, screen):
        pygame.draw.rect(
            screen, "red", (self.x, self.y, self.width, self.height), self.thickness
        )

    def update(self):
        self.x += 2
        self.y += 2
        self.width += 5
