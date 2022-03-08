import pygame, os, sys

#Importo i vari file e classi necessarie
import giocatore, menu, camera
from button import Button
from menu import get_font


# Importo le variabili Globali
import global_var as GLOB

#funzione di default
def inizializza():
    global obstacle, player, cam, clock, sceltaG

    """
 ---   Cambio il personaggio in base alla scelta del giocatore ---
        
    """

    if GLOB.Scelta==0:
        
        # SceltaG è il percorso dove si trovano i sprite per le animazioni
        sceltaG="/Senex"

        # In base alla statistica della velolità del giocatore vado ad impostrare la velocità corrente che deve avere il player nel gioco
        GLOB.PlayerRun_speed = 1 + GLOB.Senex_Stat[0]/10 / GLOB.Delta_Time * GLOB.MULT

    elif GLOB.Scelta==1:
        sceltaG="/Seima"
        GLOB.PlayerRun_speed = 1 + GLOB.Seima_Stat[0]/10 / GLOB.Delta_Time * GLOB.MULT
    elif GLOB.Scelta==2:
        sceltaG="/Alexandra"
        GLOB.PlayerRun_speed = 1 + GLOB.Aleks_Stat[0]/10 / GLOB.Delta_Time * GLOB.MULT
    elif GLOB.Scelta==3:
        sceltaG="/XPeppoz"
        GLOB.PlayerRun_speed = 1 + GLOB.Beppe_Stat[0]/10 / GLOB.Delta_Time * GLOB.MULT
    elif GLOB.Scelta==4:
        sceltaG="/Giulio"
        GLOB.PlayerRun_speed = 1 + GLOB.Dark_Stat[0]/10 / GLOB.Delta_Time * GLOB.MULT
    else:
        sceltaG="/Senex"
        GLOB.PlayerRun_speed = 1.5 / GLOB.Delta_Time * GLOB.MULT



    """
 ---   Setto il percorso degli sprite ---
        
    """
    
    #(0 => "/Senex" - 1 => "/Seima" - 2 => "/Alexandra" - 3 => "/XPeppoz" - 4 => "/Giulio" - Default => "/Senex")
    Folder_walkO = 'Characters'+sceltaG+'/WalkOrizontal'
    Folder_walkVD = 'Characters'+sceltaG+'/WalkVerticalD'
    Folder_walkVU = 'Characters'+sceltaG+'/WalkVerticalU'

    # estrapolo tutti i file (sprite/immagini) dalla cartella selezionata
    def riempi(percorso):
        FileNames = os.listdir(percorso)

        # Ordino i file e gli appendo ad una lista, in modo che le animazioni siano lineari e ordinate
        FileNames.sort()
        sorted(FileNames)

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

    # Inizializzazione Tupla di animazioni
    character_image = (GLOB.PlayerWalkingVD,GLOB.PlayerWalkingVU,GLOB.PlayerWalkingO)

    # Ottengo la larghezza e l'altezza che ha il giocatore nell'immagine ( questo per evitare di allungarla in modo sbagliato e non proporzionale )
    Player_width = pygame.image.load(os.path.join(Folder_walkVD,character_image[0][0])).convert().get_width() * GLOB.MULT / GLOB.Player_proportion
    Player_height = pygame.image.load(os.path.join(Folder_walkVD,character_image[0][0])).convert().get_height() * GLOB.MULT / GLOB.Player_proportion

    # Settaggio del Clock
    clock = pygame.time.Clock()

    # Fa Spawnare il giocatore e al centro dello schermo e con che velocità
    player = giocatore.Player(GLOB.screen_width/2, GLOB.screen_height/2, sceltaG, Player_width, Player_height, character_image)

    # Faccio nascere l'oggetto "cam"
    cam = camera.Cam()

# Funzione Gioco in Pausa
def pausa():

    # Setto visibile il cursore del mouse
    pygame.mouse.set_visible(True)

    ricominciamo = False

    BG_Seimi = pygame.image.load("assets/BG_semitransparent.png")
    BG_Seimi = pygame.transform.scale(BG_Seimi, (GLOB.screen_width, GLOB.screen_height))
	
    while not ricominciamo:

        player.setAllkeys(False)

        cam.update()
        obstacle = pygame.Rect((GLOB.screen_width/2-30*GLOB.MULT+cam.getPositionX()),(GLOB.screen_height/2-75*GLOB.MULT+cam.getPositionY()), 50*GLOB.MULT, 50*GLOB.MULT)
        pygame.draw.rect(GLOB.screen, (0,100,255), obstacle)
        player.update() # richiama la funzione di aggiornamento del giocatore


        GLOB.screen.blit(BG_Seimi, (0, 0))

        # Ottengo la posizione corrente del cursore del mouse
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE_TEXT = menu.get_font(10*int(GLOB.MULT)).render("MENU DI PAUSA", True, "#e9eef7")
        PAUSE_RECT = PAUSE_TEXT.get_rect(center=(GLOB.screen_width/2, 50*GLOB.MULT))


        PLAY_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, 110*GLOB.MULT), 
                            text_input="PLAY", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White")
        
        OPTIONS_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, 150*GLOB.MULT), 
                            text_input="OPTIONS", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White")
        
        QUIT_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, 190*GLOB.MULT), 
                            text_input="BACK TO MENU", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White")
		
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(GLOB.screen)

        for event_pausa in pygame.event.get():
			
            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_ESCAPE] or event_pausa.type == pygame.MOUSEBUTTONDOWN and PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                ricominciamo = True
                player.finish()
                main()

            if event_pausa.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event_pausa.type == pygame.QUIT:
                pygame.quit()
                sys.exit()	# mi riapplica le variabili di default quindi è come se riavviassi il gioco

            if event_pausa.type == pygame.MOUSEBUTTONDOWN:

                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                     #options()
                     print("Per ora non faccio ancora nulla")

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    menu.main_menu()

        GLOB.screen.blit(PAUSE_TEXT, PAUSE_RECT)

        pygame.display.flip()
        clock.tick(GLOB.FPS) # setto i FramesPerSecond


#funzione principale
def main():

    # Setto il cursore del mouse a non visibile
    pygame.mouse.set_visible(False)
   
    run = True # funzione mainloop() principale
    
    # Funzione che controlla se il tasto è stato premuto
    def key_pressed(event,IsPressed):

        # if event.key == pygame.K_s and event.key == pygame.K_w:
        #     player.setAllkeys(False)
        #     player.finish()

        # if event.key == pygame.K_a and event.key == pygame.K_d:
        #     player.finish()
        
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            player.setLeftPress(IsPressed)

            if IsPressed:
                player.animate()
                player.Last_keyPressed = "Left"
            else:
                player.finish()
            
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            player.setRightPress(IsPressed)

            if IsPressed:
                player.animate()
                player.Last_keyPressed = "Right"
            else:
                player.finish()

        if event.key == pygame.K_w or event.key == pygame.K_UP:
            player.setUpPress(IsPressed)

            if IsPressed:
                player.animate()
                player.Last_keyPressed = "Up"
            else:
                player.finish()

        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            player.setDownPress(IsPressed)

            if IsPressed:
                player.animate()
                player.Last_keyPressed = "Down"
            else:
                player.finish()

        if event.key == pygame.K_LSHIFT:
            if IsPressed:
                GLOB.Player_speed = GLOB.Player_speed * GLOB.PlayerRun_speed # GLOB.MULT non l'ho messo perchè lo ha gia'
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

        # if int(clock.get_fps())<110:
        #     print("| fps: "+str(int(clock.get_fps()))) # Per mostrare gli GLOB.FPS

        
        GLOB.screen.fill(GLOB.Background_Color)
        cam.update()
        player.update() # richiama la funzione di aggiornamento del giocatore
        
        # Si consiglia di mettere una grandezza non minore di 18 w/h
        obstacle = pygame.Rect((GLOB.screen_width/2-30*GLOB.MULT+cam.getPositionX()),(GLOB.screen_height/2-75*GLOB.MULT+cam.getPositionY()), 50*GLOB.MULT, 50*GLOB.MULT)

        pygame.draw.rect(GLOB.screen, (0,100,255), obstacle)
        player.HasCollision(obstacle)


        FPS_TEXT = get_font(8*int(GLOB.MULT)).render("FPS: "+str(int(clock.get_fps())), True, "white")
        FPS_RECT = FPS_TEXT.get_rect(center=(GLOB.screen_width-40*GLOB.MULT, 20*GLOB.MULT))

        #if int(clock.get_fps()) < GLOB.FPS-15:
        #    print("Gli fps sono scesi: "+str(clock.get_fps()))

        GLOB.screen.blit(FPS_TEXT, FPS_RECT)

        if keys_pressed[pygame.K_TAB]:
            pygame.draw.rect(GLOB.screen, (0,255,255), player.mesh, int(1*GLOB.MULT))


        print("La VW: "+str(GLOB.Player_default_speed)+" | La VR: "+str(GLOB.PlayerRun_speed)+" | AV: "+str(GLOB.Player_speed))


        pygame.display.flip() # ti permette di aggiornare una area dello schermo per evitare lag e fornire piu' ottimizzazione
        pygame.display.update()

        clock.tick(GLOB.FPS) # setto i FramesPerSecond

        #print("La velocità attuale è :"+str(GLOB.Player_speed)+" | Mentre il MULT è : "+str(GLOB.MULT))
    
    pygame.quit() # per stoppare pygame in modo appropriato
    sys.exit()


# se volessi importare il file non verrebbe autoeseguito automaticamente
if __name__ == "__main__":
    pygame.init()
    main()