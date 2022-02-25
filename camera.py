import pygame, os
import main
import global_var as GLOB

# Creazione della classe Player ed è figlia di sprite +ottimizzata e veloce
class Cam(pygame.sprite.Sprite):
    def __init__(self, image, pos, scala):

        #indico il giocatore impostato
        self.setPositionX(pos[0]) 
        self.setPositionY(pos[1])

        self.image = pygame.image.load(image).convert()

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.image = pygame.transform.scale(self.image,((self.width*GLOB.MULT*scala), (self.height*GLOB.MULT*scala)))


    def setPositionX(self, x):
        self.x = x

    def setPositionY(self, y):
        self.y = y

    def getPositionX(self):
        return self.x

    def getPositionY(self):
        return self.y

        
    def update(self):
        GLOB.screen.blit(self.image, (self.x, self.y))

        Moff = 1
        offset = (8 * Moff * GLOB.MULT, 4.5 * Moff * GLOB.MULT)

        a =  main.player.getPositionX() >= GLOB.screen_width - offset[0] - main.player.width
        b =  main.player.getPositionX() <= offset[1]

        c =  main.player.getPositionY() >= GLOB.screen_height - offset[0] - main.player.height
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