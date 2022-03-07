import pygame
TITLE = "The Lost Keys"

# Valori di proporzione

Delta_Time = 2 # Delta_Time (Congliabile 1/2)
Player_proportion = 1 # Divisore della grandezza del giocatore

#FPS
FPS = 60 * Delta_Time

# rapporto di proporzione allo schermo NON INFERIORE AD 1
MULT = 4

# print("Larghezza: "+str(Player_width)+" Altezza: "+str(Player_height))

Scelta = 1

Player_speed = 0.25 * MULT * Delta_Time
PlayerRun_speed = 0.7 * MULT * Delta_Time

Player_default_speed = Player_speed

# Inizializzazione lista di animazione camminata
PlayerWalkingO = []
PlayerWalkingVD = []
PlayerWalkingVU = []

# STATISTICHE
# Vel - Chimica - Storia - Inglese - Fisica - Matematica - Informatica - Italiano - Sistemi - TPSIT
Senex_Stat = [ 5, 8, 6, 7, 3, 6, 6, 5, 4, 10 ]
Seima_Stat = [ 2, 8, 10, 8, 9, 10, 10, 8, 10, 10 ] # fai schifo
Aleks_Stat = [ 5, 10, 10, 6, 2, 7, 8, 10, 7, 2 ]
Beppe_Stat = [ 6, 2, 8, 4, 2, 6, 6, 5, 9, 7 ]
Dark_Stat = [ 3, 8, 7, 9, 10, 8, 6, 7, 6, 2 ]

Stats = ( Senex_Stat, Seima_Stat, Aleks_Stat, Beppe_Stat, Dark_Stat )

Background_Color = (12, 24, 36)

# Dimensione Schermo
screen_width = 480 * MULT
screen_height = 270 * MULT

# Configurazione Schermo
screen = pygame.display.set_mode((screen_width,screen_height))
# screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption(TITLE)