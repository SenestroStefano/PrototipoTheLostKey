import pygame, os, sys
import global_var as GLOB
import main


def Chimica():
    main.load_collisions("ChimicaProva_collisioni.csv")
    GLOB.Default_Map = "MappaGioco/Tileset/Stanze/1-PianoTerra/Chimica/ChimicaProva.png"
    main.load_images(GLOB.Default_Map, 0)



def caricaStanza():
    main.animazione.aggiorna_mappa()
    if main.player.getPositionX()-main.cam.getPositionX() >= 0 and main.player.getPositionY()-main.cam.getPositionY() >= 0:
        pass
    Chimica()