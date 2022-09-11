import math
from player import Player
from file_manager import File

class glicko:
# To calculate the Ratings Deviation (RD) we need:
# old_RD, number of rating periods (t), and parameter c
# Player Class object will pass the required information for calculating rank
    def calculate_new_ranks():
        pass

# Assuming that it would take 100 rating periods for a player's
# rating deviation to return to the initial 350 & that an average
# rating deviation of 50

# Need a funtion to find the average rd of the set
# print(player_list[1].rd) => will print the rd of a given [x] value
    def find_average_rd(player_list):
        sum = 0
        iteration = 0
        for obj in player_list:
            sum = sum + float(obj.rd)
            iteration = iteration + 1
        return round(sum / iteration)
        

# c = sqrt( (350**2 - 50**2) / 100 ) ~~ 34.6
# Assumes that 50 is the average rating deviation of the total player population
    def solve_for_c(player_list):
        numerator = (350**2) - (glicko.find_average_rd(player_list)**2)
        c = math.sqrt(numerator / 100)
        return c
    
# Assuming that it would take 100 rating periods for a player's rating deviation to return to the initial 350 & that an average rating deviation of 50
    
# RD = sqrt([old_RD]^2 + c^2 * t)
    def onset_ratings_deviation(player_list, player):

        c = glicko.solve_for_c(player_list)

        new_rd = math.sqrt((player.rd**2) + c**2 * float(player.t))
        new_rd = round(new_rd) # Round the float value to nearst whole integer

# Since 350 is the max rd, any Rd above 350 exceeds the maximum rd and will be replaecd with 350 instead
        if new_rd >= 350:
            player.change_rd(350)
        elif new_rd < 350:
            player.change_rd(new_rd)

# Step 2: calculate g based on opponent's onset RD.
# g = 1/sqrt( [1 + 3 (q**2) (RD**2)] / pi**2 )
# constant q = log(e) [10 / 400] == 0.0058565
# Then E can be caluclated by: E = 1 / (1 + 10^(-g(pr - or)/400))
# where pr == player rating
#       or == opponent's rating

    def solve_for_g(opponent):
        q = 0.0058565
        pi = math.pi
        denom = (1 + (3 * (q**2)) * (opponent.rd)**2) / pi**2
        g = 1 / denom
        return g

    
    def run_solve_for_c():
        player_list = File.load_players('players.csv')
        average_rd = glicko.find_average_rd(player_list)
        new_c = glicko.solve_for_c(player_list)

        print(f'average rd is equal to: {average_rd}')
        print(f'c is equal to: {new_c}')
    
    def run_rd_test():
        player_list = File.load_players('players.csv')
        pl = Player('John P', 1500, 3, 50)
        print(f'{pl}')
        glicko.onset_ratings_deviation(player_list, pl)
        print(f'{pl}')

    def run_solve_for_g():
        pl = Player('John P', 1500, 3, 50)
        print(f'{pl}')
        g = glicko.solve_for_g(pl)
        print(f'{g}')