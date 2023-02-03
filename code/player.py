import pygame
from const import *
from stone import Stone

class Player:
    def __init__(self, surface):
        self.surface = surface
        self.width = 80
        self.stone = Stone(self.surface)
        self.slingshot = pygame.transform.scale(pygame.image.load("graphics/images/slingshot.png"), (self.width,self.width))
        self.has_stone = True
        
    def draw_player(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.position = [self.mouse_x - self.width // 2, HEIGHT - 100]
        self.surface.blit(self.slingshot, self.position)
        self.stone.draw_stone(self.width, self.position)
        rect = self.slingshot.get_rect(topleft = self.position)
        if rect.colliderect(self.stone.rect) and self.has_stone == False and self.stone.speed_y <= 0:
            self.stone.reset_stone()
            self.has_stone = True
    

        
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.position = [self.mouse_x - self.width // 2, HEIGHT - 100]
    


        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.position = [self.mouse_x - self.width // 2, HEIGHT - 100]
    

