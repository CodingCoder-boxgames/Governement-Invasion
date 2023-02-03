import pygame
from const import *
from pygame.locals import *
class UI:

    def __init__(self, surface):
        self.surface = surface
        pygame.font.init()
        self.name_font = pygame.font.Font("graphics/font/font.ttf", 30)
        self.game_font = pygame.font.Font("graphics/font/font.ttf", 100)
        self.colors = [(255,255,255), (0,0,0), (255,0,255), (255, 255, 0), (0, 255, 255)]
        self.cur_color = 0
        self.cur_time = 0
        self.show_last = False
    def draw_UI(self, cur_lvl):
        self.draw_level(cur_lvl)
        self.draw_name()
        if self.show_last:
            self.end()
    
    def draw_level(self, cur_lvl):
        # draw current level
        if cur_lvl != 10:
            level_text_surface = self.game_font.render("LEVEL: " + str(cur_lvl), True, (0,0,0))
        
        else:
            self.cur_time += 0.5
            if self.cur_time >= 10:
                if self.cur_color <= len(self.colors) - 2:
                    self.cur_color += 1
                else: 
                    self.cur_color = 0
                self.cur_time = 0
            text_surf = self.game_font.render("LAST LEVEL", True, self.colors[self.cur_color])
            level_text_surface = self.game_font.render("LEVEL: " + str(cur_lvl), True, self.colors[self.cur_color])

            self.surface.blit(text_surf, (WIDTH / 2 - text_surf.get_width() / 2, 25))
        self.surface.blit(level_text_surface, (WIDTH / 2 - level_text_surface.get_width() / 2,500))
        
    def end(self):
        last_text_surface = self.game_font.render('GOVERNMENT DESTROYED', True, self.colors[self.cur_color])

        self.surface.blit(last_text_surface, (WIDTH / 2 - last_text_surface.get_width() / 2, HEIGHT / 2 - last_text_surface.get_height() / 2))
    def draw_name(self):
        name_text_surface = self.name_font.render('Made by Staf', True, (250,250,250))
        self.surface.blit(name_text_surface, (0, HEIGHT - 20))