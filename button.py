import global_var as GLOB
import pygame, sys
from pygame import mixer

"""
    ---  Classe genera un pulsante a schermo un pulsante cliccabile	---
"""

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color, scale):
    	
		if image != None:
			self.image_w, self.image_h = image.get_width()*GLOB.MULT/scale, image.get_height()*GLOB.MULT/scale
			self.image = pygame.transform.scale(image, (self.image_w, self.image_h))
		else:
			self.image = image

		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

	def changeScale(self, position, value):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.image = pygame.transform.scale(self.image, (self.image_w * value, self.image_h * value))
			self.x_pos -= value
			self.y_pos -= value
		else:
			self.image = pygame.transform.scale(self.image, (self.image_w, self.image_h))
			self.x_pos += value
			self.y_pos += value
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

"""
    ---  Classe genera una barra (usata per le statistiche)	e ne imposta il riempimento ---
"""

class Bar():
	def __init__(self, pos, color, number, div):

		self.x_pos = pos[0]
		self.y_pos = pos[1]

		self.color = color
		self.number = number
		self.div = div

		if number > 10:
			self.number = 10
		elif number < 0:
			self.number = 0

		if div == None:
			self.div = 1
		elif div > 8:
			self.div = 8
		elif div < 1:
			self.div = 1

		self.image = pygame.image.load("assets/BarraCompletamento.png")
		self.image = pygame.transform.scale(self.image, (self.image.get_width()*GLOB.MULT/self.div, self.image.get_height()*GLOB.MULT/self.div))
		
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

		if number != 0:
			
			self.BarScore = pygame.Rect(self.x_pos-85*GLOB.MULT/self.div, self.y_pos-3*GLOB.MULT/self.div, 17*GLOB.MULT*self.number/self.div, 6*GLOB.MULT/self.div)
			
		self.BarGrey = pygame.Rect(self.x_pos-85*GLOB.MULT/self.div, self.y_pos-3*GLOB.MULT/self.div, 170*GLOB.MULT/self.div, 6*GLOB.MULT/self.div)

	def update(self, screen):
		pygame.draw.rect(GLOB.screen, "Grey", self.BarGrey)

		if self.number != 0:
			pygame.draw.rect(GLOB.screen, self.color, self.BarScore)
		
		screen.blit(self.image, self.rect)


def get_font(size): # Returns Press-Start-2P in the desired size
	return pygame.font.Font("font/font.ttf", size)

class Dialoghi():
	def __init__(self, personaggio, descrizione, text_speed):
		
		self.personaggio = personaggio
		self.descr = descrizione
		self.descr = self.descr.split("\n")
		self.descr = "".join(self.descr)

		self.delay = 0

		self.descrizione = ""
		self.descrizione1 = ""
		self.descrizione2 = ""
		self.descrizione3 = ""

		# print(self.descr.split(" "))
		# print(len(self.descr.split(" ")))

		# self.lunghezza = self.descr.split(" ")

		self.r0 = False
		self.r1 = False
		self.r2 = False
		self.r3 = False

		self.value = 64
		self.valore = 0
		self.flag_capo = True

		self.cooldown_interm = 0
		self.interm = 0

		if text_speed == 1:
			self.text_speed = 0.1
		elif text_speed == 2:
			self.text_speed = 0.2
		elif text_speed == 3:
			self.text_speed = 0.25
		elif text_speed == 4:
			self.text_speed = 0.5
		elif text_speed == 5:
			self.text_speed = 1
		else:
			self.text_speed = 0.1

		self.contatore = 0

		self.ritardo = 0

		self.CanIplay_sound = False
		self.play_sound = False
		self.cooldown_suono = 0
		self.MaxCooldwon_suono = 3

		self.descr = [self.descr[i:i+1] for i in range(0, len(self.descr), 1)]
		#print(self.descr)
    		
		self.Nome_TEXT = get_font(7*int(GLOB.MULT)).render(self.personaggio, True, "Black")
		self.Nome_RECT = self.Nome_TEXT.get_rect(center=(70*GLOB.MULT, GLOB.screen_height-10*GLOB.MULT))

		self.vignetta = pygame.image.load("Dialoghi/Characters/"+self.personaggio+".png")
		self.vignetta = pygame.transform.scale(self.vignetta, (self.vignetta.get_width()*GLOB.MULT*2, self.vignetta.get_height()*GLOB.MULT*2))

		self.sfondo = pygame.image.load("assets/Dialoghi.png")
		self.sfondo = pygame.transform.scale(self.sfondo, (self.sfondo.get_width()*GLOB.MULT, self.sfondo.get_height()*GLOB.MULT))

		self.keySound = mixer.Sound("suoni/char-sound.wav")
		self.keySound.set_volume(0.02*GLOB.AU)

	def __effetto_testo(self):
    		
		# Elenco le varie condizioni (limite massimo di caratteri)

		# if self.descrizione.split(" ") == self.lunghezza[0]:
		# 	pass
		
		# self.value = int((len(self.lunghezza)*len(self.descr))/192)
		# print(self.value)
    		
		self.condition0 = self.contatore < self.value
		self.condition1 = self.contatore >= self.value and self.contatore < self.value * 2
		self.condition2 = self.contatore >= self.value * 2 and self.contatore < self.value * 3
		self.condition3 = self.contatore >= self.value * 3 and self.contatore < self.value * 4
    		
		max = not int((self.delay+1)) > len(self.descr)

		valuex, valuey = 70, 55
		distanza_righe = 12.5

		def Condition(event):
			return self.descr[self.value*event-self.valore] != " " and self.descr[self.value*event-self.valore] != "." and (self.contatore >= self.value*event-self.valore and self.contatore < self.value*event)

		def Cerca(event):
			for value in range(len(self.descr)):
				if self.descr[self.value*event-1-value] == " " and self.flag_capo:
					#print("Trovato buco: ",value)
					self.flag_capo = False
					self.valore = value
    		

		def ScriviTesto1():
			self.descrizione += self.descr[int(round(self.delay, 1))]

			self.Descrizione_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione, True, "White")
			self.Descrizione_RECT = self.Descrizione_TEXT.get_rect(center=(GLOB.screen_width/2+valuex*GLOB.MULT, GLOB.screen_height-(valuey)*GLOB.MULT))

			self.r0 = True

		def ScriviTesto2():
			self.descrizione1 += self.descr[int(round(self.delay, 1))]

			self.Descrizione1_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione1, True, "White")
			self.Descrizione1_RECT = self.Descrizione1_TEXT.get_rect(center=(GLOB.screen_width/2+valuex*GLOB.MULT, GLOB.screen_height-(valuey-distanza_righe)*GLOB.MULT))

			self.r1 = True

		def ScriviTesto3():
			self.descrizione2 += self.descr[int(round(self.delay, 1))]

			self.Descrizione2_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione2, True, "White")
			self.Descrizione2_RECT = self.Descrizione2_TEXT.get_rect(center=(GLOB.screen_width/2+valuex*GLOB.MULT, GLOB.screen_height-(valuey-distanza_righe*2)*GLOB.MULT))

			self.r2 = True

		def ScriviTesto4():
			self.descrizione3 += self.descr[int(round(self.delay, 1))]

			self.Descrizione3_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione3, True, "White")
			self.Descrizione3_RECT = self.Descrizione3_TEXT.get_rect(center=(GLOB.screen_width/2+valuex*GLOB.MULT, GLOB.screen_height-(valuey-distanza_righe*3)*GLOB.MULT))

			self.r3 = True
		

		# vado a confrontare se il delay corisponde ad un numero intero e non decimale e anche se non ha superato il valore massimo della lista

		if int(self.delay+0.1) == round(self.delay, 1) and max and self.ritardo == 0:

			# CoolDown indicato per eseguire il suono		
			if self.MaxCooldwon_suono != 0:
				if self.cooldown_suono >= 0 and self.cooldown_suono <= self.MaxCooldwon_suono:
					self.cooldown_suono +=1
					self.play_sound = False
				else:
					self.play_sound = True
					self.cooldown_suono = 0
			else:
				self.play_sound = True

			if self.play_sound and self.CanIplay_sound:
				self.keySound.play()

			# Prima riga

			if self.condition0:
				#print("prima condizione")
				if len(self.descr) >= self.value:
        		
					Cerca(1)

					if Condition(1):
						ScriviTesto2()
					else:
						ScriviTesto1()
				else:
					ScriviTesto1()

				self.flag_capo = True

			# Seconda riga
			
			elif self.condition1:
				#print("seconda condizione")
				if len(self.descr) >= self.value*2:
            		
					Cerca(2)

					if Condition(2):
						ScriviTesto3()
					else:
						ScriviTesto2()
				else:
					ScriviTesto2()
				self.flag_capo = True

			# Terza riga

			elif self.condition2:
				#print("terza condizione")
				if len(self.descr) >= self.value*3:
            		
					Cerca(3)

					if Condition(3):
						ScriviTesto4()
					else:
						ScriviTesto3()
				else:
					ScriviTesto3()
				self.flag_capo = True

			elif self.condition3:
				#print("terza condizione")
				ScriviTesto4()

			# contatore che serve a controllare quanti caratteri sono stati inseriti
			self.contatore += 1

			"""if self.contatore >= self.value and self.descrizione[-1] != "" and self.descrizione[-1] != "=" and self.descrizione[-1] != " ":
				self.descrizione += " ="
				self.Descrizione_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione, True, "White")

			if self.contatore >= self.value*2 and self.descrizione1[-1] != "" and self.descrizione1[-1] != "=" and self.descrizione1[-1] != " ":
				self.descrizione1 += " ="
				self.Descrizione1_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione1, True, "White")

			if self.contatore >= self.value*3 and self.descrizione2[-1] != "" and self.descrizione2[-1] != "=" and self.descrizione2[-1] != " ":
				self.descrizione2 += " ="
				self.Descrizione2_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione2, True, "White")

			if self.contatore >= self.value*4 and self.descrizione3[-1] != "" and self.descrizione3[-1] != "=" and self.descrizione3[-1] != " ":
				self.descrizione3 += " ="
				self.Descrizione3_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione3, True, "White")"""
			
		# Delay aggiuntivo per dei caratteri particolari indicati
		if max and self.descr[int(round(self.delay, 1))] != "." and self.descr[int(round(self.delay, 1))] != "?" and self.descr[int(round(self.delay, 1))] != "!" or self.ritardo == 1:
			self.delay += + self.text_speed
			self.ritardo = 0
		else:
			self.ritardo += self.text_speed

		
		#print("Delay: "+str(round(self.delay, 1))+" | Intero: "+str(int(self.delay+0.1))+" | Lunghezza: "+str(len(self.descr))+" | Contatore: "+str(self.contatore)+" | Max: "+str((self.delay+1)))

	def stampa(self):

		clock = pygame.time.Clock()
		
		possoIniziare = False

		while not possoIniziare:
    		
			self.__effetto_testo()

			GLOB.screen.blit(self.sfondo, (0, GLOB.screen_height-self.sfondo.get_height()))
			GLOB.screen.blit(self.vignetta, (42.5*GLOB.MULT, GLOB.screen_height-self.vignetta.get_height()-18*GLOB.MULT))
			GLOB.screen.blit(self.Nome_TEXT, self.Nome_RECT)
			
			if self.r0:
				GLOB.screen.blit(self.Descrizione_TEXT, self.Descrizione_RECT)

			if self.r1:
				GLOB.screen.blit(self.Descrizione1_TEXT, self.Descrizione1_RECT)

			if self.r2:
				GLOB.screen.blit(self.Descrizione2_TEXT, self.Descrizione2_RECT)

			if self.r3:
				GLOB.screen.blit(self.Descrizione3_TEXT, self.Descrizione3_RECT)

			avanza = Button(image=pygame.image.load("assets/tasello.png").convert(), pos=(132*GLOB.MULT,  GLOB.screen_height-12*GLOB.MULT), 
								text_input="", font=pygame.font.Font("font/font.ttf", (8*int(GLOB.MULT))), base_color="White", hovering_color="#d7fcd4", scale=1.8)

			if self.interm == 0 or self.cooldown_interm != GLOB.FPS / 10:
				avanza.update(GLOB.screen)
				self.cooldown_interm += 0.25

			self.interm += 1
			
			if self.interm >= GLOB.FPS and self.cooldown_interm == GLOB.FPS / 10:
				self.interm = 0
				self.cooldown_interm = 0

			for event in pygame.event.get():
				keys_pressed = pygame.key.get_pressed()
    
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

    				
				if event.type == pygame.MOUSEBUTTONDOWN or keys_pressed[pygame.K_SPACE]:
					possoIniziare = True

				#delay.ActualState()


			pygame.display.flip() # ti permette di aggiornare una area dello schermo per evitare lag e fornire piu' ottimizzazione
			pygame.display.update()

			clock.tick(GLOB.FPS) # setto i FramesPerSecond


class Delay():
    def __init__(self, sec):
        self.__min = 0
        self.__max = sec * GLOB.FPS
        self.__increment = 1
        self.__flag = True

    #print(self.min, self.max, self.increment, self.function)

    def Start(self):
        if self.__flag:
            self.__min += self.__increment

            if int(self.__min) == self.__max:
                self.__flag = False
                return True

        return False

        #print(int(self.__min))

    def ReStart(self):
        if not self.__flag:
            self.__min = 0
            self.__flag = True

        #print(int(self.__min))

    def Infinite(self):
        self.ReStart()
        self.Start()

    def ActualState(self):
        print("| Current Second: %d | Max Seconds: %d | Function: %s |" %(self.__min/GLOB.FPS, self.__max/GLOB.FPS, self.__function))


# var = 0

# def miaFunzione():
#     global var
#     var += 1
#     print(var)

# delay = Delay(sec = 3, event = miaFunzione)