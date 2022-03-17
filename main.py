import pygame, os, sys

#Importo i vari file e classi necessarie
import giocatore, menu, camera
from button import Bar, Button, Dialoghi
from pygame import mixer


# Importo le variabili Globali
import global_var as GLOB

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

#funzione di default
def inizializza():
    global obstacle, player, cam, clock, sceltaG

    """
 --- Cambio il personaggio in base alla scelta del giocatore ---
        
    """
    
    GLOB.Player_speed = 2 * GLOB.MULT / GLOB.Delta_Time
    GLOB.Player_default_speed = GLOB.Player_speed
    
    if GLOB.Scelta==0:
        
        # SceltaG è il percorso dove si trovano i sprite per le animazioni
        sceltaG="/Senex"

        # In base alla statistica della velolità del giocatore vado ad impostrare la velocità corrente che deve avere il player nel gioco
        GLOB.PlayerRun_speed = 1 + GLOB.Senex_Stat[0]/10

    elif GLOB.Scelta==1:
        sceltaG="/Seima"
        GLOB.PlayerRun_speed = 1 + GLOB.Seima_Stat[0]/10
    elif GLOB.Scelta==2:
        sceltaG="/Alexandra"
        GLOB.PlayerRun_speed = 1 + GLOB.Aleks_Stat[0]/10
    elif GLOB.Scelta==3:
        sceltaG="/XPeppoz"
        GLOB.PlayerRun_speed = 1 + GLOB.Beppe_Stat[0]/10
    elif GLOB.Scelta==4:
        sceltaG="/Giulio"
        GLOB.PlayerRun_speed = 1 + GLOB.Dark_Stat[0]/10
    else:
        sceltaG="/Senex"
        GLOB.PlayerRun_speed = 1 + GLOB.Senex_Stat[0]/10



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
    player = giocatore.Player(GLOB.screen_width/2-Player_width/2, GLOB.screen_height/2-Player_height/2, sceltaG, Player_width, Player_height, character_image)

    # Faccio nascere l'oggetto "cam"
    cam = camera.Cam()


#Funzione Volume e Audio del gioco
def options_audio():
    # Setto visibile il cursore del mouse
    pygame.mouse.set_visible(True)

    indietro = False

    BG_Seimi = pygame.image.load("assets/BG_semitransparent.png")
    BG_Seimi = pygame.transform.scale(BG_Seimi, (GLOB.screen_width, GLOB.screen_height))

    while not indietro:

        cam.update(GLOB.Cam_visible)
        obstacle = pygame.Rect((GLOB.screen_width/2-30*GLOB.MULT+cam.getPositionX()),(GLOB.screen_height/2-75*GLOB.MULT+cam.getPositionY()), 50*GLOB.MULT, 50*GLOB.MULT)
        pygame.draw.rect(GLOB.screen, (0,100,255), obstacle)
        player.update() # richiama la funzione di aggiornamento del giocatore


        GLOB.screen.blit(BG_Seimi, (0, 0))

        # Ottengo la posizione corrente del cursore del mouse
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE_TEXT = menu.get_font(12*int(GLOB.MULT)).render("AUDIO SETTINGS", True, "#e9eef7")
        PAUSE_RECT = PAUSE_TEXT.get_rect(center=(GLOB.screen_width/2, 50*GLOB.MULT))

        AUDIO_TEXT = menu.get_font(10*int(GLOB.MULT)).render("EFFETTI SONORI: ", True, "#e9eef7")
        AUDIO_RECT = AUDIO_TEXT.get_rect(center=(GLOB.screen_width/2, 90*GLOB.MULT))

        MUSICA_TEXT = menu.get_font(10*int(GLOB.MULT)).render("MUSICA: ", True, "#e9eef7")
        MUSICA_RECT = MUSICA_TEXT.get_rect(center=(GLOB.screen_width/2, 130*GLOB.MULT))

        #BARRA AUDIO
        AUDIO = Bar((GLOB.screen_width/2, 100*GLOB.MULT), "#4287f5", GLOB.AU, 1)
        AUDIO.update(GLOB.screen)


        #BARRA MUSICA
        MUSICA = Bar((GLOB.screen_width/2, 140*GLOB.MULT), "#4287f5", GLOB.MU, 1)
        MUSICA.update(GLOB.screen)


        AUDIOPLUS_BUTTON = Button(image=None, pos=(GLOB.screen_width/2+20*GLOB.MULT, 110*GLOB.MULT), 
                            text_input="+", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=1)

        AUDIOLESS_BUTTON = Button(image=None, pos=(GLOB.screen_width/2-20*GLOB.MULT, 110*GLOB.MULT), 
                            text_input="-", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=1)

        MUSICPLUS_BUTTON = Button(image=None, pos=(GLOB.screen_width/2+20*GLOB.MULT, 150*GLOB.MULT), 
                            text_input="+", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=1)

        MUSICLESS_BUTTON = Button(image=None, pos=(GLOB.screen_width/2-20*GLOB.MULT, 150*GLOB.MULT), 
                            text_input="-", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=1)

        QUIT_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, 190*GLOB.MULT), 
                            text_input="BACK", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=2)
		
        for button in [AUDIOPLUS_BUTTON, AUDIOLESS_BUTTON, MUSICPLUS_BUTTON, MUSICLESS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(GLOB.screen)

        for event_pausa in pygame.event.get():

            button_sound = mixer.Sound("suoni/option-sound.wav")
            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_ESCAPE] or event_pausa.type == pygame.MOUSEBUTTONDOWN and AUDIOPLUS_BUTTON.checkForInput(MENU_MOUSE_POS):
                GLOB.AU += 1

                if GLOB.AU > 10:
                    GLOB.AU = 10

                button_sound.set_volume(0.16*GLOB.AU)
                button_sound.play()

            if keys_pressed[pygame.K_ESCAPE] or event_pausa.type == pygame.MOUSEBUTTONDOWN and AUDIOLESS_BUTTON.checkForInput(MENU_MOUSE_POS):
                GLOB.AU -= 1

                if GLOB.AU < 0:
                    GLOB.AU = 0
                
                button_sound.set_volume(0.16*GLOB.AU)
                button_sound.play()

            if keys_pressed[pygame.K_ESCAPE] or event_pausa.type == pygame.MOUSEBUTTONDOWN and MUSICPLUS_BUTTON.checkForInput(MENU_MOUSE_POS):
                GLOB.MU += 1

                if GLOB.MU > 10:
                    GLOB.MU = 10

                button_sound.set_volume(0.16*GLOB.MU)
                button_sound.play()

            if keys_pressed[pygame.K_ESCAPE] or event_pausa.type == pygame.MOUSEBUTTONDOWN and MUSICLESS_BUTTON.checkForInput(MENU_MOUSE_POS):
                GLOB.MU -= 1

                if GLOB.MU < 0:
                    GLOB.MU = 0
                
                button_sound.set_volume(0.16*GLOB.MU)
                button_sound.play()

            if event_pausa.type == pygame.QUIT:
                pygame.quit()
                sys.exit()	# mi riapplica le variabili di default quindi è come se riavviassi il gioco

            
            if event_pausa.type == pygame.MOUSEBUTTONDOWN:

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    indietro = True
                    pausa()

        GLOB.screen.blit(PAUSE_TEXT, PAUSE_RECT)
        GLOB.screen.blit(AUDIO_TEXT, AUDIO_RECT)
        GLOB.screen.blit(MUSICA_TEXT, MUSICA_RECT)
        

        pygame.display.flip()
        clock.tick(GLOB.FPS) # setto i FramesPerSecond

# Funzione Gioco in Pausa
def pausa():

    # Setto visibile il cursore del mouse
    pygame.mouse.set_visible(True)

    ricominciamo = False

    BG_Seimi = pygame.image.load("assets/BG_semitransparent.png")
    BG_Seimi = pygame.transform.scale(BG_Seimi, (GLOB.screen_width, GLOB.screen_height))
	
    while not ricominciamo:

        player.setAllkeys(False)

        cam.update(GLOB.Cam_visible)
        obstacle = pygame.Rect((GLOB.screen_width/2-30*GLOB.MULT+cam.getPositionX()),(GLOB.screen_height/2-75*GLOB.MULT+cam.getPositionY()), 50*GLOB.MULT, 50*GLOB.MULT)
        pygame.draw.rect(GLOB.screen, (0,100,255), obstacle)
        player.update() # richiama la funzione di aggiornamento del giocatore


        GLOB.screen.blit(BG_Seimi, (0, 0))

        # Ottengo la posizione corrente del cursore del mouse
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE_TEXT = menu.get_font(10*int(GLOB.MULT)).render("MENU DI PAUSA", True, "#e9eef7")
        PAUSE_RECT = PAUSE_TEXT.get_rect(center=(GLOB.screen_width/2, 50*GLOB.MULT))


        PLAY_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, 110*GLOB.MULT), 
                            text_input="PLAY", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=2)
        
        OPTIONS_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, 150*GLOB.MULT), 
                            text_input="AUDIO SETTINGS", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=2)
        
        QUIT_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, 190*GLOB.MULT), 
                            text_input="BACK TO MENU", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=2)
		
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
                sys.exit()	# mi riapplica le variabili di default quindi è come se riavviassi il gioco

            if event_pausa.type == pygame.MOUSEBUTTONDOWN:

                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                     options_audio()
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
                GLOB.Player_speed = GLOB.Player_speed * GLOB.PlayerRun_speed
            else:
                GLOB.Player_speed = GLOB.Player_default_speed

    """
    
        ---- Indico la classe dialoghi ----
    
    """
    Saluto = Dialoghi(personaggio = "Dark Angel", descrizione = "Questo messaggio, è un messaggio di prova.")

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
            if keys_pressed[pygame.K_F3]:
        
                if not GLOB.Debug:
                    GLOB.Debug = True
                    GLOB.Cam_visible = True
                elif GLOB.Debug:
                    GLOB.Debug = False
                    GLOB.Cam_visible = False
        
        GLOB.screen.fill(GLOB.Background_Color)
        cam.update(GLOB.Cam_visible)
        player.update() # richiama la funzione di aggiornamento del giocatore
        
        # Si consiglia di mettere una grandezza non minore di 18 w/h
        obstacle = pygame.Rect((GLOB.screen_width/2-30*GLOB.MULT+cam.getPositionX()),(GLOB.screen_height/2-75*GLOB.MULT+cam.getPositionY()), 50*GLOB.MULT, 50*GLOB.MULT)

        pygame.draw.rect(GLOB.screen, (0,100,255), obstacle)
        player.HasCollision(obstacle)


        # print("DEBUG: "+str(GLOB.Debug))

        Saluto.effetto_testo()
        Saluto.stampa()
            
        
                
        if GLOB.Debug:
            
            sprint = GLOB.Player_speed > GLOB.Player_default_speed

            key = "0"

            if player.getUpPress():
                key = "↑"
            elif player.getDownPress():
                key = "↓"
            elif player.getLeftPress():
                key = "←"
            elif player.getRightPress():
                key = "→"

            if sprint:
                key = "|"+key+"|"
            
            FPS_TEXT = get_font(8*int(GLOB.MULT)).render("FPS: "+str(int(clock.get_fps())), True, "white")
            FPS_RECT = FPS_TEXT.get_rect(center=(GLOB.screen_width-40*GLOB.MULT, 20*GLOB.MULT))

            DROP_TEXT = get_font(5*int(GLOB.MULT)).render("DROP "+str(100-int(clock.get_fps()*100/GLOB.FPS))+"%", True, "red")
            DROP_RECT = DROP_TEXT.get_rect(center=(GLOB.screen_width-95*GLOB.MULT, 20*GLOB.MULT))

            KEY_TEXT = get_font(10*int(GLOB.MULT)).render(key, True, "blue")
            KEY_RECT = KEY_TEXT.get_rect(center=(GLOB.screen_width-140*GLOB.MULT, 20*GLOB.MULT))

            if player.Last_keyPressed != "Null":
                GLOB.screen.blit(KEY_TEXT, KEY_RECT)

            if int(clock.get_fps()) <= (GLOB.FPS-(GLOB.FPS/20)):
                #print("Gli fps sono scesi: "+str(clock.get_fps()))
                GLOB.screen.blit(DROP_TEXT, DROP_RECT)
                

            GLOB.screen.blit(FPS_TEXT, FPS_RECT)

            if keys_pressed[pygame.K_TAB]:
                pygame.draw.rect(GLOB.screen, (0,255,255), player.mesh, int(1*GLOB.MULT))
                pygame.draw.rect(GLOB.screen, (255,0,0), obstacle, int(1*GLOB.MULT))

            if keys_pressed[pygame.K_o]:
                GLOB.Moff -= 1

            if keys_pressed[pygame.K_p]:
                GLOB.Moff += 1

            RUN_TEXT = get_font(8*int(GLOB.MULT)).render("V-A: "+str(GLOB.Player_speed), True, "white")
            RUN_RECT = RUN_TEXT.get_rect(center=(40*GLOB.MULT, 20*GLOB.MULT))

            GLOB.screen.blit(RUN_TEXT, RUN_RECT)

            POS_TEXT = get_font(8*int(GLOB.MULT)).render("x/y: "+str(int(player.getPositionX()-cam.getPositionX()))+" | "+str(int(player.getPositionY()-cam.getPositionY())), True, "white")
            POS_RECT = POS_TEXT.get_rect(center=(200*GLOB.MULT, 20*GLOB.MULT))

            GLOB.screen.blit(POS_TEXT, POS_RECT)

        
        pygame.display.flip() # ti permette di aggiornare una area dello schermo per evitare lag e fornire piu' ottimizzazione
        pygame.display.update()

        clock.tick(GLOB.FPS) # setto i FramesPerSecond
    
    pygame.quit() # per stoppare pygame in modo appropriato
    sys.exit()


# se volessi importare il file non verrebbe autoeseguito automaticamente
if __name__ == "__main__":
    pygame.init()
    main()