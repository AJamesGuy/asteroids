import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = velocity
        
    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
