import pygame

from game import Game, Point


class Snake(Game):

    def __init__(self, points, box_size, color):

        super().__init__(points, box_size, color)
        self.direction_x = 0
        self.direction_y = 1

    def change_direction(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.direction_x = -1
                self.direction_y = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.direction_x = 1
                self.direction_y = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.direction_x = 0
                self.direction_y = -1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.direction_x = 0
                self.direction_y = 1

    def move(self, events):
        self.change_direction(events=events)
        old_point = self.points[0]
        self.X=old_point.x + self.direction_x
        self.Y=old_point.y + self.direction_y
        new_point = Point(self.X, self.Y)
        self.points.pop()
        self.points.insert(0, new_point)
        

    def eat(self):
        self.points.append(self.get_first_point())
    def area(self):
        if self.X>20 or self.X<0 or self.Y>15 or self.Y<0:
            return True
    def s(self):
        return (self.X, self.Y)


       
