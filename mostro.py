import pygame, sys, math
import global_var as GLOB




class Mostro():
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


    def aggiorna(self):
        radius = 360
        rot_vector = self.line_vector.rotate(self.angle) * radius
        start = round(self.x), round(self.y)
        end = round(self.x - rot_vector.x), round(self.y - rot_vector.y)
        self.line = pygame.draw.line(GLOB.screen, (5,80,255), start, end, 8)

        val = 2

        immagine = pygame.image.load("Characters_Image/luce.png").convert_alpha()
        immagine = pygame.transform.scale(immagine, (immagine.get_width() * GLOB.MULT * val, immagine.get_height() * GLOB.MULT * val))

        immagine = pygame.transform.flip(immagine, False, False)
        immagine = pygame.transform.rotate(immagine, self.angle_triangle)

        GLOB.screen.blit(immagine, (GLOB.screen_width/2 - int(immagine.get_width()/2)  - rot_vector.x/2, GLOB.screen_height/2 - int(immagine.get_height()/2) - rot_vector.y/2))

        print(" Punto X: ",start,  " Punto Y: ", end)

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

    while True:

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