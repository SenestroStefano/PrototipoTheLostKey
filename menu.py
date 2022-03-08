import pygame, sys, os
from button import Button
from button import Bar
import global_var as GLOB

import main
from global_var import screen

pygame.init()

"""

    ---  FILE DEL MENU PRINCIPALE DELl'AVVIO DEL GIOCO	---

"""

pygame.display.set_caption(GLOB.TITLE)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    main.inizializza()
    main.main()
    
def options():
    
    flag_Fullscreen = False

    while True:

        if flag_Fullscreen == False:
            TEXT_FULLSCREEN = "SET FULLSCREEN"
        else:
            TEXT_FULLSCREEN = "TOGGLE FULLSCREEN"

        BG_Option = pygame.image.load("assets/Background.png")
        BG_Option = pygame.transform.scale(BG_Option, (GLOB.screen_width, GLOB.screen_height))

        if GLOB.Scelta==0:
            char = "Senex.png"
            name = "Senex"
        elif GLOB.Scelta==1:
            char = "Seima.png"
            name = "Seima"
        elif GLOB.Scelta==2:
            char = "Aleks.png"
            name = "Aleks"
        elif GLOB.Scelta==3:
            char = "Beppe.png"
            name = "Beppe"
        elif GLOB.Scelta==4:
            char = "Giulio.png"
            name = "Dark Angel"
        else:
            char = "Senex.png"
            name = "Senex"
            GLOB.Scelta = 0


        NAME_TEXT = get_font(12*int(GLOB.MULT)).render(name, True, "#e9eef7")
        NAME_RECT = NAME_TEXT.get_rect(center=(GLOB.screen_width/2, 80*GLOB.MULT))


        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(BG_Option, (0,0))

        screen.blit(NAME_TEXT, NAME_RECT)

        # OPTIONS_TEXT = get_font(25*int(GLOB.MULT)).render("MENU OPZIONI", True, "White")
        # OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(GLOB.screen_width/2, 20*GLOB.MULT))
        # screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        CHARACTER = pygame.image.load(os.path.join("Characters_Image",char))

        BG_Menu = pygame.image.load("assets/Background.png")
        BG_Menu = pygame.transform.scale(BG_Menu, (GLOB.screen_width, GLOB.screen_height))


        Scala = 2.5 * GLOB.MULT

        character_width = CHARACTER.get_width() * Scala
        character_height = CHARACTER.get_height() * Scala
        CHARACTER = pygame.transform.scale(CHARACTER, (character_width, character_height))

        screen.blit(CHARACTER, (GLOB.screen_width/2-character_width/2,50*GLOB.MULT))


        # VELOCITA'

        #TESTO
        Velocita_TEXT = get_font(8*int(GLOB.MULT)).render("Velocita'", True, "#e9eef7")
        Velocita_RECT = Velocita_TEXT.get_rect(center=(GLOB.screen_width/2, GLOB.screen_height/2+75*GLOB.MULT))

        screen.blit(Velocita_TEXT, Velocita_RECT)

        #BARRA
        Velocita = Bar((GLOB.screen_width/2, GLOB.screen_height/2+85*GLOB.MULT), GLOB.Stats[GLOB.Scelta][0], None)
        Velocita.update(screen)


        # MATERIE'

        posX_tabella = GLOB.screen_width-80*GLOB.MULT
        posY_tabella = GLOB.MULT*45
        scala_tabella = 1.5

        #BARRA Chimica
        Chimica = Bar((posX_tabella, posY_tabella*1.2), GLOB.Stats[GLOB.Scelta][1], scala_tabella)
        Chimica.update(screen)

        #BARRA Storia
        Storia = Bar((posX_tabella, posY_tabella*1.7), GLOB.Stats[GLOB.Scelta][2], scala_tabella)
        Storia.update(screen)

        #BARRA Inglese
        Inglese = Bar((posX_tabella, posY_tabella*2.2), GLOB.Stats[GLOB.Scelta][3], scala_tabella)
        Inglese.update(screen)

        #BARRA Fisica
        Fisica = Bar((posX_tabella, posY_tabella*2.7), GLOB.Stats[GLOB.Scelta][4], scala_tabella)
        Fisica.update(screen)

        #BARRA Matematica
        Matematica = Bar((posX_tabella, posY_tabella*3.2), GLOB.Stats[GLOB.Scelta][5], scala_tabella)
        Matematica.update(screen)

        #BARRA Informatica
        Informatica = Bar((posX_tabella, posY_tabella*3.7), GLOB.Stats[GLOB.Scelta][6], scala_tabella)
        Informatica.update(screen)

        #BARRA Italiano
        Italiano = Bar((posX_tabella, posY_tabella*4.2), GLOB.Stats[GLOB.Scelta][7], scala_tabella)
        Italiano.update(screen)

        #BARRA Sistemi
        Sistemi = Bar((posX_tabella, posY_tabella*4.7), GLOB.Stats[GLOB.Scelta][8], scala_tabella)
        Sistemi.update(screen)

        #BARRA TPSIT
        TPSIT = Bar((posX_tabella, posY_tabella*5.2), GLOB.Stats[GLOB.Scelta][9], scala_tabella)
        TPSIT.update(screen)

        #TESTO
        Chimica_TEXT = get_font(8*int(GLOB.MULT)).render("Chimica", True, "#e9eef7")
        Chimica_RECT = Chimica_TEXT.get_rect(center=(posX_tabella, posY_tabella))

        screen.blit(Chimica_TEXT, Chimica_RECT)

        #TESTO
        Storia_TEXT = get_font(8*int(GLOB.MULT)).render("Storia", True, "#e9eef7")
        Storia_RECT = Storia_TEXT.get_rect(center=(posX_tabella, posY_tabella*scala_tabella))

        screen.blit(Storia_TEXT, Storia_RECT)

        #TESTO
        Inglese_TEXT = get_font(8*int(GLOB.MULT)).render("Inglese", True, "#e9eef7")
        Inglese_RECT = Inglese_TEXT.get_rect(center=(posX_tabella, posY_tabella*2))

        screen.blit(Inglese_TEXT, Inglese_RECT)

        #TESTO
        Fisica_TEXT = get_font(8*int(GLOB.MULT)).render("Fisica", True, "#e9eef7")
        Fisica_RECT = Fisica_TEXT.get_rect(center=(posX_tabella, posY_tabella*2.5))

        screen.blit(Fisica_TEXT, Fisica_RECT)

        #TESTO
        Matematica_TEXT = get_font(8*int(GLOB.MULT)).render("Matematica", True, "#e9eef7")
        Matematica_RECT = Matematica_TEXT.get_rect(center=(posX_tabella, posY_tabella*3))

        screen.blit(Matematica_TEXT, Matematica_RECT)

        #TESTO
        Informatica_TEXT = get_font(8*int(GLOB.MULT)).render("Informatica", True, "#e9eef7")
        Informatica_RECT = Informatica_TEXT.get_rect(center=(posX_tabella, posY_tabella*3.5))

        screen.blit(Informatica_TEXT, Informatica_RECT)

        #TESTO
        Italiano_TEXT = get_font(8*int(GLOB.MULT)).render("Italiano", True, "#e9eef7")
        Italiano_RECT = Italiano_TEXT.get_rect(center=(posX_tabella, posY_tabella*4))

        screen.blit(Italiano_TEXT, Italiano_RECT)

        #TESTO
        Sistemi_TEXT = get_font(8*int(GLOB.MULT)).render("Sistemi", True, "#e9eef7")
        Sistemi_RECT = Sistemi_TEXT.get_rect(center=(posX_tabella, posY_tabella*4.5))

        screen.blit(Sistemi_TEXT, Sistemi_RECT)

        #TESTO
        TPSIT_TEXT = get_font(8*int(GLOB.MULT)).render("TPSIT", True, "#e9eef7")
        TPSIT_RECT = TPSIT_TEXT.get_rect(center=(posX_tabella, posY_tabella*5))

        screen.blit(TPSIT_TEXT, TPSIT_RECT)



        Rchange = Button(image=None, pos=(GLOB.screen_width/2+50*GLOB.MULT, GLOB.screen_height/2), 
                            text_input=">", font=get_font(20*int(GLOB.MULT)), base_color="White", hovering_color="red")

        Rchange.changeColor(OPTIONS_MOUSE_POS)
        Rchange.update(screen)

        Lchange = Button(image=None, pos=(GLOB.screen_width/2-50*GLOB.MULT, GLOB.screen_height/2), 
                            text_input="<", font=get_font(20*int(GLOB.MULT)), base_color="White", hovering_color="red")

        Lchange.changeColor(OPTIONS_MOUSE_POS)
        Lchange.update(screen)


        Screen_480x270 = Button(image=pygame.image.load("assets/Select Rect.png"), pos=(80*GLOB.MULT, GLOB.screen_height/2-110*GLOB.MULT), 
                            text_input="480 x 270", font=get_font(8*int(GLOB.MULT)), base_color="White", hovering_color="#2f3131")

        Screen_480x270.changeColor(OPTIONS_MOUSE_POS)
        Screen_480x270.update(screen)

        Screen_960x540 = Button(image=pygame.image.load("assets/Select Rect.png"), pos=(80*GLOB.MULT, GLOB.screen_height/2-70*GLOB.MULT), 
                    text_input="960 x 540", font=get_font(8*int(GLOB.MULT)), base_color="White", hovering_color="#2f3131")

        Screen_960x540.changeColor(OPTIONS_MOUSE_POS)
        Screen_960x540.update(screen)

        Screen_1440x810 = Button(image=pygame.image.load("assets/Select Rect.png"), pos=(80*GLOB.MULT, GLOB.screen_height/2-30*GLOB.MULT), 
                    text_input="1440 x 810", font=get_font(8*int(GLOB.MULT)), base_color="White", hovering_color="#2f3131")

        Screen_1440x810.changeColor(OPTIONS_MOUSE_POS)
        Screen_1440x810.update(screen)

        Screen_1920x1080 = Button(image=pygame.image.load("assets/Select Rect.png"), pos=(80*GLOB.MULT, GLOB.screen_height/2+10*GLOB.MULT), 
                    text_input="1920 x 1080", font=get_font(8*int(GLOB.MULT)), base_color="White", hovering_color="#2f3131")

        Screen_1920x1080.changeColor(OPTIONS_MOUSE_POS)
        Screen_1920x1080.update(screen)


        Screen_3840x2160 = Button(image=pygame.image.load("assets/Select Rect.png"), pos=(80*GLOB.MULT, GLOB.screen_height/2+50*GLOB.MULT), 
                    text_input="3840 x 2160", font=get_font(8*int(GLOB.MULT)), base_color="White", hovering_color="#2f3131")

        Screen_3840x2160.changeColor(OPTIONS_MOUSE_POS)
        Screen_3840x2160.update(screen)


        Screen_FULL = Button(image=pygame.image.load("assets/Select Rect.png"), pos=(80*GLOB.MULT, GLOB.screen_height/2+90*GLOB.MULT), 
                    text_input=TEXT_FULLSCREEN, font=get_font(8*int(GLOB.MULT)), base_color="White", hovering_color="#2f3131")

        Screen_FULL.changeColor(OPTIONS_MOUSE_POS)
        Screen_FULL.update(screen)




        OPTIONS_BACK = Button(image=None, pos=(GLOB.screen_width/2, 250*GLOB.MULT), 
                            text_input="BACK", font=get_font(20*int(GLOB.MULT)), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag_screen = False

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

                if Screen_480x270.checkForInput(OPTIONS_MOUSE_POS):
                    GLOB.MULT=1
                    flag_screen = True

                if Screen_960x540.checkForInput(OPTIONS_MOUSE_POS):
                    GLOB.MULT=2
                    flag_screen = True

                if Screen_1440x810.checkForInput(OPTIONS_MOUSE_POS):
                    GLOB.MULT=3
                    flag_screen = True

                if Screen_1920x1080.checkForInput(OPTIONS_MOUSE_POS):
                    GLOB.MULT=4
                    flag_screen = True

                if Screen_3840x2160.checkForInput(OPTIONS_MOUSE_POS):
                    GLOB.MULT=5
                    flag_screen = True
                
                if Screen_FULL.checkForInput(OPTIONS_MOUSE_POS):
                    flag_screen = True
                    
                    if flag_Fullscreen == False:
                        flag_Fullscreen = True
                    else:
                        flag_Fullscreen = False

                if flag_screen:
                    GLOB.screen_width = 480*GLOB.MULT
                    GLOB.screen_height = 270*GLOB.MULT

                    if not flag_Fullscreen:
                        GLOB.screen = pygame.display.set_mode((GLOB.screen_width,GLOB.screen_height))
                    else: 
                        GLOB.screen = pygame.display.set_mode((GLOB.screen_width,GLOB.screen_height),pygame.FULLSCREEN)

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
        MENU_RECT = MENU_TEXT.get_rect(center=(GLOB.screen_width/2, 20*GLOB.MULT))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(GLOB.screen_width/2, 80*GLOB.MULT), 
                            text_input="PLAY", font=get_font(20*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White")
        
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(GLOB.screen_width/2, 150*GLOB.MULT), 
                            text_input="OPTIONS", font=get_font(20*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White")
        
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(GLOB.screen_width/2, 220*GLOB.MULT), 
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