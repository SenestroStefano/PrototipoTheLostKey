import pygame, os, sys
import giocatore
import menu
from button import Button

import global_var as GLOB

#funzione di default
def inizializza():
    global obstacle, player, clock, sceltaG


    if GLOB.Scelta==1:
        sceltaG="/Senex"
    elif GLOB.Scelta==2:
        sceltaG="/Seima"
    elif GLOB.Scelta==3:
        sceltaG="/Alexandra"
    elif GLOB.Scelta==4:
        sceltaG="/XPeppoz"
    elif GLOB.Scelta==5:
        sceltaG="/Giulio"
    else:
        sceltaG="/Senex"

 
    Folder_walkO = 'Characters'+sceltaG+'/WalkOrizontal'
    Folder_walkVD = 'Characters'+sceltaG+'/WalkVerticalD'
    Folder_walkVU = 'Characters'+sceltaG+'/WalkVerticalU'

    # estrapolo tutti i file dalla cartella selezionata
    def riempi(percorso):
        FileNames = os.listdir(percorso)

        for filename in FileNames:
            if percorso == Folder_walkO:
                # print("Trovato Percorso WO")
                GLOB.PlayerWalkingO.append(filename)
            if percorso == Folder_walkVD:
                # print("Trovato Percorso WVD")
                GLOB.PlayerWalkingVD.append(filename)
            if percorso == Folder_walkVU:
                # print("Trovato Percorso WVU")
                GLOB.PlayerWalkingVU.append(filename)

            # print("File name:"+filename+"\n\n")

    riempi(Folder_walkO)
    riempi(Folder_walkVD)
    riempi(Folder_walkVU)

    # Inizializzazione Vettore di animazioni
    character_image = (GLOB.PlayerWalkingVD,GLOB.PlayerWalkingVU,GLOB.PlayerWalkingO)

    # print(character_image)

    Player_width = pygame.image.load(os.path.join(Folder_walkVD,character_image[0][0])).get_width() * GLOB.MULT / GLOB.Player_proportion
    Player_height = pygame.image.load(os.path.join(Folder_walkVD,character_image[0][0])).get_height() * GLOB.MULT / GLOB.Player_proportion

    # Settaggio del Clock
    clock = pygame.time.Clock()

    # Fa Spawnare il giocatore e al centro dello schermo e con che velocità
    player = giocatore.Player(GLOB.screen_width/2, GLOB.screen_height/2, sceltaG, Player_width, Player_height, character_image)

    # Si consiglia di mettere una grandezza non minore di 18 w/h
    obstacle = pygame.Rect(GLOB.screen_width/2-30*GLOB.MULT,GLOB.screen_height/2-75*GLOB.MULT, 50*GLOB.MULT, 50*GLOB.MULT)

    GLOB.Player_speed = 0.5 * GLOB.MULT
    GLOB.Player_default_speed = GLOB.Player_speed


def pausa():
    pygame.mouse.set_visible(True)

    ricominciamo = False

    BG_Seimi = pygame.image.load("assets/BG_semitransparent.png")
    BG_Seimi = pygame.transform.scale(BG_Seimi, (GLOB.screen_width, GLOB.screen_height))
	
    while not ricominciamo:

        player.setAllkeys(False)

        player.update() # richiama la funzione di aggiornamento del giocatore
        
        pygame.draw.rect(GLOB.screen, (0,100,255), obstacle)


        GLOB.screen.blit(BG_Seimi, (0, 0))

        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE_TEXT = menu.get_font(10*int(GLOB.MULT)).render("MENU DI PAUSA", True, "#e9eef7")
        PAUSE_RECT = PAUSE_TEXT.get_rect(center=(GLOB.screen_width/2, 50*GLOB.MULT))


        PLAY_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, 110*GLOB.MULT), 
                            text_input="PLAY", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White")
        
        OPTIONS_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, 150*GLOB.MULT), 
                            text_input="OPTIONS", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White")
        
        QUIT_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, 190*GLOB.MULT), 
                            text_input="QUIT", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White")
		
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(GLOB.screen)

        for event_pausa in pygame.event.get():
			
            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_ESCAPE] or event_pausa.type == pygame.MOUSEBUTTONDOWN and PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                ricominciamo = True
                player.finish()
                main()	# mi riapplica le variabili di default quindi è come se riavviassi il gioco

            if event_pausa.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event_pausa.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event_pausa.type == pygame.MOUSEBUTTONDOWN:

                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                     #options()
                     print("Per ora non faccio ancora nulla")

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    menu.main_menu()

        GLOB.screen.blit(PAUSE_TEXT, PAUSE_RECT)

        pygame.display.flip()
        clock.tick(GLOB.FPS) # setto gli FramesPerSecond


        # print("Sono in pausa")

#funzione principale
def main():

    pygame.mouse.set_visible(False)
   
    run = True # funzione mainloop() principale
    
    def key_pressed(event,IsPressed):

        # if event.key == pygame.K_s and event.key == pygame.K_w:
        #     player.setAllkeys(False)
        #     player.finish()

        if event.key == pygame.K_a and event.key == pygame.K_d:
            player.finish()
        
        if event.key == pygame.K_a:
            player.setLeftPress(IsPressed)

            if IsPressed:
                player.animate()
                player.Last_keyPressed = "Left"
            else:
                player.finish()
            
        if event.key == pygame.K_d:
            player.setRightPress(IsPressed)

            if IsPressed:
                player.animate()
                player.Last_keyPressed = "Right"
            else:
                player.finish()

        if event.key == pygame.K_w:
            player.setUpPress(IsPressed)

            if IsPressed:
                player.animate()
                player.Last_keyPressed = "Up"
            else:
                player.finish()

        if event.key == pygame.K_s:
            player.setDownPress(IsPressed)

            if IsPressed:
                player.animate()
                player.Last_keyPressed = "Down"
            else:
                player.finish()

        if event.key == pygame.K_LSHIFT:
            if IsPressed:
                GLOB.Player_speed = GLOB.Player_speed * 1.4 # GLOB.MULT non l'ho messo perchè lo ha gia'
            else:
                GLOB.Player_speed = GLOB.Player_default_speed



    while run:
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get(): # per ogni evento che viene eseguito in pygame.event.get()
            keys_pressed = pygame.key.get_pressed()

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                key_pressed(event,True)
                # print("Ultima key: ",player.Last_keyPressed)
                
            if event.type == pygame.KEYUP:
                key_pressed(event,False)
                player.Last_keyPressed = "Null"

            if keys_pressed[pygame.K_ESCAPE]:
                # run = False
                # menu.main_menu()
                pausa()

        #print(str(int(clock.get_GLOB.FPS()))) # Per mostrare gli GLOB.FPS
            
        GLOB.screen.fill(GLOB.Background_Color) # colora lo sfondo con dei colori

        player.update() # richiama la funzione di aggiornamento del giocatore
        
        pygame.draw.rect(GLOB.screen, (0,100,255), obstacle)
        player.HasCollision(obstacle)


        if keys_pressed[pygame.K_TAB]:
            pygame.draw.rect(GLOB.screen, (255,0,0), player.mesh, int(1*GLOB.MULT))


        pygame.display.flip() # ti permette di aggiornare una area dello schermo per evitare lag e fornire piu' ottimizzazione

        clock.tick(GLOB.FPS) # setto gli FramesPerSecond

        #print("La velocità attuale è :"+str(GLOB.Player_speed)+" | Mentre il MULT è : "+str(GLOB.MULT))
    
    pygame.quit() # per stoppare pygame in modo appropriato
    sys.exit()




# se volessi importare il file non verrebbe autoeseguito automaticamente
if __name__ == "__main__":
    pygame.init()
    main()