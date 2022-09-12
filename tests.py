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
        elif user_input == 'g': glicko.run_solve_for_g()
        elif user_input == 'ng': glicko.run_solve_for_neg_g()
        elif user_input == 'e': glicko.run_solve_for_E()
        elif user_input == 'rd': glicko.run_rd_test()
        elif user_input == 'd**2': glicko.run_solve_for_d_squared()
        elif user_input == 'nrd': glicko.run_solve_for_new_rd()

if __name__ == '__main__':
    main()