import pygame
import global_var as GLOB
import main
from collections import OrderedDict

class Map():
    def __init__(self, risoluzione, tipo_stanza, path):
        self.path = path
        self.tiles_stanza = tipo_stanza
        self.tiles_risoluzione = risoluzione
        self.tiles_mappa = pygame.image.load(path+"nero.png").convert()
        self.tiles_immagini = {}
        val = None

        self.tiles_collisioni = {
            "Bancone_chimica1" : (6, 12, 30, 14),
            "Bancone_chimica2" : (0, 12, 24, 14),
            "Banco" : (6, 12, 24, 14),
            "Banco_obliquo" : (0, 0, 32, 32),
        }


        self.tiles_oggetti = {
            
            "Bancone_chimica1" : ["bancone1-0", val, self.tiles_collisioni.get("Bancone_chimica1")],
            "Bancone_chimica2" : ["bancone1-1", val, self.tiles_collisioni.get("Bancone_chimica2")],
            "Bancone_chimica3" : ["bancone2-0", val, self.tiles_collisioni.get("Bancone_chimica1")],
            "Bancone_chimica4" : ["bancone2-1", val, self.tiles_collisioni.get("Bancone_chimica2")],
            "Bancone_chimica5" : ["bancone3-0", val, self.tiles_collisioni.get("Bancone_chimica1")],
            "Bancone_chimica6" : ["bancone3-1", val, self.tiles_collisioni.get("Bancone_chimica2")],
            "Bancone_chimica7" : ["bancone4-0", val, self.tiles_collisioni.get("Bancone_chimica1")],
            "Bancone_chimica8" : ["bancone4-1", val, self.tiles_collisioni.get("Bancone_chimica2")],

            "Banco" : ["banco", val, self.tiles_collisioni.get("Banco")],
            "Banco_obliquo" : ["banco-obliquo", val, self.tiles_collisioni.get("Banco_obliquo")],
        }

    def load_images(self, event, id):
        self.tiles_oggetti[event][1] = id
        #print(self.path+self.tiles_oggetti[event][0]+".png")
        if str(type(self.tiles_oggetti[event][0])) != "<class 'pygame.Surface'>":
            value = pygame.image.load(self.path+self.tiles_oggetti[event][0]+".png").convert_alpha()
            value = pygame.transform.scale(value, (value.get_width() * GLOB.MULT, value.get_height() * GLOB.MULT))
            self.tiles_oggetti[event][0] = value

    def load_map(self, path):
        self.tiles_mappa = pygame.image.load(path).convert()
        self.tiles_mappa = pygame.transform.scale(self.tiles_mappa, (self.tiles_mappa.get_width() * GLOB.MULT, self.tiles_mappa.get_height() * GLOB.MULT))

    def render(self, lista, object, var, hitbox):
        x = 0
        y = 0

        for valore_y in range(len(lista)):

            x = 0
            for valore_x in range(len(lista[valore_y])):
                condition = lista[valore_y][valore_x] == var

                if condition and object != None and not GLOB.Drop_Frames:
                    GLOB.screen.blit(object, (main.cam.getPositionX()+x * GLOB.MULT, main.cam.getPositionY()+y * GLOB.MULT))
                    #print("Render | Oggetto a schermo!", object)
                    
                if condition and hitbox != None:
                    collisione = pygame.Rect((main.cam.getPositionX()+(x+hitbox[0]) * GLOB.MULT),(main.cam.getPositionY()+(y+hitbox[1]) * GLOB.MULT), hitbox[2] * GLOB.MULT, hitbox[3] * GLOB.MULT)
                    #print("Render | Collisione Oggetto Impostata!", collisione)
                    main.player.HasCollision(collisione)
                
                    if GLOB.Debug:
                        pygame.draw.rect(GLOB.screen, (255,0,0), collisione, int(1*GLOB.MULT))

                x += self.tiles_risoluzione

            y += self.tiles_risoluzione

    def render_gamemapCollision(self, lista, var, collisione):
        self.render(lista, None, var, collisione)

    def render_object(self, event):
        lista_chiavi = list(self.tiles_oggetti.keys())

        if not GLOB.Drop_Frames:

            for value in range(len(lista_chiavi)):
                condition =  str(type(self.tiles_oggetti.get(lista_chiavi[value])[0])) == "<class 'pygame.Surface'>"
                print(str(lista_chiavi[value])+" | "+str(condition))
                if condition:
                    
                    try:      
                        if  self.tiles_oggetti.get(lista_chiavi[value])[2] == None:
                            collisione = (0, 0, self.tiles_risoluzione, self.tiles_risoluzione)
                        else:
                            collisione = self.tiles_oggetti.get(lista_chiavi[value])[2]

                        self.render(lista = event, object = self.tiles_oggetti.get(lista_chiavi[value])[0], var = self.tiles_oggetti.get(lista_chiavi[value])[1], hitbox = collisione)
                        print("Render_object | Oggetto Caricato!")
                    except KeyError:
                        print("Render_object | Errore nel caricare l'oggetto")

    def render_collision(self, event):
        self.render(event, None, 3, (0, 0, 32, 32))

    def render_map(self, pos):
        GLOB.screen.blit(self.tiles_mappa, (main.cam.getPositionX() + pos[0] * GLOB.MULT, main.cam.getPositionY() + pos[1] * GLOB.MULT))



chimica_oggetti = [
[-1],
[-1],
[-1],
[-1],
[-1],
[-1,-1,6,1,-1,2,3,-1,4,5,-1],
[-1],
[-1,-1,2,3,-1,6,7,-1,6,7,-1],
[-1],
[-1,-1,4,5,-1,2,3,-1,0,3,-1],
[-1]
]

chimica_collisioni = [

[6,6,6,6,6,6,6,6,6,6,6,6],
[6,0,0,0,0,0,0,0,0,0,0,6],
[6,0,0,0,0,0,0,0,0,0,0,6],
[6,3,3,3,3,3,3,3,3,3,3,6],
[6,-1,11,10,-1,11,10,-1,11,10,-1,6],
[6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,6],
[6,-1,11,10,-1,11,10,-1,11,10,-1,6],
[6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,6],
[6,-1,11,10,-1,11,10,-1,11,10,-1,6],
[6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,6],
[6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,6],
[6,7,7,7,7,7,7,7,7,7,7,7,6],
[6,6,6,6,6,6,6,6,6,6,6,6,6]


]