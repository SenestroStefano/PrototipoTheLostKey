import pygame, sys
import global_var as GLOB

class Delay():
    def __init__(self, sec, event):
        self.__min = 0
        self.__max = sec * GLOB.FPS
        self.__increment = 1
        self.__function = event
        self.__flag = True
        self.__times = 0

    # | Avvia il delay -> Poi si interromperà |
    def Start(self):
        if self.__flag:
            self.__min += self.__increment

            if int(self.__min) >= self.__max:
                self.__function()
                self.__flag = False

    # | Restarta il delay |
    def ReStart(self):
        if not self.__flag:
            self.__min = 0
            self.__flag = True

    # | Imposta il delay a infinito |
    def Infinite(self):
        self.ReStart()
        self.Start()

    def TotTimes(self, val):
        if self.__times <= val * GLOB.FPS:
            self.ReStart()
            self.Start()
            self.__times += 1

    # | Stampa lo stato attuale del delay |
    def ActualState(self):
        print("| Current Second: %d | Max Seconds: %d | Function: %s |" %(self.__min/GLOB.FPS, self.__max/GLOB.FPS, self.__function))

def inizializza():
    global clock, immagine, immagine_width, immagine_height, mappa, delay, val, val_player, val_sfondo, flag_reverse, flag_animazione, superficie
    pygame.display.set_caption("Effetto")
    clock = pygame.time.Clock()
    immagine = pygame.image.load("Characters_image/Senex.png").convert_alpha()
    immagine = pygame.transform.scale(immagine, (immagine.get_width() * GLOB.MULT, immagine.get_height() * GLOB.MULT))
    immagine_width, immagine_height = immagine.get_width(), immagine.get_height()
    
    mappa = pygame.image.load("mappa/Mappa.png").convert()
    mappa = pygame.transform.scale(mappa, (mappa.get_width() * GLOB.MULT, mappa.get_height() * GLOB.MULT))

    delay = Delay(sec = 0.05, event = sgrana)
    val = 0
    val_player = 0
    flag_reverse = False
    flag_animazione = False

    superficie = pygame.surface.Surface((GLOB.screen_width, GLOB.screen_height))
    superficie.fill((0,0,0))

def sgrana():
    global immagine, val, val_player, flag_reverse, flag_animazione, mappa

    flag_player = False
    flag_screem = False

    if flag_animazione:

        if not flag_reverse:
            val_player += 4
            val += 16
        else:
            val_player -= 4
            val -= 16

        print(val, val_player)

        if val_player >= 310 or val >= 255:
            immagine = pygame.image.load("Characters_image/Senex.png").convert_alpha()
            immagine = pygame.transform.scale(immagine, ( immagine.get_width() * GLOB.MULT, immagine.get_height() * GLOB.MULT))
            mappa = pygame.image.load("mappa/Mappa.png").convert()
            mappa = pygame.transform.scale(mappa, (mappa.get_width() * GLOB.MULT, mappa.get_height() * GLOB.MULT))
        elif val_player <= 1:
            immagine = pygame.image.load("Characters_image/Senex.png").convert_alpha()
            immagine = pygame.transform.scale(immagine, (immagine.get_width() * GLOB.MULT, immagine.get_height() * GLOB.MULT))
            mappa = pygame.image.load("mappa/Mappa.png").convert()
            mappa = pygame.transform.scale(mappa, (mappa.get_width() * GLOB.MULT, mappa.get_height() * GLOB.MULT))

        if val >= 310:
            val = 310
            val_player = 1
            flag_reverse = True
        elif val <= 0:
            val = 0
            val_player = 1
            flag_reverse = False
            flag_animazione = False

        if val_player >= 256:
            val_player = 256
            flag_player = True
        elif val_player <= 1:
            val_player = 1
            flag_player = False

        num_alpha = 250

        mappa.set_alpha(val_player+num_alpha)
        immagine.set_alpha(val_player+num_alpha)
        superficie.set_alpha(val)

        if not flag_player:
            immagine = pygame.transform.scale(immagine, (immagine.get_width() / val_player, immagine.get_height() / val_player))
            immagine = pygame.transform.scale(immagine, (immagine.get_width() * val_player, immagine.get_height() * val_player))

        if not flag_screem:
            mappa = pygame.transform.scale(mappa, (mappa.get_width() / val_player, mappa.get_height() / val_player))
            mappa = pygame.transform.scale(mappa, (mappa.get_width() * val_player, mappa.get_height() * val_player))

def disegna():
    GLOB.screen.fill((0,0,0))

    GLOB.screen.blit(mappa, (val_player, val_player))
    GLOB.screen.blit(immagine, (GLOB.screen_width/2 - immagine.get_width()/2, GLOB.screen_height/2 - immagine.get_height()/2))

    delay.Infinite()
    GLOB.screen.blit(superficie, (0, 0))
    #rettangolo = pygame.Rect(GLOB.screen_width/2 - immagine.get_width()/2, GLOB.screen_height/2 - immagine.get_height()/2, immagine.get_width(), immagine.get_height())
    #pygame.draw.rect(GLOB.screen, (255, 0, 0), rettangolo, 1)

def main():
    global flag_animazione
    inizializza()

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                flag_animazione = True

        disegna()

        clock.tick(GLOB.FPS)
        pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    main()