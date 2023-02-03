from const import *
from game import Game
import pygame, sys

pygame.mixer.init()

class Main:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.game = Game(self.screen)
        self.background = pygame.image.load("graphics/images/background.jpg")
    def mainloop(self):
        clock = pygame.time.Clock()
        pygame.mixer.music.load("graphics/sounds/PitcherPerfectTheme.wav")
        pygame.mixer.music.play(-1, 0.0)
        while True:
            self.screen.blit(self.background, (0,0))
            pygame.init()
            pygame.display.set_caption('Governement Invasion')
            pygame.display.set_icon(pygame.image.load("graphics/images/bird_walk.png"))
            self.game.gameloop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.game.shoot()
            clock.tick(FPS)
            pygame.display.update()
main = Main()
if __name__ == "__main__":
    main.mainloop()
    