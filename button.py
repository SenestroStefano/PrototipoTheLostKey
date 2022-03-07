import global_var as GLOB
import pygame

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
    	
		if image != None:
			image_w, image_h = image.get_width()*GLOB.MULT/2, image.get_height()*GLOB.MULT/2
			self.image = pygame.transform.scale(image, (image_w, image_h))
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


class Bar():
	def __init__(self, pos, number, div):

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
		else:
			if div > 8:
				self.div = 8
			elif div < 1:
				self.div = 1

		self.image = pygame.image.load("assets/BarraCompletamento.png")
		self.image = pygame.transform.scale(self.image, (self.image.get_width()*GLOB.MULT/self.div, self.image.get_height()*GLOB.MULT/self.div))

		if number != 0:
			self.BarGreen = pygame.image.load("assets/BarraVerde.png").convert()
			self.BarGreen = pygame.transform.scale(self.BarGreen, (self.BarGreen.get_width()*self.number*GLOB.MULT/self.div, self.BarGreen.get_height()*GLOB.MULT/self.div))

		self.BarGrey = pygame.image.load("assets/BarraGrigia.png").convert()
		self.BarGrey = pygame.transform.scale(self.BarGrey, (self.BarGrey.get_width()*GLOB.MULT/self.div, self.BarGrey.get_height()*GLOB.MULT/self.div))

		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

#(GLOB.screen_width/2-image.get_width()/2,GLOB.screen_height/2+70*GLOB.MULT)

	def update(self, screen):
		screen.blit(self.BarGrey, self.rect)
		screen.blit(self.BarGreen, self.rect)
		screen.blit(self.image, self.rect)