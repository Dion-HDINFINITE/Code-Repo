import pygame

class Land():

	image = pygame.transform.scale(pygame.image.load("images/land.png"), (2*screen_rect.width, screen_rect.height//5))
	rect = image.get_rect()
	rect.midbottom = screen_rect.midbottom

	@classmethod
	def move(self):
		self.rect.x -= Settings.land_speed
		if self.rect.centerx <= 0:
			self.rect.left = screen_rect.left

	@classmethod
	def show(self):
		screen.blit(self.image, self.rect)