import math
from optparse import OptionParser
from player import Player
from file_manager import File

class glicko:
# To calculate the Ratings Deviation (RD) we need:
# old_RD, number of rating periods (t), and parameter c
# Player Class object will pass the required information for calculating rank
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
        new_rd = math.sqrt((float(player.rd)**2) + c**2 * float(player.t))
        
# Since 350 is the max rd, any Rd above 350 exceeds the maximum rd and will be replaecd with 350 instead
        if new_rd >= 350:
            player.change_rd(350)
        elif new_rd < 350:
            player.change_rd(new_rd)

# Step 2: calculate g based on opponent's onset RD.
# g = 1/sqrt( [1 + 3 (q**2) (RD**2)] / pi**2 )
# constant q = ln(10) / 400 == 0.0057565...
# Then E can be caluclated by: E = 1 / (1 + 10^(-g(pr - or)/400))
# where pr == player rating
#       or == opponent's rating

    def solve_for_g(opponent):
        q = 0.0057565
        pi = math.pi
        denom = math.sqrt(1 + (((3 * (q**2)) * (opponent.rd)**2) / pi**2))
        g = 1 / denom
        return g

    def negative_g(g): return -g

    def solve_for_E(player1, player2, g):
        g = glicko.negative_g(g)
        rank_difference = (int(player1.rank) - int(player2.rank))
        e = 1 / (1 + 10**((g * rank_difference) / 400 ))
        return e

# After the previous steps, new_RD is found with these 2 formulas
# d**2 == 1 / (q**2 g**2 E (1 - E))
    def solve_for_d_squared(player, g, e):
        q = 0.0057565
        d_squared = 1 / ((q**2)*(g**2)*(e)*(1 - e))
        return d_squared

    def new_RD(player, d_squared):
        print(f'{(player.rd)**2}')
        print(f'{(d_squared)**2}')

        new_rd = 1 / math.sqrt((1/(player.rd)**2) + (1/(d_squared**2)))

        if new_rd >= 350:
            player.change_rd(350)
        elif new_rd < 350:
            player.change_rd(round(new_rd))

# Lastly, to calculate the ranks we need:
# S == result of the game (0 == loss, 0.5 == draw, 1 == win)
# The new rank is calculated with: r_post == r_pre + q*(new_rd**2)*g*(S-E)

    def solve_for_new_rank(player, g, s, e):
        q = 0.0057565
        r_post = round(float(player.rank) + q*(float(player.rd)**2)*g*(float(s) - float(e)))
        player.change_rank(round(r_post))

    def run(player_list, player, opponent, result):
    # 1st Find onset_RD for both players
        glicko.onset_ratings_deviation(player_list, player)
        glicko.onset_ratings_deviation(player_list, opponent)

    # Next, solve for g using opponent's onset_RD
        g = glicko.solve_for_g(opponent)

    # After, we need to solve for E
        e = glicko.solve_for_E(player, opponent, g)

    # Then we find the new RD by first finding d**2
        d_squared = glicko.solve_for_d_squared(player, g, e)
        glicko.new_RD(player, d_squared)

    # Finally, Calculate the rank s == result of the game
        glicko.solve_for_new_rank(player, g, result, e)


# Test functions for each function in the class
# All of these functions are called in test.py
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
        pl = Player('John P', 1780, 1, 60)
        print(f'{pl}')
        g = glicko.solve_for_g(pl)
        print(f'g: {g}')
    
    def run_solve_for_neg_g():
        pl = Player('John P', 1500, 3, 50)
        print(f'{pl}')
        g = glicko.solve_for_g(pl)
        print(f'g: {g}')
        g = glicko.negative_g(g)
        print(f'negitive g: {g}')

    def run_solve_for_E():
        pl1 = Player('John P', 1500, 1, 60)
        pl2 = Player('Jeff L', 1780, 1, 60)
        print(f'{pl1}\n{pl2}')
        g = glicko.solve_for_g(pl2)
        e = glicko.solve_for_E(pl1, pl2, g)
        print(f'E: {e}')

    def run_solve_for_d_squared():
        pl1 = Player('John P', 1500, 1, 60)
        pl2 = Player('Jeff L', 1780, 1, 60)
        print(f'Player 1: {pl1}\nPlayer 2: {pl2}')
        print(f'{pl1}\n{pl2}')
        g = glicko.solve_for_g(pl1)
        print(f'g: {g}')
        e = glicko.solve_for_E(pl1, pl2, g)
        print(f'E: {e}')
        d_squared = glicko.solve_for_d_squared(pl1, g, e)
        print(f'D**2: {d_squared}')

    def run_solve_for_new_rd():
        pl1 = Player('John P', 1500, 1, 60)
        pl2 = Player('Jeff L', 1780, 1, 60)
        print(f'Player 1: {pl1}\nPlayer 2: {pl2}')
        print(f'{pl1}\n{pl2}')
        glicko.onset_ratings_deviation(pl1)
        print(f'{pl1}\n{pl2}')
        g = glicko.solve_for_g(pl1)
        print(f'g: {g}')
        e = glicko.solve_for_E(pl1, pl2, g)
        print(f'E: {e}')
        d_squared = glicko.solve_for_d_squared(pl1, g, e)
        print(f'D**2: {d_squared}')
        glicko.new_RD(pl1, d_squared)
        print(f'{pl1}\n{pl2}')
        
    def run_glicko_test():
        pl1 = Player('John P', 1500, 1, 60)
        pl2 = Player('Jeff L', 1780, 1, 60)
        print(f'Player 1: {pl1}\nPlayer 2: {pl2}')
        glicko.onset_ratings_deviation(pl1)
        print(f'{pl1}\n{pl2}')
        g = glicko.solve_for_g(pl1)
        print(f'g: {g}')
        e = glicko.solve_for_E(pl1, pl2, g)
        print(f'E: {e}')
        d_squared = glicko.solve_for_d_squared(pl1, g, e)
        print(f'D**2: {d_squared}')
        glicko.new_RD(pl1, d_squared)
        print(f'{pl1}')
        s = int(input("\nEnter Result (0 == lose, 0.5 == draw, 1 == win: ) "))
        if s > 1: 
            print("Invalid Input") 
        elif s < 0:
            print("Invalid Input")
        else:
            glicko.solve_for_new_rank(pl1, g, s, e)
        print(f'{pl1}')