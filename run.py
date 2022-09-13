from player import Player
from file_manager import File
from glicko import glicko

def main():
# Load the player list and ask user for the two players that are playing
    player_list = File.load_players('players.csv')
    user_input_1 = input('Enter the name of the Player: ')
    user_input_2 = input('Enter the name of their opponent: ')

# Find the two players in the list
    player1 = File.find_player(player_list, user_input_1)
    player2 = File.find_player(player_list, user_input_2)

# Prompt the user for the result & calculate the new ranks
    user_input_result = input('Who won the game?')
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

    print(f'Player 1: {player1}\nPlayer 2: {player2}')

# Save new results to test.csv
    player_list = File.save_players('test.csv')

if __name__ == '__main__':
    main()