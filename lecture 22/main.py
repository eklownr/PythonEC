import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Pygame App")

rect_x, rect_y = 100, 100

clock = pygame.time.Clock()
fps = 60
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect_x -= 10
            elif event.key == pygame.K_RIGHT:
                rect_x += 10
            elif event.key == pygame.K_UP:
                rect_y -= 10
            elif event.key == pygame.K_DOWN:
                rect_y += 10

    screen.fill("black")

    rect_width, rect_height = 200, 150
    pygame.draw.rect(screen, "red", (rect_x, rect_y, rect_width, rect_height), 2)

    pygame.display.flip()
    clock.tick(fps)
