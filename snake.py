import pygame

pygame.init()

game_width = 500
game_height = 500

win = pygame.display.set_mode((game_width,game_height))

pygame.display.set_caption("First game")

x = 20
y = 20 
width = 20
height = 20 
vel = 20

clock = pygame.time.Clock()

run = True

font = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font.render(msg, True, color)
    win.blit(mesg, [game_width/2, game_height/2])

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
            x -= vel
    if keys[pygame.K_RIGHT]:
            x += vel
    if keys[pygame.K_UP]:
            y -= vel
    if keys[pygame.K_DOWN]:
            y += vel

    if x > game_width or x < 0 or y > game_height or y < 0:
        run = False

    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 153, 51), (x, y, width, height))
    pygame.display.update()

    clock.tick(10)

message("You have failed", (255, 0, 0))
pygame.display.update()
time.sleep(2000)


pygame.quit()
quit