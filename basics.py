import pygame
import sys
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('traffic')
        self.screen = pygame.display.set_mode((1920, 1080))
        self.background_image = pygame.image.load("bg.png")
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load('car.png')
        self.img_pos = [1,526]
        self.movement = [False,False]
    def run(self):
        while True:
            #Refreshing screen after each frame
            self.screen.blit(self.background_image, (0,0))

            #Converting the boolean values to integers true = 1 and moving the image 1px at a time
            self.img_pos[1] += self.movement[1] - self.movement[0]
            self.screen.blit(self.img, self.img_pos)

            #logic for movement
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
            pygame.display.update()
            self.clock.tick(60)

Game().run()