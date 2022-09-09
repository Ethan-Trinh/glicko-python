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

    def run_test():
        player_list = File.load_players('players.csv')

        for obj in player_list:
            print(obj)