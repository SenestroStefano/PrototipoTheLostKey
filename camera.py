import pygame
import main
import global_var as GLOB


"""

    ---  Classe che controlla la posizione attuale del giocatore dello schermo e aggiorna i contenuti dello schermo spostandoli 

                In questo modo ferma anche il giocatore e da' l'illusione che tutto si sta muovendo

"""

class Cam():
    def __init__(self):

        #indico il giocatore impostato
        self.setPositionX(0) 
        self.setPositionY(0)

        #self.image = pygame.image.load("assets/BackgroundCam.png").convert()

        #self.width = self.image.get_width()
        #self.height = self.image.get_height()

        #self.image = pygame.transform.scale(self.image,((self.width*GLOB.MULT*1), (self.height*GLOB.MULT*1)))


    def setPositionX(self, x):
        self.x = x

    def setPositionY(self, y):
        self.y = y

    def getPositionX(self):
        return self.x

    def getPositionY(self):
        return self.y

        
    def update(self):
        #GLOB.screen.blit(self.image, (self.x, self.y))

        offset = (4 * GLOB.Moff * GLOB.MULT, 2.25 * GLOB.Moff * GLOB.MULT)

        a =  main.player.getPositionX() >= GLOB.screen_width - offset[0] - main.player.width
        b =  main.player.getPositionX() <= offset[0]

        c =  main.player.getPositionY() >= GLOB.screen_height - offset[1] - main.player.height
        d =  main.player.getPositionY() <= offset[1]

        a1 = main.player.getRightPress()
        b1 = main.player.getLeftPress()

        c1 = main.player.getDownPress()
        d1 = main.player.getUpPress()

        if a and a1:
            main.player.setPositionX(main.player.getPositionX()-main.player.getVelocitaX())
            self.x -= main.player.getVelocitaX()
            # print("A vero")
    

        if b and b1:
            main.player.setPositionX(main.player.getPositionX()-main.player.getVelocitaX())
            self.x += -main.player.getVelocitaX()
            # print("B vero")


        if c and c1:
            main.player.setPositionY(main.player.getPositionY()-main.player.getVelocitaY())
            self.y -= main.player.getVelocitaY()
            # print("C vero")
    

        if d and d1:
            main.player.setPositionY(main.player.getPositionY()-main.player.getVelocitaY())
            self.y += -main.player.getVelocitaY()
            # print("D vero")
        
        #print("Posizione x: "+str(main.player.getPositionX())+" | Posizione y: "+str(main.player.getPositionY())+" | VelocitàX: "+str(main.player.getVelocitaX()))