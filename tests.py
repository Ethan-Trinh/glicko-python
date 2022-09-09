from player import Player
from file_manager import File
from glicko import glicko

def main():

# Shell Terminal to run various tests
    while user_input != 'exit':
        user_input = input()
        if user_input == 'Player': Player.run_test()
        elif user_input == 'File': File.load_player_base()

if __name__ == '__main__':
    main()