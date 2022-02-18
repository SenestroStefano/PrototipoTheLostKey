import pygame, os
import giocatore
import global_var as glob

# estrapolo tutti i file dalla cartella selezionata

try:
    a = int(input("Inserisci un numero 1-2-3-4: "))
except ValueError:
    a = 1


if a==1:
    sceltaG="/Senex"
else:
    if a==2:
        sceltaG="/Seima"
    else:
        if a==3:
            sceltaG="/Alexandra"
        else:
            if a==4:
                sceltaG="/XPeppoz"
            else:
                sceltaG="/Senex"


Folder_walkO = 'Characters'+sceltaG+'/WalkOrizontal'
Folder_walkVD = 'Characters'+sceltaG+'/WalkVerticalD'
Folder_walkVU = 'Characters'+sceltaG+'/WalkVerticalU'

def riempi(percorso):
    FileNames = os.listdir(percorso)
    
    for filename in FileNames:
        if percorso == Folder_walkO:
            # print("Trovato Percorso WO")
            glob.PlayerWalkingO.append(filename)
        if percorso == Folder_walkVD:
            # print("Trovato Percorso WVD")
            glob.PlayerWalkingVD.append(filename)
        if percorso == Folder_walkVU:
            # print("Trovato Percorso WVU")
            glob.PlayerWalkingVU.append(filename)

        # print("File name:"+filename+"\n\n")

riempi(Folder_walkO)
riempi(Folder_walkVD)
riempi(Folder_walkVU)

# Inizializzazione Vettore di animazioni
character_image = (glob.PlayerWalkingVD,glob.PlayerWalkingVU,glob.PlayerWalkingO)

# print(character_image)

Player_width = pygame.image.load(os.path.join(Folder_walkVD,character_image[0][0])).get_width() * glob.MULT / glob.Player_proportion
Player_height = pygame.image.load(os.path.join(Folder_walkVD,character_image[0][0])).get_height() * glob.MULT / glob.Player_proportion

# Settaggio del Clock
clock = pygame.time.Clock()

# Fa Spawnare il giocatore e al centro dello schermo e con che velocitò
player = giocatore.Player(glob.screen_width/2, glob.screen_height/2, sceltaG, Player_width, Player_height, character_image)

def key_pressed(event,IsPressed):
    
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
            glob.Player_speed = glob.Player_speed * 1.4 # glob.MULT non l'ho messo perchè lo ha gia'
        else:
            glob.Player_speed = glob.Player_default_speed


#funzione principale
def main():
    run = True # funzione mainloop() principale
    
    # Si consiglia di mettere una grandezza non minore di 18 w/h
    obstacle = pygame.Rect(glob.screen_width/2-30*glob.MULT,glob.screen_height/2-75*glob.MULT, 50*glob.MULT, 50*glob.MULT)
    while run:
        for event in pygame.event.get(): # per ogni evento che viene eseguito in pygame.event.get()
            
            keys_pressed = pygame.key.get_pressed()

            if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
                run = False

            if event.type == pygame.KEYDOWN:
                key_pressed(event,True)
                # print("Ultima key: ",player.Last_keyPressed)
                
            if event.type == pygame.KEYUP:
                key_pressed(event,False)
                player.Last_keyPressed = "Null"

        #print(str(int(clock.get_glob.FPS()))) # Per mostrare gli glob.FPS
            
        glob.screen.fill(glob.Background_Color) # colora lo sfondo con dei colori

        player.update() # richiama la funzione di aggiornamento del giocatore
        
        pygame.draw.rect(glob.screen, (0,100,255), obstacle)
        player.HasCollision(obstacle)

        if keys_pressed[pygame.K_TAB]:
            pygame.draw.rect(glob.screen, (255,0,0), player.mesh, 4)


        pygame.display.flip() # ti permette di aggiornare una area dello schermo per evitare lag e fornire piu' ottimizzazione

        clock.tick(glob.FPS) # setto gli FramesPerSecond
    
    pygame.quit() # per stoppare pygame in modo appropriato

# se volessi importare il file non verrebbe autoeseguito automaticamente
if __name__ == "__main__":
    pygame.init()
    main()