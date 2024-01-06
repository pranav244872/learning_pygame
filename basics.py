import pygame
import sys
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('traffic')
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load('obj.png')
        self.img_pos = [160,260]
    def run(self):
        while True:
            self.screen.blit(self.img, self.img_pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit

            pygame.display.update()
            self.clock.tick(60)

Game().run()