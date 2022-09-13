import csv
from player import Player

class File:
    def load_players(file_name):
        player_list = []
        with open(file_name) as file_obj:
            heading = next(file_obj)                # Skips the heading of the CSV File
            read_obj = csv.reader(file_obj)
            for row in read_obj: player_list.append(Player(row[0], row[1], row[2], row[3]))
        return player_list

    def save_players(file_name, player_list):
        heading = ['Name', 'Rank', 't', 'rd']
        with open(file_name, 'w', newline='') as file_obj:
            csv_write = csv.writer(file_obj)
            csv_write.writerow(heading)

            for obj in player_list:
                current_row = [obj.name, obj.rank, obj.t, obj.rd]
                csv_write.writerow(current_row)

    def find_player(player_list, target_player):
        for obj in player_list:
            if target_player == obj.name: 
                target_player = Player(obj.name, obj.rank, obj.t, obj.rd)
                return target_player # if player is found, return the player object
        #return target_player in player_list

    def run_load_test():
        player_list = File.load_players('players.csv')

        for obj in player_list:
            print(obj)

    def run_save_test():
        player_list = File.load_players('players.csv')
        File.save_players('test.csv', player_list)
        print("Saved to test.csv")

    def run_find_test():
        player_list = File.load_players('players.csv')
        user_input = input("\nEnter the name of the player you wish to find: ") 
        target_player = File.find_player(player_list, user_input)
        print(f'{target_player}')