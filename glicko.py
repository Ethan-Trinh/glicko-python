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
        return math.sqrt( (self.rd**2) + c**2 * self.t )

    @staticmethod
    def run():
        Player = player(350, 0, 1500)
        print(player.onset_ratings_deviation())

def main():
    player.run()

if __name__ == '__main__':
    main()

