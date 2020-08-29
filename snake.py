import pygame
import random

pygame.init()

GAME_WIDTH = 500
GAME_HEIGHT = 500
SNAKECOLOR = (255, 153, 51)
FOODCOLOR = (51, 153, 255)
SNAKEBLOCK = 20

win = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))
pygame.display.set_caption("Anthony Kugel Snake Game")
x = 40
y = 40 
vel = 20
clock = pygame.time.Clock()
run = True
font = pygame.font.SysFont(None, 30)
lost = False
xDelta = 0
yDelta = 0
score = 0



def message(msg, color, x, y):
    mesg = font.render(msg, True, color)
    win.blit(mesg, [int(x), int(y)])

class Snake:
    def __init__(self, body):
        self.body = body
        self.x = body[0][0]
        self.y = body[0][1]
        self.size = SNAKEBLOCK
        self.xDelta = 0
        self.yDelta = 0

    def draw(self):
        for x in self.body:
            pygame.draw.rect(win, SNAKECOLOR, [x[0], x[1], self.size, self.size])
    def grow(self, x, y):
        self.body.append([x, y])
    def slither(self, x, y):
        self.body.insert(0, [x, y])
        self.body.pop()
        
class Food:
    def __init__(self, food_x=0, food_y=0):
        self.size = SNAKEBLOCK
        self.location_x = food_x
        self.location_y = food_y
    def newfood(self):
        randX = random.randint(0, GAME_WIDTH-self.size)
        randXModulus = randX % SNAKEBLOCK
        self.location_x = randX - randXModulus
        randY = random.randint(0, GAME_HEIGHT-self.size)
        randYModulus = randY % SNAKEBLOCK
        self.location_y = randY - randYModulus
    def drawFood(self):
        pygame.draw.rect(win, FOODCOLOR, [self.location_x, self.location_y, self.size, self.size])

food = Food()
food.newfood()
snake = Snake([[20,20],[40,20],[60,20]])

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if snake.xDelta != vel:
            snake.xDelta = -(vel)
            snake.yDelta = 0
    if keys[pygame.K_RIGHT]:
        if snake.xDelta != -(vel):
            snake.xDelta = vel
            snake.yDelta = 0
    if keys[pygame.K_UP]:
        if snake.yDelta != vel:
            snake.xDelta = 0
            snake.yDelta = -(vel)
    if keys[pygame.K_DOWN]:
        if snake.yDelta != -(vel):
            snake.xDelta = 0
            snake.yDelta = vel
    snake.x += snake.xDelta
    snake.y += snake.yDelta

    if x > GAME_WIDTH or x < 0 or y > GAME_HEIGHT or y < 0:
        lost = True
        run = False
        break

    if snake.body[0] in snake.body[1:] and score > 0:
        lost = True
        run = False
        break

    if food.location_x == snake.x and food.location_y == snake.y:
        food.newfood()
        score += 5
        snake.grow(snake.x, snake.y)

    snake.slither(snake.x, snake.y)

    win.fill((0,0,0))
    snake.draw()
    food.drawFood()
    message(f"{score}", (255, 0, 0), 10, 10)
    pygame.display.update()


    clock.tick(10)

if lost:
    message(f"You lose! Your score is {score}", (255, 0, 0), GAME_WIDTH/4, GAME_HEIGHT/2)
    pygame.display.update()

    pygame.time.wait(2000)


pygame.quit()
quit