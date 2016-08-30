import sys, pygame

class Prey(object):
	def __init__(self, window, color, pos_x, pos_y, size_x, size_y, is_alive):
		#draw head
		pygame.draw.rect(window, color, [pos_x, pos_y, size_x, size_y])