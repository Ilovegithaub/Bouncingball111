import pygame
import sys


pygame.init()




screen_width = 800
screen_height = 600




screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Basics")

font=pygame.font.Font(None, 40)
text_render=font.render("Play", True, 'black')
text_render2=font.render("Exit", True, 'black')

def bouncingball():

    width = 800
    height = 400
    speedx, speedy = 0.5, 0.5
    x, y = 100, 100
    font=pygame.font.Font(None, 40)
    text_render3=font.render("Exit", True, 'black')

    Recttt=pygame.Rect(320, 155, 155, 50)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame")
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Recttt.collidepoint(event.pos):
                    running = False
        screen.fill("blue")

        x += speedx
        y -= speedy

        if x + 20 > width or x - 20 < 0:
            speedx = -speedx

        if y + 20 > height or y - 20 < 0:
            speedy = -speedy


        pygame.draw.circle(screen, "Yellow", (x, y), 20)
        pygame.draw.rect(screen, "yellow", Recttt, border_radius=40)
        screen.blit(text_render3, (Recttt.x+50, Recttt.y+15))
        pygame.display.flip()

    return

button1=pygame.Rect(320, 155, 155, 50)
background_color = (0, 128, 255)

button2=pygame.Rect(320, 250, 155, 50)


running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

       if event.type == pygame.MOUSEBUTTONDOWN:
           if button2.collidepoint(event.pos):
               running=False

           if button1.collidepoint(event.pos):
               bouncingball()
   screen.fill(background_color)
   pygame.draw.rect(screen, "red", button1, border_radius=60)
   screen.blit(text_render, (button1.x+50, button1.y+15))
   pygame.draw.rect(screen, "red", button2, border_radius=60)
   screen.blit(text_render2, (button2.x+50, button2.y+15))
   pygame.display.flip()
