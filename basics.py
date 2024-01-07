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
        self.coordinates = [(1, 526), (472, 526)]
        self.img_pos = tuple(self.coordinates[0])  # Use list() to create a copy
        self.current_target_index = 0
        self.speed = 2

    def run(self):
        while True:
            # Refreshing screen after each frame
            self.screen.blit(self.background_image, (0, 0))

            target_coordinates = self.coordinates[self.current_target_index]
            vector = pygame.Vector2(target_coordinates[0] - self.img_pos[0], target_coordinates[1] - self.img_pos[1])

            # Check if the vector has non-zero length before normalizing
            if vector.length() > 0:
                vector.normalize_ip()

            # Move the image along the direction vector
            self.img_pos = ( self.img_pos[0] + vector.x * self.speed, self.img_pos[1] + vector.y * self.speed)

            # Draw the car image
            self.screen.blit(self.img, self.img_pos)


            # Update the display
            pygame.display.flip()

            # Control the frame rate
            self.clock.tick(60)

            # Check if the car has reached the target coordinates
            if pygame.Vector2(self.img_pos[0] - target_coordinates[0], self.img_pos[1] - target_coordinates[1]).length() < self.speed:
                self.current_target_index += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()