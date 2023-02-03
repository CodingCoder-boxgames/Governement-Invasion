import pygame
from const import *

class Level:
    def __init__(self):
        self.static_birds = []
        self.dynamic_birds = []
        self.iron_bars = []
        self.stars = []
        
        self.bird_lines = [150 - 85, 240 - 85, 330 - 85, 415 - 85]
        self.star_lines = [150 - 7, 240 - 7, 330 - 7, 415 - 7]
        self.iron_lines = [150 - 50, 240 - 50, 330 - 50, 420 - 50]

        self.dir_speed_bird = 3
        self.dir_speed_star = 2
        self.middle = WIDTH / 2 - 85 / 2
    def level1(self):
        self.static_birds = [[WIDTH / 2 - 85 / 2, self.bird_lines[3]]]
        self.dynamic_birds = []
        self.iron_bars = []
        self.stars = []
        

    def level2(self):
        self.static_birds = [[self.middle, self.bird_lines[3]], [100, self.bird_lines[1]]]
        self.dynamic_birds = []
        self.iron_bars = [[self.middle, self.iron_lines[1]]]
        self.stars = []
    def level3(self):
        self.static_birds = []
        self.dynamic_birds = [[self.middle, self.bird_lines[3], self.dir_speed_bird]]
        self.iron_bars = []
        self.stars = []
    def level4(self):
        self.static_birds = [[800, self.bird_lines[0]]]
        self.dynamic_birds = [[self.middle, self.bird_lines[3], -self.dir_speed_bird]]
        self.iron_bars = [[self.middle, self.iron_lines[1]]]
        self.stars = []
    def level5(self):
        self.static_birds = []
        self.dynamic_birds = [[self.middle, self.bird_lines[0], -self.dir_speed_bird],
                              [self.middle, self.bird_lines[1], self.dir_speed_bird],
                              [self.middle, self.bird_lines[2], -self.dir_speed_bird]]
        self.iron_bars = []
        self.stars = []
    def level6(self):
        self.static_birds = [[self.middle, self.bird_lines[0]]]
        self.dynamic_birds = []
        self.iron_bars = []
        self.stars = [[100, self.star_lines[3], self.dir_speed_star],
                      [150, self.star_lines[3], self.dir_speed_star],
                      [200, self.star_lines[3], self.dir_speed_star],
                      [250, self.star_lines[3], self.dir_speed_star],
                      [300, self.star_lines[3], self.dir_speed_star],
                      [WIDTH - 100, self.star_lines[3], -self.dir_speed_star],
                      [WIDTH - 150, self.star_lines[3], -self.dir_speed_star],
                      [WIDTH - 200, self.star_lines[3], -self.dir_speed_star],
                      [WIDTH - 250, self.star_lines[3], -self.dir_speed_star],
                      [WIDTH - 300, self.star_lines[3], -self.dir_speed_star]]
    def level7(self):
        self.static_birds = [[200, self.bird_lines[3]], [900, self.bird_lines[1]]]
        self.dynamic_birds = [[self.middle, self.bird_lines[2], self.dir_speed_bird]]
        self.iron_bars = [[self.middle, self.iron_lines[0]], [200, self.iron_lines[1]]]
        self.stars = [[100, self.star_lines[3], self.dir_speed_star],
                      [170, self.star_lines[3], self.dir_speed_star],
                      [230, self.star_lines[3], self.dir_speed_star],
                      [200, self.star_lines[3], self.dir_speed_star],
                      [400, self.star_lines[3], self.dir_speed_star],
                      [WIDTH - 180, self.star_lines[3], -self.dir_speed_star],
                      [WIDTH - 300, self.star_lines[3], -self.dir_speed_star],
                      [WIDTH - 100, self.star_lines[3], -self.dir_speed_star],
                      [WIDTH - 230, self.star_lines[3], -self.dir_speed_star],
                      [WIDTH - 350, self.star_lines[3], -self.dir_speed_star]]
    def level8(self):
        self.static_birds = [[900, self.bird_lines[3]]]
        self.dynamic_birds = [[self.middle, self.bird_lines[0], -self.dir_speed_bird],
                              [self.middle, self.bird_lines[1], self.dir_speed_bird],
                              [self.middle, self.bird_lines[2], -self.dir_speed_bird],
                              [self.middle, self.bird_lines[3], self.dir_speed_bird]]
        self.stars = [[380, self.star_lines[2], self.dir_speed_star],
                      [90, self.star_lines[2], self.dir_speed_star],
                      [170, self.star_lines[3], self.dir_speed_star],
                      [230, self.star_lines[3], self.dir_speed_star],
                      [300, self.star_lines[2], self.dir_speed_star],
                      [WIDTH - 50, self.star_lines[3], -self.dir_speed_star],
                      [WIDTH - 180, self.star_lines[2], -self.dir_speed_star],
                      [WIDTH - 220, self.star_lines[2], -self.dir_speed_star],
                      [WIDTH - 330, self.star_lines[2], -self.dir_speed_star],
                      [WIDTH - 400, self.star_lines[3], -self.dir_speed_star]]
        self.iron_bars = [[900, self.iron_lines[0]]]
    
    def level9(self):
        self.static_birds = []
        self.dynamic_birds = [[self.middle, self.bird_lines[0], self.dir_speed_bird]]
        self.stars = [[380, self.star_lines[1], self.dir_speed_star],
                      [50, self.star_lines[2], self.dir_speed_star],
                      [170, self.star_lines[3], self.dir_speed_star],
                      [600, self.star_lines[0], self.dir_speed_star],
                      [300, self.star_lines[1], self.dir_speed_star],
                      [WIDTH - 50, self.star_lines[2], -self.dir_speed_star],
                      [WIDTH - 180, self.star_lines[3], -self.dir_speed_star],
                      [WIDTH - 220, self.star_lines[0], -self.dir_speed_star],
                      [WIDTH - 330, self.star_lines[1], -self.dir_speed_star],
                      [WIDTH - 400, self.star_lines[2], -self.dir_speed_star]]
        self.iron_bars = []
    def level10(self):
        self.static_birds = [[100, self.bird_lines[2]],
                             [220, self.bird_lines[2]],
                             [340, self.bird_lines[2]],
                             [460, self.bird_lines[2]],
                             [580, self.bird_lines[2]],
                             [700, self.bird_lines[2]],
                             [820, self.bird_lines[2]],
                             [940, self.bird_lines[2]]]
        self.dynamic_birds = []
        self.iron_bars = []
        self.iron_bars = [[100, self.iron_lines[0]],
                             [200, self.iron_lines[0]],
                             [300, self.iron_lines[0]],
                             [400, self.iron_lines[0]],
                             [500, self.iron_lines[0]],
                             [600, self.iron_lines[0]],
                             [700, self.iron_lines[0]],
                             [800, self.iron_lines[0]],
                             [900, self.iron_lines[0]]]
        self.stars = []

