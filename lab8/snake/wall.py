from game import Game, Point
from snak import Snake



class Wall(Game):

    def __init__(self, box_size, color):
        super().__init__(self.get_points(), box_size, color)
        self.level = 0

    def get_points(self):
        f = open("level0.txt", "r")
        self.points = []
        y = 0
        for column in f:
            x = 0
            for row in column:
                if row == '#':
                    self.points.append(Point(x, y))
                x += 1
            y += 1
        print (self.points)
        return self.points
    def board(self):
        return self.points
