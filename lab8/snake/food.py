from game import Game


class Food(Game):

    def can_eat(self, point):
        if point == self.get_first_point():
            return True
        return False