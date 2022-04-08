from numpy import angle
import pygame, sys, math
import global_var as GLOB




class Mostro(pygame.sprite.Sprite):
    def __init__(self, pos, vel, wh):
        self.x = pos[0]
        self.y = pos[1]
        self.width = wh[0]
        self.height = wh[1]
        self.vel = vel
        self.x, self.y = GLOB.screen.get_rect().center
        self.line_vector = pygame.math.Vector2(1, 0)
        self.angle = 90
        self.angle_triangle = 0

        self.larg = 50
        self.lung = 0

    def aggiorna(self):
        radius = 360
        rot_vector = self.line_vector.rotate(self.angle) * radius
        start = round(self.x), round(self.y)
        end = round(self.x - rot_vector.x), round(self.y - rot_vector.y)

        start_line = round(self.x + self.width/2), round(self.y)
        end_line = round(self.x + self.width/2 - rot_vector.x), round(self.y - rot_vector.y)
        self.line = pygame.draw.line(GLOB.screen, (5,80,255), start_line, end_line, 8)


        if self.angle == 360 or self.angle == -360:
            self.angle = 0


        if self.angle == 90 or self.angle == -90 or self.angle == 270 or self.angle == -270:
            self.larg = 50
            self.lung = 0
        else:
            self.larg -= 1
            self.lung = 50

        if self.angle == 0 or self.angle == 360 or self.angle == -180 or self.angle == 180:
            self.lung = 50
            self.larg = 0
        else:
            self.lung += 1
            self.larg = 50

        lunghezza1 = (self.x - self.larg) -rot_vector.x
        lunghezza2 = (self.x + self.larg) -rot_vector.x

        larghezza1 = (self.y - self.lung) -rot_vector.y
        larghezza2 = (self.y + self.lung) -rot_vector.y

        fine = round(self.y - rot_vector.y)

        print(" Lungh: ", self.lung,  " Largh: ", self.larg, "Angle: ", self.angle)

        self.triangle = pygame.draw.polygon(surface=GLOB.screen, color=(255, 0, 0),points=[start_line, (lunghezza1, larghezza1), (lunghezza2, larghezza2)])

        val = 2

        immagine = pygame.image.load("Characters_Image/luce.png").convert_alpha()
        immagine = pygame.transform.scale(immagine, (immagine.get_width() * GLOB.MULT * val, immagine.get_height() * GLOB.MULT * val))

        immagine = pygame.transform.flip(immagine, False, False)
        immagine = pygame.transform.rotate(immagine, self.angle_triangle)

        # mask_image = immagine.convert()
        # mask_image.set_colorkey("#e40000")
        # mask = pygame.mask.from_surface(mask_image)

        GLOB.screen.blit(immagine, (GLOB.screen_width/2 - int(immagine.get_width()/2)  - rot_vector.x/2, GLOB.screen_height/2 - int(immagine.get_height()/2) - rot_vector.y/2))

        # rect = pygame.Rect(MENU_MOUSE_POS[0], MENU_MOUSE_POS[1], 1, 1) 
        # print(rect)
        # if not pygame.sprite.collide_mask(mask, rect):
        #     print("Sto collidendo")

    def ruota_destra(self):
        self.angle += 1
        self.angle_triangle -= 1

        print(self.angle)

    def ruota_sinistra(self):
        self.angle -= 1
        self.angle_triangle += 1

        print(self.angle)




def inizializza():
    global clock, animazione, mostro
    pygame.display.set_caption("Effetto")
    clock = pygame.time.Clock()
    mostro = Mostro((500,500), 20, (10 * GLOB.MULT, 80 * GLOB.MULT))

def disegna():
    GLOB.screen.fill((12,24,36))
    mostro.aggiorna()
    #rettangolo = pygame.Rect(GLOB.screen_width/2 - immagine.get_width()/2, GLOB.screen_height/2 - immagine.get_height()/2, immagine.get_width(), immagine.get_height())
    #pygame.draw.rect(GLOB.screen, (255, 0, 0), rettangolo, 1)

def testa():
    inizializza()
    global MENU_MOUSE_POS

    while True:

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        if pygame.mouse.get_pressed()[0]:
            mostro.ruota_destra()

        if pygame.mouse.get_pressed()[2]:
            mostro.ruota_sinistra()

        disegna()

        clock.tick(GLOB.FPS)
        pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    testa()