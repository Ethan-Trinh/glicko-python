import csv

class File:
# Load player base will load csv file and read
    def load_player_base():
        with open('players.csv') as file_object:
            heading = next(file_object)

            read_obj = csv.reader(file_object)
    
            for row in read_obj: 
                print(row)
