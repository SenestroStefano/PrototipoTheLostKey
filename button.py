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
	def __init__(self, pos, number, div, type):

		self.x_pos = pos[0]
		self.y_pos = pos[1]

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

		if number != 0:
			
			if type == 1:
				self.BarScore = pygame.image.load("assets/BarraVerde.png").convert()
			else:
				self.BarScore = pygame.image.load("assets/BarraBlu.png").convert()
			
			self.BarScore = pygame.transform.scale(self.BarScore, (self.BarScore.get_width()*self.number*GLOB.MULT/self.div, self.BarScore.get_height()*GLOB.MULT/self.div))

		self.BarGrey = pygame.image.load("assets/BarraGrigia.png").convert()
		self.BarGrey = pygame.transform.scale(self.BarGrey, (self.BarGrey.get_width()*GLOB.MULT/self.div, self.BarGrey.get_height()*GLOB.MULT/self.div))

		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		screen.blit(self.BarGrey, self.rect)

		if self.number != 0:
			screen.blit(self.BarScore, self.rect)
		
		screen.blit(self.image, self.rect)