import pygame

class Bird():

	def __init__(self):
		self.image = pygame.image.load("images/bird.png")
		self.rect = self.image.get_rect()
		self.rect.center = screen_rect.center

		self.fly = False
		self.pass_pipe = False


	def move(self):
		if self.fly:
			self.rect.y -= Settings.bird_fly_speed
		else:
			self.rect.y += Settings.bird_fall_speed

	def show(self):
		screen.blit(self.image, self.rect)