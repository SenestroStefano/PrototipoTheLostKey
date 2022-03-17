from posixpath import split
from turtle import color
import global_var as GLOB
import pygame

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
	return pygame.font.Font("assets/font.ttf", size)

class Dialoghi():
	def __init__(self, personaggio, descrizione):
		
		self.personaggio = personaggio
		self.descr = descrizione

		self.delay = 0
		self.descrizione = ""

		n = 1
		self.descr = [self.descr[i:i+n] for i in range(0, len(self.descr), n)]

		self.Nome_TEXT = get_font(7*int(GLOB.MULT)).render(self.personaggio, True, "Black")
		self.Nome_RECT = self.Nome_TEXT.get_rect(center=(70*GLOB.MULT, GLOB.screen_height-10*GLOB.MULT))

		self.vignetta = pygame.image.load("Dialoghi/"+self.personaggio+".png")
		self.vignetta = pygame.transform.scale(self.vignetta, (self.vignetta.get_width()*GLOB.MULT*2, self.vignetta.get_height()*GLOB.MULT*2))

		self.sfondo = pygame.image.load("assets/Dialoghi.png")
		self.sfondo = pygame.transform.scale(self.sfondo, (self.sfondo.get_width()*GLOB.MULT, self.sfondo.get_height()*GLOB.MULT))

	def effetto_testo(self):
		#print(self.descr)

		if int(self.delay+0.1) == round(self.delay, 1) and not int((self.delay+1)) > len(self.descr):
			#print(len(self.descr))
			#print(int(self.delay))
			self.descrizione = self.descrizione + self.descr[int(round(self.delay, 1))]
			#print("Descrizione: "+str(self.descrizione)+" | Delay: "+str(int(self.delay))+" | Max: "+str(len(self.descr*self.text_speed)))

		self.delay += + 0.2
		#print("Delay: "+str(round(self.delay, 1))+" | Intero: "+str(int(self.delay+0.1))+" | Lunghezza: "+str(len(self.descr))+" | Descrizione: "+str(self.descrizione)+" | Max: "+str((self.delay+1)))

		self.Descrizione_TEXT = get_font(6*int(GLOB.MULT)).render(self.descrizione, True, "White")
		self.Descrizione_RECT = self.Descrizione_TEXT.get_rect(center=(GLOB.screen_width/2+70*GLOB.MULT, GLOB.screen_height-50*GLOB.MULT))

	def stampa(self):

		GLOB.screen.blit(self.sfondo, (0, GLOB.screen_height-self.sfondo.get_height()))
		GLOB.screen.blit(self.vignetta, (45*GLOB.MULT, GLOB.screen_height-self.vignetta.get_height()-18*GLOB.MULT))
		GLOB.screen.blit(self.Nome_TEXT, self.Nome_RECT)
		GLOB.screen.blit(self.Descrizione_TEXT, self.Descrizione_RECT)