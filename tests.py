from player import Player
from file_manager import File
from glicko import glicko

def main():
    print('Welcome to the test module for the Glicko python program. To exit the program, enter "exit"')

# Shell Terminal to run various tests
    while True:

# Prompts the user to enter specific test cases
        user_input = input("\nEnter Command: ")

        if user_input == 'exit': break
# player.py functions
        elif user_input == 'player': Player.run_test()

# file_manager.py functions
        elif user_input == 'load': File.run_load_test()
        elif user_input == 'save': File.run_save_test()
        elif user_input == 'find': File.run_find_test()

#glicko.py functions
        elif user_input == "c": glicko.run_solve_for_c()

if __name__ == '__main__':
    main()