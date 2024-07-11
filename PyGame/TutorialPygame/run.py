import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
box = pygame.Rect(10, 10, 50, 50)

while True:
    # Events handle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)

    # Checking inputs
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        box.x += 1
    if keys[pygame.K_a]:
        box.x -= 1
    if keys[pygame.K_s]:
        box.y += 1
    if keys[pygame.K_w]:
        box.y -= 1


    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 255), box)
    pygame.display.flip()