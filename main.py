import pygame
import random
pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width = screen.get_width()
screen_height = screen.get_height()

clock = pygame.time.Clock()

size = 50
rects = [pygame.Rect(10 * size, 10 * size, size, size)]
fit_height = int(screen_height/size)
fit_width = int(screen_width/size)
fruits = []
for i in range(5):
    fruits.append(pygame.Rect(random.randint(0, fit_width - 2) * size,
                              random.randint(0, fit_height - 2) * size, size, size))


class Moving:
    def __init__(self):
        pass
    right = False
    left = False
    up = False
    down = False


counter = 0
eating = False
running = True
while running:
    mx, my = pygame.mouse.get_pos()

    screen.fill((50, 50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                Moving.right = False
                Moving.left = False
                Moving.up = True
                Moving.down = False
            if event.key == pygame.K_DOWN:
                Moving.right = False
                Moving.left = False
                Moving.up = False
                Moving.down = True
            if event.key == pygame.K_RIGHT:
                Moving.right = True
                Moving.left = False
                Moving.up = False
                Moving.down = False
            if event.key == pygame.K_LEFT:
                Moving.right = False
                Moving.left = True
                Moving.up = False
                Moving.down = False

    for rect in rects:
        for fruit in fruits:
            if fruit.colliderect(rect):
                eating = True
                fruits.remove(fruit)

    counter += 1
    if counter > 20:
        counter = 0
    if counter == 1:
        if Moving.left:
            rects.append(pygame.Rect(rects[0][0] - 1 * size, rects[0][1], size, size))
            if eating:
                eating = False
            else:
                rects.remove(rects[0])
        if Moving.right:
            rects.append(pygame.Rect(rects[0][0] + 1 * size, rects[0][1], size, size))
            rects.remove(rects[0])
        if Moving.down:
            rects.append(pygame.Rect(rects[0][0], rects[0][1] + 1 * size, size, size))
            rects.remove(rects[0])
        if Moving.up:
            rects.append(pygame.Rect(rects[0][0], rects[0][1] - 1 * size, size, size))
            rects.remove(rects[0])

    for fruit in fruits:
        pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(fruit.x, fruit.y, size, size))

    for rect in rects:
        pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(rect.x, rect.y, size, size))

    x = 0
    y = 0
    startingpoint = 0
    gridsize = 50
    for i in range(20):
        for i in range(20):
            pygame.draw.line(screen, (100, 100, 100),
                             ((x*gridsize)+startingpoint, gridsize*y*2), (startingpoint+(gridsize*(x+1)), gridsize*y*2))
            y += 1
            if y > 20:
                y = 0
        x += 3
    x = 0
    y = 0
    startingpoint = 0
    gridsize = 0
    for i in range(20):
        for i in range(20):
            pygame.draw.line(screen, (100, 100, 100),
                             ((x*gridsize)+startingpoint + 10, gridsize*y*2 + 10),
                             (startingpoint+(gridsize*(x+1) + 10), gridsize*y*2 + 10))
            y += 1
            if y > 20:
                y = 0
        x += 3

    pygame.display.update()
    clock.tick(60)
