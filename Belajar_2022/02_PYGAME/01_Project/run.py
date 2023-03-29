import pygame
import sys

pygame.init()

class Settings():

	fps = 25
	screen_size = [500, 500]
	screen_bg_color = [245, 66, 239]
	land_speed = 5
	bird_fly_speed = 3
	bird_fall_speed = 1


screen = pygame.display.set_mode(Settings.screen_size)
screen_rect = screen.get_rect()

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

class Pipe():
	pass


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

pipe_1 = Pipe()
pipe_2 = Pipe()
bird = Bird()

def main():

	while True:

		screen.fill(Settings.screen_bg_color)

		# screen.blit(bird.image, bird.rect)
		bird.show()
		bird.move()

		Land.show()
		Land.move()

		pygame.display.flip()
		pygame.time.Clock().tick(Settings.fps)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					pass
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					pass
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_position = pygame.mouse.get_pos()



if __name__ == '__main__':
	main()