import pygame

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Racing')
clock = pygame.time.Clock()

racecar = pygame.image.load('car.png')
racecar_width = 73


def draw_car(x, y):
    screen.blit(racecar, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    car_speed = 0

    crashed = False
    message = "First"

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    x_change = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    y_change = 0

        x += x_change
        y += y_change
        screen.fill(white)
        draw_car(x, y)

        if x > display_width - racecar_width:
            print("hit right wall")
            message = "right"
            #crashed = True
        if x < 0:
            print("hit left wall")
            message = "left"
            #crashed = True
        if y > display_height - racecar_width:
            print("hit bottom wall")
            message = "bottom"
            #crashed = True
        if y < 0:
            print("hit top wall")
            message = "top"
            #crashed = True

        message_display(message)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
