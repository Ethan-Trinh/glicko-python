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
    
    def run_solve_for_c():
        player_list = File.load_players('players.csv')
        average_rd = glicko.find_average_rd(player_list)
        new_c = glicko.solve_for_c(player_list)

        print(f'average rd is equal to: {average_rd}')
        print(f'c is equal to: {new_c}')