import math

class glicko:
# To calculate the Ratings Deviation (RD) we need:
# old_RD, number of rating periods (t), and parameter c
# Player Class object will pass the required information for calculating rank
    def calculate_new_ranks():
        pass

# Player class object stores:
# Rating Deviations (RD), number of rating periods (t), Glicko_Rank (rank)
# New players will start with a RD = 350, t = 0, rank = 1500
class player:
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
        self.change_rd(new_rd)

    @staticmethod
    def run():
        pl = player(50, 0, 1500)
        pl.onset_ratings_deviation()
        print(f'Testing : {pl}')

def main():
    player.run()

if __name__ == '__main__':
    main()

