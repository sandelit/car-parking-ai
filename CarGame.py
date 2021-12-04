import pygame
import time
from Car import Car

CAR = pygame.image.load("imgs/car.png")
PARKINGSPOT = pygame.image.load("imgs/parkingspot.png")
FPS = 60
WIDTH, HEIGHT = 1440, 810
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Parking AI")




class ParkingSpot():
    """docstring for ."""
    def __init__(self):
        self.img = pygame.image.load("imgs/parkingspot.png")






def draw_parkingspots(n, startpos):
    posx, posy = (startpos)
    pos = (posx, posy)
    for i in range(n):
        WINDOW.blit(PARKINGSPOT, (posx, posy))
        posx += 80

def draw(window, car):
    WINDOW.fill((100, 100, 100))
    draw_parkingspots(10, (100, 100))
    draw_parkingspots(10, (100, 500))

    car.draw(window)
    pygame.display.update()

clock = pygame.time.Clock()
car = Car(5, 2)

################################## GAME LOOP ###################################
running = True
while running:
    clock.tick(FPS)

    draw(WINDOW, car)
    #WINDOW.fill((100, 100, 100))
    #### Draw parkingspots
    #draw_parkingspots(15)
    ###
    #WINDOW.blit(CAR, (40, 405))

    #pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        car.rotate(left=True)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        car.rotate(right=True)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        moved = True
        car.move_forward()
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        moved = True
        car.move_backward()

    if not moved:
        car.reduce_speed()
pygame.quit()
