import pygame
from utils import blit_rotate_center
import math

class Car:
    """docstring for ."""
    def __init__(self, max_vel, rotation_vel):
        self.img = pygame.image.load("imgs/car.png")
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = -90
        self.x = 50
        self.y = 360
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, window):
        blit_rotate_center(window, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel / 2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        if self.vel >= 0:
            self.vel = max(self.vel - self.acceleration / 2, 0)
            self.move()
        else:
            self.vel = max(self.vel + self.acceleration / 2, 0)
            self.move()
