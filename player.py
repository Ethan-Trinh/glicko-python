# plyer.py by Ethan Trinh
# This file is used to handle individual player information as 
# a class object. Funtions within this class will handle an individual
# player in the leaderboard of players

import math

# Player class object stores:
# Rating Deviations (RD), number of rating periods (t), Glicko_Rank (rank)
# New players will start with a RD = 350, t = 0, rank = 1500
class Player:
    def __init__(self, name, rank, t, rd):
        self.name = name
        self.rank = rank
        self.rd = rd
        self.t = t
    
    def __repr__(self):
        return f'{self.name}: Rank = {self.rank}, Rating Periods = {self.t}, Rating Deviation = {self.rd}'

# Methods for changing rd, t and rank
    def change_name(self, name): self.name = name
    def change_rd(self, rd): self.rd = rd
    def change_t(self, t): self.t = t
    def change_rank(self, rank): self.rank = rank

# Assuming that it would take 100 rating periods for a player's
# rating deviation to return to the initial 350 & that an average
# rating deviation of 50

# c = sqrt( (350**2 - 50**2) / 100 ) ~~ 34.6

#TODO: Add a feature that takes the average RD of all players and
# solve for c using the variable avg_rd
    def solve_for_c():
        pass
    
    # RD = sqrt([old_RD]^2 + c^2 * t)
    def onset_ratings_deviation(self):
        c = 34.6
        new_rd = math.sqrt( (self.rd**2) + c**2 * self.t )

    # Round the float value to nearst whole integer
        new_rd = round(new_rd)

    # Since 350 is the max rd, any Rd above 350 exceeds the maximum rd
    # will be replaecd with 350 instead
        if new_rd >= 350:
            self.change_rd(350)
        elif new_rd < 350:
            self.change_rd(new_rd)

    @staticmethod
    def run_test():
        pl = Player('John P', 1500, 3, 50)
        pl.onset_ratings_deviation()
        print(f'{pl}')
