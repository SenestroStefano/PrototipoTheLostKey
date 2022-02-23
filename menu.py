import pygame, sys, os
from button import Button
import global_var as GLOB

import main
from global_var import screen, screen_width, screen_height

pygame.init()

pygame.display.set_caption("Menu")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    main.inizializza()
    main.main()
    
def options():
    while True:

        BG_Option = pygame.image.load("assets/Background.png")
        BG_Option = pygame.transform.scale(BG_Option, (GLOB.screen_width, GLOB.screen_height))

        if GLOB.Scelta==1:
            char = "Senex.png"
        elif GLOB.Scelta==2:
            char = "Seima.png"
        elif GLOB.Scelta==3:
            char = "Aleks.png"
        elif GLOB.Scelta==4:
            char = "Beppe.png"
        elif GLOB.Scelta==5:
            char = "Giulio.png"
        else:
            char = "Senex.png"


        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(BG_Option, (0,0))

        OPTIONS_TEXT = get_font(11*int(GLOB.MULT)).render("Scegli il personaggio e la dimensione.", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(int(GLOB.screen_width/2), 50*GLOB.MULT))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        CHARACTER = pygame.image.load(os.path.join("Characters_Image",char))

        BG_Menu = pygame.image.load("assets/Background.png")
        BG_Menu = pygame.transform.scale(BG_Menu, (GLOB.screen_width, GLOB.screen_height))


        Scala = 2.5 * GLOB.MULT

        character_width = CHARACTER.get_width() * Scala
        character_height = CHARACTER.get_height() * Scala
        CHARACTER = pygame.transform.scale(CHARACTER, (character_width, character_height))

        screen.blit(CHARACTER, (int(GLOB.screen_width/2)-character_width/2,50*GLOB.MULT))

        Rchange = Button(image=None, pos=(int(GLOB.screen_width/2)+140, int(GLOB.screen_height/2)), 
                            text_input=">", font=get_font(20*int(GLOB.MULT)), base_color="White", hovering_color="red")

        Rchange.changeColor(OPTIONS_MOUSE_POS)
        Rchange.update(screen)

        Lchange = Button(image=None, pos=(int(GLOB.screen_width/2)-140, int(GLOB.screen_height/2)), 
                            text_input="<", font=get_font(20*int(GLOB.MULT)), base_color="White", hovering_color="red")

        Lchange.changeColor(OPTIONS_MOUSE_POS)
        Lchange.update(screen)

        MRchange = Button(image=None, pos=(int(GLOB.screen_width/2)+220, int(GLOB.screen_height/2)), 
                            text_input="+", font=get_font(20*int(GLOB.MULT)), base_color="White", hovering_color="red")

        MRchange.changeColor(OPTIONS_MOUSE_POS)
        MRchange.update(screen)


        MLchange = Button(image=None, pos=(int(GLOB.screen_width/2)-220, int(GLOB.screen_height/2)), 
                            text_input="-", font=get_font(20*int(GLOB.MULT)), base_color="White", hovering_color="red")

        MLchange.changeColor(OPTIONS_MOUSE_POS)
        MLchange.update(screen)


        OPTIONS_BACK = Button(image=None, pos=(int(GLOB.screen_width/2), 220*GLOB.MULT), 
                            text_input="BACK", font=get_font(20*int(GLOB.MULT)), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

                if Rchange.checkForInput(OPTIONS_MOUSE_POS):
                    GLOB.Scelta+=1

                    if GLOB.Scelta>5:
                        GLOB.Scelta=1

                if Lchange.checkForInput(OPTIONS_MOUSE_POS):
                    GLOB.Scelta-=1

                    if GLOB.Scelta<1:
                        GLOB.Scelta=5

                if MLchange.checkForInput(OPTIONS_MOUSE_POS):
                    GLOB.MULT-=0.1

                    if GLOB.MULT<=1:
                        GLOB.MULT=1



                if MRchange.checkForInput(OPTIONS_MOUSE_POS):
                    GLOB.MULT+=0.1

                    if GLOB.MULT>=4:
                        GLOB.MULT=4

                GLOB.screen_width = 480*GLOB.MULT
                GLOB.screen_height = 270*GLOB.MULT

                GLOB.screen = pygame.display.set_mode((GLOB.screen_width,GLOB.screen_height))

        CHARACTER = pygame.transform.scale(CHARACTER, (character_width, character_height))
                
        pygame.display.flip()
        pygame.display.update()

def main_menu():
    pygame.mouse.set_visible(True)
    while True:

        BG_Menu = pygame.image.load("assets/Background.png")
        BG_Menu = pygame.transform.scale(BG_Menu, (GLOB.screen_width, GLOB.screen_height))

        screen.blit(BG_Menu, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(25*int(GLOB.MULT)).render("MENU PRINCIPALE", True, "#e9eef7")
        MENU_RECT = MENU_TEXT.get_rect(center=(int(GLOB.screen_width/2), 20*GLOB.MULT))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(int(GLOB.screen_width/2), 80*GLOB.MULT), 
                            text_input="PLAY", font=get_font(20*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White")
        
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(int(GLOB.screen_width/2), 150*GLOB.MULT), 
                            text_input="OPTIONS", font=get_font(20*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White")
        
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(int(GLOB.screen_width/2), 220*GLOB.MULT), 
                            text_input="QUIT", font=get_font(20*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        pygame.display.update()

main_menu()