from file_manager import File
from glicko import glicko

# This function performs the action where the user can see the rank changes when
# The user enters the name of two players and who won.
def main():
# Load the player list and ask user for the two players that are playing
    player_list = File.load_players('test.csv')
    user_input_1 = input('Enter the name of the Player: ')
    user_input_2 = input('Enter the name of their opponent: ')

# Find the two players in the list
    player1 = File.find_player(player_list, user_input_1)
    player2 = File.find_player(player_list, user_input_2)

    #player_obj_1 = Player(player1.name, player1.rank, player1.t, player1.rd)

# Prompt the user for the result & calculate the new ranks
    user_input_result = input('Who won the game?: ')
    if user_input_result == player1.name: 
        result1 = 1
        result2 = 0
    elif user_input_result == player2.name:
        result1 = 0
        result2 = 1
    elif user_input_result == 'draw':
        result1 = 0.5
        result2 = 0.5
    
    glicko.run(player_list, player1, player2, result1)
    glicko.run(player_list, player2, player1, result2)

# Because the players just played a game, their rating periods since their last game == 0
    player1.change_t(1)
    player2.change_t(1)

    print(f'Player 1: {player1}\nPlayer 2: {player2}')

# Update & Save new results to test.csv
    File.update_list(player_list, player1, player2)
    File.save_players('test.csv', player_list)

if __name__ == '__main__':
    main()