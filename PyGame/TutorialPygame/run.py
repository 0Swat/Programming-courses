import sys

import pygame

screen = pygame.display.set_mode((1280, 720))

while True:
    # Events handle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

        # Drawing
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(10, 50, 200, 100))
        pygame.display.flip()