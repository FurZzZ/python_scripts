import sys, pygame
from lib.Snake import Snake

pygame.init()

white = (255, 255 ,255)
black = (0, 0, 0)
red = (255, 0 , 0)
darkgreen = (0, 100, 0)
blue = (0, 0, 255)

ground = (139, 90, 0)

pos_x = 100
pos_y = 100

lead_x_change = 5
lead_y_change = -5

gameDisplay = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Snake rampage!')

pygame.display.update()

gameExit = False


current_dir = "RIGHT"

clock = pygame.time.Clock()

while not gameExit:

	for event in pygame.event.get():

		#exit game if esc pressed
		if event.type == pygame.QUIT:
			gameExit = True


		if event.type == pygame.KEYDOWN:

			if event.key in (pygame.K_ESCAPE, pygame.K_q):
				gameExit = True

			if event.key == pygame.K_LEFT:
				if current_dir not in ("RIGHT", "LEFT"):
					lead_x_change *= -1
					current_dir = "LEFT"

			if event.key == pygame.K_DOWN:
				if current_dir not in ("UP", "DOWN"):
					lead_y_change *= -1
					current_dir = "DOWN"

			if event.key == pygame.K_UP:
				if current_dir not in ("DOWN", "UP"):
					lead_y_change *= -1
					current_dir = "UP"

			if event.key == pygame.K_RIGHT:
				if current_dir not in ("LEFT", "RIGHT"):
					lead_x_change *= -1
					current_dir = "RIGHT"
		
	if current_dir in ("RIGHT", "LEFT"):
		pos_x += lead_x_change 
	else:
		pos_x += 0

	if current_dir in ("UP", "DOWN"):
		pos_y += lead_y_change 
	else:
		pos_y += 0


	if pos_x > 790 or pos_x < 10 or pos_y > 590 or pos_y < 10:
		gameExit = True

	gameDisplay.fill(ground)

	#draw snake
	snake = Snake(gameDisplay, darkgreen, pos_x, pos_y)

	#draw walls
	pygame.draw.rect(gameDisplay, red, [0, 0, 10, 600])
	pygame.draw.rect(gameDisplay, red, [0, 0, 800, 10])
	pygame.draw.rect(gameDisplay, red, [790, 0, 10, 600])
	pygame.draw.rect(gameDisplay, red, [0, 590, 800, 10])
	pygame.display.update()

	clock.tick(60)

pygame.quit()
quit()