import sys, pygame
from math import sin, cos, radians, pi
from pygame.locals import QUIT, MOUSEBUTTONDOWN
pygame.init()
SURFACE = pygame.display.set_mode((780,920))
FPSCLOCK = pygame.time.Clock()

def Line():
    center_x, center_y = SURFACE.get_rect().center
    radius = 100
    line_vector = pygame.math.Vector2(1, 0)
    angle = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if pygame.mouse.get_pressed()[0]:
            angle -= 1
            print(angle)

        if pygame.mouse.get_pressed()[2]:
            angle += 1
            print(angle)
        
        rot_vector = line_vector.rotate(angle) * radius
        start = round(center_x + rot_vector.x), round(center_y + rot_vector.y)
        end = round(center_x - rot_vector.x), round(center_y - rot_vector.y)
       
        SURFACE.fill((255,0,0))
        pygame.draw.line(SURFACE, (5,80,255), start, end, 8)
        pygame.display.update()
        FPSCLOCK.tick(60)

if __name__ == '__main__' :
    Line()