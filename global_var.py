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

Player_speed = 0.5 * MULT
Player_default_speed = Player_speed

# Inizializzazione lista di animazione camminata
PlayerWalkingO = []
PlayerWalkingVD = []
PlayerWalkingVU = []

Background_Color = (12, 24, 36)

# Dimensione Schermo
screen_width = 480*MULT
screen_height = 270*MULT

# Configurazione Schermo
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(TITLE)
pygame.mouse.set_visible(False)