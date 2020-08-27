import pygame
import random

pygame.init()

game_width = 500
game_height = 500
snakecolor = (255, 153, 51)
foodcolor = (51, 153, 255)
win = pygame.display.set_mode((game_width,game_height))
pygame.display.set_caption("Anthony Kugel Snake Game")
x = 20
y = 20 
snakeblock = 20
vel = 20
clock = pygame.time.Clock()
run = True
font = pygame.font.SysFont(None, 30)
lost = False
xDelta = 0
yDelta = 0
score = 0



def message(msg, color):
    mesg = font.render(msg, True, color)
    win.blit(mesg, [int(game_width/3), int(game_height/2)])

class Snake:
    def __init__(self, body):
        self.body = body
    def draw(self):
        for x in self.body:
            pygame.draw.rect(win, snakecolor, [x[0], x[1], snakeblock, snakeblock])
    def grow(self, x, y):
        self.body.append([x, y])
    def slither(self, x, y):
        self.body.insert(0, [x, y])
        self.body.pop()
        
class Food:
    def __init__(self, food_x=0, food_y=0):
        self.size = snakeblock
        self.location_x = food_x
        self.location_y = food_y
    def newfood(self):
        randX = random.randint(0, game_width-snakeblock)
        randXModulus = randX % snakeblock
        self.location_x = randX - randXModulus
        randY = random.randint(0, game_height-snakeblock)
        randYModulus = randY % snakeblock
        self.location_y = randY - randYModulus
    def drawFood(self):
        pygame.draw.rect(win, foodcolor, [self.location_x, self.location_y, self.size, self.size])

food = Food()
food.newfood()
snake = Snake([[20,20],[40,20],[60,20]])

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if xDelta != vel:
            xDelta = -(vel)
            yDelta = 0
    if keys[pygame.K_RIGHT]:
        if xDelta != -(vel):
            xDelta = vel
            yDelta = 0
    if keys[pygame.K_UP]:
        if yDelta != vel:
            xDelta = 0
            yDelta = -(vel)
    if keys[pygame.K_DOWN]:
        if yDelta != -(vel):
            xDelta = 0
            yDelta = vel
    x += xDelta
    y += yDelta

    if x > game_width or x < 0 or y > game_height or y < 0:
        lost = True
        run = False

    if food.location_x == x and food.location_y == y:
        food.newfood()
        score += 5
        snake.grow(x, y)

    snake.slither(x, y)

    win.fill((0,0,0))
    snake.draw()
    food.drawFood()
    pygame.display.update()


    clock.tick(10)

if lost:
    message(f"You suck! Your score is {score}", (255, 0, 0))
    pygame.display.update()

    pygame.time.wait(2000)


pygame.quit()
quit