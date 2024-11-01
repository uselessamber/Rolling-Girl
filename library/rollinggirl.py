import pygame
import math

class RollingGirl():
    baseImage = None
    angle = 0
    angularSpeed = 0
    size = 500
    x, y = 0, 0

    def __init__(self):
        self.baseImage = pygame.image.load("./sprite/miku.png")
        self.baseImage = self.baseImage.convert_alpha()
        
    def setCoordinate(self, x, y):
        self.x, self.y = x, y

    def getSurface(self):
        tmp = pygame.transform.rotate(self.baseImage, self.angle)
        output = pygame.Surface((self.size, self.size), pygame.SRCALPHA, 32)
        output = output.convert_alpha()
        output.blit(tmp, (
            (self.size - tmp.get_width()) // 2,
            (self.size - tmp.get_height()) // 2
        ))
        return output
    
    def draw(self, surface : pygame.Surface):
        surface.blit(self.getSurface(), (
            self.x - self.size // 2,
            self.y - self.size // 2
        ))

    def update(self, delta):
        self.angle = ((self.angle + (self.angularSpeed * delta) % 360) % 360) // 1
        self.angularSpeed = (self.angularSpeed * 0.98)

    def spin(self, x2 : int, y2 : int, x3 : int, y3 : int, delta):
        def vLength(v):
            return (v[0] * v[0] + v[1] * v[1]) ** 0.5
        v1 = (
            x2 - self.x,
            y2 - self.y
        )
        v2 = (
            x3 - self.x,
            y3 - self.y
        )
        v3 = (
            x3 - x2,
            y3 - y2
        )
        P = v1[0] * v2[1] - v1[1] * v2[0]
        speed = ((v3[0] * v3[0] + v3[1] * v3[1]) ** 0.5) * (-P)
        self.angularSpeed = (speed / (self.size // 2))