import pygame
from const import *
from pygame.locals import *

class Stone:

    def __init__(self, surface):
        self.surface = surface
        self.max_speed = 10
        
        self.speed_y = 0
        self.scale = 50
        self.stone_img = pygame.transform.scale(pygame.image.load("graphics/images/stone.png"), (self.scale,self.scale))
        self.position_y = HEIGHT - 120
        self.position_x = 100
        self.rect = self.stone_img.get_rect(topleft = (self.position_x, self.position_y))

    def draw_stone(self, player_width, player_position):
        self.position_y -= self.speed_y
        if self.speed_y == 0:
            self.position_x = player_position[0] + player_width // 2 - self.scale // 2
        self.rect = self.stone_img.get_rect(topleft = (self.position_x, self.position_y))
        self.surface.blit(self.stone_img, (self.position_x,self.position_y))

    def reset_stone(self):

        self.speed_y = 0
        self.position_x, self.position_y = 100 ,HEIGHT - 120
    




        