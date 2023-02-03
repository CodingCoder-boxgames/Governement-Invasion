import pygame
from level import Level
from const import *
from stone import Stone
from pygame.locals import *
class Bird:

    def __init__(self, surface):
        self.level = Level()
        self.bird = pygame.transform.scale(pygame.image.load("graphics/images/bird.png"), (85, 85))
        self.bird_walk = pygame.transform.scale(pygame.image.load("graphics/images/bird_walk.png"), (80,80))
        self.star = pygame.transform.scale(pygame.image.load("graphics/images/star.png"), (15,15))
        self.iron_bar = pygame.image.load("graphics/images/iron_bar.png")
        self.surface = surface

        self.touched_star = False
        self.stone = Stone(self.surface)
        self.bird_dir, self.bird_dir_ = 3, -3
        self.bird_counter, self.bird_counter_ = 0, 0

        self.star_dir, self.star_dir_ = 0.5, -0.5
        self.distance = 200
    def draw_birds(self, player, level):
        # draw STATIC birds
        if len(level.static_birds) != 0:
            for _bird in level.static_birds:
                rect = self.bird.get_rect(topleft = (_bird[0], _bird[1]))
                self.surface.blit(self.bird, (_bird[0], _bird[1]))
                if rect.colliderect(player.stone.rect):
                    pygame.mixer.music.set_volume(1.5)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("graphics/sounds/hit.wav"))
                    level.static_birds.remove(_bird)
        
        # draw DYNAMIC birds
        if len(level.dynamic_birds) != 0:
            for bird in level.dynamic_birds:
                rect = self.bird.get_rect(topleft = (bird[0], bird[1]))

              
                if bird[2] == self.level.dir_speed_bird:
                    if self.bird_counter < self.distance and self.bird_dir == bird[2]:
                        bird[0] += self.bird_dir
                        self.bird_counter += bird[2]
                        self.surface.blit(pygame.transform.flip(self.bird_walk, True, False), (bird[0], bird[1]))
                    else:
                        if self.bird_counter > -self.distance:
                            self.bird_dir = -bird[2]
                            bird[0] += self.bird_dir
                            self.bird_counter -= bird[2]
                            self.surface.blit(self.bird_walk, (bird[0], bird[1]))

                        else:
                            self.bird_dir = bird[2]
                

                if bird[2] == -self.level.dir_speed_bird:
                    if self.bird_counter_ > -self.distance * 2 and self.bird_dir_ == bird[2]:
                        bird[0] += self.bird_dir_
                        self.bird_counter_ -= 3
                        self.surface.blit(self.bird_walk, (bird[0], bird[1]))

                    else:
                        if self.bird_counter_ < self.distance* 2:
                            self.bird_dir_ = -bird[2]
                            bird[0] += self.bird_dir_
                            self.bird_counter_ += 3
                            self.surface.blit(pygame.transform.flip(self.bird_walk, True, False), (bird[0], bird[1]))

                        else: self.bird_dir_ = bird[2]
                
                    
      
                if rect.colliderect(player.stone.rect):
                    level.dynamic_birds.remove(bird)
                    pygame.mixer.music.set_volume(1.5)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("graphics/sounds/hit.wav"))

        # DRAW THE STARS

        if len(level.stars) != 0:
            for star in level.stars:
                    
                if star[2] == self.level.dir_speed_star:
                    rect = self.star.get_rect(topleft = (star[0], star[1]))
                    if star[0] < WIDTH - 70 and self.star_dir == star[2]:
                        star[0] += self.star_dir 
                        self.surface.blit(self.star, (star[0], star[1]))
                    else:
                        if star[0] > 50:
                            self.star_dir = -star[2]
                            star[0] += self.star_dir 
                            self.surface.blit(self.star, (star[0], star[1]))

                        else:
                            self.star_dir = star[2]
                    
                    if rect.colliderect(player.stone.rect):
                        self.touched_star = True
                        player.stone.reset_stone()

                    
                if star[2] == -self.level.dir_speed_star:
                    rect = self.star.get_rect(topleft = (star[0], star[1]))
                    if star[0] > 50 and self.star_dir_ == star[2]:
                        star[0] += self.star_dir_

                        self.surface.blit(self.star, (star[0], star[1]))

                    else:
                        if star[0] < WIDTH - 70:
                            self.star_dir_ = -star[2]
                            star[0] += self.star_dir_
                            self.surface.blit(self.star, (star[0], star[1]))
                        else: self.star_dir_ = star[2]
                    if rect.colliderect(player.stone.rect):
                        
                        self.touched_star = True
                        player.stone.reset_stone()
            # STAR COLLIDING
   

        # draw the IRONBARS
        if len(level.iron_bars) != 0:
            for iron_bar in level.iron_bars:

             rect = self.iron_bar.get_rect(topleft = (iron_bar[0], iron_bar[1]))
             self.surface.blit(self.iron_bar, (iron_bar[0], iron_bar[1]))

             if rect.colliderect(player.stone.rect):
                player.stone.speed_y = -player.stone.speed_y
                pygame.mixer.music.set_volume(1.5)
                pygame.mixer.Channel(2).play(pygame.mixer.Sound("graphics/sounds/iron_bar.wav"))

