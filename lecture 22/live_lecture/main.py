import pygame
import sys
from my_rect import MyRect


# Ifall man inte har pygame installerat kör pip install pygame
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lecture 22")

clock = pygame.time.Clock()
fps = 60  # frames per second

# vi börjar i en punkt (rect_x, rect_y bland våra pixlar) och ritar + 150 xled och + 150 yled
# rect_x, rect_y, rect_width, rect_height = 100, 100, 150, 150
# rect_thickness = 5

all_rectangles = []


def update():
    for rectangle in all_rectangles:
        rectangle.update()


def draw():
    for rectangle in all_rectangles:
        rectangle.draw(screen)


def create_rectangles():
    amount_of_rects = 3
    x = 100
    y = 100
    width = 75
    height = 75
    thickness = 5
    for _ in range(amount_of_rects):
        rect = MyRect(x, y, width, height, thickness)
        y += 100
        all_rectangles.append(rect)


def main():
    # global rect_x
    create_rectangles()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill("black")
        update()
        draw()

        pygame.display.flip()

        clock.tick(fps)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
