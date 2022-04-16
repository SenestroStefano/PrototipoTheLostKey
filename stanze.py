import pygame, os, sys
import global_var as GLOB
import main


def Chimica():
    main.load_collisions()
    GLOB.Default_Map = "MappaGioco/Tileset/Stanze/1-PianoTerra/Chimica/Chimica.png"
#    print(GLOB.Default_Map)
    main.collisions.load_map(GLOB.Default_Map)



def caricaStanza():
    if main.player.getPositionX()-main.cam.getPositionX() >= 0 and main.player.getPositionY()-main.cam.getPositionY() >= 0:
        Chimica()