import pygame, os, sys
import global_var as GLOB
import main


def Chimica():
    main.load_collisions("ChimicaProva_CollisioniStefano.csv")
    GLOB.Default_Map = "MappaGioco/Tileset/Stanze/1-PianoTerra/Chimica/Chimica.png"
#    print(GLOB.Default_Map)
    main.load_images(GLOB.Default_Map, 0)



def caricaStanza():
    if main.player.getPositionX()-main.cam.getPositionX() >= 0 and main.player.getPositionY()-main.cam.getPositionY() >= 0:
        pass
    Chimica()