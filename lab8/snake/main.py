import pygame, time
from random import randint
from food import Food
from game import Point
from snak import Snake
from wall import Wall
from pygame.locals import *
pygame.init()
font_score = pygame.font.SysFont("Arial", 20, bold=True)
score=0
screen = pygame.display.set_mode((400, 320))
clock = pygame.time.Clock()
fps=4



done = False
def create_background(screen, width, height):
    colors = [(255, 255, 255), (150, 146, 135)]
    box_size = 20
    row = 0
    while row <= width:
        column = 0
        while column <= height:
            x = row // box_size + column // box_size
            pygame.draw.rect(screen, colors[x % 2], (row, column, box_size, box_size))
            column += box_size
        row += box_size


box_size = 20
food = Food(points=[Point(randint(0, 19), randint(0, 15))], box_size=box_size, color=(252, 186, 3))
class w():
    def __init__():
        wall = Wall(box_size=box_size, color=(227, 9, 38))
        return wall
wall = Wall(box_size=box_size, color=(227, 9, 38))
snake = Snake(points=[Point(1, 1)], box_size=box_size, color=(6, 114, 153))



while not done:
    create_background(screen, 400, 300)
    render_score=font_score.render(f"SCORE:{score}", 100, pygame.Color('orange'))
    screen.blit(render_score,(5,5) )
    # Event filtering
    filtered_events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else:
            filtered_events.append(event)
    
    snake.move(filtered_events)
#random food
    if food.can_eat(snake.get_first_point()):
        score+=1
        fps+=1
        snake.eat()
        x=randint(0, 19)
        y=randint(0, 15)
        food = Food(points=[Point(x,y)], box_size=box_size, color=(252, 186, 3))
#Checking for border
    if snake.area():
        done=True


    food.draw(screen)
    wall.draw(screen)

    snake.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
