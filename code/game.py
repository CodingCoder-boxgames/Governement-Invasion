import pygame
from const import *
from player import Player
from level import Level
from bird import Bird
from ui import UI

class Game:

    def __init__(self, surface):
        self.surface = surface
        self.level = Level()
        self.bird = Bird(self.surface)
        self._level = 1
        self._level_str = "level" + str(self._level)
        self.level_gen = False
        self.player = Player(self.surface)
        self.ui = UI(self.surface)
        self.can_throw_stone = True
    def gameloop(self):
        self.ui.draw_UI(self._level)
        self.check_stone()
        if self.level_gen == False:
            self._level_str = "level" + str(self._level)
            level = getattr(self.level, self._level_str)
            level()
            self.level_gen = True
        if len(self.level.static_birds) == 0 and len(self.level.dynamic_birds) == 0:
            # NEXT LEVEL
            self.bird.bird_counter = 0
            self.bird.bird_counter_ = 0
            self.bird.bird_dir, self.bird.bird_dir_ = 1, -1
            self.bird.star_dir, self.bird.star_dir_ = 0.5, -0.5
            if self._level != 10:
                self.level_gen = False
                self._level += 1
                self.player.stone.reset_stone()

        if self._level == 10:
            self.player.stone.rect = self.player.stone.stone_img.get_rect(topleft = (self.player.stone.position_x, self.player.stone.position_y))
            if len(self.level.static_birds) == 0 and len(self.level.dynamic_birds) == 0:
                self.ui.show_last = True
                self.can_throw_stone = False
            else: self.ui.show_last = False

        self.bird.draw_birds(self.player, self.level)
        self.player.draw_player()
      
    def shoot(self):
        if self.player.has_stone and self.can_throw_stone:
            self.player.stone.speed_y = self.player.stone.max_speed
            self.player.has_stone = False
            pygame.mixer.Channel(5).play(pygame.mixer.Sound("graphics/sounds/shoot.wav"))

    def check_stone(self):
        if self.player.stone.position_y < 0 or self.player.stone.position_y > HEIGHT or self.bird.touched_star:
            pygame.mixer.Channel(3).set_volume(1.5)
            pygame.mixer.Channel(3).play(pygame.mixer.Sound("graphics/sounds/dead.wav"))
            self.player.stone.reset_stone()
            self.level_gen = False
            self.bird.bird_counter, self.bird.bird_counter_ = 0, 0
            self.bird.touched_star = False
            self.level_gen = False


