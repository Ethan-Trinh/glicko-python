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
        elif user_input == 'player': Player.run_test()
        elif user_input == 'file': File.run_test()
        elif user_input == "c": glicko.run_solve_for_c()

if __name__ == '__main__':
    main()