import pygame, os
import main
import global_var as GLOB

# Creazione della classe Player ed è figlia di sprite +ottimizzata e veloce
class Cam(pygame.sprite.Sprite):
    def __init__(self, image, pos):

        #indico il giocatore impostato
        self.setPositionX(pos[0]) 
        self.setPositionY(pos[1])

        self.image = pygame.image.load(image).convert()

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.image = pygame.transform.scale(self.image,((self.width*GLOB.MULT*5), (self.height*GLOB.MULT*5)))


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

        a =  main.player.getPositionX() >= GLOB.screen_width - 80*GLOB.MULT
        b =  main.player.getPositionX() <= 20*GLOB.MULT

        c =  main.player.getPositionY() >= GLOB.screen_height - 80*GLOB.MULT
        d =  main.player.getPositionY() <= 20*GLOB.MULT

        if a:
            main.player.setPositionX(main.player.getPositionX()-main.player.getVelocitaX())
            self.x -= 1
            print("A vero")
    

        if b:
            main.player.setPositionX(main.player.getPositionX()-main.player.getVelocitaX())
            self.x += 1
            print("B vero")


        if c:
            main.player.setPositionY(main.player.getPositionY()-main.player.getVelocitaY())
            self.y -= 1
            print("C vero")
    

        if d:
            main.player.setPositionY(main.player.getPositionY()-main.player.getVelocitaY())
            self.y += 1
            print("D vero")
        
        print("Posizione x: "+str(main.player.getPositionX())+" | Posizione y: "+str(main.player.getPositionY())+" | VelocitàX: "+str(main.player.getVelocitaX()))