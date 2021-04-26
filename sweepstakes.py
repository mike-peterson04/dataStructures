import random

class Sweepstakes:
    def __init__(self):
        self.contestants = {}

    def add_contestant(self,index,contestant):
        self.contestants[index]=contestant

    def select_winner(self):
        return self.contestants[random.randint(1,len(self.contestants))]