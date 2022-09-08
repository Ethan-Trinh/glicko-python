# plyer.py by Ethan Trinh
# This file is used to handle individual player information as 
# a class object. Funtions within this class will handle an individual
# player in the leaderboard of players

import math

# Player class object stores:
# Rating Deviations (RD), number of rating periods (t), Glicko_Rank (rank)
# New players will start with a RD = 350, t = 0, rank = 1500
class Player:
    def __init__(self, rd, t, rank):
        self.rd = rd
        self.t = t
        self.rank = rank
    
    def __repr__(self):
        return f'Player rd = {self.rd}, t = {self.t}, rank = {self.rank}'

# Methods for changing rd, t and rank
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
        
        if new_rd >= 350:
            self.change_rd(350)
        elif new_rd < 350:
            self.change_rd(new_rd)

    @staticmethod
    def run_test():
        pl = Player(120, 1, 1500)
        pl.onset_ratings_deviation()
        print(f'Testing : {pl}')

def main():
    Player.run_test()

if __name__ == '__main__':
    main()